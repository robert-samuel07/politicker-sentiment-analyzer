# This is a sample of feasibility for my sentiment analyzer

import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize, sent_tokenize
import re
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

documents = []

sam_file = open("gun_control_sample.txt","r")
stop_words = list(set(stopwords.words('english')))

def get_wordnet_pos(nltk_tag):
    
""" This fucntion uses converts nltk tagged to wordnet tagged"""

    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def lemmatize_paragraph(p):
    # Tokenize and POS tage the tokens
    tokenized_word = nltk.pos_tag(nltk.word_tokenize(cleaned))
    print("\nTokenizing Text into words and converting it to a Dictionary!\n\n")
    print("\n\n",tokenized_word,"\n\n")

    #create a tuple of (token,wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], get_wordnet_pos(x[1])), tokenized_word)
    lemmatized_p = []

    for word, tag in wordnet_tagged:
        if tag is None:
            # If no tag is available append as is
            lemmatized_p.append(word)
        else:
            # use the tag to lemmatize tokens
            lemmatized_p.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_p)


lemmatizer = WordNetLemmatizer()
for p in sam_file:
    documents.append( (p,"pos") )
    print(p)

    cleaned = re.sub(r'[^(a-zA-Z)\s]','',p)
    print("\nCleaning Text!\n")
    print(cleaned)

    #stopped = [w for w in tokenized_sent if not w in stop_words]
    #print("\nRemoving Stopwords!\n")
    #print(stopped)

    print("\nLemmatizing Article\n")
    print(lemmatize_paragraph(cleaned))


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
