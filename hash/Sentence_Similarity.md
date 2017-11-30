# 734. Sentence Similarity

Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

    For example, "great acting skills" and "fine drama talent" are similar,
    if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

    Note that the similarity relation is not transitive.
    For example, if "great" and "fine" are similar, and "fine" and "good" are similar,
    "great" and "good" are not necessarily similar.

    However, similarity is symmetric.
    For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

    Also, a word is always similar with itself.
    For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar,
    even though there are no specified similar word pairs.

    Finally, sentences can only be similar if they have the same number of words.
    So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

- The length of words1 and words2 will not exceed 1000.
- The length of pairs will not exceed 2000.
- The length of each pairs[i] will be 2.
- The length of each words[i] and pairs[i][j] will be in the range [1, 20].

## Method:

using defaultdict(list):

    class Solution(object):
        def areSentencesSimilar(self, words1, words2, pairs):
            """
            :type words1: List[str]
            :type words2: List[str]
            :type pairs: List[List[str]]
            :rtype: bool
            """
            d=collections.defaultdict(list)
            for p in pairs:
                d[p[0]].append(p[1])
                d[p[1]].append(p[0])
            if len(words1)==len(words2):
                if all(words1[i] in d[words2[i]] or words1[i]==words2[i] for i in range(len(words1))):
                    return True
            return False

## Solution:

using defaultdict(set) can remove duplicates:

    class Solution(object):
        def areSentencesSimilar(self, words1, words2, pairs):
            """
            :type words1: List[str]
            :type words2: List[str]
            :type pairs: List[List[str]]
            :rtype: bool
            """
            d=collections.defaultdict(set)
            for p in pairs:
                d[p[0]].add(p[1])
                d[p[1]].add(p[0])
            if len(words1)==len(words2):
                if all(words1[i] in d[words2[i]] or words1[i]==words2[i] for i in range(len(words1))):
                    return True
            return False