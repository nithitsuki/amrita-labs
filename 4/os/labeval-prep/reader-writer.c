#include <stdio.h>

int mutex = 1;
int rw_mutex = 1;
int readcount = 0;

// wait function
void wait(int *s)
{
    while (*s <= 0){
        ; // busy wait
    }
    (*s)--;
}

// signal function
void signal(int *s)
{
    (*s)++;
}

// reader function
void reader(int id)
{
    wait(&mutex);
    readcount++;

    if (readcount == 1)
        wait(&rw_mutex);

    signal(&mutex);

    printf("Reader %d is reading\n", id);

    wait(&mutex);
    readcount--;

    if (readcount == 0)
        signal(&rw_mutex);

    signal(&mutex);
}

// writer function
void writer(int id)
{
    wait(&rw_mutex);

    printf("Writer %d is writing\n", id);

    signal(&rw_mutex);
}

int main()
{
    int r, w, i;

    printf("Enter number of readers: ");
    scanf("%d", &r);

    printf("Enter number of writers: ");
    scanf("%d", &w);

    // simulate readers
    for (i = 1; i <= r; i++)
        reader(i);

    // simulate writers
    for (i = 1; i <= w; i++)
        writer(i);

    return 0;
}