"""Calcul du prix d'une option barriere (CALL/PUT) par recurrence"""
    
def option_BAR_rec(S0, K, r, sigma, T, N,OPT_BAR):

    # intialisation calcul des valeurs 
    u,d,p,delta=valeurs(sigma,n,t,r,T)
    # initialisation de l'arbre
    prix = [[0.0 for j in xrange(i + 1)] for i in xrange(N + 1)]
    if type=="CALL":
    # Calcul prix finaux
        for j in xrange(i+1):
            if S0 * u**j * d**(N - j)<OPT_BAR:
                prix[N][j] = max(S0 * u**j * d**(N - j)-K, 0.0)
            else : 
                prix[N][j]=0
    else: 
        for j in xrange(i+1):
            if S0 * u**j * d**(N - j)>OPT_BAR:
                prix[N][j] = max(K-S0 * u**j * d**(N - j), 0.0)
            else : 
                prix[N][j]=0        
    # Recurrence
    for i in xrange(N-1, -1, -1):
        for j in xrange(i + 1):
            prix[i][j] = math.exp(-r * delta) * (p * prix[i + 1][j + 1] + (1.0 - p) * prix[i + 1][j])
    return prix[0][0]