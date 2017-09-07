def primfaktorzerlegung(n):
    """Gibt die Primfaktoren zurück"""
    
    Rest = n
    Primfaktoren = []
    for i in range(2,n):
        if Rest % i: # teilerfremd
            continue
        else:
            Primfaktoren.append(i)
            Rest = Rest / i
    if not Primfaktoren:
        Primfaktoren = 'prim'
    return(Primfaktoren)

