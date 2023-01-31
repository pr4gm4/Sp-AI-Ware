import graphics as gr

def outType(type):
    print("\nDalle informazioni fornite e' probabile che il programma sospetto sia un Malware di tipo "+type+"\n")
    print("\nCaricamento dell'informazione sulla base di conoscenza\n")

def invalidChoice():
    print("\nAttenzione: la scelta inserita non e' valida\n")

def outGray():
    print("\nDalle informazioni fornite e' difficile stabilire con una buona probabilita' se il programma sia dannoso oppure no. Tuttavia poiche' i suoi dati binari sono stati segnalati, si provvedera' a categorizzare questo software come Grayware ovvero un software la cui pericolosita' e' dubbia\n")

def questionTree():
    yes_no="\n[1]Si\n[2]No\n"
    print("\nHai notato piu' copie del programma sospetto all'interno della tua macchina dopo il suo utilizzo ?\n")
    choice = gr.numericInput(1,2,yes_no)
    if choice == 1 :
        print("\nDopo aver usato il programma sospetto, noti delle anomalie anche nell'uso di software quotidiano che hai sempre usato ? \n")
        choice = gr.numericInput(1,2,yes_no)
        if choice == 1:
            outType("Virus")
            return "Virus"
        elif choice == 2:
            print("\nHai notato delle anomalie all'interno della tua rete ? (ad esempio traffico insolito ) o in altri dispositivi connessi alla tua rete ? \n")
            choice = gr.numericInput(1,2,yes_no)
            if choice == 1:
                outType("Worm")
                return "Worm"
            elif choice == 2:
                outGray()
                return "Grayware"
    elif choice == 2:
        print("\nIl programma sospetto si propone di esere un programma utile per la tua macchina(es. editor di testo, strumento di pulizia , antivirus ecc) ? \n")
        choice = gr.numericInput(1,2,yes_no)
        if choice == 1:
            print("\nNoti delle anomalie evidenti nel dispositivo relative alla privacy? (il led della webcam si accende senza il suo utilizzo ecc) ?\n")
            choice = gr.numericInput(1,2,yes_no)
            if choice == 1:
                outType("Spyware")
                return "Spyware"
            elif choice == 2:
                print("\nIl programma comunica delle allerte Malware fittizie, insolite, infondate  e/o con errori grammaticali evidenti ? \n")
                choice = gr.numericInput(1,2,yes_no)
                if choice == 1:
                    outType("Rogue")
                    return "Rogue"
                elif choice == 2:
                    outType("Trojan")
                    return "Trojan"
        elif choice == 2:
            print("\nla tua macchina presenta file criptati e/o scritte incomprensibili opzionalmente un messaggio chiedendo un riscatto in denaro ?\n")
            choice = gr.numericInput(1,2,yes_no)
            if choice == 1:
                outType("Ransomware")
                return "Ransomware"
            elif choice == 2:
                print("\nLa tua macchina mostra pubblicita' in maniera continua e invasiva ? (notifiche sul desktop , sul browser ecc)\n")
                choice = gr.numericInput(1,2,yes_no)
                if choice == 1:
                    outType("Adware")
                    return "Adware"
                elif choice == 2:
                    print("\nAlcuni o tutti i tuoi file presenti sul dispositivo sono stati cancellati ? \n")
                    choice = gr.numericInput(1,2,yes_no)
                    if choice == 1:
                        outType("Wiper")
                        return "Wiper"
                    elif choice == 2:
                        print("\nNoti un rallentamento del dispositivo utilizzando periferiche di input come mouse e/o tastiere ?\n")
                        choice = gr.numericInput(1,2,yes_no)
                        if choice == 1:
                            outType("Keylogger")
                            return "Keylogger"
                        
                        elif choice == 2:
                            print("\nHai notato modifiche o accessi insoliti al dispositivo ? Specie in file di log ecc\n")
                            choice = gr.numericInput(1,2,yes_no)
                            if choice == 1:
                                outType("Backdoor")
                                return "Backdoor"
                            elif choice == 2:
                                print("\nHai notato errori di sistema gravi che rendono il dispositio inutilizabile? (es Blue Screen Of Death ecc.)\n")
                                choice = gr.numericInput(1,2,yes_no)
                                if choice == 1:
                                    outType("Rootkit")
                                    return "Rootkit"
                                elif choice == 2:
                                    outGray()
                                    return "Grayware"
    if choice not in [1,2]:
        invalidChoice()                
        return
