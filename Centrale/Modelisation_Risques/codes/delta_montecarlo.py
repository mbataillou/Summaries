""" Calcul du delta d'une option europeene de part la 
methode de Monte-Carlo"""

def delta_MC(S0, K, r, sigma, T, type, n, tirages,delta_S):
    # initialisation du vecteur prix
    prix_up = 0
    prix_down = 0
    
    #generation des variations aleatoires suivant une loi normale autour de S, avec la fonction scipy.stats.norm.rvs qui nous donne l'option d'obtenir les valeurs aleatoires de la loi normale
    for i in range(tirages):
        S_up = S0+delta_S
        S_down = S0-delta_S
        #generation des epsilon aleatoires suivant une loi normale
        epsilons = scipy.stats.norm.rvs(size=1) 
        #On calcule l'evolution du sous-jacent avec un differentiel de difference
        S_up = S_up * math.exp((r-(sigma**2)/2)*T + sigma*math.sqrt(T) * epsilons)
        S_down = S_down * math.exp((r-(sigma**2)/2) * T + sigma*math.sqrt(T) * epsilons)
        if type=="CALL":
            prix_up += max(S_up - K, 0.0)
            prix_down += max(S_down - K, 0.0)
        else :
            prix_up += max(K-S_up, 0.0)
            prix_down += max(K-S_down, 0.0)
            
    p_up=scipy.mean(prix_up)*math.exp(-r*T)
    p_down=scipy.mean(prix_down)*math.exp(-r*T)
    greek_delta=float(p_up-p_down)/float(2*delta_S)       
    return greek_delta/tirages 