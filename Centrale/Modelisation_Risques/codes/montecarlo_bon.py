"""Calcul du prix d'une option europeenne de part la simulation de Monte-Carlo"""
def Option_euro_MC(S0, K, r, sigma, T, type,tirages):
    # initialisation du vecteur prix
    prix=0
    #generation des variations aleatoires suivant une loi normale autour de S, avec la fonction scipy.stats.norm.rvs qui nous donne l'option d'obtenir les valeurs aleatoires de la loi normale
    for i in xrange(tirages):
        S_t = S0*math.exp(T*(r-0.5*sigma**2))
         #generation des epsilon aleatoires suivant une loi normale
        epsilon = scipy.stats.norm.rvs(size=1) 
        #variations autour de S en simulant un mouvement Brownien
        S_t = S_t*math.exp(epsilon*(T*sigma**2)**0.5) 
        if type=="CALL":
            prix += max(S_t - K, 0.0)
        else :
            prix += max(K-S_t, 0.0)
    prix=prix/(tirages)*math.exp(-r*T)
    return prix #obtention de la moyenne de mouvements aleatoires (Browniens)