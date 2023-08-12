def is_proper_subset(subset, superset):
    return subset.issubset(superset) and subset != superset

# Conjuntos dados
set_A = {1, 2, 3}
set_C = {1, 2, 3, 4, 5}
set_D = {5, 3, 4, 2, 1}

# Verificar se A é um subconjunto próprio de C
result_A = is_proper_subset(set_A, set_C)
print("A é subconjunto próprio de C:", result_A)

# Verificar se D é um subconjunto próprio de C
result_D = is_proper_subset(set_D, set_C)
print("D é subconjunto próprio de C:", result_D)


