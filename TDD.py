def f1(a,b=0):
    return a*a + b

def f2(a):
    if len(a) >0:
        return a[0]
    else:
        return "BUUUUM"

def f3(a):
    if a==1:
        return "jeden"
    elif a==2:
        return "dwa"
    elif a==3:
        return "trzy"
    else:
        return "other"

def f4(a,b=""):
    if len(b)>0:
        return a + " ma kota " + "i " + b
    else:
        return a+ " ma kota"

def f5(a, step=1):
    return range(a)[ : : step]

def f6(a, b):
    return b * a

def f7(a):
    if (isinstance(a,str) and a[-1] =="."):
        return "zdanie"

    elif(isinstance(a,str) and a[0] == "<" and a[-1] == ">"):
        return "tag poczatkowy"
    elif(isinstance(a, str)):
        return "slowo"
    elif(isinstance(a, int) and a < 0):
        return "liczba_ze_znakiem"
    elif(isinstance(a, int) and a < 10):
        return "cyfra"
    elif(isinstance(a, int)):
        return "liczba"
