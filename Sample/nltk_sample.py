# This is a sample of feasibility for my sentiment analyzer

import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize, sent_tokenize
import re
from nltk.corpus import stopwords

documents = []

sam_file = open("gun_control_sample.txt","r")
stop_words = list(set(stopwords.words('english')))
allowed_word_types = ['J',]

for p in sam_file:
    documents.append( (p,"pos") )
    print(p)
    tokenized_sent = sent_tokenize(p)
    print("Tokenizing Text into sentnences!")
    print(tokenized_sent)
    cleaned = re.sub(r'[^(a-zA-Z)\s]','',p)
    print("Cleaning Text!")
    print(cleaned)
    tokenized_word = word_tokenize(cleaned)
    print("Tokenizing Text into words!")
    print(tokenized_word)
    stopped = [w for w in tokenized_sent if not w in stop_words]
    print("Removing Stopwords!")
    print(stopped)

# Constants#

# BOOST_INCR = 0.293
# BOOST_DCRS = -0.293

# BOOSTER_DICT = \
#     {"absolutely": B_INCR, "amazingly": B_INCR, "awfully": B_INCR,
#      "completely": B_INCR, "considerable": B_INCR, "considerably": B_INCR,
#      "decidedly": B_INCR, "deeply": B_INCR, "effing": B_INCR, "enormous": B_INCR, "enormously": B_INCR,
#      "entirely": B_INCR, "especially": B_INCR, "exceptional": B_INCR, "exceptionally": B_INCR,
#      "extreme": B_INCR, "extremely": B_INCR,
#      "fabulously": B_INCR, "flipping": B_INCR, "flippin": B_INCR, "frackin": B_INCR, "fracking": B_INCR,
#      "fricking": B_INCR, "frickin": B_INCR, "frigging": B_INCR, "friggin": B_INCR, "fully": B_INCR,
#      "fuckin": B_INCR, "fucking": B_INCR, "fuggin": B_INCR, "fugging": B_INCR,
#      "greatly": B_INCR, "hella": B_INCR, "highly": B_INCR, "hugely": B_INCR,
#      "incredible": B_INCR, "incredibly": B_INCR, "intensely": B_INCR,
#      "major": B_INCR, "majorly": B_INCR, "more": B_INCR, "most": B_INCR, "particularly": B_INCR,
#      "purely": B_INCR, "quite": B_INCR, "really": B_INCR, "remarkably": B_INCR,
#      "so": B_INCR, "substantially": B_INCR,
#      "thoroughly": B_INCR, "total": B_INCR, "totally": B_INCR, "tremendous": B_INCR, "tremendously": B_INCR,
#      "uber": B_INCR, "unbelievably": B_INCR, "unusually": B_INCR, "utter": B_INCR, "utterly": B_INCR,
#      "very": B_INCR,
#      "almost": B_DECR, "barely": B_DECR, "hardly": B_DECR, "just enough": B_DECR,
#      "kind of": B_DECR, "kinda": B_DECR, "kindof": B_DECR, "kind-of": B_DECR,
#      "less": B_DECR, "little": B_DECR, "marginal": B_DECR, "marginally": B_DECR,
#      "occasional": B_DECR, "occasionally": B_DECR, "partly": B_DECR,
#      "scarce": B_DECR, "scarcely": B_DECR, "slight": B_DECR, "slightly": B_DECR, "somewhat": B_DECR,
#      "sort of": B_DECR, "sorta": B_DECR, "sortof": B_DECR, "sort-of": B_DECR}
