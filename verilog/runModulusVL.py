import os

answer = int(input("Co otworzyć? 1-obliczanie modułu, 2-mnożenie"))

if answer == 1:
    filename = "modulus.vl"
else:
    filename = "multModulus.vl"


if os.path.exists("modulus"):
    os.system("del modulus && iverilog -o modulus " + filename + " && vvp modulus && del modulus")

else:
    os.system("iverilog -o modulus " + filename + " && vvp modulus && del modulus")


