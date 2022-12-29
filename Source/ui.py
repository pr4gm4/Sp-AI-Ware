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
    intro = """
Benvenuto/a in Sp-AI-Ware, un laboratorio per rilevazione e analisi di Malware potenziato da algoritmi di Machine Learning
e dotato di Base di Conoscenza basata su Web Semantico! 
"""
    print(intro)

def prompt():
    prompt = """
Scegli una delle seguenti azioni da fare:
[1]Inserire Metadati di file eseguibile per una classificazione con algoritmo ML
[2]Passare all'interrogazione della Base di Conoscenza per avere piu' info sui Malware gia' rilevati
"""
    print(prompt)

def menu():
    choose = 0
    while True:
        prompt()
        choose = input()
        if choose == '1':
            print("TODO insert record")
        elif choose == '2':
            print("TODO Query KB")
        elif choose =='3':
            break
    print("Arrivederci !")
    
printLogo()
printIntro()
menu()    

