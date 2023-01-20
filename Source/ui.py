import pandas as pd 
import numpy as np
import pickle as pick
def printLogo():
    logo = """
   _____                    _____   __          __            
  / ____|             /\   |_   _|  \ \        / /            
 | (___  _ __ ______ /  \    | |_____\ \  /\  / /_ _ _ __ ___ 
  \___ \| '_ \______/ /\ \   | |______\ \/  \/ / _` | '__/ _ \\
  ____) | |_) |    / ____ \ _| |_      \  /\  / (_| | | |  __/
 |_____/| .__/    /_/    \_\_____|      \/  \/ \__,_|_|  \___|
        | |                                                   
        |_|                                                   
"""
    print(logo)
    
def printIntro():
    intro = """\n
Benvenuto/a in Sp-AI-Ware, un laboratorio per rilevazione e analisi di Malware potenziato da algoritmi di Machine Learning
e dotato di Base di Conoscenza basata su Web Semantico!\n 
"""
    print(intro)

def prompt():
    prompt = """\n
Scegli una delle seguenti azioni da fare:
[1]Scannerizzare un file sospetto (AI-Powered)
[2]Consultare l'intelligence online riguardo Malware gia' rilevati
[3]Esci da Sp-AI-Ware\n
"""
    print(prompt)

def main_menu(query_set,model):
    choose = 0
    while True:
        prompt()
        choose = input()
        if choose == '1':
            scanMetaData(query_set,model)
        elif choose == '2':
            print("TODO Query KB")
        # elif choose =='3':
        #     query_set = loadingQuerySet()
        elif choose =='3':
            break
    print("\nArrivederci !\n")



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
        print("\nATTENZIONE: il programma selezionato ha avuto esito positivo ed e' un Malware\n")

        while True:
            print("\nVuoi fornire ulteriori dati da caricare sulla base di conoscenza online?\n")
            print("\n[1] Si\n[2] No\n")
            choice = int(input())  
            
            if choice == 1:
                print("TODO DECISION TREE MANUAL")
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
        
    
     

# def chooseQuerySet(query_set):
#     print("\nScegliere uno dei file eseguibili da analizzare, ("+str(query_set.shape([0]))+" file)"+"\n")      

#MAIN
model = loadModel("../Model/classifier.pkl")
query_set = pd.read_csv("../Datasets/50dataset.csv")
printLogo()
printIntro()
main_menu(query_set,model)    
# takeQueryset()


















