## Memory Leak (Perdita di Memoria)

Esempio con Memory Leak
```c
#include <stdlib.h>

void funzione_pericolosa() {
    int *ptr = malloc(100 * sizeof(int));  // Alloca 400 byte (se int = 4 byte)
    // ... usa ptr ...
    // Dimenticato free(ptr)!
}  // ptr esce dallo scope, ma i 400 byte restano bloccati
```
Cosa succede in memoria:

    Dopo la chiamata a funzione_pericolosa, il puntatore ptr viene distrutto (perché è una variabile locale), ma i 400 byte allocati rimangono occupati.

    Non puoi più accedere a quella memoria (perché hai perso il puntatore), ma il sistema operativo non la riutilizzerà finché il programma non termina.

Se Chiami funzione_pericolosa() più volte:
```c
for (int i = 0; i < 1000; i++) {
    funzione_pericolosa();  // Perde 400 byte a ogni chiamata!
}
```
Dopo 1000 chiamate, 400 KB di memoria sono persi!

Il programma diventa sempre più lento e potrebbe crashare per esaurimento memoria.

### Conseguenze di un Memory Leak

Nei programmi brevi: Non è un grosso problema (la memoria viene liberata quando il programma termina).

Nei programmi lunghi/demonio:

    La memoria occupata cresce indefinitamente.

    Il sistema operativo potrebbe uccidere il processo.

    Nei dispositivi embedded (es. schede elettroniche), può causare crash irreversibili.

### Come Evitare Memory Leak?
A. Sempre usare free()
```c
void funzione_sicura() {
    int *ptr = malloc(100 * sizeof(int));
    // ... usa ptr ...
    free(ptr);  // Libera la memoria prima di uscire!
}
```
B. Usare strumenti di debug

Valgrind (Linux/macOS):
```bash
valgrind --leak-check=full ./tu_programma
```
Ti mostra esattamente dove hai dimenticato free().

AddressSanitizer (gcc/clang):
```bash
gcc -fsanitize=address -g tuo_file.c
./a.out
```
### Esempio Reale
Con Memory Leak ❌
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = malloc(5 * sizeof(int));  // Alloca 20 byte
    arr[0] = 10;
    printf("%d\n", arr[0]);
    // Dimenticato free(arr)!
    return 0;
}
```
Check con Valgrind:

LEAK SUMMARY:
    definitely lost: 20 bytes in 1 blocks

Senza Memory Leak ✅
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = malloc(5 * sizeof(int));
    arr[0] = 10;
    printf("%d\n", arr[0]);
    free(arr);  // Memoria liberata correttamente
    return 0;
}
```
    Check con Valgrind:
    
    All heap blocks were freed -- no leaks are possible

### Casi Particolari
Se perdi il puntatore prima di free()
```c
int *ptr = malloc(100);
ptr = NULL; // Sovrascrivi ptr senza free() → memory leak!
// Ora non puoi più chiamare free(ptr) perché ptr non punta più alla memoria allocata.
```

Regola d'oro

    Ogni malloc() deve avere un free() corrispondente.

### Riassunto

    free() dimenticato → Memory leak → memoria persa finché il programma non termina.
    Strumenti come Valgrind aiutano a trovare leak.
    Nei sistemi critici (es. medicale, aerospaziale), i memory leak possono essere disastrosi.
