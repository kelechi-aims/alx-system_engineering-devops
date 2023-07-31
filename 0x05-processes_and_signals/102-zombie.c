#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Function to stimulate an infinite loop
 * Return: 0 on success
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
 * main - Entry point of the function
 * Return: 0 on success
 */
int main(void)
{
	pid_t zombie_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid == 0)
			exit(0);
		else if (zombie_pid > 0)
			printf("Zombie process created, PID: %d\n", zombie_pid);
		else
		{
			perror("fork");
			return (1);
		}
	}
	infinite_while();
	return (0);
}
