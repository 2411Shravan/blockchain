genesis_block={'previous_hash':'','index':0,'Transactions':[]}
blockchain=[genesis_block]
open_transactions=[]
coinsender="Shravan"

def mineblock():
    last_block=blockchain[-1]
    hashed_block=[last_block[key] for key in last_block]
    for keys in last_block:
        value=last_block[keys]
        hashed_block=hashed_block+str(value)

    print(hashed_block)
    block={'previous_hash':hashed_block,'index':len(blockchain),'Transactions':open_transactions}
    blockchain.append(block)
    

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
    print("3: Mine a new block")
    print("q: Quit")

    inp=getoption()
    if(inp=="1"):
        s=(get_input())
        recipient,amount=s
        add_transactions(coinsender,recipient,amount)

    elif(inp=="2"):
        for block in open_transactions:
            i=1
            print("Printing block "+str(i)+" in blockchains : \n")
            i=i+1
            print(block)

    elif(inp=="3"):
        mineblock()
    else:
        break
    


print(open_transactions)
