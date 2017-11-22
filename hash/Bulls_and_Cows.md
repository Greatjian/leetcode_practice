# 299. Bulls and Cows

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

For example:

    Secret number:  "1807"
    Friend's guess: "7810"
    Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate digits, for example:

    Secret number:  "1123"
    Friend's guess: "0111"
    In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".

You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

## Method:

compute a first, then collect the left to compute b:

    class Solution(object):
        def getHint(self, secret, guess):
            """
            :type secret: str
            :type guess: str
            :rtype: str
            """
            d=collections.Counter(secret)
            a, b=0, 0
            c=[]
            for i in range(len(secret)):
                if secret[i]==guess[i]:
                    a+=1
                    d[guess[i]]-=1
                else:
                    c.append(guess[i])
            for i in range(len(c)):
                if c[i] in d and d[c[i]]>0:
                    b+=1
                    d[c[i]]-=1
            return str(a)+'A'+str(b)+'B'
            
count together in one for-loop:

    class Solution(object):
        def getHint(self, secret, guess):
            """
            :type secret: str
            :type guess: str
            :rtype: str
            """
            bulls = 0
            for i in xrange(len(secret)):
                if secret[i] == guess[i]:
                    bulls += 1
            both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
            return '%dA%dB' % (bulls, both-bulls)