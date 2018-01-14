"""Calcul du delta d'une option par recurrence/modele binomial"""

def delta_df(delta_S,type):    
    delta = (modele_binomial(S+ delta_S, K, r, sigma, T,n,type,"EURO") - modele_binomial(S- delta_S, K, r, sigma, T,n,"EURO",style)) / (2*delta_S)
    return delta