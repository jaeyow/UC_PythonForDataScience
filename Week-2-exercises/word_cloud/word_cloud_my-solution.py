# exercise 1 - word cloud - count the top 10 most used words contained in input_file
# excluding the words in stopword_file
import collections

# open file resources
input_file=open('98-0.txt', encoding="utf8")
stopword_file=open('stopwords.txt', encoding="utf8")

num_words = 10

# prepare stopwords table
stopwords=set(stopword_file)
stopwords_list = list(val \
    .strip('?; ()-#_.,\"\n\'') \
    .lower() \
    .replace("'", "") \
    .replace("!", "") \
    .replace("-", "") \
    .replace("?", "") \
    for val in stopwords)

# prepare sanitised key
wordcount={}
for key in input_file.read().split():
    sanitised_key = key \
        .strip('?; ()-#_.,\"\n\'') \
        .lower() \
        .replace("'", "") \
        .replace("!", "") \
        .replace("?", "") \
        .replace("-", "")
        
    # conditionally populate dictionary
    if sanitised_key not in stopwords_list:
        if sanitised_key in wordcount:
            wordcount[sanitised_key] = wordcount[sanitised_key] + 1
        else:
            wordcount[sanitised_key] = 1
 
# print summary
print('Top 10 Wordcount: ')
for w in sorted(wordcount, key=wordcount.get, reverse=True)[:num_words]:
    print(w, wordcount[w])
