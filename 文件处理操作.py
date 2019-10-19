def Save(a,b,count):
    file_name_a="a"+str(count)+".txt"
    file_name_b="b"+str(count)+".txt"

    a_file=open(file_name_a,"w")
    b_file=open(file_name_b,"w")

    a_file.writelines(a)
    b_file.writelines(b)

    a_file.close()
    b_file.close() 

def Split(file_name):
    
    f=open(file_name)

    a=[]
    b=[]
    count=1

    for line in f:
        if line[:]!="\n":
            (role,word)=line.split(":",1)
            if role =="a":
                a.append(word)
            if role =="b":
                b.append(word)
        else:
            Save(a,b,count)
            
            a=[]
            b=[]
            count+=1
            
    Save(a,b,count)
    
    f.close()

Split("D:\\test2.txt")


