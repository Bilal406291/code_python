# Given an array of integers, find the sum of its elements.
def list_sum(ar):
    total=0
    l=len(ar)
    for i in range(l):
        total+=ar[i]
    return(total)

def list_sum2(ar):
    sm=0
    for i in ar:
        sm+=i
    return(sm)

if __name__ == "__main__":
    
    s = input()
    nums = list(map(int, s.split()))
    aval=list_sum(nums)
    bval=list_sum2(nums)
    
    print('The sum from list_sum',aval)
    print('The sum from list_sum2',bval)


    

    
