#include <stdio.h> // printf, scanf
#include <stdlib.h> // malloc

void memory_leak(int n) {
    int* ptr = malloc(n * sizeof(int));  // (se int = 4 byte) Alloca (n * 4)byte
    // ... usa ptr ...
    // Dimenticato free(ptr)!
}  // ptr esce dallo scope, ma i (n * 4)byte restano bloccati

int main() {
    int n=0;
    printf("Size of array? ");
    scanf("%d", &n);
    for (int i=0; i<1000; i++) {
        memory_leak(n);
    }
}
