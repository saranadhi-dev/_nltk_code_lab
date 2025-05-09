corpus = """I'm a passionate and curious individual who loves exploring new ideas and 
turning them into meaningful projects. With a background in IT, 
I enjoy collaborating with others, solving problems creatively, and continuously learning.
"""

from nltk.tokenize import sent_tokenize;
from nltk.tokenize import word_tokenize;
from nltk.tokenize import wordpunct_tokenize;
from nltk.tokenize import TreebankWordTokenizer;
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

fdist = FreqDist()
tree_tokenize = TreebankWordTokenizer()

sentTokenize = sent_tokenize(corpus)
wordTokenize = word_tokenize(corpus)
workPuncTokenize =wordpunct_tokenize(corpus)
treeTokenize = tree_tokenize.tokenize(corpus)


print('sentence')
print(sentTokenize)

print('word')
print(wordTokenize)

print('Word Punctuation')
print(workPuncTokenize)

print('Tree Punctuation')
print(treeTokenize)

print('Frequency')
for word in wordTokenize:
    fdist[word.lower()]+=1

print(fdist.pprint())
fdist.plot(50, title = 'Frequency of Top 20 Words in Text')
plt.show()