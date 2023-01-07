import pandas as pd 
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
[1]Inserire Metadati di file eseguibile per una classificazione con algoritmo ML
[2]Passare all'interrogazione della Base di Conoscenza per avere piu' info sui Malware gia' rilevati
[3]Caricare un nuovo insieme di file esegubili da poter analizzare
[4]Esci da Sp-AI-Ware\n
"""
    print(prompt)

def main_menu():
    choose = 0
    query_set = pd.read_csv("../Datasets/query_set_5k.csv")#TODO leave this a
    while True:
        prompt()
        choose = input()
        if choose == '1':
            scanMetaData(query_set)
        elif choose == '2':
            print("TODO Query KB")
        elif choose =='3':
            query_set = loadingQuerySet()
        elif choose =='4':
            break
    print("\nArrivederci !\n")


def loadingQuerySet():
    filename = input("\nInserisci il nome del file per i  metadati di eseguibili da analizzare(in formato csv)\n")
    try:
        query_set = pd.read_csv("../Datasets/"+filename+".csv")
    except FileNotFoundError:
        print("\nErrore: il percorso inserito non e' un percorso valido\n")
    except Exception:
        print("\nErrore: ",Exception,"\n")    
    else:
        print("\nCaricamento effettuato con successo\n")
        return query_set

def scanMetaData(query_set):
    
    try:
        print("\nSelezionare i metadati da analizzare tra i seguenti file\n")
        for i in query_set:
            print(type(query_set))
            
    except Exception as e:
        print("\nErrore: il query set non e' stato caricato correttamente\n")
        print(e)
        return
    
    
     

# def chooseQuerySet(query_set):
#     print("\nScegliere uno dei file eseguibili da analizzare, ("+str(query_set.shape([0]))+" file)"+"\n")      

#MAIN
printLogo()
printIntro()
main_menu()    
# takeQueryset()


















