file_name=input("输入你要打开的文件名：")
f=open(file_name)
print("文件的内容是:")
for line in f:
    print(line)
