import index_builder as ib
import spelling_correction as sc
import re
import phrasequery as pq
import results as res
import tokenquery as tq

def main():
    make=int(raw_input("Enter \n 1: if you want to make a new dict \n 2: if you want to load existing dict \n >> "))
    if make==1:
        data,len_docs=ib.rebuild()
    else:
        data,len_docs=ib.run()
    do=4
    while True:
        if do==4:
            query=str(raw_input("Enter Query \n >> "))
            if query is None or len(query) == 0: continue
            if query[0]=="'" or query[0]=='"':
                queryflag=1 #phrasequery
            else:queryflag=2#tokenquery
        do=int(raw_input("Enter \n 1: result of tokenization and normalization \n 2: spell check only\n 3: search the query in the database\n 4: Enter new Query\n 5: Exit \n >> "))
        if do==1:
            tokens,_=ib.tokenize(query,ib.stop_words())
            print tokens
        if do==2:
            words=filter(None, re.split("[, \-!?:\'\"]+",query))
            newwords=sc.onlyspellcorrection(words)
            if(newwords == words): print "Your spelling is correct"
            # print words
        if do==3:
            if queryflag==1:
                words=filter(None, re.split("[, \-!?:\'\"]+",query))
                words=sc.spellcorrection(words)
                if words is None or words == []:
                    print "no results found (trivial)"
                    do=4 
                    continue
                result=pq.phrasequery(" ".join(words),data)
                if result ==-1:
                    result=[]
                res.print_results(result[:20])
                
            else:
                words=filter(None, re.split("[, \-!?:\'\"]+",query))
                words=sc.spellcorrection(words)
                if words is None or words == []:
                    print "no results found (trivial)"
                    do=4 
                    continue
                tokens,_= ib.tokenize(" ".join(words),ib.stop_words())
                result=tq.run(data,len_docs,tokens)
                res.print_results(result[:20])
            while True:
                if len(result)==0: break
                disp=int(raw_input("Enter\n No.: if you want to open document \n 0: if you want to skip\n >> "))
                if disp==0:break
                res.fileopen(result,disp)
        if do==4:
            continue
        if do==5:
            break
    return

if __name__ == "__main__":
    main()