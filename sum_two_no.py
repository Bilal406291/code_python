def sum_two_int(a,b):
    return(a+b)

def avr_two_int(a,b):
    sum=a+b
    arv=sum/2
    return(arv)

def diff(a,b):
    return(a-b)

def mult(a,b):
    return(a*b)

def div(a,b):
    if (a>b):
        return(a/b)
    else:
        return(b/a)
    
if __name__ == "__main__":
    
    x=int(input("Enter the first integer:"))
    y=int(input("Enter the second integer"))
    sum_of_two=sum_two_int(x,y)
    avr=avr_two_int(x,y)
    diff_xy=diff(x,y)
    mult_xy=mult(x,y)
    div_xy=div(x,y)

    print('The sum of the two integers is',sum_of_two)
    print('The average of the two intergers you input is ',avr)
    print('The difference of the two integers is ',diff_xy)
    print('The product of the two integers is ',mult_xy)
    print('The quetient of', x, 'and', y, 'is',div_xy)
    



