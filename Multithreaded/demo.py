
import threading


class A(threading.Thread):

    def __init__(self):
        # 初始化该线程
        threading.Thread.__init__(self)
        # 该线程要执行的程序内容

    def run(self):
        for i in range(30):
            print("我是线程A")


class B(threading.Thread):

    def __init__(self):
        # 初始化该线程
        threading.Thread.__init__(self)
        # 该线程要执行的程序内容

    def run(self):
        for i in range(30):
            print("我是线程B")


# 实例化线程A为t1
t1 = A()
# 启动线程t1
t1.start()
# 实例化线程B为t2
t2 = B()
# 启动线程t2，此时与t1一起执行
t2.start()
