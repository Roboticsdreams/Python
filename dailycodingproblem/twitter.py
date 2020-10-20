from dailycodingproblem import commonutils

class Twitter:
    """"
    Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
    return all strings in the set that have s as a prefix.
    For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
    Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
    """

    def autocomplete(self, str, keys):
        t = commonutils.Trie()
        t.formTrie(keys)
        return t.getAutoSuggestions(str)

def twittermain():
    twitter = Twitter()
    str = "de"
    orglist = ['dog','deer','deal']
    print(twitter.autocomplete(str, orglist))
    return 1
