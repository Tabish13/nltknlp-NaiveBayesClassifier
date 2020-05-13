# nltknlp-NaiveBayesClassifier
Intent detection  using the naive bayes classifier


```
GET http://localhost:5000/?model=livanlp&query=best%20fashion%20in%20town

curl --location --request POST 'http://localhost:5000/train?model=livanlp2020' \
--header 'Content-Type: application/json' \
--data-raw '{
	
	"inten_name1":{
		"utterances":["i want apple", "i want to buy apple"]
	},
	"inten_name2":{
		"utterances":["i want oranges", "i want to buy oranges"]
	}
	
}'
```
