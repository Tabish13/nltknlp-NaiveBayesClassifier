from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
from nltk.tokenize import sent_tokenize, word_tokenize
from flask import request
import json

from train import train_nlp
from wordProcessing import processing





app = Flask(__name__)
api = Api(app)



# argument parsing
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('query')
parser.add_argument('model')
#parser.add_argument('model',location='headers')
parser.add_argument('Content-Type',location='headers')
parser.add_argument('data',type=list,location='json')


class PredictSentiment(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()

        statuscode = 500        

        if 'query' not in args or args['query'] is None:
            return "Query is missing", statuscode
        if 'model' not in args or args['model'] is None:            
            return "Model name is missing", statuscode

        user_query = args['query']
        classifier_name = args['model']
        #data = user_query


        try:                         
            #loadinng classifier from cache                                    
            f = open(classifier_name+'.pickle', 'rb')
            classifier = pickle.load(f)
            f.close()
                       
            #print(processing(user_query))
            intentName = classifier.classify(processing(user_query))
            #intentName = classifier.prob_classify(processing(user_query))
            
            statuscode = 200
            # create JSON object
            output = {'intentName': intentName, 'text':user_query}
        except Exception as e:
            output = "Unable to load classifier "
            print(e)
            #print("Unable to load classifier ".join(str(e)))
        finally:
            return output, statuscode
        
       
        
        



class TrainNLPModel(Resource):
   def post(self):
        # use parser and find the user's query
        args = parser.parse_args()
        
        statuscode = 500

        if 'model' not in args or args['model'] is  None:
            return "Model is not defined", statuscode
        model_name = args['model']
        #print(model_name)
        #print(args)
        
        try:             
            trainingData = request.get_json()            
            statuscode = 200                      
            train_nlp(trainingData, model_name)
            output = "Training Successfull"
        except Exception as e:            
            output = "Something went wrong"
            print(e)
            statuscode = 400
        finally:
            #output = args
            return output, statuscode


            

# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictSentiment, '/')
api.add_resource(TrainNLPModel, '/train')


if __name__ == '__main__':
    app.run(debug=True)