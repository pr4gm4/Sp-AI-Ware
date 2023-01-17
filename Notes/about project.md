j










come implementare il ragionamento automatico nel progetto ? 
con delle domande all'utente per avere piu informazioni -> che domande ? 
il reasoner riuscirebbe a inferire certe cose ? ad esempio : se l'utente specifica che e' un file eseguibile .exe , il reasoner capisce che e' un sistema windows ? 
come si potrebbe amalgamare il dataset originario e il dataset della base di conoscenza ? -> forse potrebbero essere distinti e fatto in modo di avewre 2 classificazioni cioe :

1) l'utente introduce il record dell'eseguibile 
2) se positivo , il sistema chiede dettagli per il secondo dataset che viene avvalorato a partire dalla owl
3) in futuro se l'utente descrivera' caratteristiche simili avra' una seconda classificazione piu' specifica 
qui ad esempio potrebbero uscire tutte le info sul malware probabile come nome, descrizione , modalita' d'attacco e tutte le cose che un utente normale potrebbe capire
quindi evitando di scrivere paroloni che manco io capisco

in tutti i casi andrebbe creata un ontologia e bisogna cercare di metterci owlready2 per manipolarla con python , almeno per fare le istanze

come si collegano le domande che faccio all'utente alla base di conoscenza owl ? =>

quando il sistema chiede le domande all'utente , quando il sistema capisce che tipo di caratteristiche ha, crea un istanza del malware sulla base di conoscenza 
fornendo tutti i dettagli proposti . potrebbe funzionare 

c'e' qualcosa che non mi convince , nel senso che non c'e' un vero e proprio ragionamento sulla base di conoscenza o nei dataset 

devo cercare di capire bene come funziona il reasoner come hermit o altri senno' so cazzi 

dopo aver trovato il tipo di classificazione specifica, e' buono magari chiedere maggiori informazioni per la base di conoscenza in modo che hermit o un reasoner possano inferire nuove cose 
