def rendre_somme(argent):
    # processus du rendu d'argent, avec une list contenant les billets utilisables et une liste de liste contenant les rendus
    money=[100,50,20,10,5,2,1]
    result=[]
    for i in money:
        if argent>=i:
            avg=argent//i
            argent-=avg*i
            result.append((avg,"billets de",i))
    return result
