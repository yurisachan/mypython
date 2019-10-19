import easygui as g
import sys

while 1:
    g.msgbox("hello world")

    msg="以下那个是正确的:"
    title="game"
    choices=["A.你是傻逼","B.他是傻逼","C.你们是傻逼","D.她是傻逼"]

    choice=g.choicebox(msg,title,choices)

    g.msgbox("你的选择是:"+str(choice),"结果")

    msg="begin again?"
    title="请选择"

    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
