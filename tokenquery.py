import index_builder as ib
import results as r
from math import log10

def query_token(inv_index,token):
	if token in inv_index.keys():
		return [filename for filename in inv_index[token].keys()]
	else:
		return []

def process_query(tokens_list,inv_index):
	result = []
	for token in tokens_list:
		result+=query_token(inv_index,token)
	return list(set(result))

def score(listDoc, words,inv_index,avg_len,len_docs):
	for word in words:
		for doc in listDoc:
			if word in inv_index.keys() and doc in inv_index[word].keys():
				termFreq = len(inv_index[word][doc])
				docFreq = len(inv_index[word])
				k = 1.60 ## k is parameter, usually [1.2,2.0]
				b = 0.75 ## b is paramtere, usually 0.75
				idfScore = log10(float(len(listDoc)+1)/docFreq)
				totalScore = (idfScore * termFreq * (k+1)) / (termFreq + k*(1 - b + (b*len_docs[doc]/avg_len)))
				listDoc[doc] += totalScore		
			else:
				listDoc[doc] += 0
		
def get_count(onetuple):
      return onetuple[1]

def print_top(dict):
	i=0
	list1=[]
	for value in sorted((dict.items()),key=get_count,reverse= True):
		if i>19:break
		list1.append(value)
        i+=1
	list_tuples=[]
	for item in list1:
		list_tuples.append((item[0],item[1],[]))
	return list_tuples

def run(data, len_docs, tokens_query):
	avg_len=0
	for docID in len_docs.keys():
		avg_len+=len_docs[docID]
	avg_len/=float(len(len_docs))
	relevant_docs=process_query(tokens_query,data)
	score_doc={}
	for doc in relevant_docs:
		score_doc[str(doc)]=0
	score(score_doc,tokens_query,data,avg_len,len_docs)
	result_list=print_top(score_doc)
	return result_list