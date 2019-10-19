def zhihu(func):
    def decration():
        print("谢邀")
        func()
        print("以上")
    return decration
@zhihu
#修饰器 decorator
def answer1():
    print("good")
    
@zhihu
def answer2():
    print("hello world")

def answer3():
    print("sorry")
answer3=zhihu(answer3)

answer1()
answer2()
answer3()
