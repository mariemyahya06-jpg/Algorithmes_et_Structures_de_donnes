def tri_a_bulle(T):
    n = len(T)
    passe = 1
    for i in range(n-1, 0, -1):
        print("--- Passe ", passe, " ( i = ", i ," ) ---")
        for j in range(i):
            if T[j+1] < T[j]:
                T[j+1] , T[j] = T[j] , T[j+1]
                print("j = ", j, " : echange --> ", T)
            else:
                print("j = ", j, " : rien --> ", T)
        passe = passe + 1

n= int(input("Combien d'element ? "))
T = []
for k in range(n) :
    x = int(input("Element "+ str(k+1) + " = "))
    T.append(x)

print("Avant trie --> ", T)
tri_a_bulle(T)
print("Aprés trie --> ", T)
