# 249. Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, 

    for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

    "abc" -> "bcd" -> ... -> "xyz"

Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

    For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
    A solution is:
    
    [
      ["abc","bcd","xyz"],
      ["az","ba"],
      ["acef"],
      ["a","z"]
    ]

## Method:

    class Solution(object):
        def groupStrings(self, strings):
            """
            :type strings: List[str]
            :rtype: List[List[str]]
            """
            d=collections.defaultdict(list)
            for string in strings:
                key=""
                offset=ord(string[0])-ord('a')
                for s in string:
                    new=chr(ord(s)-offset)
                    if ord(new)<ord('a'):
                        new=chr(ord(new)+26)
                    key+=new
                d[key].append(string)
            return [d[k] for k in d.keys()]
            
利用%化简key:

    class Solution(object):
        def groupStrings(self, strings):
            """
            :type strings: List[str]
            :rtype: List[List[str]]
            """
            d=collections.defaultdict(list)
            for string in strings:
                key=tuple((ord(s)-ord(string[0]))%26 for s in string)
                d[key].append(string)
            return d.values()