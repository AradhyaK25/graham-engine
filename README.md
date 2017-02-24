#GRAHAM SEARCH ENGINE
An implementation of a text-based search engine based on the Vector Space Model using Python. We have used the publically available Reuters-21578 "ApteMod" corpus for text categorization.

code available online at: https://github.com/aadijain/graham-engine

##Features
1. Phrase Queries and Proximity Queries
2. Retrieved documents ranked according to relevance
3. File preview of all the retrieved documents
4. Option to open returned documents in a new window
5. Category classification of the retrieved documents.
6. Reduces the vocabulary size and the retrieval time by eliminating common words (stop words)
7. Searches for similar forms of words
8. Spelling correction in queries

##Prerequisites
1. software required:
	- python2.7
	- gedit

2. python2.7 libraries required:
	- nltk
	- textblob
	- math
	- re
	- json
	- time
	- sortedcontainers
	- os

##Assumptions
- This program must be run on a linux system
- The user enters a valid option when prompted
- The program was tested on a ubuntu 16.04LTS system with 4GB of ram
- The corpus provided contains a "cats.txt" file which maps file names to specified categories

##Getting Started
1. Ensure all required software and libraries are installed 
2. Run 'python driver.py' in a terminal to start the program
3. The program will prompt for input as and when required
4. Choose the option to rebuild corpus in case any changes are made to the corpus or during the first run of the program (Note: this may take upto 30mins depending on the system specs and corpus size) 
5. Entering the query:
	-queries not enclosed in quotes are treated as list of tokens and are searched using vector space model
	-if the query is enclosed in quotes it will be treated as a phrase query and the entire phrase is searched as a unit
	-the "*" wildcard can be used to in phrase queries to match any(one) token to include proximity
6. Any Result files can be opened in Write mode

##Modifying Corpus
1. Any of the following files can be specified
	- A list of common words which don't add any value are present in corpora/reuters/stopwords
	- Category information for each file is present in corpora/reuters/cats.txt
	- The database files are present in corpora/reuters/test and corpora/reuters/training
2. Rebuild the index if any changed are made
NOTE: modifying the corpus is not recommended

##Authors
1. Aadi       Jain 			(2015A7PS104P)
2. Aayushmaan Jain 			(2015A7PS043P)
3. Aradhya    Khandelwal 	(2015A7PS036P)
4. Samip      Jasani 		(2015A7PS127P)
5. Tanvi      Aggarwal 		(2015A7PS140P)