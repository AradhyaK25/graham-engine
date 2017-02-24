import nltk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

nltk.data.path.append(BASE_DIR)
from nltk import word_tokenize
from nltk.corpus import reuters
from nltk.stem.porter import PorterStemmer
from sortedcontainers import SortedList
import re
import json
import time
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

#splits string into tokens 
#"String" ,[tokens] => [token], len
def tokenize(text, stopwords):
    p = re.compile('[a-zA-Z0-9]+');
    words = map(lambda word: word.lower(), word_tokenize(text));   
    count_twords=len(words)
    tokens = list(map(lambda token: (token if stopwords.count(token)>=1 else str(PorterStemmer().stem(token))), words));
    filtered_tokens =  list(filter(lambda token: p.match(token), tokens));
    return filtered_tokens,count_twords

#returns dictionary of tokens with positional info
#[token], [tokens] => [token->[pos]]
def index_tokens(tokens, stopwords):
	indexedTokens = {}
	for index, token in enumerate(tokens):
		if token in indexedTokens.keys():
			indexedTokens[token].append(index)
		elif stopwords.count(token) == 0:
			indexedTokens[token] = [index]
	return indexedTokens

#returns non-inverted index
#[file], [tokens] => [file->[token->[pos]]], [len]
def index_files(documents, stopwords):
	index = {}
	len_docs = {}
	for file in documents:
		#print file
		index[file], len_docs[file] = tokenize(str(reuters.raw(file)),stopwords)
		index[file] = index_tokens(index[file], stopwords)
	return index, len_docs;

#returns inverted index
#[file->[token->[pos]]], [tokens] => [token->[file->[pos]]], [len]
def inverted_index(documents, stopwords):
	print "building index..."
	index, len_docs = index_files(documents, stopwords)
	print "inverting index..."
	inv_index = {}
	for file in index.keys():
		for token in index[file].keys():
			if token in inv_index.keys():
				if file in inv_index[token].keys():
					inv_index[str(token)][str(file)].extend(index[file][token])
				else:
					inv_index[str(token)][str(file)] = index[file][token]
			else:
				inv_index[str(token)] = {str(file): index[file][token]}
	return inv_index, len_docs

def stop_words():
    	stopwords = SortedList() 
        for word in reuters.words("stopwords"):
			stopwords.add(word)
        return stopwords

#build the inverted index and saves it to a json file
def rebuild():
	start_time = time.time()
	stopwords = stop_words()
	documents = reuters.fileids()
	data, len_docs = inverted_index(documents[:],stopwords)
	print "done building index..."
	with open('backup.json','w') as fp:
		json.dump((data, len_docs),fp)
	print "index saved in backup.json"
	print("--- %s minutes taken to build index ---" % ((time.time() - start_time)/60))
	return data, len_docs

#loads the inverted index in main memory from the json file
def run():
	with open('backup.json','r') as fp:
		data, len_docs = json.load(fp)
	return data, len_docs	