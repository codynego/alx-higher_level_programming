#include lists.h

/**
 * insert_node - inserts a number into a sorted linked list
 * 
 * @head: the beginning of the list
 * @number: the number to be inserted
 *
 * return: returns the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	current = NULL;
	pin = NULL;
	pin = (listint_t)malloc(sizeof(listint_t));
	current = (listint_t)malloc(sizeof(listint_t));
	current = *head;
	head_addr = &head

	pin->n = number;
	pin->next = NULL;

	if *head == NULL
	{
		*head = pin;
	}
	else
	{
		if (current->n < number && current->next->n > number)
		{
			current->next = pin;
			pin->next = current->next;
		}
		else
		{
			current = current->next;
		}
	}

	return head_addr;
}
