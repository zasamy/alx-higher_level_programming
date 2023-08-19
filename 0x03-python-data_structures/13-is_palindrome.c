#include "lists.h"
/**
 * is_palindrome - sees if list is palidrome
 * @head: pointer to start
 * Return: conditions of result
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_palindrome(head, *head));
}

/**
 * check_palindrome - checks the function
 * @head: pointer to start
 * @last: pointer to finish
 * Return: conditions of result
 */
int check_palindrome(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_palindrome(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
