#include <stdio.h>
#include <stdlib.h>

typedef struct Nodo {
    int data;
    struct Nodo* next;
} Nodo;

int main(){
    Nodo* head = malloc(sizeof(Nodo));
    head->data = 101;

    head->next = malloc(sizeof(Nodo));
    head->next->data = 202;

    printf("Linked List:\n");
    printf("%d -> %d\n", head->data, head->next->data);

    Nodo* current = head;
    while(current->next != NULL) {
        Nodo* temp = current;
        current = current->next;
        free(temp);
    }
    return 0;
}


// Array vs Linked List
