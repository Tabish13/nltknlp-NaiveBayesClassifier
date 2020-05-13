#nltk imports
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def processing(sentence):
	stopWords = set(stopwords.words('english'))
	words = word_tokenize(sentence)
	#filter with stopwords
	wordsStopFiltered = []
	 
	for w in words:
	    if w not in stopWords:
	        wordsStopFiltered.append(w)

	#Word stemming
	ps = PorterStemmer()
	wordsStem = []

	for w in wordsStopFiltered:
		wordsStem.append(ps.stem(w))

	#word feature for traing
	def word_feats(words):
	    return dict([(word, True) for word in words])

	return word_feats(wordsStem)
