# quizzettone
Simulatore di esami, prende domande e risposte da un file per proporle in varie modalità

lanciare il file con
> python3 quizzettone.py

inserire in input il nome del file strutturato come da README.md (o il suo percorso se eseguito in directory diverse)


#### struttura file domande:
    le domande vengono lette da [tipologia] a '///' 
    il file termina con '!!!'
    l'ultima domanda deve essere scritta due volte

    [tipologia]
    [domanda]
    > [opzione 1] [risposta]
    ...
    > [opzione n] [risposta]
    ///
    
#### tipologia:
    "---" per le domande a scelta multipla
    "+++" per i vero - falso

#### risposta:
    0 se falsa / sbagliata
    1 se vera / corretta (da crocettare)
    !!! la risposta deve essere l'ultimo carattere della riga, non ci devono essere spazi !!!

#### opzioni:
    il codice funziona con 5 opzioni, modificare la condizione a riga 153 per cambiare

##### es:
    +++
    V - F
    > opzione vera 1
    > opzione falsa 0
    ///
    ---
    Domanda
    > opzione corretta 1
    > opzione sbagliata 0 
    ///
