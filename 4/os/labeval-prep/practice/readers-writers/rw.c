#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/shm.h>
#include <sys/wait.h>

typedef struct {
    int data;
    int readcount;
    int mutex;      // guards readcount
    int rw_mutex;   // blocks writers while readers active
} shm_layout;

// classic semaphore semantics
void wait_and_get_lock(int *s)   { while (*s <= 0); (*s)--; }
// release_lock is just incrementing the semaphore value, which may allow other waiting processes to proceed.
void release_lock(int *s) { (*s)++; }

void reader(shm_layout *sh, int id) {
    // --- entry ---
    wait_and_get_lock(&(sh->mutex));
        sh->readcount++;
        if (sh->readcount == 1){
            // first reader locks out writers
            wait_and_get_lock(&(sh->rw_mutex));
        }
    release_lock(&(sh->mutex));

    // --- read ---
    printf("[READER %d]: data = %d\n", id, sh->data);

    // --- exit ---
    wait_and_get_lock(&(sh->mutex));
        sh->readcount--;
        if (sh->readcount == 0)   // last reader lets writers in
            release_lock(&(sh->rw_mutex));
    release_lock(&(sh->mutex));
}

void writer(shm_layout *sh, int id) {
    wait_and_get_lock(&(sh->rw_mutex));       // exclusive access
        int r = rand() % 10;
        sh->data += r;
        printf("[WRITER %d]: added %d, data now = %d\n", id, r, sh->data);
    release_lock(&(sh->rw_mutex));
}

int main() {
    int shmid = shmget(IPC_PRIVATE, sizeof(shm_layout), IPC_CREAT | 0666);
    shm_layout *sh = (shm_layout*)shmat(shmid, NULL, 0);

    sh->data      = 0;
    sh->readcount = 0;
    sh->mutex     = 1;
    sh->rw_mutex  = 1;

    int roles[5] = {0, 0, 0, 1, 1}; // 0 = reader, 1 = writer
    int ids[5]   = {1, 2, 3, 1, 2};

    srand((unsigned)getpid());
    for (int i = 4; i > 0; --i) {
        int j = rand() % (i + 1);
        int tmp = roles[i]; roles[i] = roles[j]; roles[j] = tmp;
        tmp = ids[i]; ids[i] = ids[j]; ids[j] = tmp;
    }

    for (int i = 0; i < 5; i++) {
        if (fork() == 0) {
            if (roles[i] == 0) reader(sh, ids[i]);
            else writer(sh, ids[i]);
            exit(0);
        }
    }

    for (int i = 0; i < 5; i++)
        wait(NULL);

    printf("[MAIN]: final data = %d\n", sh->data);

    shmdt(sh);
    shmctl(shmid, IPC_RMID, NULL);
    return 0;
}