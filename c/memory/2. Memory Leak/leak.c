#include <stdlib.h>

void leak_memory() {
    int n=0;
    printf("Size of array? ");
    scanf("%d", &n);
    int *ptr = malloc(n * sizeof(int));  // Alloca 400 byte (se int = 4 byte)
    // ... usa ptr ...
    // Dimenticato free(ptr)!
}  // ptr esce dallo scope, ma i 400 byte restano bloccati

int main() {
    leak_memory();
}