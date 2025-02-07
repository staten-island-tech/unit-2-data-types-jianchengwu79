"""
def login(password):
    if password == "secret":
        print("logged in")
    else:
        print("wrong password!!!!")
login("secrets") """

def temp(x):
    if x >=80:
        print("too hot")
    elif x > 60:
        print("nice")
    else:
        print("too cold")
x = (input("what is the temp.."))
temp(x)