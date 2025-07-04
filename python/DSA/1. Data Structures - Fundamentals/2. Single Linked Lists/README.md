## La teoria in C
### Array e Linked List
```c
#include <stdio.h>

int main() {
    int arr[3];
}
```

### Layout in Memoria (RAM)
    Indirizzo di memoria   |   Dato (4 byte per int)
    -----------------------|------------------------
    0x1000                 |   arr[0] (non inizializzato)
    0x1004                 |   arr[1] (non inizializzato)
    0x1008                 |   arr[2] (non inizializzato)

Ogni int occupa 4 byte contigui (gli indirizzi sono consecutivi: 0x1000, 0x1004, 0x1008).
Se int occupasse 2 byte (sistemi embedded), gli indirizzi sarebbero 0x1000, 0x1002, 0x1004.

Se assegniamo valori:

```c
arr[0] = 10;  // 0x0000000A (hex)
arr[1] = 20;  // 0x00000014
arr[2] = 30;  // 0x0000001E
```

La RAM diventa:

    Indirizzo   |   Byte 3   Byte 2   Byte 1   Byte 0   |   Valore (int)
    ------------|---------------------------------------|----------------
    0x1000      |   00       00       00       0A       |   10 (arr[0])
    0x1004      |   00       00       00       14       |   20 (arr[1])
    0x1008      |   00       00       00       1E       |   30 (arr[2])

- little-endian:  I byte sono salvati in ordine inverso (il meno significativo per primo)

### Python List
```python
my_list = [2, 3, 4]

# Insert at head (all elements shift right → O(n))
my_list.insert(0, 1)  # [1, 2, 3, 4]

# Delete at head (all elements shift left → O(n))
my_list.pop(0)  # [2, 3, 4]

"""While appends and pops from the end of list are fast,
doing inserts or pops from the beginning of a list is slow
(because all of the other elements have to be shifted by one).
[https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues]
"""

```
    Problem: If you do this THOUSANDS of times, it becomes inefficient.

### Array e Frammentazione
Problema degli Array/Liste Contigue

    Gli array (e le liste contigue come Python list) richiedono blocchi di memoria contigua.

    Se hai un array grande e lo elimini/ridimensioni spesso, lasci "buchi" nella memoria:
    python

    # Esempio: un array di 1 MB viene liberato, ma la RAM ora ha un "buco" da 1 MB
    arr = [0] * 10**6  # Alloca 1 MB contiguo
    del arr             # Libera 1 MB, ma può non essere riutilizzabile per allocazioni più piccole

    Risultato: La memoria si frammenta, e anche se c’è spazio libero totale, non puoi allocare un nuovo array grande perché non c’è un blocco contiguo sufficiente.

Perché è un Problema?

    Se il sistema operativo non riesce a trovare un blocco contiguo per un nuovo array, devi:

        Spostare dati in memoria (costoso).

        Fallire l’allocazione (out-of-memory, anche se teoricamente c’è spazio).

### Usare una Linked List (Veloce per operazioni sulla Head)
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):  # O(1)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_head(self):  # O(1)
        if self.head:
            self.head = self.head.next

# Usage
ll = LinkedList()
ll.insert_at_head(2)  # 2 → None
ll.insert_at_head(1)  # 1 → 2 → None
ll.delete_at_head()   # 2 → None
```
    Advantage: No shifting! Just pointer updates → Much faster if done repeatedly.

### Single Linked List in C
```c
#include <stdio.h>
#include <stdlib.h>

// Definizione del nodo
struct Nodo {
    int dato;
    struct Nodo *next;  // Puntatore al prossimo nodo
};

