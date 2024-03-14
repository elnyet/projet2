def rendre_somme(argent):
    money=[100,50,20,10,5,2,1]
    result=[]
    for i in money:
        if argent>=i:
            avg=argent//i
            argent-=avg*i
            result.append((i,"billets de",avg))
    return result
