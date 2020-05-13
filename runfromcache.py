from nltk.tokenize import sent_tokenize, word_tokenize
import pickle
f = open('livanlp.pickle', 'rb')
classifier = pickle.load(f)
f.close()



#word feature for traing
def word_feats(words):
    return dict([(word, True) for word in words])


data = "i want to sell clothes"
words = word_tokenize(data)
intentName = classifier.classify(word_feats(words))

print(intentName)