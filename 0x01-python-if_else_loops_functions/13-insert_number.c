#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list of numbers
 * @head: address of head to the list
 * @number: number to be added
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *previous, *tmp;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!*head)
	{
		*head = new;
		return (new);
	}
	tmp = *head;
	if ((*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (tmp && (tmp->n < number))
	{
		previous = tmp;
		tmp = tmp->next;
	}
	new->next = tmp;
	previous->next = new;
	return (new);
}
