
# To run this code user the command: python3 nltk_sample.py
import re
import nltk
import csv
import random
import pandas as pd
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from matplotlib import pyplot as plt

documents = []
valence_dict = []
dominance_dict = []


# read csv file as a list of lists
with open('Ratings_Warriner_et_al.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

with open("IHD_Speech.txt",'r') as file:
    p =file.read().replace('\n', '')
    #print(p)
    cleaned = re.sub(r'[^(a-zA-Z)\s]','',p)
    prepped_text = cleaned.lower()

    print(type(prepped_text))
    print(prepped_text)
text_list = prepped_text.split(" ")
print(text_list)


def Extract_words(list_of_rows):
    return [item[1] for item in list_of_rows]

def Extract_valence_value(list_of_rows ):
    return [item[2] for item in list_of_rows]

def Extract_dominance_value(list_of_rows):
    return [item[8] for item in list_of_rows]

lexicon = Extract_words(list_of_rows)
#print(lexicon)
valence_list = Extract_valence_value(list_of_rows)
#print(valence_list)
dominance_list = Extract_dominance_value(list_of_rows)
#print(dominance_list)

def get_wordnet_pos(nltk_tag):
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

def lemmatize_paragraph_into_words():
    lemmatizer = WordNetLemmatizer()
    # Tokenize and POS tage the tokens
    tokens = nltk.pos_tag(nltk.word_tokenize(cleaned))
    #print("\nTokenizing Text into words and converting it to a Dictionary!\n\n")
    #print("\n\n",tokens,"\n\n")
    #create a tuple of (token,wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], get_wordnet_pos(x[1])), tokens)
    lemmatized_tokens = []
    for word, tag in wordnet_tagged:
        if tag is None:
            # If no tag is available append as is
            lemmatized_tokens.append(word)
        else:
            # use the tag to lemmatize tokens
            lemmatized_tokens.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_tokens)

def tokenize_sentences():
    sentence_txt = nltk.sent_tokenize(p) # gives a list
    # loop over each sentence and tokenize them seperately
    for sentence in sentence_txt:
        tokenized_sentence = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokenized_sentence)
        #print(tagged)


common_words = []
data_frame_positions = []
valence_values = []
domiannce_values = []
# Printing words shared between the article and data
for element in text_list:
    if element in lexicon:
        common_words.append(element)
print(common_words)


#Printing the element of each word to reference the valence list
for i in range(len(text_list)):
    for j in range(len(lexicon)):
        if text_list[i] == lexicon[j]:
            data_frame_positions.append(j)
#Get values at each position, that correspond with the word
valence_values = [valence_list[i] for i in data_frame_positions]
#print(valence_values)
dominance_values = [dominance_list[i] for i in data_frame_positions]
#print(dominance_values)

# Convert the valence and dominance values in lists from strings to ints
converted_valence_values = list(map(float,valence_values))
converted_dominance_values = list(map(float,dominance_values))
number_common_words = len(common_words)
print("\n Number of Words in Coomon with Data: ", number_common_words)

def valence_score():
# Get the mean valence and domiance score of the text
    theValenceSum = sum(converted_valence_values)
    mean_valence_score = theValenceSum/number_common_words
    return mean_valence_score

def dominance_score():
    theDominanceSum = sum(converted_dominance_values)
    mean_dominance_score = theDominanceSum/number_common_words
    return mean_dominance_score

give_valence_score = valence_score()
print("The average valence score: ", give_valence_score)
give_dominance_score = dominance_score()
print("The average dominance score: ", give_dominance_score)



def plotting():
    fig = plt.figure()
    plt.xlim(5,6)
    plt.ylim(5,6)
    plt.axhline(y=5.5, color='r', linestyle='-')
    plt.axvline(x=5.5, color='r', linestyle='-')
    fig.suptitle('Political Location', fontsize = 20)
    plt.xlabel('Valence Score', fontsize=18)
    plt.ylabel('Dominance Score', fontsize=18)
    plt.scatter(give_valence_score,give_dominance_score)
    plt.show()

print("\nEnd\n")

print("\n\n",plotting())
