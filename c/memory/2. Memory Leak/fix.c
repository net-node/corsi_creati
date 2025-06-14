#include <stdlib.h>

void leak_memory() {
    int *ptr = malloc(100 * sizeof(int));
    // ... usa ptr ...
    free(ptr);
}

int main() {
    for (int i=0; i<100; i++) {
        leak_memory();
    }
}