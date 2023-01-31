import pickle as pick
import numpy as np
import ifelsetree as ifel
import apiont as ont
import glob as gl
import graphics as gr

onto = ont.loadOntology(gl.ONTPATH)

def printResults(model,xinput):
    print("\nRisultati per i diversi modelli:\n")
    for estimator in model.estimators_:
        print(estimator.__class__.__name__)
        print(estimator.predict(np.array([xinput,])))

    

def scanMetaData(query_set,model):
    count = 0
    list_sha = query_set.loc[:,"sha"]
    for i in list_sha:
        print("programma->"+str(count)+" "+i)
        count+=1
        
    choice = gr.numericInput(0,len(list_sha)-1,message="\nscegliere uno dei seguenti programmi da analizzare (il codice sha identifica univocamente il programma)\n")
    gr.printSeparator()

    program =query_set.loc[choice,:]

    shaprog = program["sha"]
    shaprog = str(shaprog)
    del program["sha"]

    if ont.alreadyScanned(gl.ONTPATH,shaprog) == True:
        print("\nl'hash del programma indicato e' stato riconosciuto all'interno della base di conoscenza online! Questo vuol dire che il software indicato e' stato in precedenza riconosciuto come malevolo, si consiglia la sua rimozione\n")
        print("\nEcco le informazioni sul Malware all'interno della base di conoscenza\n")

        instance = ont.loadIndByLabel(gl.ONTPATH,shaprog)
        if instance == None:
            print("Errore: impossibile caricare l'istanza")
            return False
        ont.showInstanceInfo(gl.ONTPATH,instance)

        print("\nVuoi aggiungere ulteriori informazioni a riguardo di questo Malware sulla base di conoscenza ? \n")
        choice = gr.numericInput(1,2,"\n[1]Si\n[2]No\n")
        gr.printSeparator()
        if choice == 1:
            ont.uploadInfo(instance,gl.ONTPATH)
        elif choice ==2:
            print("Ritorno al menu' principale")                    
            return True
            

    else:
        y_pred = model.predict(np.array([program,]))
        if y_pred == 1 :
            print("\nATTENZIONE: il programma selezionato ha avuto esito positivo ed e' probabilmente un Malware\n")
            printResults(model,program)
            print("\nRisultato finale del modello a Stack\n")
            print(y_pred)
            choice = gr.numericInput(1,2,"\nVuoi fornire ulteriori dati da caricare sulla base di conoscenza online?\n\n[1] Si\n[2] No\n")  
            gr.printSeparator()
            
            if choice == 1:
                maltype =ifel.questionTree()
                
                
                if  ont.uploadInstance(maltype,shaprog,gl.ONTPATH) == False:
                    print("Errore nel caricamento delle informazioni sulla base di conoscenza")
                    return False
                
                print("\nInformazioni caricate correttamente nella base di conoscenza online\n")
                print("\nIl malware e le relative informazioni sono state caricate sulla base di conoscenza online, tuttavia fornendo specifici dettagli del suo funzionamento potrebbe aiutare te e gli altri utilizzatori di Sp-AI-Ware a riconoscere i sintomi del Malware e a informarsi con maggior dettaglo, vuoi fornire queste informazioni?(Attenzione: le informazioni da fornire potrebbero risultare piuttosto tecniche, si consiglia di inserirle qualora si abbiano le competenze tecniche necessarie)\n")
                while True:
                    choice = gr.numericInput(1,2,"\nvuoi fornire informazioni?\n[1] Si\n[2] No\n")
                    gr.printSeparator()
                    if choice == 1:
                        malinstance = ont.loadIndByLabel(gl.ONTPATH,shaprog)
                        if ont.uploadInfo(malinstance,gl.ONTPATH) == False:
                            print("Errore nel caricamento delle ulteriori informazioni")
                            return False
                    elif choice ==2:
                        print("Ritorno al menu' principale")                    
                        return True

            elif choice == 2:
                print("\nRitorno al menu' principale\n")
                return True
        else :
            print("\nla scansione sul programma non ha rilevato codice malevolo, e' possibile continuare a utilizzare il programma senza rischi\n")


def loadModel(file_path):
    
    with open(file_path,"rb") as f:
        model = pick.load(f)
        
    return model
