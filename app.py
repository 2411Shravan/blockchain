blockchain=[1]
open_transactions=[]

def mineblock():
    pass

def add_value(sa):
    blockchain.append([blockchain[-1],sa])



def get_input():
    return input("What is the input currency that you wish to invest ? :")

def getoption():
    return input("What's your option?")




match=True
while match:
    print("1 : Invest amount(Enter in INR)")
    print("2: Show current investments")
    print("q: Quit")

    inp=getoption()
    if(inp=="1"):
        s=(get_input())
        add_value(float(s))

    elif(inp=="2"):
        for block in blockchain:
            i=1
            print("Printing block "+str(i)+" in blockchains : \n")
            i=i+1
            print(block)

    else:
        break
    


