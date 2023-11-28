#include "lists.h"

int check_cycle(listint_t *list){
	listint_t *fixed = list;
	listint_t *temp = list;

	while(temp){
		temp = temp->next;
		if(temp == fixed)
			return 1;
	}
	return 0;
}
