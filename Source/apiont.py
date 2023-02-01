from owlready2 import *
import re
import graphics as gr
import random


def loadOntology(ontpath):
    """funzione che carica l'ontologia a partire dal filepath indiciato

    Args:
        ontpath (): filepath della posizione dell'ontolofia

    Returns:
        l'ontologia di Sp-AI-Ware
    """
    ontology = get_ontology(ontpath).load()
    return ontology

def uploadInstance(maltype,sha,ontpath):
    """funzione che carica nell'ontologia l'istanza del malware rilevato , fornendo sha e tipo di malware e sincronizza il reasoner Hermitt

    Args:
        maltype (): Stringa che indica il tipo di malware rilevato
        sha (): Stringa che identifica univocamnete l'istanza nell'ontologia
        ontpath (): filepath dell'ontologia

    Returns:
        True se tutto va a buon fine, False altrimenti
    """
    
    ontology = loadOntology(ontpath)
    upmal = ontology.search_one(label = maltype)(sha)
    upmal.sha.append(sha)
    upmal.label.append(str(sha))
    try:
        sync_reasoner(ontology)
        ontology.save(file=ontpath,format="rdfxml")
    except owlready2.base.OwlReadyInconsistentOntologyError:
        print("\nErrore: l'informazione inserita non e' consistente con la base di conoscenza\n")
        return False
    return True


def exploreClass(classes):
    """funzione che esplora con algoritmo Depth First Search le classi e sottoclassi dell'ontologia

    Args:
        classes (): Lista di classi da esplorare ricorsivamente

    Returns:
        la classe scelta dall'utente tra tutte quelle illustrate
    """
    j = 0
    for i in classes:
        print("["+str(j)+"]"+str(i.label))
        j+=1

    choice = gr.numericInput(0,len(classes)-1)
    sublist = list(classes[choice].subclasses())
    if len(sublist) == 0:
        return classes[choice]
    else:
        return exploreClass(sublist)






def uploadInfo(malware_ind,ontpath):
    """funzione per aggiungere nell'ontologia , ulteriori informazioni a riguardo di un istanza di malware, come ad esempio il tipo di attacco, 
    propagazione ecc .

    Args:
        malware_ind (): istanza di cui si vuole aggiungere l'informazione
        ontpath (): filepath dell'ontologia

    Returns:
        : True se tutto va a buon fine
          False altrimenti       
    """
    
    
    
    ontology = loadOntology(ontpath)
    list_prop = list(ontology.object_properties())

    j = 0
    for i in list_prop:
        print("["+str(j)+"]"+str(i.label))
        j+=1

    choice = gr.numericInput(0,len(list_prop)-1)

    list_obj = list_prop[choice].range
    list_obj = list(list_obj[0].subclasses())
    objclass = exploreClass(list_obj)
    label = re.sub('[\[\]\'\"\s]', '', str(objclass.label)+str(malware_ind.sha))
    objind = objclass(re.sub('[\[\]\'\"\s]', '', str(objclass.label)+str(random.randint(0,9999))))
    objind.label = label
    

    if choice == 0 :
        malware_ind.attack_type.append(objind)
    elif choice == 1 :
        malware_ind.attacks.append(objind)
    elif choice == 2 :
        malware_ind.combined_with.append(objind)
    elif choice == 3 :
        malware_ind.exploits.append(objind)
    elif choice == 4 :
        malware_ind.has_property.append(objind)
    elif choice == 5 :
        malware_ind.host_program.append(objind)
    elif choice == 6 :
        malware_ind.propagation.append(objind)
    elif choice == 8 :
        malware_ind.written_in.append(objind)
    
    try:
        sync_reasoner(ontology)
        ontology.save(file=ontpath,format="rdfxml")
    except owlready2.base.OwlReadyInconsistentOntologyError:
        print("\nErrore: l'informazione inserita non e' consistente con la base di conoscenza\n")
        return False
        
    return True

    
    
    
def alreadyScanned(ontpath,sha):
    """funzione per controllare se un eseguibile identificato dal suo sha e' gia' stato scansionato

    Args:
        ontpath (): filepath ontologia
        sha (): identificatore dell'eseguibile all'interno dell'ontologia

    Returns:
        True se il software e' stato scansionato, False altrimenti
    """
    ontology = loadOntology(ontpath)
    instance = ontology.search_one(sha=sha)
    if instance == None:
        return False
    else:
        return True

def showInstanceInfo(ontpath,mal_ind):
    """funzione per mostrare le informazioni e le relazioni di un'istanza dentro la base di conoscenza

    Args:
        ontpath (): filepath dell'ontologia
        mal_ind (): istanza di cui estrapolare le informazioni
    """
    print("nome")
    print(mal_ind.label)
    print()
    print("tipo")
    print(str(mal_ind.__class__))
    loadOntology(ontpath)
    properties = list(mal_ind.get_properties())
    for i in properties:
            if len(str(i.label)) > 2:
                print("\n")
                print(i.label)
                for value in i[mal_ind]:
                    print(value.label)

def loadIndByLabel(ontpath,label):
    """funzione per caricare un istanza a partire dalla sua label nell'ontologia

    Args:
        ontpath (): filepath dell'ontologia
        label (): proprieta' rdfs:label posseduta dall'istanza

    Returns:
        ritorna l'istanza indicata dalla label se presente, False altrimenti
    """
    
    
    ontology = loadOntology(ontpath)
    instance = ontology.search_one(label=label)
    if instance == None:
        print("\nErrore: l'istanza cercata non esiste nella base di conoscenza\n")
        return False
    else:
        return instance
    
    
    
    
    
    
    
    
    