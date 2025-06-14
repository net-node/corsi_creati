#include <stdio.h> // printf, scanf
#include <stdlib.h> // malloc

int main() {
    int n=0;
    printf("Size of array? ");
    scanf("%d", &n);

    int* ptr = malloc(n * sizeof(int));
    ptr[0] = 101;

    printf("%d\n", ptr[0]);
}

// uscita dello scope
// n, ptr distrutti dallo stack
