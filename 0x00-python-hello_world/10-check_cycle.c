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
	listint_t *slow = list;
	listint_t *fast = list;
	
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		
		if (slow == fast)
			return (1);
	}
	
	return (0);
}

