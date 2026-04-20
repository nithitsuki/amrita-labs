// Create a shared counter program. Two processes, a "Counter" and a "Monitor," share a single integer variable in shared memory.

// The Counter increments this integer from 0 to 100, one increment at a time. The Monitor reads the current value and prints it whenever the value changes.

// ### The Requirements

// 1.  **Synchronization:** Use Peterson's algorithm to wrap every read and write of the shared integer in a critical section.
// 2.  **Atomicity:** Ensure the Counter cannot increment the value while the Monitor is reading it.
// 3.  **Efficiency:** The Monitor should only print when the value actually increases, not in a tight loop printing the same number repeatedly.
// 4.  **Cleanup:** Ensure that once the Counter reaches 100, the Monitor detects the completion and both processes exit cleanly, removing the shared memory.

// ### The Core Logic Challenge

// Think about why Peterson's algorithm is required here. If you removed the critical section and the Counter incremented the variable while the Monitor was in the middle of a `printf` operation, what could go wrong if the integer was larger (e.g., a `long long` or a `struct`)?



// Why is Peterson's algorithm specifically designed for only two processes, and what architectural changes would be required to make this work for three or more processes?
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>

typedef enum {
    P0 = 0,
    P1 = 1
} PID;

typedef struct shm_layout
{
    int counter;
    bool want_cs[2];   // intent flags for Peterson's algorithm
    PID turn;
} shm_layout;

void enter_critical_zone(shm_layout *shared, PID self_process_id, PID other_process_id)
{
    shared->want_cs[self_process_id] = true;
    shared->turn = other_process_id;
    while (shared->want_cs[other_process_id] && (shared->turn == other_process_id));    
}

void exit_critical_zone(shm_layout *shared, PID self_process_id, PID other_process_id){
    shared->want_cs[self_process_id] = 0;
    shared->turn = other_process_id;
}

void process(shm_layout *shared, PID self_process_id, PID other_process_id){
    for (int i = 0; i < 10; i+ i++)
    {
    enter_critical_zone(shared,self_process_id,other_process_id);
    shared->counter++;
    printf("P%d: counter = %d\n",self_process_id,shared->counter);
    exit_critical_zone(shared,self_process_id,other_process_id);
    }
    exit(0);
}

int main(){
    int shmid = shmget(IPC_PRIVATE,sizeof(shm_layout),IPC_CREAT|0666);
    shm_layout* shared = shmat(shmid,NULL,0);
    if(fork() == 0 ) {process(shared,P0,P1);}
    if(fork() == 0 ) {process(shared,P1,P0);}
    wait(NULL);
    wait(NULL);
    printf("Final counter = %d\n",shared->counter);
    shmdt(shared);
    shmctl(shmid,IPC_RMID,NULL);
    return 0;
}