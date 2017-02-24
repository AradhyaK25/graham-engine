import index_builder as ib;
import os

#prints results on screeen
def print_results(result):
	cat = {}
	for line in open('corpora/reuters/cats.txt','r'):
		fst, _, lst = line.partition(' ')
		cat[fst] = lst[:-1]
	print("Number of results: %d\n" % (len(result)))
	for index, (file, score, _) in enumerate(result):
		print("RANK %d" % (index+1))
		print("FileName:\t%s" % file)
		print("Score:\t\t%s" % score)
		print("Category(s):\t%s" % cat[file])	
		print("File Preview:")	
		f = open("corpora/reuters/"+file,'r')		
		f.seek(0)
		print("%s..." % f.read(200))
		print

#opens specified file in gedit
def fileopen(results, index):
    if index <=0 or index>min(len(results),20): return	
    os.system("gedit corpora/reuters/" + results[index-1][0])
    return