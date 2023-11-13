import sys
import argparse
from nltk.tag.stanford import StanfordPOSTagger, StanfordNERTagger
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tree import *
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.parse.corenlp import GenericCoreNLPParser
import nltk
import os

inputString = " "
java_path = "C:\\Program Files\\Java\\jdk-9.0.4\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path
for each in range(1,len(sys.argv)):
    inputString += sys.argv[each]
inputString += " "
# inputString = raw_input("Enter the String to convert to ISL: ")
parser=GenericCoreNLPParser(url='http://localhost:9000')
# o=parser.parse(s.split())
englishtree=[tree for tree in parser.parse(inputString.split())]
parsetree=englishtree[0]
dict={}
# "***********subtrees**********"
parenttree= ParentedTree.convert(parsetree)
for sub in parenttree.subtrees():
    dict[sub.treeposition()]=0

#"----------------------------------------------"
isltree=Tree('ROOT',[])
i=0
for sub in parenttree.subtrees():
    if(sub.label()=="NP" and dict[sub.treeposition()]==0 and dict[sub.parent().treeposition()]==0):
        dict[sub.treeposition()]=1
        isltree.insert(i,sub)
        i=i+1
if(sub.label()=="VP" or sub.label()=="PRP"):
    for sub2 in sub.subtrees():
        if((sub2.label()=="NP" or sub2.label()=='PRP')and dict[sub2.treeposition()]==0 and
dict[sub2.parent().treeposition()]==0):
            dict[sub2.treeposition()]=1
            isltree.insert(i,sub2)
            i=i+1

for sub in parenttree.subtrees():
    for sub2 in sub.subtrees():
        # print sub2
        # print len(sub2.leaves())
        # print dict[sub2.treeposition()]
        if(len(sub2.leaves())==1 and dict[sub2.treeposition()]==0 and
dict[sub2.parent().treeposition()]==0):
            dict[sub2.treeposition()]=1
            isltree.insert(i,sub2)
            i=i+1


parsed_sent=isltree.leaves()
words=parsed_sent
stop_words=set(stopwords.words("english"))
# print stop_words
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
lemmatized_words=[]
for w in parsed_sent:
# w = ps.stem(w)
    lemmatized_words.append(lemmatizer.lemmatize(w))
    
islsentence = ""
print(lemmatized_words)
for w in lemmatized_words:
    if w not in stop_words:
        islsentence+=w
islsentence+=" "
print(islsentence)