#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>      /* mmap, munmap, PROT_*, MAP_* */
#include <sys/wait.h>      /* wait()                      */
#include <fcntl.h>         /* O_CREAT, O_RDWR, O_RDONLY   */

/* ── configuration ────────────────────────────────────────── */
#define SHM_NAME   "/my_shared_array"
#define ARRAY_SIZE 10

/* Layout of the shared-memory region:
 *   [ int count ][ int data[ARRAY_SIZE] ]
 * Using a struct keeps everything in one contiguous block.
 */
typedef struct {
    int count;
    int data[ARRAY_SIZE];
} SharedData;

/* ── writer process (parent) ──────────────────────────────── */
void writer_process(void)
{
    printf("[Writer] PID %d starting.\n", getpid());

    /* 1. Create (or open) a shared memory object. */
    int fd = shm_open(SHM_NAME, O_CREAT | O_RDWR, 0666);
    if (fd == -1) { perror("shm_open (writer)"); exit(EXIT_FAILURE); }

    /* 2. Set the size of the shared memory object. */
    if (ftruncate(fd, sizeof(SharedData)) == -1) {
        perror("ftruncate"); exit(EXIT_FAILURE);
    }

    /* 3. Map it into our address space (read + write). */
    SharedData *shm = mmap(NULL, sizeof(SharedData),
                           PROT_READ | PROT_WRITE,
                           MAP_SHARED, fd, 0);
    if (shm == MAP_FAILED) { perror("mmap (writer)"); exit(EXIT_FAILURE); }
    close(fd);   /* fd no longer needed after mmap */

    /* 4. Fill the array with sample integers. */
    shm->count = ARRAY_SIZE;
    printf("[Writer] Storing array: ");
    for (int i = 0; i < ARRAY_SIZE; i++) {
        shm->data[i] = (i + 1) * 10;   /* 10, 20, 30 … 100 */
        printf("%d ", shm->data[i]);
    }
    printf("\n[Writer] Data written to shared memory.\n\n");

    /* 5. Unmap (the data stays in the named shm object). */
    munmap(shm, sizeof(SharedData));
}

/* ── reader process (child) ───────────────────────────────── */
void reader_process(void)
{
    printf("[Reader] PID %d starting.\n", getpid());

    /* 1. Open the *existing* shared memory object (read-only). */
    int fd = shm_open(SHM_NAME, O_RDONLY, 0666);
    if (fd == -1) { perror("shm_open (reader)"); exit(EXIT_FAILURE); }

    /* 2. Map it into our address space (read-only). */
    SharedData *shm = mmap(NULL, sizeof(SharedData),
                           PROT_READ,
                           MAP_SHARED, fd, 0);
    if (shm == MAP_FAILED) { perror("mmap (reader)"); exit(EXIT_FAILURE); }
    close(fd);

    /* 3. Read the array and compute the sum. */
    long long sum = 0;
    printf("[Reader] Reading array: ");
    for (int i = 0; i < shm->count; i++) {
        printf("%d ", shm->data[i]);
        sum += shm->data[i];
    }
    printf("\n[Reader] Sum of %d elements = %lld\n", shm->count, sum);

    /* 4. Unmap. */
    munmap(shm, sizeof(SharedData));
}

/* ── main ─────────────────────────────────────────────────── */
int main(void)
{
    printf("=== Shared Memory Demo (Linux syscalls) ===\n\n");

    /* Parent writes FIRST, then forks the reader child. */
    writer_process();

    pid_t pid = fork();
    if (pid < 0) { perror("fork"); exit(EXIT_FAILURE); }

    if (pid == 0) {
        /* ── child : reader ── */
        reader_process();
        exit(EXIT_SUCCESS);
    }

    /* ── parent : wait for child, then clean up ── */
    int status;
    wait(&status);

    /* Remove the named shared memory object from the system. */
    if (shm_unlink(SHM_NAME) == -1) {
        perror("shm_unlink");
    } else {
        printf("\n[Main]   Shared memory '%s' unlinked. Done.\n", SHM_NAME);
    }

    return 0;
}
