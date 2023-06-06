import math

import numpy as np

a =45 #45
b =15 #15

p=1   #47
wynik=(a*b)%p
a = bin(a)[2:]

n=len(a)
r=math.ceil(math.log2(p))
r=3
k= math.ceil(n/r)



if len(a) < k*r:
    a = (k * r - n) * "0" + a

aList=[]
for i in range(1, k + 1):
    aList.append(a[len(a) - i * r:len(a) - (i - 1) * r])

print("a =",a)
print("A1,A2,... =",aList)







b = bin(b)[2:]
if len(b) < k*r:
    b = (k * r - len(b)) * "0" + b

bList=[]
for i in range(1, k + 1):
    bList.append(b[len(b) - i * r:len(b) - (i - 1) * r])

print("b =",b)
print("B1,B2,... =",bList)


s_temp=0

for i in range(1,k+1):
    for j in range(1,k+1):
        s_temp+=(int(aList[i-1],2)*int(bList[j-1],2)*(2**(3*(i+j-2)))%p)


print("s_temp=",s_temp)


while s_temp>2*p:
    print("--------------------------Pętla sie wykonała")
    s_temp = bin(s_temp)[2:]
    n_temp=len(s_temp)
    k_temp=math.ceil(n_temp/r)

    if len(s_temp)<k_temp*r:
        s_temp = (k_temp * r - n_temp) * "0" + s_temp

    sList=[]
    for i in range(1, k_temp + 1):
        sList.append(s_temp[len(s_temp) - i * r:len(s_temp) - (i - 1) * r])

    newS_temp=0
    for i in range(1,k_temp+1):
        newS_temp+=int(sList[i-1],2)*(pow(2,r*(i-1))%p)
    print("s_temp",int(s_temp,2))
    s_temp=newS_temp



if p<=s_temp:
    s=s_temp-p
else:
    s=s_temp


print("s               =",s)
print("prawidlowy wynik=",wynik)
if wynik!=s:
    print("WYNIK SIE NIE ZGADZA")
else:
    print("WYNIK SIE ZGADZA")
