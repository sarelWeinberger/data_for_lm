import abc
from nltk.corpus import reuters
from collections import Counter

counts = Counter(reuters.words())
# total_count = len(reuters.words())


# The most common 20 words are ...
# print
# counts.most_common(n=20)
# # [(u'.', 94687), (u',', 72360), (u'the', 58251), (u'of', 35979), (u'to', 34035), (u'in', 26478), (u'said', 25224), (u'and', 25043), (u'a', 23492), (u'mln', 18037), (u'vs', 14120), (u'-', 13705), (u'for', 12785), (u'dlrs', 11730), (u"'", 11272), (u'The', 10968), (u'000', 10277), (u'1', 9977), (u's', 9298), (u'pct', 9093)]
#
# # Compute the frequencies
# for word in counts:
#     counts[word] /= float(total_count)
#
# # The frequencies should add up to 1
# print
# sum(counts.values())  # 1.0
#
# import random
#
# # Generate 100 words of language
# text = []
#
# for _ in range(100):
#     r = random.random()
#     accumulator = .0
#
#     for word, freq in counts.iteritems():
#         accumulator += freq
#
#         if accumulator >= r:
#             text.append(word)
#             break
#
# print
# ' '.join(text)
# tax been its and industrial and vote " decision rates elimination and 2 . base Ltd one merger half three division trading it to company before CES mln may to . . , and U is - exclusive affiliate - biggest its Association sides above two nearby NOTES 4TH prepared term areas growth said to each gold policy 0 PLOUGH kind economy director currencies requiring . ' loan growth , 83 . new The target Refining 114 STAKE the it on . to ; measure deposit Corp Emergency on 63 the reported the TREASURY state EC to Grosso as basius


# code courtesy of https://nlpforhackers.io/language-models/

# from nltk.corpus import reuters
# from nltk import bigrams, trigrams
# from collections import Counter, defaultdict
#
# # Create a placeholder for model
# model = defaultdict(lambda: defaultdict(lambda: 0))
#
# # Count frequency of co-occurance
# for sentence in reuters.sents():
#     for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
#         model[(w1, w2)][w3] += 1
#
# # Let's transform the counts to probabilities
# for w1_w2 in model:
#     total_count = float(sum(model[w1_w2].values()))
#     for w3 in model[w1_w2]:
#         model[w1_w2][w3] /= total_count