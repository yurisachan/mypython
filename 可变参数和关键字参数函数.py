def whoget(name,*gets):
    allget=0
    for get in gets:
        allget+=get
    print(name,"allget:",allget)
whoget('bob',2,4,5)

def howget(name,**gets):
    for what,price in gets.items():
        print(name,what,price)
howget("bob",work=20,work2=50,work3=30)
