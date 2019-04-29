import numpy as np
import matplotlib.pyplot as plt
from gensim.models import word2vec
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import nltk,re, pprint
from nltk.chunk.regexp import *
from nltk.corpus import stopwords
from nltk.chunk.regexp import tag_pattern2re_pattern


############### Extract candidate words ##################
def extract_candidate_words(text, good_tags=set(['JJ','JJR','JJS','NN','NNP','NNS','NNPS'])):
    import itertools, nltk, string

    # exclude candidates that are stop words or entirely punctuation
    punct = set(string.punctuation)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    # tokenize and POS-tag words
    tagged_words = itertools.chain.from_iterable(nltk.pos_tag_sents(nltk.word_tokenize(sent)
                                                                    for sent in nltk.sent_tokenize(text)))
    # filter on certain POS tags and lowercase all words
    candidates = [word.lower() for word, tag in tagged_words
                  if tag in good_tags and word.lower() not in stop_words
                  and not all(char in punct for char in word)]

    return candidates

text="The name Bollywood is a portmanteau derived from Bombay (the former name for Mumbai) and Hollywood (in California), the center of the American film industry.[18] Bollywood does not exist as a physical place. The name Bollywood is criticized by some film journalists and critics by arguing that it makes the industry look like a poor cousin to Hollywood."      
candidate_terms=extract_candidate_words(text)
print(candidate_terms)