genesis_block={'previous_hash':'','index':0,'Transactions':[]}
blockchain=[genesis_block]
open_transactions=[]
coinsender="Shravan"
participants={"Shravan"}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balances(participant):
    curr_sender=[[tx['Amount'] for tx in block['Transactions'] if tx['Sender']==participant] for block in blockchain]
    curr_reciever=[[tx['Amount'] for tx in block['Transactions'] if tx['Recipient']==participant] for block in blockchain]
    amount_sent=0
    amount_recieved=0
    for tx in curr_sender:
        if (len(tx)>0):
            amount_sent+=float(tx[0])

    for tr in curr_reciever:
        if (len(tr)>0):
            amount_recieved+=float(tx[0])
    return {amount_sent,amount_recieved}

def mineblock():
    last_block=blockchain[-1]
    hashed_block=hash_block(last_block)
    for keys in last_block:
        value=last_block[keys]
        hashed_block=hashed_block+str(value)

    print(hashed_block)
    block={'previous_hash':hashed_block,'index':len(blockchain),'Transactions':open_transactions}
    blockchain.append(block)
    return True
    

def verify_chain():
    for (index,block) in enumerate(blockchain):
        if(index==0):
            continue
        if block['previous_hash']==hash_block(blockchain[index-1]):
            return False
    
    return True

def add_value(sa):
    blockchain.append([blockchain[-1],sa])

def add_transactions(sender,reciever,amount=2.0):

    transaction={'Sender':sender, 'Recipient':reciever,'Amount':amount}
    open_transactions.append(transaction)
    participants.add(coinsender)
    participants.add(reciever)

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
    print("4: Check participants")
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
        if mineblock():
            open_transactions=[]

    elif(inp=="4"):
        print(participants)

    else:
        break
    
    print(float(get_balances(coinsender)))


print(open_transactions)
if not verify_chain():
    print("Invalid blockchain transaction")

else:
    print("Valid blockchain")