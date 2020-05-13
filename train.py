#training imports
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import pickle
from wordProcessing import processing


def train_nlp(nlptraindata, model_name):
    

    #word feature for traing
    def word_feats(words):
        return dict([(word, True) for word in words])

    
    train_set = []

    for intentkey in nlptraindata:
        #print(intentkey)
        if("utterances" in nlptraindata[intentkey]):
            for utterance in nlptraindata[intentkey]["utterances"]:                
                train_set.append((processing(utterance), intentkey))
                
    #print("TRAIN DATA")
    #print(train_set)
    classifier = NaiveBayesClassifier.train(train_set)

    #write classifier to use in read
    f = open(model_name+'.pickle', 'wb')
    pickle.dump(classifier, f)
    f.close()