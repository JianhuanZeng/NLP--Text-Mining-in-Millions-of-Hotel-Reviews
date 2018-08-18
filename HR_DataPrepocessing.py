import pandas as pd
import os
import re
import json
###from pandas import Series, DataFrame




################################### data reading ##############################

# read data
dt = pd.read_csv(os.path.join("/Users/cengjianhuan/Documents/Fall2017/BigDataAnalysics/Project/RawData", 'HotelsReviews.csv'), header=None)
### del dt['Unnamed: 9']

# R0 is raw data
###R0=R.copy()

# other read
texts=[]
with open('/Users/cengjianhuan/Documents/Fall2017/BigDataAnalysics/Project/RawData/Reviews0.csv', 'r') as file:
    for txt in file:
        texts.append(txt)
####################### make a unique id for each hotel ########################
Hotels=dt[3]
Hotels=set(Hotels)
Hotels=list(Hotels)
H_ids={} # hotel ids

# dictionary to record the id for each hotel
for i in range(len(Hotels)):
    H_ids[i]=Hotels[i]

#### output dictionary
###with open('hotels_ids.txt','w') as data:
###    data.write(str(H_ids))

# output dictionary
import json
with open('hotels_ids.txt', 'w') as file:
     file.write(json.dumps(H_ids))

####################### find the most frequent words ###########################
# hotels reviews
###for i in range(8):
###    del R[i]# a bag of reviews is current R
texts=str(R)

# remove non-letters
txt = re.sub("[^a-zA-Z]"," ",texts)
# convert to lower case
words = txt.lower().split()
# remove stop words
stop_wds=set(stopwords.words("english"))
stop_wds.add('nan')
words = [w for w in words if not w in stop_wds]

# count words:
count={}
for w in words:
    if w in count.keys():
        count[w]+=1
    else:
        count[w]=1

# the most frequent words
thrd=len(count.keys())/50  # the withhold
fre={}
for w in count.keys():
    if count[w]>thrd:
        #count.pop(w, None)
        fre[w]=count[w]/len(words)

########################### clean review ######################################
import re
from nltk.corpus import stopwords
# different funcs
from nltk.corpus import stopwords

def text2wordlist( text):
    # remove non-letters
    txt=re.sub("[^a-zA-Z]"," ",text)
    # convert to lower case
    words=txt.lower().split()
    # remove stop words
    stop_wds=set(stopwords.words("english"))
    stop_wds.add('nan')
    words = [w for w in words if not w in stop_wds]
    return words
#// download engilish stop words for nltk library
#// download the punkt tokenizer for sentence splitting
import nltk.data
nltk.download()

############################## tokenizer ######################################
import nltk.data
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')

def text2sentences( text, tokenizer):
    # the NLTK tokenizer to split the paragraph into sentences
    raw_sentences = tokenizer.tokenize(text.strip())
    sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            sentences.append( text2wordlist( raw_sentence))
    return sentences
hotel=dt['Hotel Name'][1]
HotelID=[hotel]
words_i=[]

############################## text analysis ######################################
for i in range(len(texts)):
    if dt['Hotel Name'][i]==hotel:
        words_i.append(text2sentences(texts[i],tokenizer))
    else:
        print('now for hotel: '+str(hotel))
        HotelID.append(dt['Hotel Name'][i])
        hotel=dt['Hotel Name'][i]

############################## save ######################################
with open('hotels_ids.txt', 'w') as file:
     file.write(str(HotelID))
with open('hotels_review.txt', 'w') as file:
     file.write(str(words_i))
