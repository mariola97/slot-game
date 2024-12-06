import random

simbol=['🍒', '🍋', '🍉', '🍊', '🍇', '🔔', '💎']

def nasumicni_odabir():
    simbol_1 = random.choice(simbol)
    simbol_2 = random.choice(simbol)
    simbol_3 = random.choice(simbol)

    return simbol_1, simbol_2, simbol_3

def provjeri(simbol_1, simbol_2, simbol_3):
    if simbol_1==simbol_2==simbol_3:
        return True
    return False

def vockice():
    while True:
            input("Stisni Enter da započneš igru!")
            budget=100000


            while budget>0:
                ulog=int(input("Stavi ulog: "))
                simbol_1, simbol_2, simbol_3  = nasumicni_odabir()
                print(f"\nRezultat: {simbol_1} | {simbol_2} | {simbol_3}  ")
        
                if provjeri(simbol_1, simbol_2, simbol_3)==True:
                    print("Čestitam, dobili ste!")
                    dobitak=ulog*15
                    budget=budget+dobitak
                    print(f"\n Vaš dobitak: {dobitak}")
                    print(f"\n Stanje racuna: {budget}")


                else:                
                    print("Žao mi je, pokušajte ponovno.")
                    budget=budget-ulog
                    print(f"Stanje racuna:  {budget}")
         
                igraj_ponovo=input("\nŽelite li pokušati ponovno? y/n: ")
                if igraj_ponovo!="y":
                    print("Hvala na igri, vidimo se!")
                    break
            break


vockice()
