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

            # FILTERING THE DATA IN JSON FILES
            for i in tokenized_text:
                if i not in stop_words:
                    if i.isalpha():
                        if i not in unwords:
                            stems.append(stemmer.stem(i))

    # stems.sort()
    stems = list(dict.fromkeys(stems))

    for i in stems:
        if i in mydict2:
            mydict2[i].append(documentID[filecounter - 1])
        else:
            mydict2.update({i: [documentID[filecounter - 1]]})

    #  UPDATING THE DICTIONARY
    # mydict.update({documentID[filecounter-1] : stems})
    file.close()

# WRITING THE DICTIONARY TO THE JSON FILE
# with open("sample.json", "w") as outfile:
#     json.dump(mydict, outfile)

# # for i in mydict:
# #      for j in mydict[i]:
# #           get_key(j)
# print(mydict2)
# # keys = set(tuple(element) for element in keys)
# # keys = [list(t) for t in set(tuple(element) for element in keys)]

with open("sample2.json", "w") as outfile:
    json.dump(mydict2, outfile)

# with open("sample.json", "w") as outfile:
#     json.dump(, outfile)
