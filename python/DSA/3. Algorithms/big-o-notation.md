
## Cosa significa "Big O Notation"?
La O sta per "Ordine di" e indica il tempo (o spazio) che un algoritmo impiega, quando i dati crescono.

Se diciamo "Questo algoritmo è O(n)", significa che il suo tempo di esecuzione cresce nell’ordine di n (cioè in modo lineare).

### Tipi
#### O(1) - Tempo costante
    Esempio: Accedere a un elemento di un array tramite indice.
    Non importa quanto è grande l'array, ci vuole sempre lo stesso tempo/spazio.

#### O(log n) - Crescita logaritmica
    Esempio: Ricerca binaria in un array ordinato.
    Anche se *n* raddoppia, il tempo/spazio aumenta solo di un passo in più.

#### O(n) - Crescita lineare
    Esempio: Cercare un elemento in un array non ordinato (scansione uno per uno).
    Se l'array raddoppia, anche il tempo/spazio raddoppia.

#### O(n²) - Crescita quadratica
    Esempio: Bubble Sort (confronti a coppie annidati).
    Se *n* diventa 10 volte più grande, il tempo/spazio diventa ~100 volte più grande!


#### Altri esempi nella vita reale:

    O(1): Accendere la luce (è sempre immediato).

    O(log n): Cercare una parola nel dizionario (saltando le pagine).

    O(n): Trovare un amico in fila (controllare uno per uno).

    O(n²): Stringere la mano a tutti a una festa (ognuno con tutti).

![big o notation graph](./big-o.png)

### Perché è utile?
- Confrontare algoritmi: Ci aiuta a scegliere la soluzione più efficiente.
- Prevedere le prestazioni: Capire come si comporterà l'algoritmo con input grandi.
- Ottimizzare il codice: Identificare i colli di bottiglia.

