#include "lists.h"
/**
 * check_cycle - Checks for a linked list
 * @list: A pointer to the list
 *
 * Return: 1 if there is a cycle, 0 if there isn't a cylce
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
