blockchain=[1]

def add_value(sa):
    blockchain.append([blockchain[-1],sa])
    print(blockchain)


def get_input():
    return input("What is the input currency that you wish to invest ? :")


s=(get_input())
add_value(float(s))
s=(get_input())
add_value(float(s))
s=(get_input())
add_value(float(s))