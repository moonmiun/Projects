import getpass

#Costruzione della parola
parola = list(getpass.getpass(prompt = "Questa è la frase scelta = "))

display = []
for letter in parola:
    if letter != " ":
        display.append("_ ")
    else:
        display.append(" ")
    
usate = []
tentativi = 5
    
#########################


print("""Gioco dell'impiccato
Le regole le sai: hai cinque tentativi per indovinare la frase.

Questa è la frase che devi indovinare: """)

print("".join(display))


while tentativi > 0:
    if "_ " in display:
        lettera = input("Dimmi una lettera: ")
        if lettera not in usate:
            usate.append(lettera)
            if lettera in parola:
                n = 0
                while n < len(parola):
                    if parola[n] == lettera:
                        display[n] = f"{lettera} " 
                    n += 1
                print("".join(display))
            else:
                print("Questa lettera non c'è nella parola!")
                tentativi -= 1
                print(f"Tentativi rimasti: {tentativi}")
        else:
            print("Hai già usato questa lettera, prova un'altra")
    else:
        print("Ce l'hai fatta!")
        break

if tentativi == 0:
    print("Game over!!!!")