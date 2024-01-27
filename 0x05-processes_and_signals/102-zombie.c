#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - This will Run an infinite while loop.
 *
 * Return: return 0.
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - This will Creates five zombie processes.
 * Return: Always 0.
 */

int main(void)
{
	pid_t child_pid;
	char zombie_count = 0;

	while (zombie_count < 5)
	{
		child_pid = fork();
		if (child_pid > 0)

		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
            		zombie_count++;
		}

	else

		 exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
