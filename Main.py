# IMPORTING THE REQUIRED LIBRARIES
import nltk
import json
from os import listdir
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from os.path import isfile, join


# DEFINING THE FUNCTION TO GET THE KEY OF THE DICTIONARY
def get_key(val):
    for key, value in mydict.items():
        for i in value:
            if i == val:
                keys.append(key)


# DEFINING THE PATH TO THE JSON FILES
path = r"E:\Elementry Search Engine\Backend\Dataset\nela-gt-2021\newsdata"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# DOWNLOADING THE NLTK LIBRARIES
nltk.download('stopwords')
stemmer = PorterStemmer()

# DEFINING THE VARIABLES
articleCounter = 0
filecounter = 0
mydict = {}
mydict2 = {}
docID = 0
keys = []
documentID = []
unwords = [',', ';', '“', '”']
# APPENDING THE UNECESSARY WORDS TO BE REMOVED FROM THE ARTICLES
for i in range(33, 65):
    unwords.append(chr(i))
for i in range(123, 128):
    unwords.append(chr(i))

for i in range(91, 97):
    unwords.append(chr(i))

# PARSING THE JSON FILES
for file in onlyfiles:
    with open(r"E:\Elementry Search Engine\Backend\Dataset\nela-gt-2021\newsdata\\" + file, "r") as file:
        data = json.load(file)

    print(file)
    filecounter += 1
    stems = []

    # DEFINING THE LIMIT OF THE NUMBER OF ARTICLES TO BE PARSED
    if articleCounter >= 100000:
        break
    else:
        docID += 1
        documentID.append("documentID" + str(docID))
        for dict in data:
            articleCounter += 1
            tokenized_text = word_tokenize(dict['content'])

            stop_words = set(stopwords.words("english"))
