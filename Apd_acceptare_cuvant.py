#Implementam un automat push_down
from collections import deque
f = open("intrare.txt","r")
n = int( f.readline() ) #nr de stari in automat
s=f.readline()
stari=[ x for x in s.split()]#vector pt starile din automat
i = f.readline()  # starea initiala
init=i[0]
nrf = int( f.readline() ) #nr de stari finale
sir = f.readline()
starif = [ x for x in sir.split() ]# vector de stari finale
nrtranz = int( f.readline() )  # nr de tranzitii
lista=[]
for i in range(nrtranz): # construim o matrice pt tranzitii
    sir2 = f.readline().split() # s_init,s_fin, lit, caz_stiva, cuv adaugat in stiva pt caz
    # lista de tranzitii de forma stare, stare->tranz->stari in care poate ajunge cu tranz resp
    lista.append([ x for x in sir2 ])
cuv = f.readline() # citim cuv care trebuie verificat
L = deque([ x for x in cuv[:len(cuv)-1]] )#punem literele intr-un vector
L+=['&']
stiva = [ 'Z' ]
def parcurgere(poz, init ):


    gasit=0
    if poz==len(cuv) -1 and init in starif  and len(stiva)<=1: #daca am parcurs intreg cuvantul, starea curenta
         return 1  # este stare initiala, si stiva e goala sau are Z atunci cuv e acceptat

    for x in lista:
        if x[0]==init and x[2]==cuv[poz] and x[3]==stiva[-1]:

            if  x[4]=='&': # pe post de lambda, facem pop de pe stiva
                stiva.pop()
            else:
                for i in range(len(x[4])-1):
                    stiva.append(x[4][i])   #adaugam in stiva
            gasit=1
            return parcurgere(poz+1,x[1]) #apelul recursiv
        elif x[0]==init and x[2]=='&' and x[3]==stiva[-1]: #daca avem lambda, stiva ramane nemodificata
            gasit = 1
            return parcurgere(poz,x[1])
    if gasit==0: #inseamna ca nu am gasit tranzitie
        return 0
x=parcurgere(0,init)
if x==0:
    print("Cuvantul nu a fost acceptat")
else:
    print("Cuvantul a fost accepatat")






'''
3
0 1 2
0
1
2
12
0 0 0 Z 0Z
0 0 1 Z 1Z
0 0 0 0 00
0 0 0 1 01
0 0 1 0 10
0 0 1 1 11
0 1 c Z Z
0 1 c 0 0
0 1 c 1 1
1 1 0 0 &
1 1 1 1 &
1 2 & Z Z
011c110
abbb
ccdddd
aaaabbbbbbccccdd
aabbbccd
'''