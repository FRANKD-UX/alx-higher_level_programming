#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list */
struct listint_s
{
    int n;
    struct listint_s *next;
};
typedef struct listint_s listint_t;

/* Function to reverse a linked list */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;
    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev;
}

/* Function to check if two linked lists are identical */
int compare_lists(listint_t *head1, listint_t *head2)
{
    while (head1 != NULL && head2 != NULL)
    {
        if (head1->n != head2->n)
        {
            return 0;
        }
        head1 = head1->next;
        head2 = head2->next;
    }
    return (head1 == NULL && head2 == NULL);
}

/* Function to check if a singly linked list is a palindrome */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow, *second_half, *mid_node = NULL;
    int result;

    if (*head == NULL || (*head)->next == NULL)
    {
        return 1;
    }

    /* Initialize pointers */
    slow = *head;
    fast = *head;
    prev_slow = NULL;

    /* Find the middle of the linked list */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    /* Handle odd-sized lists */
    if (fast != NULL)
    {
        mid_node = slow;
        slow = slow->next;
    }

    second_half = slow;
    prev_slow->next = NULL;

    /* Reverse the second half of the list */
    second_half = reverse_list(second_half);

    /* Compare the first half and the reversed second half */
    result = compare_lists(*head, second_half);

    /* Restore the original list */
    second_half = reverse_list(second_half);

    if (mid_node != NULL)
    {
        prev_slow->next = mid_node;
        mid_node->next = second_half;
    }
    else
    {
        prev_slow->next = second_half;
    }

    return result;
}

