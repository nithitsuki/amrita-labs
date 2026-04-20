
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>

struct shared_data {
    int readcount;
    int x;
};

int mutex = 1;
int rw_mutex = 1;

void wait_sem(int *s) {
    while (*s <= 0)
    {
        // block until the semaphore is available
    }
    (*s)--;
}

void signal_sem(int *s) {
    (*s)++;
}

void reader(struct shared_data *sh, int id) {
    wait_sem(&mutex);
    sh->readcount++;

    if (sh->readcount == 1)
        wait_sem(&rw_mutex);

    signal_sem(&mutex);

    // Reading shared data
    printf("Reader %d reads x = %d\n", id, sh->x);
    sleep(1);

    wait_sem(&mutex);
    sh->readcount--;

    if (sh->readcount == 0)
        signal_sem(&rw_mutex);

    signal_sem(&mutex);
}

void writer(struct shared_data *sh, int id) {
    wait_sem(&rw_mutex);

    // Modifying shared data
    sh->x += 1;
    printf("Writer %d modifies x = %d\n", id, sh->x);
    sleep(1);

    signal_sem(&rw_mutex);
}

int main() {
    int shmid;
    struct shared_data *sh;
    int r, w, i;

    shmid = shmget(IPC_PRIVATE, sizeof(struct shared_data), IPC_CREAT | 0666);
    sh = (struct shared_data*) shmat(shmid, NULL, 0);

    sh->readcount = 0;
    sh->x = 1;  // Initial value

    printf("Enter number of readers: ");
    scanf("%d", &r);

    printf("Enter number of writers: ");
    scanf("%d", &w);

    // Create reader processes
    for (i = 1; i <= r; i++) {
        if (fork() == 0) {
            reader(sh, i);
            exit(0);
        }
    }

    // Create writer processes
    for (i = 1; i <= w; i++) {
        if (fork() == 0) {
            writer(sh, i);
            exit(0);
        }
    }

    for (i = 0; i < r + w; i++)
        wait(NULL);

    shmdt(sh);
    shmctl(shmid, IPC_RMID, NULL);

    return 0;
}