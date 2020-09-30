class Google:
    """"
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    For example, given[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    """
    def containsPairWithSum(self, listinput, total):
        dict = {}
        for i in listinput:
            if (total - i) in dict:
                return True
            else:
                dict[i] = i
        return False


def googlemain():
    google = Google()
    print(google.containsPairWithSum([10, 15, 3, 7],17))
    return 1