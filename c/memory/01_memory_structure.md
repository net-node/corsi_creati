## Struttura della memoria
```
+---------------------+  Indirizzi alti
|       Stack         |  (Variabili locali, cresce verso il basso)
|---------------------|  - Variabili locali
|         ↓           |  - Chiamate a funzione
|                     |
|         ↑           |
|---------------------|
|       Heap          |  (Memoria dinamica, cresce verso l'alto)
|---------------------|  - malloc(), calloc()
|                     |  - Dati dinamici
|                     |
|---------------------|
|   Data Segment      |  (.data: variabili GLOBALI inizializzate | .bss: var. GLOBALI non inizializzate)
|---------------------|  Contiene:
|                     |  → Variabili GLOBALI inizializzate (es. `int x = 10;`)
|                     |  → Variabili GLOBALI non inizializzate (es. `int y;`)
|---------------------|
|   Text Segment      |  ← Il tuo codice binario eseguibile (read-only)
|                     |  cioè il codice macchina compilato delle tue funzioni
+---------------------+  Indirizzi bassi
```
### Stack, Heap, Data Segment e Text Segment: Sono Concetti Legati Solo al C o a Tutti i Linguaggi?

Questi concetti non sono esclusivi del C, ma sono fondamentali per come i computer gestiscono la memoria RAM a basso livello. Ecco una spiegazione chiara:
#### Sono Legati al C o al Computer?

    Sono un meccanismo del computer (CPU + sistema operativo), non solo del C.

    Tutti i linguaggi (Java, Python, C++, Rust, ecc.) usano questi segmenti di memoria, ma spesso li nascondono per comodità.

    Il C ti fa vedere esplicitamente come funziona la memoria, mentre altri linguaggi (es. Java/Python) lo gestiscono "dietro le quinte".

## 1. Stack (Memoria Automatica)

Cos'è:

    Una regione di memoria ordinata e prevedibile, gestita automaticamente dal compilatore.

    Usato per variabili locali e chiamate di funzione.

Come funziona:

    La memoria viene allocata/liberata automaticamente all'inizio/fine di un blocco di codice.

    Accesso ultra-veloce (la CPU gestisce lo stack direttamente).

Esempio:
```c

void funzione() {
    int x = 10;          // Allocato nello stack
    char c = 'A';        // Anche questo nello stack
} // Qui x e c vengono automaticamente deallocati
```
Caratteristiche:
✅ Vantaggi:

    Velocità (allocazione/deallocazione in 1 ciclo CPU).

    Nessun rischio di memory leak (gestione automatica).
    ❌ Limiti:

    Dimensione limitata (es. 1-8 MB, dipende dal sistema).

    La dimensione deve essere nota a compile-time.

### 2. Heap (Memoria Dinamica)

Cos'è:

    Una regione di memoria disordinata e flessibile, gestita manualmente dal programmatore.

    Usato per dati che devono persistere o hanno dimensione sconosciuta a compile-time.

Come funziona:

    Allocazione con malloc()/calloc(), liberazione con free().

    Accesso più lento (richiede lookup indiretto).

Esempio:
```c

int* crea_array(int n) {
    int* arr = malloc(n * sizeof(int));  // Allocato nell'heap
    return arr;
}

int main() {
    int* ptr = crea_array(100);
    free(ptr);  // Deallocazione manuale obbligatoria!
}
```
Caratteristiche:
✅ Vantaggi:

    Dimensione illimitata (dipende dalla RAM disponibile).

    Dimensione decisa a runtime.
    ❌ Limiti:

    Rischio di memory leak se non si usa free().

    Frammentazione della memoria.


📌 Caso 1: Perché usare lo stack?
```c

void calcola() {
    int risultato = 0;  // Variabile temporanea → perfetta per lo stack
    // ... calcoli ...
} // Risultato deallocato automaticamente
```
    Ideale per dati temporanei e a vita breve.

📌 Caso 2: Perché usare l'heap?
```c

int* leggi_file(const char* filename) {
    FILE* file = fopen(filename, "r");
    int size = ...;  // Dimensione sconosciuta a compile-time
    int* dati = malloc(size * sizeof(int));  // Heap necessario!
    // ... lettura dati ...
    return dati;  // Dati devono persistere dopo la funzione
}
```
    Necessario per dati grandi o che devono sopravvivere al scope.

### 3. Data Segment
A. Variabili Globali (allocazione nel Data Segment)
```c

#include <stdio.h>

int global_var = 10;         // .data (inizializzata)
static int static_var = 20;  // .data (inizializzata)
int uninit_var;              // .bss  (non inizializzata)

int main() {
    printf("%d\n", global_var);  // Output: 10
    printf("%d\n", uninit_var);  // Output: 0 (default)
    return 0;
}
```
B. Variabili Locali vs Globali
```c

void function() {
    static int local_static = 5;  // Anche questa è nel Data Segment!
    int local_stack = 10;         // Questa è nello stack
}
```
    local_static persiste tra le chiamate a funzione (memoria nel .data).

    local_stack viene distrutta alla fine della funzione (memoria nello stack).

#### Confronto con Altri Segmenti
#### A. Data Segment vs Stack
```c

int global = 10;  // Data Segment

void foo() {
    int stack_var = 20;  // Stack
}
```
    global esiste sempre, stack_var viene distrutta alla fine di foo().

#### B. Data Segment vs Heap
```c

int *heap_var = malloc(sizeof(int));  // Heap
*heap_var = 30;
```
    heap_var deve essere liberato manualmente con free(), mentre le variabili globali no.

### 4. Text Segment
```c

#include <stdio.h>

int main() {
    printf("Hello, Text Segment!\n");  // Questa istruzione vive nel Text Segment!
    return 0;
}
```
Quando compili questo codice, l'istruzione printf viene convertita in linguaggio macchina e memorizzata nel Text Segment.