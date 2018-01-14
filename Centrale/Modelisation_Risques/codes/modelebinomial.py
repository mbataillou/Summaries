"""Calcul du prix d'une option par avec le modele binomial"""
    
#type prend les valeurs CALL ou PUT 
#style prend les valeurs EURO ou AMER

def modele_binomial(S0, K, r, sigma, T, N,type,style):

    # initialisation calcul des valeurs 
    u,d,p,delta=valeurs(sigma,n,t,r,T) # obtention des valeurs du modele
    # initialisation de l'arbre 
    prix = [[0.0 for j in xrange(i + 1)] for i in xrange(N + 1)]   
    # Calcul prix finaux en fonction du type d'option
    if type=="CALL": 
        for j in xrange(i+1):
            prix[N][j] = max(S0 * u**j * d**(N - j)-K, 0.0) 
        if style=="AMER":
            for i in xrange(N-1, -1, -1):
                for j in xrange(i + 1):
                    prix[i][j] = math.exp(-r * delta) * (p * prix[i + 1][j + 1] + (1.0 - p) * prix[i + 1][j])
                    exercise = S0 * u**j * d**(i - j)-K
                    prix[i][j] = max(prix[i][j],exercise)
        else : 
            for i in xrange(N-1, -1, -1):
                for j in xrange(i + 1):
                    prix[i][j] = math.exp(-r * delta) * (p * prix[i + 1][j + 1] + (1.0 - p) * prix[i + 1][j])
    else : 
        for j in xrange(i+1):
            prix[N][j] = max(K- S0 * u**j * d**(N - j), 0.0)
        if style=="AMER":
            for i in xrange(N-1, -1, -1):
                for j in xrange(i + 1):
                    prix[i][j] = math.exp(-r * delta) * (p * prix[i + 1][j + 1] + (1.0 - p) * prix[i + 1][j])
                    exercise = K-S0 * u**j * d**(i - j)
                    prix[i][j] = max(prix[i][j],exercise)
        else : 
            for i in xrange(N-1, -1, -1):
                for j in xrange(i + 1):
                    prix[i][j] = math.exp(-r * delta) * (p * prix[i + 1][j + 1] + (1.0 - p) * prix[i + 1][j])
    return prix[0][0] 