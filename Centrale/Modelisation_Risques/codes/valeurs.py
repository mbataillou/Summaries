"""Fonction de simulation de calcul des valeurs a utiliser"""

def valeurs(sigma,n,t,r,T) :
    delta=T/float(n-t) 
    u=math.exp(math.sqrt(delta)*sigma)
    d=1/u
    R=math.exp(r*T/(n-t))
    p=(R-d)/(u-d)
    return u,d,p,delta 