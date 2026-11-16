T = [8, 5, 2, 1]
def est_tri(T):
    for i in range(len(T) - 1):
        if T[i] > T[i + 1]:
            return False
    return True
print("Avant le tri : ",T)
print("Trié ? ",est_tri(T))
T_trie = sorted(T)
print("Aprés le tri : ", T_trie)
print("Trié ? ",est_tri(T_trie))