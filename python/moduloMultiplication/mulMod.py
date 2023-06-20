
a = 53
b = 19
p = 47

print("a= ", a, "b= ", b)

a = bin(a)[2:]
b = bin(b)[2:]

if len(a) > 6:
    print("Za duże a")
    exit()
if len(b) > 6:
    print("Za duże b")
    exit()

if len(a) < 6:
    a = (6 - len(a)) * "0" + a
if len(b) < 6:
    b = (6 - len(b)) * "0" + b

a = list(a)
b = list(b)

print("a= ", a, "b= ", b)

label1 = int(int(''.join(map(str, a[3:6])), 2)) * int(int(''.join(map(str, b[3:6])), 2))
label2 = (int(int(''.join(map(str, a[3:6])), 2)) * int(int(''.join(map(str, b[:3])), 2)) * 8) % p
label3 = (int(int(''.join(map(str, a[:3])), 2)) * int(int(''.join(map(str, b[3:6])), 2)) * 8) % p
label4 = (int(int(''.join(map(str, a[:3])), 2)) * int(int(''.join(map(str, b[:3])), 2)) * 17) % p

temp_R_1 = label1 + label2 + label3 + label4
temp_R_1 = bin(temp_R_1)[2:]

if len(temp_R_1) < 8:
    temp_R_1 = (8 - len(temp_R_1)) * "0" + temp_R_1

label5 = (int(''.join(map(str, temp_R_1[2:5])), 2) * 8) % p
label6 = (int(''.join(map(str, temp_R_1[:2])), 2) * 17) % p

temp_R_2 = int(temp_R_1[5:], 2) + label5 + label6

if temp_R_2 >= p:
    temp_R = temp_R_2 - p
else:
    temp_R = temp_R_2

R = temp_R

print("R =", R)

a = ''.join(str(bit) for bit in a)
a = int(a, 2)

b = ''.join(str(bit) for bit in b)
b = int(b, 2)

print("Poprawny wynik:", (a * b) % p)

