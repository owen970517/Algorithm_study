change = int(input())
mok = change//5
na = change%5
result=0
if(na%2==1):
    result += (mok-1)
    change -= 5*(mok-1)
    result+=change//2
elif(na==0):
    result += mok
else :
    result += mok
    change -= 5*mok
    result+=change//2
print(result)
