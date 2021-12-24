genesis_block={'previous_hash':'','index':0,'Transactions':[]}
blockchain=[genesis_block]
open_transactions=[]
coinsender="Shravan"
participants={"Shravan"}

mining_reward = 10

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def verify_transaction(transaction):
    sent,recieved,balance=get_balances(transaction['Sender'])
    if float(balance) >= float(transaction['Amount']):
        return True
    else:
        return False

def get_balances(participant):
    curr_sender=[[tx['Amount'] for tx in block['Transactions'] if tx['Sender']==participant] for block in blockchain]
    open_curr_sender=[tx['Amount'] for tx in open_transactions if tx['Sender']==participant]
    curr_sender.append(open_curr_sender)
    curr_reciever=[[tx['Amount'] for tx in block['Transactions'] if tx['Recipient']==participant] for block in blockchain]
    amount_sent=0
    amount_recieved=0
    for tx in curr_sender:
        if (len(tx)>0):
            amount_sent+=float(tx[0])

    for tr in curr_reciever:
        if (len(tr)>0):
            amount_recieved+=float(tr[0])
    return (amount_sent,amount_recieved,amount_recieved-amount_sent)

def mineblock():
    last_block=blockchain[-1]
    hashed_block=hash_block(last_block)
    reward_transaction={
        'Sender': 'Mining',
        'Recipient': coinsender,
        'Amount': mining_reward
    }

    copied_transactions=open_transactions[:]
    copied_transactions.append(reward_transaction)

    open_transactions.append(reward_transaction)
    for keys in last_block:
        value=last_block[keys]
        hashed_block=hashed_block+str(value)

    print(hashed_block)
    block={'previous_hash':hashed_block,'index':len(blockchain),'Transactions':copied_transactions}
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

def add_transactions(sender,reciever,amount=1.0):

    transaction={'Sender':sender, 'Recipient':reciever,'Amount':amount}
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(coinsender)
        participants.add(reciever)
        return True
    return False

def get_input():

    recipient=input("Enter the recipient of the transaction : \n")
    currency=input("What is the input currency that you wish to invest ? :")
    return (recipient,currency)

def getoption():
    return input("What's your option?")


def valid_transaction():
    let_mes=True
    for tx in open_transactions:
        if verify_transaction(tx):
            let_mes=True
        else:
            let_mes=False

    return let_mes

match=True
while match:
    print("1 : Invest amount(Enter in INR)")
    print("2: Show current investments")
    print("3: Mine a new block")
    print("4: Check participants")
    print("5: Transaction Validity")
    print("q: Quit")

    inp=getoption()
    if(inp=="1"):
        s=(get_input())
        recipient,amount=s
        if add_transactions(coinsender,recipient,amount):
            print("Transaction Successful")
        else:
            print("Transaction Failed")

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


    elif(inp=="5"):
        result=valid_transaction()
        if result:
            print("Valid Transaction")
        else:
            print("Invalid Transaction")

    else:
        break
    send,recieve,total=get_balances(coinsender)
    print(send,recieve,total)


print(open_transactions)
if not verify_chain():
    print("Invalid blockchain transaction")

else:
    print("Valid blockchain")