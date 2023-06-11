import os

filename = "hello"

if os.path.exists("modulus"):
    os.system("del modulus && iverilog -o modulus modulus.vl && vvp modulus && del modulus")

else:
    os.system("iverilog -o modulus modulus.vl && vvp modulus && del modulus")


