def myPow(power, num):
    powered = num
    if num == 0.0:
        return 1.0
    n=0
    while n<power-1:
        powered *= num
        n=n+1
    return float(powered)


def myFactorial(n):
    if n ==0:
        return 1.0
    temp=n
    while n>1:
        temp*=(n-1)
        n=n-1
    return float(temp)


def exponent(x):
    exp=1
    i=1
    while i<100:
        exp+= myPow(i,x)/myFactorial(i)
        i+=1
    return float(exp)
        

def myAbs(x):
    if x<0:
        x=-x
    return float(x)


def Ln(x):
    if x<=0:
        return (0.0)    
    aa= 0.0
    ab= x-1.0
    while 0.001 < myAbs(aa-ab):
        aa = ab 
        ab = ab + 2*((x-exponent(ab))/(x+exponent(ab)))
    return float(ab)


def XtimesY(x,y):
    ans= exponent(y*Ln(x))
    if x<=0:
        return(0.0)
    return float(ans)


def sqrt(x,y):
    if x==0:
        return (0.0)
    elif x%2.0==0.0:
        if y<0.0:
            return(0.0)
    return float(XtimesY(y, 1.0/x))

def calculate(x):
    if x==0:
        return (0.0)
    elif x%2.0==0.0:
        if x<0.0:
            return (0.0)
    return float(exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x))
    



    

