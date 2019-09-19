import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#from main import converse, alienResponse


def get_jaccard_sim(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
#    print(c)
    return float(len(c)) / (len(a) + len(b) - len(c))


def lemmaTokens(tokens):
    lemma_stem = nltk.stem.WordNetLemmatizer()
    return [lemma_stem.lemmatize(token) for token in tokens]

def normalize(text):
    
    return lemmaTokens(nltk.word_tokenize(text.lower()))

def cosineSimilarity(text1,text2):
    vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    tfidf=vectorizer.fit_transform([text1, text2])
    arr_cosine_sim = cosine_similarity(tfidf[0:1], tfidf)
    #print(arr_cosine_sim)
    return round(arr_cosine_sim[0][1],5)


def sortRankCosine(dictionary):
    #sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1))
    sorted_dictionary = sorted(dictionary.items() , reverse=True, key=lambda x: x[1])
    #sorted(dictionary.items(), reverse=True):
    #copy_dict = sorted_dictionary
    #print(copy_dict)
#    for k,v in copy_dict.items():
#        print(str(k)+ ": "+str(v))
    if sorted_dictionary[0][1] > 0.30:
        return sorted_dictionary[0][0]
    else:
#        alienResponse("Sorry I did not understand your question can you repeat the question")
#        converse(df_new,pre_list_FAQ)
        return ''
        
        


def rankSimilarity(pre_list_FAQ,res):
    rank_cosine={}
    for i in pre_list_FAQ:
#        score=cosineSimilarity(res,i)
        score = cosineSimilarity(res,i)
        rank_cosine[i] = score
    id1 = sortRankCosine(rank_cosine)
    return id1










