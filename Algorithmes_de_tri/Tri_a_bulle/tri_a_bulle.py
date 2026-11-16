def tri_a_bulle(T):
    n = len(T)
    for i in range(n - 1):
        echange = False
        for j in range(n - 1 - i):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
                echange = True
        print("Passe ", i + 1, ":", T)
        if echange == False:
            break

T = [3, 1, 4, 2]
print("Avant le tri : ", T)
tri_a_bulle(T)
print("Aprés le tri : ", T)