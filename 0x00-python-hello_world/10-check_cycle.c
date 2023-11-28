#include "lists.h"

/**
 * check_cycle - function to check if linked list a cycle
 *
 * @list: the linked list
 *
 * Return: true if a cycle, false if not
*/

int check_cycle(listint_t *list)
{
	listint_t *fixed = list;
	listint_t *temp = list;

	while (temp)
	{
		temp = temp->next;
		if (temp == fixed)
			return (1);
	}
	return (0);
}

