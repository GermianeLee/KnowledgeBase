def conjunction(a, b):
    return a and b

def implication(a, b):
    return (not a) or b

# Generate all combinations of truth values for P, Q, R
combinations = [
    (P, Q, R)
    for P in [True, False]
    for Q in [True, False]
    for R in [True, False]
]

# Header
print(f"{'P':<5}{'Q':<5}{'R':<5}{'(P ^ Q) => R':<17}{'Q => P':<10}{'Q':<5}{'KB':<6}{'R':<5}{'KB => R':<10}")

for P, Q, R in combinations:
    pq_and = conjunction(P, Q)
    pq_imp_r = implication(pq_and, R)
    q_imp_p = implication(Q, P)
    q_fact = Q
    kb = pq_imp_r and q_imp_p and q_fact
    kb_imp_r = implication(kb, R)

    print(f"{str(P):<5}{str(Q):<5}{str(R):<5}{str(pq_imp_r):<17}{str(q_imp_p):<10}{str(q_fact):<5}{str(kb):<6}{str(R):<5}{str(kb_imp_r):<10}")
