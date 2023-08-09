#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle
 * @list: list to check
 *
 * Return: 0 if there is no cycle. 1 if there is
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *n = list;

	while (n->next)
	{
		if (n->next == list)
			return (0);
		n = n->next;
	}
	return (1);
}
