lookup_dict = {'liv':'liva', 'fabrik':'fabric', "fab" : "fabric", "by" :"buy","bye":"buy"}
def _lookup_words(input_text):
    #words = input_text.split() 
    words = input_text    
    new_words = [] 
    for word in words:
        if word.lower() in lookup_dict:        	
            word = lookup_dict[word.lower()]
        new_words.append(word) 
        new_text = " ".join(new_words) 

    return new_words
