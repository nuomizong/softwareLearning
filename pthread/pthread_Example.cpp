#include <pthread\pthread.h>
#include <cstdio>
#include <cstdlib>
#define NUM_THREADS     5

#pragma comment(lib, "pthreadVC2.lib") 

void* PrintHello(void *threadid)
{
	long tid;
	tid = (long)threadid;
	std::printf("Hello World! It's me, thread #%ld!\n", tid);
	pthread_exit(NULL);
	return 0; // added by nuomizong~
}

int main (int argc, char *argv[])
{
	pthread_t threads[NUM_THREADS];
	int rc;
	long t;
	for(t=0; t<NUM_THREADS; t++)
	{
		std::printf("In main: creating thread %ld\n", t);
		rc = pthread_create(&threads[t], NULL, PrintHello, (void *)t);
		if (rc)
		{
			std::printf("ERROR; return code from pthread_create() is %d\n", rc);
			std::exit(-1);
		}
	}

	/* Last thing that main() should do */
	pthread_exit(NULL);
}

