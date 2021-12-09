blockchain=[1]
open_transactions=[]
coinsender="Shravan"

def mineblock():
    pass

def add_value(sa):
    blockchain.append([blockchain[-1],sa])

def add_transactions(sender,reciever,amount=2.0):

    transaction={'Sender':sender, 'Recipient':reciever,'Amount':amount}
    open_transactions.append(transaction)

def get_input():

    recipient=input("Enter the recipient of the transaction : \n")
    currency=input("What is the input currency that you wish to invest ? :")
    return (recipient,currency)

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
    


