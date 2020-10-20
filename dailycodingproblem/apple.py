import time


class Apple:
    """
    Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
    """
    def scheduler(self, f, n):
        time.sleep(n)
        f()

    def hello_world(self):
        print ("Hello World")


def applemain():
    apple = Apple()
    print(apple.scheduler(apple.hello_world, 1))
    return 1
