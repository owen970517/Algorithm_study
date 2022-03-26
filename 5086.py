while(True):
    a,b = map(int,input().split())
    if (a == 0 and b ==0):
        break
    elif(a%b == 0):
        result = "multiple"
        print(result)
    elif (a%b !=0 and a//b != 0 ):
        result = "neither"
        print(result)
    else :
        result ='factor'
        print(result)