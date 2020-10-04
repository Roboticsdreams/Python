class JaneStreet:
    """
    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
    For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
    Given this implementation of cons:
    def cons(a, b):
        def pair(f):
            return f(a, b)
        return pair

    Implement car and cdr.
    """

    def cons(self, a, b):
        def pair(f):
            return f(a, b)

        return pair

    def car(self, cons):
        return cons(lambda a, b: a)

    def cdr(self, cons):
        return cons(lambda a, b: b)


def janestreetmain():
    js = JaneStreet()
    print(js.car(js.cons(3, 4)))
    print(js.cdr(js.cons(3, 4)))
    return 1