int main() {
    // Creazione nodi
    struct Nodo *n1 = malloc(sizeof(struct Nodo));
    struct Nodo *n2 = malloc(sizeof(struct Nodo));
    struct Nodo *n3 = malloc(sizeof(struct Nodo));

    n1->dato = 10; n1->next = n2;
    n2->dato = 20; n2->next = n3;
    n3->dato = 30; n3->next = NULL;

    // Stampa
    struct Nodo *current = n1;
    while (current != NULL) {
        printf("%d ", current->dato);
        current = current->next;
    }

    // Libera memoria
    free(n1);
    free(n2);

    return 0;
}
```

La RAM diventa:

    Indirizzo   |   Dato (Nodo)          |   Puntatore (next)  
    ------------|------------------------|-------------------
    0x2000      |  10                   |  0x3000 → (punta al nodo 2)
      ...       |  [Altri dati non correlati]  ← La memoria è frammentata!
    0x3000      |  20                   |  0x4000 → (punta al nodo 3)
    0x4000      |  30                   |  NULL (fine lista)
      ...       |  [Altri dati non correlati]  ← La memoria è frammentata!

### Linked List e Frammentazione
Problema delle Linked List

    Le linked list non richiedono memoria contigua: ogni nodo vive in un punto qualsiasi della RAM.

    Non causano frammentazione della memoria fisica, perché il sistema operativo può allocare i nodi dove c’è spazio libero.

    Ma hanno un altro tipo di frammentazione:

        Overhead dei puntatori: Ogni nodo spreca memoria per next/prev.

        Cache misses: I nodi sparsi in RAM rallentano l’accesso (nessuna località di riferimento).

## Perché Python Non Usa Linked List per Tutto?
- Accesso casuale: Le linked list sono lente per operazioni come lista[1000] (O(n)).
- Cache locality: Gli array sono più veloci perché i dati sono vicini in memoria (le linked list no).
- Python usa deque: Una via di mezzo (lista doppiamente linkata con ottimizzazioni).

## Python
While Python’s built-in list covers most needs, singly linked lists are useful when:
1. You need frequent insertions/deletions at the head.
2. You want memory-efficient dynamic growth (no reallocation).
3. You’re implementing stacks, queues, or functional structures.
4. You’re solving linked-list-specific algorithms (e.g., cycle detection).

# 1. You need frequent insertions/deletions at the head.
Che significa "Inserire/eliminare nella/dalla Head" frequentemente?
Significa aggiungere/rimuovere in testa alla lista in modo frequente.

Perchè è importante?
    In a Python list (dynamic array), inserting/deleting at the head is slow (O(n)) because all other elements must be shifted.

    In a singly linked list, inserting/deleting at the head is fast (O(1)) because you just update a pointer.

## Applicazioni nella vita reale
### Real-Time Transaction Logs (Order Matters, Fast Writes)

    Esempio: un sistema che logga le transazioni in tempo reale.

    Le nuove transazioni sono aggiunte nel head (la più recente è la prima).

    Una linked list permette O(1) inserimenti per transazione.

    Anche list.append() è O(1), ma se la lista deve mantenere l'ordine LIFO (Last In First Out)
    una linked list evita il reversing necessario a "list".

```python
class TransactionLog:
    def __init__(self):
        self.head = None  # Most recent transaction

    def add_transaction(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

log = TransactionLog()
log.add_transaction("Deposit €100")
log.add_transaction("Withdraw €50")  # Newest is always at head.
```

### Polynomial Arithmetic (Sparse Representations)

    Esempio: librerie matematiche "simboliche" come "sympy" rappresentano i polinomi in modo efficiente.

    Polinomi come "3x² + 5x + 1" vengono storati come termini "linkati".

    sommare/moltiplicare polinomi è più facile con le linked list che con gli array (non si spreca spazio per gli esponenti che mancano).

```python
class PolynomialTerm:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None

# 3x² + 5x + 1
poly = PolynomialTerm(3, 2)
poly.next = PolynomialTerm(5, 1)
poly.next.next = PolynomialTerm(1, 0)
```

### Sound Playlist (Dynamic Reordering)

    Esempio: Una playlist dove le tracce sono spostate/inserite frequentemente

    Cancellare una traccia dal mezzo della playlist
    e inserirla altrove è O(1) con i puntatori
    (invece che O(n) con le list in Python)

    E' pratico nello streaming audio a bassa latenza:
    - Inserimento/rimozione rapida: Se l’audio è organizzato in una linked list, spostare una traccia (es. per inserire una pubblicità) non causa ritardi.
    - Nessuna riallocazione di memoria: Le liste Python potrebbero dover ridimensionarsi, introducendo micro-ritardi.

```python
class Track:
    def __init__(self, name):
        self.name = name
        self.next = None

playlist = Track("Lesson-1.mp3")
playlist.next = Track("Lesson-2.mp3")
new_track = Track("Lesson-3.mp3")
new_track.next = playlist.next # "Lesson-3.mp3" -> "Lesson-2.mp3"
playlist.next = new_track # "Lesson-1.mp3" -> "Lesson-3.mp3" -> "Lesson-2.mp3"
```

### Garbage Collection (Reference Tracking)

    Esempio: il Garbage Collector (GC) di Python traccia gli oggetti in memoria.

    Le Linked List gestiscono in modo efficiente set di oggetti non più usati, "morti" ("unreachable")
    Se il GC usasse un array per tenere traccia degli oggetti, rimuovere un elemento "morto" richiederebbe:
    - Spostare tutti gli elementi successivi (O(n)).
    - Riallocare memoria se l’array cresce.

    Perché è Importante?
    - Efficienza: In Python, il GC lavora spesso in background. Usare strutture O(1) evita rallentamenti.
    - Memoria non contigua: Le linked list non hanno problemi di frammentazione della memoria.

    Con le Linked List eliminare oggetti "morti" costa O(1) per nodo.

```python
class ObjectNode:
    def __init__(self, obj):
        self.obj = obj
        self.next = None


# Lista di oggetti gestita dal GC (A -> B -> C -> D)
head = ObjectNode("A")
head.next = ObjectNode("B")
head.next.next = ObjectNode("C")
head.next.next.next = ObjectNode("D")

# Se "B" diventa unreachable, il GC lo rimuove:
head.next = head.next.next  # Ora A -> C -> D
```

### Blockchain (Immutable Ledger)

    Esempio: ogni block in una blockchain punta al blocco precendente (come una linked list).

    Appending di nuovi blocchi è O(1).

    Tampering richiede il rebuild dell'intera catena (security feature).

```python
class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.next = None

blockchain = Block("Genesis", None)
blockchain.next = Block("Tx1", hash(blockchain))
```

### File System Directories (Hierarchical Structures)

    Esempio: I filesystem Unix reppresentano le directory come Linked List.
    
    Ogni entry nella directory punta al prossimo file/subdirectory.
    Efficiente per aggiungere/eliminare in modo dinamico.

### MRU Cache (Most Recently Used)

    Esempio: Caching systems (e.g., functools.lru_cache in Python).

    L'item più recentemente usato è messo in head (O(1) usando linked list + hashmap).
    OrderedDict di Python usa una simile idea internamente.

```python
class MRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.key_to_node = {}  # Hashmap for O(1) access

    def _move_to_head(self, node):
        # Remove node from current position
        # Insert at head (implementation omitted for brevity)
        pass
```

### Low-Level Network Packets (Kernel-Level Queues)

    Esempio: I driver di rete (network drivers) processano i pacchetti in ordine FIFO (First In First Out).

    Pacchetti arrivano in ordine casuale:
    - Pacchetto 3 (inizio del video).
    - Pacchetto 1 (intestazione).
    - Pacchetto 2 (metà del video).

    Il driver di rete:
    - Li inserisce in una linked list nell’ordine di arrivo.
    - Il protocollo TCP/IP si occupa di riordinarli prima di passarli al browser.

    Se usassimo una lista contigua (array):
    - Dovremmo spostare continuamente i dati per fare spazio.
    - Rallenterebbe la ricezione (specialmente con video 4K).

    Python asyncio.Queue usa concetti simili.

