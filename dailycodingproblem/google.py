from dailycodingproblem.commonutils import Node

deserializecnt = 0


class Google:
    """"
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    For example, given[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    """

    def containsPairWithSum(self, listinput, total):
        dicts = {}
        for i in listinput:
            if (total - i) in dicts:
                return True
            else:
                dicts[i] = i
        return False

    """"
    Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
    and deserialize(s), which deserializes the string back into the tree.
    
    For example, given the following Node class
    class Node:
        def _init_(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    The following test should pass:
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        assert deserialize(serialize(node)).left.left.val == 'left.left'
    """

    def serialize(self, node, s=""):
        if not node:
            s += "# "
            return s
        s += (str(node.val) + " ")
        s = self.serialize(node.left, s=s)
        s = self.serialize(node.right, s=s)
        return s

    def deserialize(self, s):
        global deserializecnt
        if s[deserializecnt] == "#":
            if deserializecnt < len(s) - 2:
                deserializecnt += 2
            return None
        else:
            space = s[deserializecnt:].find(" ")
            sp = space + deserializecnt
            node = Node(s[deserializecnt:sp])
            deserializecnt = sp + 1
            node.left = self.deserialize(s)
            node.right = self.deserialize(s)
            return node

def googlemain():
    google = Google()
    print(google.containsPairWithSum([10, 15, 3, 7], 17))
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(google.deserialize(google.serialize(node)).left.left.val)
    return 1
