
# ENCOMP

 - COS'È ENCOMP

**ENCOMP** è un metodo di compressione a dizionario, sviluppato su linguaggio **Python**.
***
 - COME FUNZIONA

Esso sfrutta una lista di **279.894** parole italiane, ordinate in ordine di lunghezza crescente, detto “*dizionario*”, per comprimere frasi o parole di qualsiasi lunghezza, sintatticamente corrette e non. 

Il programma le renderà incomprensibili agli occhi di chi non ha in possesso il “dizionario”, rendendo questo metodo di compressione anche un efficiente metodo di codifica.
***
 - PSEUDOCODIFICA
> Supponiamo che dovessimo comprimere e codificare la parola
> “comparati”.
> Inseriamo la parola “comparati” all’interno dello script Python.
> Il programma andrà a ricercare nel “dizionario” la medesima parola e
> ne riporterà la posizione nella lista di parole.
> 
> . . .
> 
> 91.210 comparata
> 
> 91.211 comparate
> 
> 91.212 comparati <<<
> 
> 91.213 comparato
> 
> 91.214 comparira
> 
> . . .
> 
> La parola “comparati” è situata nella posizione 91.212.
> 
> Possiamo notare come, utilizzando solamente questa prima conversione,
> questo metodo sia riuscito a risparmiare 4 caratteri. (“comparati” >>>
> “91212”)
> 
> Il programma converte poi questo numero da decimale a esadecimale.
> 
> (“91212” >>> “1644c”)
> 
> In questo caso il numero di caratteri non è stato ridotto ma se la
> posizione fosse stata “12389”, convertita in esadecimale, risulterebbe
> uguale a “3065”, risparmiando ulteriori caratteri.
> 
> Gli accenti della stringa inserita verranno rimossi.
> 
> La punteggiatura della stringa inserita verrà rimossa.
> 
> Le lettere maiuscole verranno trasformate in minuscole.
> 
> Nel caso la stringa inserita contenesse numeri, si procederà
> convertendo il numero in esadecimale, aggiungendo un punto esclamativo
> “!” dopo l’ultima cifra.
> 
> (“2021” >>> “7e5!”)
> 
> Il numero non verrà compresso.
> 
> Le parole con errori grammaticali o non esistenti all’interno della
> lista verranno riportate come originali.
> 
> (“compartai” >> “compartai”)

***
 - LIMITI

**ENCOMP**, attualmente, supporta solamente la lingua italiana, ma non si esclude che altre lingue possano essere aggiunte in futuro.

Questo metodo di compressione è basato su un dizionario, di conseguenza gli accenti della stringa inserita verranno rimossi, la punteggiatura della stringa inserita verrà rimossa, le lettere maiuscole verranno trasformate in minuscole. In futuro questo potrà cambiare e proprio per questo motivo, attualmente, è una compressione lossy.
***

 - VANTAGGI

Uno degli aspetti più vantaggiosi di **ENCOMP** è quello di lasciare il file compresso in un file con formato “.txt” evitando modifiche di estensioni che potrebbero causare l’aumento delle dimensioni del file.

Di seguito si mostrano le comparazioni tra **7zip, WinZip e ENCOMP**.



File Originale: 381 byte
7z: 391 byte
WinZip: 351 byte
ENCOMP: 248 byte

La compressione **ENCOMP**, tra le 3, *risulta la migliore*.



**Il contenuto del file originale è**: “

> Esso sfrutta una lista di 279.894 parole italiane, ordinate in ordine
> crescente di lunghezza, detto “dizionario”, per comprimere frasi o
> parole di qualsiasi lunghezza, sintatticamente corrette e non. Il
> programma le renderà incomprensibili agli occhi di chi non ha in
> possesso il “dizionario”, rendendo questo metodo di compressione anche
> un efficiente metodo di codifica.

”

**Il contenuto del file compresso con il metodo ENCOMP è**: “

> 32a a209 111 1360 c 44556! 3f7b ef10 ff13 1a 3e14 167ae c 19189 d9b
> "dizionario" e2 215ca 1017 4 3f7b c 1afc9 19189 42ed8 d340 2 cc 19
> 1adbe 1e 977f 424ab 145 164c c 6e cc 17 1a 10887 19 "dizionario" 10f6c
> 42aa 3a96 c 354c9 83d 32 22307 3a96 c d058

”

**Il contenuto del file decompresso è**: “

> esso sfrutta una lista di 279894 parole italiane ordinate in ordine
> crescente di lunghezza detto "dizionario" per comprimere frasi o
> parole di qualsiasi lunghezza sintatticamente corrette e non il
> programma le rendera incomprensibili agli occhi di chi non ha in
> possesso il "dizionario" rendendo questo metodo di compressione anche
> un efficiente metodo di codifica

”

In futuro **ENCOMP** verrà migliorato, integrando anche la punteggiatura, le lettere maiuscole e gli accenti.
