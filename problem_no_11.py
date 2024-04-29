def papersizes(i,n,l,b):
    if n !=0:
        print(f'A{i}:L={int(l)}B={int(b)}')
        newb=l/2
        newl=b
        n-=1
        i+=1
        papersizes(i,n,newl,newb)

papersizes(0,7,1189,841)


class Complex:
    def __init__(self,r=0.0,i=0.0):
        self.__real=r
        self.__imag=i
    def __eq__(self,other):
        if self.__real==other.__real and self.__imag==other.__imag:
            return True
        else:
            return False
c1=Complex(1.1,0.2)
c2=Complex(2.1,0.4)
c3=c1
if c1==c2:
    print('Attributes of c1 and c2 are same')
print('Attributes of c1 and c2 are different')
if type(c1)==type(c3):
    print('c1 and c3 are of same type')
else:
    print('c1 and c3 are of different type')
if c1 is c3:
    print('c1 and c3 are pointing to same object')
else:
    print('c1 and c3 are pointing to different object')    
