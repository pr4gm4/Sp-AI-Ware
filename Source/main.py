import pandas as pd 
import graphics as gr
import apiml as api
import dbpediapi as dbp

ontpath = "../Ontologies/Sp-AI-Ware-OWL.owl"

def main_menu(query_set,model):
    """funzione menu principale

    Args:
        query_set (): 50 programmi da scansionare 
        model (): modello allenato per poter scansionare i programmi
    """
    while True:
        gr.prompt()
        choose = gr.numericInput(1,3)
        gr.printSeparator()
        if choose == 1:
            api.scanMetaData(query_set,model)
        elif choose == 2:
            dbp.queryDbpedia(ontpath)          
        elif choose == 3:
                print("\nArrivederci\n")
                break



#MAIN

model = api.loadModel("../Model/classifier.pkl")
query_set = pd.read_csv("../Datasets/50dataset.csv")
gr.printLogo()
gr.printIntro()
main_menu(query_set,model)    


















