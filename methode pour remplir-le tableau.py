#Methode1 boucle pour(for i in range)
def Remplir(T, c, ch):                                            # T est un tableau, c est la taille du tableau, ch est la phrase
    ch = ch + " "                                                 # Ajouter un espace à la fin pour garantir que chaque mot est suivi d'un espace
    for i in range(c):                                            # Boucle pour traiter chaque mot
        T[i] = ch[0:ch.find(" ")]                                 # Extraire le mot du début jusqu'au premier espace
        ch = ch[ch.find(" ") + 1:len(ch)]                         # Supprimer le mot traité de la chaîne


        
#autre methode boucle pour (for i in range)
def Remplir(T, c, ch):
    for i in range(c - 1):  
        pos = ch.find(" ")
        T[i] = ch[:pos]
        ch = ch[pos + 1:]
    T[c - 1] = ch                                  # Ajouter le dernier mot restant (qui n'a pas d'espace après)




#methode2 boucle while(repeter....jusquà)
def Remplir(ch, T, n):
    i = 0
    p = ch.find(" ")
    while p != -1:
        T[i] = ch[:p]
        ch = ch[p+1:]
        i += 1
        p = ch.find(" ")
    T[i] = ch  # Add the last word
#autre methode boucle while
def Remplir(ch, T, n):
    i = 0
    p = ch.find(" ")
    while p != -1:
        T[i] = ch[:p]
        ch = ch[p+1:]
        i += 1
        p = ch.find(" ")
    T[i] = ch  # Add the last word

    
#methode3 parour la mot caractere par caractére 
def Remplir(ch, T, n):
    debut = 0
    i = 0
    for j in range(len(ch)):
        if ch[j] == " ":
            T[i] = ch[start:j]
            debut= j + 1
            i += 1
    if start < len(ch):
        T[i] = ch[start:]


