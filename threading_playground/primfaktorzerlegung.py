def primfaktorzerlegung(n):
    """Gibt die Primfaktoren zurück"""
    
    Rest = n
    Primfaktoren = []
    for i in range(1,n+1):
        if Rest % i: # teilerfremd
            continue
        else:
            Primfaktoren.append(i)
            Rest = Rest / i

    return(Primfaktoren)

