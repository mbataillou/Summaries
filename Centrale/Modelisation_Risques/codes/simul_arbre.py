"""Fonction de simulation du resultat d'un arbre binomial """

def arbre(S,n,p,u):
    S_arbre=[]
    u,d,p,delta=valeurs(sigma,n,t,r,T) #obtention des valeurs
    for i in range(1,n+1): 
        if rd.binomial(1, p, 1)==True : 
            S_arbre.append(S*u)
            S=S*u        
        else: 
            S_arbre.append(S*d)
            S=S*d 
    return S_arbre,S #on obtiens un simulation du "chemin" prit par S