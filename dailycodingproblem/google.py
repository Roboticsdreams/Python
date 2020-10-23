from dailycodingproblem.commonutils import Node
from collections import deque

deserializecnt = 0


class Google:
    """"
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    For example, given[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    """

    def containspairwithsum(self, listinput, total):
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

    def serialize(self, node=None, s=""):
        if node is None:
            return None

        stack = deque()
        stack.append(node)
        while stack:
            node = stack.pop()
            if node is not None:
                s += node.val + ","
                stack.append(node.right)
                stack.append(node.left)
            else:
                s += "#,"
        return s

    def deserialize(self, s):
        if s is None:
            return None

        arr = s.split(",")
        return self.helper(arr, 0)

    def helper(self, arr, t):
        if arr[t] == "#":
            return None
        else:
            root = Node(arr[t])
            t = t + 1
            root.left = self.helper(arr, t)
            t = t + 1
            root.right = self.helper(arr, t)
            return root

    """"
    Given an array of integers where every integer occurs three times except for one integer, 
    which only occurs once, find and return the non-duplicated integer.
    For example, 
    Given [6, 1, 3, 3, 3, 6, 6], return 1. 
    Given [13, 19, 13, 13], return 19.
    Do this in O(N) time and O(1) space.
    """

    def nonrepeatingelement(self, arr):
        ones = 0
        twos = 0

        for i in range(len(arr)):
            twos = twos | (ones & arr[i])
            ones = ones ^ arr[i]
            common_bit_mask = ~(ones & twos)
            ones &= common_bit_mask
            twos &= common_bit_mask
        return ones


def googlemain():
    google = Google()
    print(google.containspairwithsum([10, 15, 3, 7], 17))
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(google.deserialize(google.serialize(node)).left.left.val)
    print(google.nonrepeatingelement([13, 19, 13, 13]))
    return 1
