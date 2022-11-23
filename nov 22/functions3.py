# functions3.py
# 11/22/2022
# daniel roberts
# demonstrates functions calling functions

def dodge():
    str1=" great power"
    return(str1)

def baffle():
    str2="with"
    str2=str2+dodge()
    str2=str2+" comes great"
    return(str2)

def tricks():
    str3=baffle()
    str3=str3+" responsibility."
    return str3

if __name__=="__main__":
    print("can you find the secret message?")
    print("\n",tricks(),"\n")
    print("congratulations, you found it!")