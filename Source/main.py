import pandas as pd 
import graphics as gr
import apiml as api


def main_menu(query_set,model):
    choose = 0
    while True:
        gr.prompt()
        choose = input()
        if choose == '1':
            api.scanMetaData(query_set,model)
        elif choose == '2':
            print("TODO Query KB")
        # elif choose =='3':
        #     query_set = loadingQuerySet()
        elif choose =='3':
            break
    print("\nArrivederci !\n")




#MAIN
model = api.loadModel("../Model/classifier.pkl")
query_set = pd.read_csv("../Datasets/50dataset.csv")
gr.printLogo()
gr.printIntro()
main_menu(query_set,model)    


















