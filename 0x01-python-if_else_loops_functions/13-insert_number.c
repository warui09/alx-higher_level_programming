#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: head of the linked list
 * @number to insert
 *
 * Return: address of new node or NULL if failed
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	
	new_node->n = number;
	new_node->next = NULL;
	
	if (!*head || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	
	while (current->next && current->next->n < number)
		current = current->next;
	
	new_node->next = current->next;
	current->next = new_node;
	
	return (new_node);
}
