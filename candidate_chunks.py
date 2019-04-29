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
nltk.download('stopwords')
nltk.download('punkt')


######## Extracting candidate terms in the form of chunks ###################
def extract_candidate_chunks(text, grammar=r'KT: {(<JJ>* <NN.*>+ <IN>)? <JJ>* <NN.*>+}'):
    
    
    import itertools, nltk, string
    
    # exclude candidates that are stop words or entirely punctuation
    punct = set(string.punctuation)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    
    # tokenize, POS-tag, and chunk using regular expressions
    chunker = nltk.chunk.regexp.RegexpParser(grammar)
    tagged_sents = nltk.pos_tag_sents(nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text))
    
    print(tagged_sents)
    all_chunks = list(itertools.chain.from_iterable(nltk.chunk.tree2conlltags(chunker.parse(tagged_sent))
                                                    for tagged_sent in tagged_sents))
    
    print(all_chunks)
    
    # join constituent chunk words into a single chunked phrase
    candidates = [' '.join(word for word, pos, chunk in group).lower()
                  for key, group in itertools.groupby(all_chunks, lambda (word,pos,chunk): chunk != 'O') if key]
    return candidates
                

text="The name Bollywood is a portmanteau derived from Bombay (the former name for Mumbai) and Hollywood (in California), the center of the American film industry.[18] Bollywood does not exist as a physical place. The name Bollywood is criticized by some film journalists and critics by arguing that it makes the industry look like a poor cousin to Hollywood."                
candidate_chunks=extract_candidate_chunks(text)
print(candidate_chunks)