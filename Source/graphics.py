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

def numericInput(lowbound,upbound,message=""):
    while True:
        try:    
            choice = int(input(message))
            if choice < lowbound or choice > upbound:
                print("\nScelta non valida, inserire solo i numeri nel range indicato\n")
            else:
                return choice
        except ValueError:
            print("\nScelta non valida, inserire solo numeri\n")

def printSeparator():
    print()
    print("="*100)
    print()