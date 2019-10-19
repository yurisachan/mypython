#引入模块
import sys
sys.path.append("D:\\pythonfile")#搜索路径扩展
import 九九乘法表 as b
print(b)


'''for i in range(10):
    if i%2!=0:
        print(i)
        continue
    i+=2
    print(i)
 '''   
a=[2,34,54,6,7,75,5,5]

#顺序排列
a.sort()
print(a)

#逆序排列
a.sort(reverse=True)
print(a)

#元组切片
b=(1,2,4,5)
b=b[:2]+(3,)+b[2:]
print(b)
