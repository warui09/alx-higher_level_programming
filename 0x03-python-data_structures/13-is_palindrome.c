#include "lists.h"

/**
 * is_palindrome - check is a singly linked list is a palindrome
 * @head: head of the singly linked list
 *
 * Return: 1 if list is palindrome, 0 otherwise
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t node = head->next;

	while(node->next)
	{
		printf("%d\n", node->n);
		node = node->next;
	}

	return (0);
}
