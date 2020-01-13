class Introduction:


    def fun_helloworld(self):
        print("Hello, World!")


    def fun_ifelse(self,n):
        if (n % 2 != 0) or (6 <= n <= 20):
            print("Weird")
        else:
            print("Not Weird")


    def fun_arithematicoperators(self, a, b):
        print(a + b)
        print(a - b)
        print(a * b)


    def fun_division(self, a,b):
        print(a//b)
        print(a/b)


def intromain():
    intro = Introduction()
    intro.fun_helloworld()
    intro.fun_ifelse(3)
    intro.fun_arithematicoperators(3,2)
    intro.fun_division(4,3)
    return 1