
import nltk
import re
from nltk.corpus import stopwords
import string


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
GREETING_INPUTS = ["hello", "hi", "sup", "what's up","hey", "hi there","help","know","may","can","I am glad","morning","good","evening","afternoon"]
REPLACE_BY_SPACE_RE = re.compile('[!"$%&\'()*/:;<=>?@[\\]^`{|}~]')
BAD_SYMBOL_RE = re.compile('[^0-9a-z #+_]')
STOP_WORDS = set(stopwords.words('english'))





def textPrepare(text):
    text = text.lower()
    text = REPLACE_BY_SPACE_RE.sub(" ",text)
    text = BAD_SYMBOL_RE.sub("",text)
    text = ' '.join([w for w in text.split() if w not in STOP_WORDS])
    text = ' '.join([wd for wd in text.split() if wd not in GREETING_INPUTS and len(wd) > 2])
    return text


#res = textPrepare("what is Hire me")




    
    
    