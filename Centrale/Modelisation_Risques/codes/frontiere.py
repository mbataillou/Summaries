"""Calcul de la frontiere d'exercice d'une option americaine """

def frontiere(S0, K, r, sigma, T, N,type):
    # initialisation calcul des valeurs 
    u,d,p,delta=valeurs(sigma,n,t,r,T)
    # initialisation de l'arbre 
    valeur_exercice=[] ; temps=[] ; stock=[]
    prix = [[0.0 for j in xrange(i + 1)] for i in xrange(N + 1)]  
    # Calcul prix finaux en fonction du type d'option
    if type=="CALL": 
        for j in xrange(i+1):
            prix[N][j] = max(S0 * u**j * d**(N - j)-K, 0.0) 
        for i in xrange(N-1, -1, -1):
            exercice_iter=[] ; temps_iter=[] ; stock_iter=[]
            m=False
            for j in xrange(i + 1):
                prix[i][j] = math.exp(-r * delta) * (p * prix[i + 1][j + 1]+ (1.0 - p) * prix[i + 1][j])
                exercise = S0 * u**j * d**(i - j)-K
                if max(prix[i][j],exercise)==exercise :
                    m=True
                    stock_iter.append(exercise)
                    exercice_iter.append(j)
                    temps_iter.append(i)
            if m==True: 
                valeur_exercice.append(max(exercice_iter))
                temps.append(max(temps_iter))
                stock.append(max(stock_iter))
    else : 
        for j in xrange(i+1):
            prix[N][j] = max(K- S0 * u**j * d**(N - j), 0.0)
        for i in xrange(N-1, -1, -1):
            exercice_iter=[] ; temps_iter=[] ; stock_iter=[]
            m=False
            for j in xrange(i + 1):
                prix[i][j] = math.exp(-r * delta) * (p * prix[i + 1][j + 1]+ (1.0 - p) * prix[i + 1][j])
                exercise = K-S0 * u**j * d**(i - j)
                if max(prix[i][j],exercise)==exercise :
                    m=True
                    stock_iter.append(exercise)
                    exercice_iter.append(j)
                    temps_iter.append(i)
            if m==True: 
                valeur_exercice.append(max(exercice_iter))
                temps.append(max(temps_iter))
                stock.append(S0 * u**max(exercice_iter) * d**(max(temps_iter) - max(exercice_iter)))
    return stock,temps