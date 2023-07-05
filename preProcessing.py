import os
import re
from stopWords import remove_stopwords

Data_folder = "LC_scrapping/Data"

pattern = "Example 1:"

all_lines = []

for i in range (1,2131):
    file_path = os.path.join(Data_folder,"{}/{}.txt".format(i,i))

    doc = ""
    with open(file_path, "r",encoding = 'utf-8', errors = "ignore") as file:
        lines = file.readlines()

    for line in lines:
        if pattern in line:
            break
        else :
            doc += line
    
    all_lines.append(doc)

def preprocess(text):
    text=re.sub(r'[^a-zA-Z0-9\s-]','',text)
    text = remove_stopwords(text)
    # print(text)
    words = [word.lower() for word in text.strip().split()]
    return words

vocab = {}
docs = []

for (index,line) in enumerate(all_lines):
    tokens = preprocess(line)
    # break
    docs.append(tokens)

    tokens = set(tokens)

    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else :
            vocab[token] += 1

vocab = dict( sorted(vocab.items(), key = lambda item: item[1], reverse = True))

# print("No of documents : ", len(docs))
# print("Size of vocab : ", len(vocab))
# print("Example document: ", docs[100])

# keys of vocab thus is a set of distinct words across all docs
# save them in file vocab

with open("vocab.txt", "w", encoding = 'utf-8', errors = "ignore") as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

# save idf values
with open("idf_values.txt", "w", encoding = 'utf-8', errors = "ignore") as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])


#save the documents(lists of words for each doc)
with open("document.txt", "w", encoding = 'utf-8', errors = "ignore") as f:
    for doc in docs:
        f.write("%s\n" % doc)


inverted_index = {}         # word : list of index of docs the word is present in.
                    # inserting word multiple times from same doc too, so that we even get the term freq from here itself
for (index, doc) in enumerate(docs, start = 1):
    for token in doc:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)


# save the inverted index in a file
with open("inverted_index.txt", 'w', encoding = 'utf-8', errors = "ignore") as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        
        doc_indexes = ' '.join([str(term) for term in inverted_index[key]])
        f.write("%s\n" % doc_indexes)


