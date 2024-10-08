counter = 0
def chiedinumero():
    print("Inserisci un numero positivo e intero")
    a = input()
    if a.isdigit():
        avvia(int(a))

    else:
        print("La congettura funziona solo con numeri interi positivi.")
        chiedinumero()

def avvia(a):
    if(epari(a)):
        a = a // 2
    else:
        a = a * 3 + 1
    print(" Il numero:" + str(a))
    global counter
    counter += 1
    if(a == 1):
        print("Il numero è diventato 1, passaggi impiegati:" + str(counter))
    else:
        avvia(a)
    

def epari(a):
    b = a//2
    c = a/2
    if(b == c):
        return True
    else:
        return False
    
chiedinumero()