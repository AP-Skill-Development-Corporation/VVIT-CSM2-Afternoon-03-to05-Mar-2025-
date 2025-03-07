print('
welcome to r+ mode') for dig in range(1,n//2+1):
        if n%dig==0:
            fc+=1
    if fc==1:
        return True
    else:
        return False
    
    
#def is_prime(n)