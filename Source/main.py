import pandas as pd 
import graphics as gr
import apiml as api


def main_menu(query_set,model):
    while True:
        gr.prompt()
        choose = gr.numericInput(1,3)
        gr.printSeparator()
        if choose == 1:
            api.scanMetaData(query_set,model)
        elif choose == 2:
            print("TODO Query KB")
        elif choose == 3:
                print("\nArrivederci\n")
                break



#MAIN

model = api.loadModel("../Model/classifier.pkl")
query_set = pd.read_csv("../Datasets/50dataset.csv")
gr.printLogo()
gr.printIntro()
main_menu(query_set,model)    


















