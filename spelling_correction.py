from textblob import Word

  
def onlyspellcorrection(query_tokens):
    "Corrects the spelling errors in the query"
    corrected_query = []
    for t in query_tokens:
        w = Word(t)
        a = w.correct()
        corrected_query.append(a)
    if cmp(corrected_query,query_tokens)==0:
        return query_tokens
    else:
        s = ""
        for i in corrected_query:
            s += i
            s += " "
        print "Did you mean: " + s + "?"

def spellcorrection(query_tokens):
    "Corrects the spelling errors in the query"
    corrected_query = []
    for t in query_tokens:
        w = Word(t)
        a = w.correct()
        corrected_query.append(a)
    if cmp(corrected_query,query_tokens)==0:
        return query_tokens
    else:
        s = ""
        for i in corrected_query:
            s += i
            s += " "
        print "Did you mean: " + s + "?"
        choice = int(raw_input("Press 1 to continue with the original query, otherwise Press 0\n"))
        if choice==0:
            return corrected_query
        else:
            return query_tokens
