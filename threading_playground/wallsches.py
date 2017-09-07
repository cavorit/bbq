def wallsches(n):
    """ Berechnet das n-te Partialprodukt einer Reihe, die als Wallisches Produkt bekannt ist"""
    pi_halbe = 1
    zaehler, nenner = 2.0, 1.0
    for i in range(n):
        pi_halbe *= zaehler / nenner
        if i % 2:
            zaehler += 2
        else:
            nenner += 2
    print("Annaeherung mit {} Faktoren: {:.16f}".format(n, 2*pi_halbe))

