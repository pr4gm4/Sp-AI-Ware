import pickle as pick
import numpy as np
import ifelsetree as ifel
import apiont as ont
import glob as gl
onto = ont.get_ontology("file://../Ontologies/Sp-AI-Ware-OWL.owl").load()

def printResults(model,xinput):
    print("\nRisultati per i diversi modelli:\n")
    for estimator in model.estimators_:
        print(estimator.__class__.__name__)
        print(estimator.predict(np.array([xinput,])))

    

def scanMetaData(query_set,model):
    
    count = 0
    for i in query_set.loc[:,"sha"]:
        print("programma->"+str(count)+" "+i)
        count+=1
        
    choice = input("\nscegliere uno dei seguenti programmi da analizzare (il codice sha identifica univocamente il programma)\n")

    program =query_set.loc[int(choice),:]

    shaprog = program["sha"]
    del program["sha"]
    
    y_pred = model.predict(np.array([program,]))
    if y_pred == 1 :
        print("\nATTENZIONE: il programma selezionato ha avuto esito positivo ed e' probabilmente un Malware\n")
        printResults(model,program)
        print("\nRisultato finale del modello a Stack\n")
        print(y_pred)
        while True:
            print("\nVuoi fornire ulteriori dati da caricare sulla base di conoscenza online?\n")
            print("\n[1] Si\n[2] No\n")
            choice = int(input())  
            
            if choice == 1:
                maltype =ifel.questionTree()
                if ont.uploadInstance(maltype,shaprog,onto) == True:
                    print("\nInformazioni caricate correttamente nella base di conoscenza online\n")
                    print("\nIl malware e le relative informazioni sono state caricate sulla base di conoscenza online, tuttavia fornendo specifici dettagli del suo funzionamento potrebbe aiutare te e gli altri utilizzatori di Sp-AI-Ware a riconoscere i sintomi del Malware e a informarsi con maggior dettaglo, vuoi fornire queste informazioni?(Attenzione: le informazioni da fornire potrebbero risultare piuttosto tecniche, si consiglia di inserirle qualora si abbiano le competenze tecniche necessarie)\n")
                    print("\n[1] Si\n[2] No\n")
                    choice = int(input())
                    if choice == 1:
                        pass
                    elif choice ==2:
                        pass
                    else:
                        print("\nscelta non valida\n")
                        break
                    onto.save(file=gl.ONTPATH,format="rdfxml")


            elif choice == 2:
                print("\nRitorno al menu' principale\n")
                break
            else :
                print("\nScelta non valida\n")

    else :
        print("\nla scansione sul programma non ha rilevato codice malevolo, e' possibile continuare a utilizzare il programma senza rischi\n")


def loadModel(file_path):
    
    with open(file_path,"rb") as f:
        model = pick.load(f)
        
    return model
