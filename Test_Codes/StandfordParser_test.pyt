import os
from nltk.parse.stanford import StanfordParser
os.environ['STANDARD_PARSER']='D:\\stanford-parser-full-2018-02-27'
os.environ['STANDARD_MODELS']='D:\\stanford-parser-full-2018-02-27'
os.environ['CLASSPATH']='D:\\stanford-parser-full-2018-02-27'
parser = StanfordParser(model_path='D:\\stanford-parser-full-2018-02-27\\edu\\stanford\\nlp\\models\\lexparser\\englishPCFG.ser.gz')

sentences = parser.raw_parse_sents(("Hello, My name is Melroy.","What is your name?"))

print(sentences)

for line in sentences:
    for sentence in line:
        sentence.draw()
        
