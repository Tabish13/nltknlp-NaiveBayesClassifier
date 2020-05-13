#nltk imports
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#training imports
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier


#pickle for serializing object
import pickle

#custom imports
from replaceSlang import _lookup_words


 
data = "tell me a fashion tips"
stopWords = set(stopwords.words('english'))


#stopWords.update([",", "."])
#print(len(stopWords))

words = word_tokenize(data)

print("ORIGINAL WORDS")
print(words)

#filter with stopwords
wordsStopFiltered = []
 
for w in words:
    if w not in stopWords:
        wordsStopFiltered.append(w)

print("FILTERED STOPWORDS ")
print(wordsStopFiltered)


#replace with custom slangs
wordsSlangFiltered = _lookup_words(wordsStopFiltered)
print("AFTER CUSTOM SLANG REPLACED")
print(wordsSlangFiltered)


#Word stemming
ps = PorterStemmer()
wordsStem = []

for w in wordsSlangFiltered:
	wordsStem.append(ps.stem(w))

 
print("AFTER STEMMING FINAL")	
print(wordsStem)


#word feature for traing
def word_feats(words):
    return dict([(word, True) for word in words])


buy_liva = [ 'buy', 'buy', 'buye', 'want', 'want to buy', 'buy' , 'get' ]
sell_liva = [ 'sell', 'selling', 'sel', 'sale', 'sell liva','partner to sell' ]
fashion_encyclopedia = [ 'encyclopedia','fashion', 'gallery', 'collections']

buy_liva_features = [(word_feats(buy_liva), "buy_liva")  ]
sell_liva_features = [(word_feats(sell_liva), "sell_liva") ]
fashion_encyclopedia_features = [(word_feats(fashion_encyclopedia), "fashion_encyclopedia")]


train_set = buy_liva_features + sell_liva_features + fashion_encyclopedia_features

print("TRAIN DATA")
print(train_set)


classifier = NaiveBayesClassifier.train(train_set)

f = open('livanlp.pickle', 'wb')
pickle.dump(classifier, f)
f.close()

print(classifier)


intentName = classifier.classify(word_feats(wordsStem))


print("Mached Intent")
print(intentName)