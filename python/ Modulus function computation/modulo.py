import math

x=9876543210
p=17

x=bin(x)[2:]

n=len(x)
r=math.ceil(math.log2(p))
k= math.ceil(n/r)

if len(x)<k*r:
    x = (k * r - n) * "0" + x

xList=[]

for i in range(1, k + 1):
    xList.append(x[len(x) - i * r:len(x) - (i - 1) * r])


s=0
for i in range(1,k+1):
    s+=int(xList[i-1],2)*(pow(2,r*(i-1))%p)


s_temp=s

while s_temp>=2*p: #tu norówność ostra została zmieniona na nieostrą z podowu błędu w pseudokodzie
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
    s_temp=newS_temp

if p<=s_temp:
    s=s_temp-p
else:
    s=s_temp

print("s=",s)
