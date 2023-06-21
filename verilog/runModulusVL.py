import os

answer = int(input("Co otworzyć? 1-obliczanie modułu, 2-mnożenie, 3-mnożenie dla zmiennego p"))

if answer == 1:
    filename = "modulus.vl"
elif answer==2:
    filename = "multModulus.vl"
else:
    filename = "corectedMultModulus.vl"


if os.path.exists("modulus"):
    os.system("del modulus && iverilog -o modulus " + filename + " && vvp modulus && del modulus")

else:
    os.system("iverilog -o modulus " + filename + " && vvp modulus && del modulus")


