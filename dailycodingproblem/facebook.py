class Facebook:
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
    You can assume that the messages are decodable. For example, '001' is not allowed.
    """

    def numDecodings(self, s):
        if s == '0' or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        res = [0] * (len(s) + 1)
        res[0] = 1
        for i in range(1, len(res)):
            if s[i - 1] != '0':
                res[i] = res[i - 1]
            if i != 1 and '10' <= s[i - 2:i] <= '26':
                res[i] += res[i - 2]
        return res[-1]

def facebookmain():
    fb = Facebook()
    print(fb.numDecodings('111'))
    return 1
