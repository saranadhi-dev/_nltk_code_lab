import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

from nltk.tokenize import word_tokenize

text = "This is an example sentence, showing off the tokenization process."

tokens = word_tokenize(text)

print(tokens)

text = "Hi good morning how are you"

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)

print(scores)