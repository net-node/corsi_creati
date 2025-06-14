#include <stdio.h> // printf, scanf
#include <stdlib.h> // malloc

void fix_memory_leak() {
    int n=0;
    printf("Size of array? ");
    scanf("%d", &n);
    int *ptr = malloc(n * sizeof(int));  // (se int = 4 byte) Alloca (n * 4)byte
    // ... usa ptr ...
    free(ptr); // libero la memoria dello heap!
}

int main() {
    for(int i=0; i<1000; i++) {
        fix_memory_leak();
    }
}