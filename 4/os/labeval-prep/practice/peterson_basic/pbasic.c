#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <sys/shm.h>
#include <sys/wait.h>

typedef struct {
    int counter;
    int want_cs[2];   // intent flags for Peterson's algorithm
    int turn;
} shared_state_t;

void enter_critical_section(shared_state_t *shared, int process_id) {
    int other_process = 1 - process_id;
    shared->want_cs[process_id] = 1;
    shared->turn = other_process;

    while (shared->want_cs[other_process] == 1 && shared->turn == other_process) {
        // busy wait
    }
}

void leave_critical_section(shared_state_t *shared, int process_id) {
    shared->want_cs[process_id] = 0;
}

void run_process(shared_state_t *shared, int process_id) {
    for (int iteration = 0; iteration < 5; iteration++) {
        enter_critical_section(shared, process_id);
        shared->counter++;
        printf("P%d: counter = %d\n", process_id, shared->counter);
        leave_critical_section(shared, process_id);
    }
}

int main() {
    int shared_mem_id = shmget(IPC_PRIVATE, sizeof(shared_state_t), IPC_CREAT | 0666);
    shared_state_t *shared = (shared_state_t *)shmat(shared_mem_id, NULL, 0);

    shared->counter = 0;
    shared->want_cs[0] = 0;
    shared->want_cs[1] = 0;

    if (fork() == 0) {
        run_process(shared, 0);
        exit(0);
    }

    if (fork() == 0) {
        run_process(shared, 1);
        exit(0);
    }

    wait(NULL);
    wait(NULL);

    printf("Final counter = %d\n", shared->counter);  // always 10

    shmdt(shared);
    shmctl(shared_mem_id, IPC_RMID, NULL);
}