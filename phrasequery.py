import sys
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer 
from nltk.corpus import reuters
import json

StopWords=reuters.words("stopwords")

def search(token,data):
    if token in data:return data[token]
    else:
        print "No such phrase found"
        return -1

#converts phrase into token plus positionid(posid)
# "Phrase"=[(token,posid),...]    
def tokenisenstem(phrase):
    words=filter(None, re.split("[, \-!?:\'\"]+",phrase))
    count=0
    wordplace=[]
    for word in words:
        if word=='*':
            count+=1
        else:
            wordplace.append((word,count))
            count+=1
    if len(wordplace)==0:return -1
    wordcount=[]
    for word in wordplace   :
        if word[0] in StopWords:
           # wordplace.remove(word)
        else:
            wordcount.append(word)
    tokenise=lambda token: PorterStemmer().stem(token)
    tokenplace=[]
    for word in wordcount:
        token=(str(tokenise(word[0])),word[1])
        tokenplace.append(token)
    return tokenplace

#returns list of dict with [key=docid:value=list of position index]
#input is list of [(token,posid)]
def getdoclist(tokenplace,data):
    doclist=[]
    for token in tokenplace:
        docs=search(token[0],data)
        if docs == -1:return -1
        doclist.append(docs)
    return doclist

#finds intersect of docids in form of list for list of dict with [key=docid:value=list of position index]
def findintersect(doclist):
    setdoclist=map(lambda x:set(x.keys()),doclist)
    intersectdocids=reduce(lambda x,y: x&y,setdoclist)
    intersectdocids=list(intersectdocids)
    return intersectdocids

#input specific docid, entire doclist and tokenplace list of tuples
def countin(docid,data,tokenplace):
    relativeposindex={}
    for token in tokenplace:
        relativeposindex[token[0]]=map(lambda x:x-token[1],data[token[0]][docid])
    setpoindex={}
    setpoindex=map(lambda x:set(x),relativeposindex.values())
    posindexlist=reduce(lambda x,y:x&y,setpoindex)
    posindexlist=list(posindexlist)
    count = len(posindexlist)
    if count==0:return docid,0,0
    pos=posindexlist[0] 
    return str(docid),count,pos

def mycount(tuple):
    return tuple[1]

def phrasequery(phrase,data):
    tokenplace=tokenisenstem(phrase)
    if tokenplace==-1: return -1
    doclist=getdoclist(tokenplace,data)
    if doclist == -1: return -1
    intersectdocids=findintersect(doclist)
    score=[]
    for docid in intersectdocids:
        score.append(countin(docid,data,tokenplace))
    topscore=sorted(score,key=mycount,reverse=True)
    topscore=list(filter(mycount,topscore))
    return topscore 
