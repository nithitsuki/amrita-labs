// Write a program where a parent stores the number 7 in shared memory, forks a child, and the child prints it. Include cleanup.

//A parent writes the string "hello" into shared memory. The child reads it and writes it to a file called out.txt using fprintf. Sketch the key lines (no need for full boilerplate).

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#include <sys/shm.h>
#include <sys/wait.h>

typedef struct shm_data {
    int shared_num;
    bool done_using;
    char* flag;
} shm_data;
#define SHMSIZE sizeof(shm_data)

int main() {
    int shmid = shmget(IPC_PRIVATE,SHMSIZE,IPC_CREAT|0666);
    void* shm_ptr = shmat(shmid,NULL,0);
    shm_data* s = shm_ptr;
    s->shared_num = 7;
    s->done_using = false;
    char flag[] = "bi0sblr{5HM_1Z_C00L}";
    s->flag = malloc(sizeof(flag));
    strcpy(s->flag,flag);
    int pid = fork();
    if(pid == -1){
        perror("FORK FAILED\n");
    }
    if(pid==0){
        printf("This is child process of parent %d\n",getppid());
        printf("The shared number is %d\n",s->shared_num);
        printf("writing %s to out.txt",s->flag);
        FILE* f_ptr = fopen("out.txt","w"); 
        fprintf(f_ptr,"%s",flag);
        s->done_using = true;
        exit(0);
    }
    else{
        printf("This is parent process\n");
        wait(NULL);
        shmdt(shm_ptr);
        shmctl(shmid,IPC_RMID,NULL);
    }
    return 0;
}