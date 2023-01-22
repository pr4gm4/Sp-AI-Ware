import pickle as pick
import numpy as np
import ifelsetree as ifel

def scanMetaData(query_set,model):
    
    count = 0
    for i in query_set.loc[:,"sha"]:
        print("programma->"+str(count)+" "+i)
        count+=1
        
    choice = input("\nscegliere uno dei seguenti programmi da analizzare (il codice sha identifica univocamente il programma)\n")

    program =query_set.loc[int(choice),:]

    del program["sha"]

    y_pred = model.predict(np.array([program,]))

    if y_pred == 1 :
        print("\nATTENZIONE: il programma selezionato ha avuto esito positivo ed e' probabilmente un Malware\n")

        while True:
            print("\nVuoi fornire ulteriori dati da caricare sulla base di conoscenza online?\n")
            print("\n[1] Si\n[2] No\n")
            choice = int(input())  
            
            if choice == 1:
                maltype =ifel.questionTree()
                
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
