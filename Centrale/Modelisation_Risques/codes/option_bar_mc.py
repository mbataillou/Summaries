"""Calcul du prix d'une option euro avec option barriere par simulation de Monte-Carlo"""

def Option_euro_BAR_MC(S0, K, r, sigma, T, type, tirages,OPT_BAR): 
    # initialisation de prix et S_t
    prix = 0 
    S_t = S0
    #Calcul constant x pour ameliorer efficience de l'algorithme     
    x=(r-0.5*sigma**2)*T      
    if type=="CALL":   
        for i in range(tirages):     
            epsilons = scipy.stats.norm.rvs(size=1)
            S_t = S0*math.exp(x+sigma*math.sqrt(T)*epsilons)         
            if S_t < OPT_BAR :   #condition barriere CALL
                prix += max(S_t - K, 0)
            else : 
                prix += 0
    else :        
         for i in range(tirages):        
            epsilons = scipy.stats.norm.rvs(size=1)
            S_t = S0*math.exp(x+sigma*math.sqrt(T)*epsilons)  
            if S_t > OPT_BAR :  #condition barriere PUT          
                prix += max(K-S_t, 0)
            else : 
                prix += 0
            
    return math.exp(-r*T)*prix/tirages #obtention de la moyenne  