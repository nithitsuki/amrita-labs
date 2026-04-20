#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <signal.h>

#define LINE_BUFFER_SIZE 256
#define SHM_KEY 0x1234

enum ProcessId {
	READER_ID = 0,
	WRITER_ID = 1
};

typedef struct {
	bool interested[2];          // Peterson flags
	int turn;                    // Peterson turn
	char line[LINE_BUFFER_SIZE]; // Shared line buffer
	bool line_ready;             // True when writer published a line
	bool transfer_done;          // True when writer reached EOF
} SharedState;

static void enter_critical_section(SharedState *state, int self_id) {
	int other_id = 1 - self_id;
	state->interested[self_id] = true;
	state->turn = other_id;
	while (state->interested[other_id] && state->turn == other_id) {
		// busy wait
	}
}

static void leave_critical_section(SharedState *state, int self_id) {
	state->interested[self_id] = false;
}

static void writer_process(SharedState *state, const char *input_path) {
	FILE *input_file = fopen(input_path, "r");
	if (!input_file) {
		perror("Failed to open input file");
		_exit(EXIT_FAILURE);
	}

	char local_line[LINE_BUFFER_SIZE];

	while (fgets(local_line, sizeof(local_line), input_file) != NULL) {
		bool published = false;

		while (!published) {
			enter_critical_section(state, WRITER_ID);

			if (!state->line_ready) {
				strncpy(state->line, local_line, LINE_BUFFER_SIZE - 1);
				state->line[LINE_BUFFER_SIZE - 1] = '\0';
				state->line_ready = true;
				published = true;
			}

			leave_critical_section(state, WRITER_ID);

			if (!published) {
				usleep(1000);
			}
		}
	}

	// Signal completion once buffer is free
	bool done_marked = false;
	while (!done_marked) {
		enter_critical_section(state, WRITER_ID);
		if (!state->line_ready) {
			state->transfer_done = true;
			done_marked = true;
		}
		leave_critical_section(state, WRITER_ID);

		if (!done_marked) {
			usleep(1000);
		}
	}

	fclose(input_file);
	_exit(EXIT_SUCCESS);
}

static void reader_process(SharedState *state, const char *output_path) {
	FILE *output_file = fopen(output_path, "w");
	if (!output_file) {
		perror("Failed to open output file");
		_exit(EXIT_FAILURE);
	}

	bool finished = false;

	while (!finished) {
		bool consumed_line = false;

		enter_critical_section(state, READER_ID);

		if (state->line_ready) {
			fputs(state->line, output_file);
			state->line_ready = false;
			consumed_line = true;
		} else if (state->transfer_done) {
			finished = true;
		}

		leave_critical_section(state, READER_ID);

		if (!consumed_line && !finished) {
			usleep(1000);
		}
	}

	fclose(output_file);
	_exit(EXIT_SUCCESS);
}

int main(void) {
	char input_path[256];
	char output_path[256];

	printf("Enter input file path: ");
	if (scanf("%255s", input_path) != 1) {
		fprintf(stderr, "Invalid input path\n");
		return EXIT_FAILURE;
	}

	printf("Enter output file path: ");
	if (scanf("%255s", output_path) != 1) {
		fprintf(stderr, "Invalid output path\n");
		return EXIT_FAILURE;
	}

	int shared_memory_id = shmget(SHM_KEY, sizeof(SharedState), IPC_CREAT | 0660);
	if (shared_memory_id < 0) {
		perror("shmget failed");
		return EXIT_FAILURE;
	}

	SharedState *shared_state = (SharedState *)shmat(shared_memory_id, NULL, 0);
	if (shared_state == (void *)-1) {
		perror("shmat failed");
		shmctl(shared_memory_id, IPC_RMID, NULL);
		return EXIT_FAILURE;
	}

	// Initialize shared state
	memset(shared_state, 0, sizeof(SharedState));
	shared_state->turn = READER_ID;

	pid_t writer_pid = fork();
	if (writer_pid < 0) {
		perror("fork failed for writer");
		shmdt(shared_state);
		shmctl(shared_memory_id, IPC_RMID, NULL);
		return EXIT_FAILURE;
	}
	if (writer_pid == 0) {
		writer_process(shared_state, input_path);
	}

	pid_t reader_pid = fork();
	if (reader_pid < 0) {
		perror("fork failed for reader");
		kill(writer_pid, SIGTERM);
		waitpid(writer_pid, NULL, 0);
		shmdt(shared_state);
		shmctl(shared_memory_id, IPC_RMID, NULL);
		return EXIT_FAILURE;
	}
	if (reader_pid == 0) {
		reader_process(shared_state, output_path);
	}

	waitpid(writer_pid, NULL, 0);
	waitpid(reader_pid, NULL, 0);

	shmdt(shared_state);
	shmctl(shared_memory_id, IPC_RMID, NULL);

	printf("Transfer completed.\n");
	return EXIT_SUCCESS;
}
