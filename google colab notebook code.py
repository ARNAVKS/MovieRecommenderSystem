#this code is just a back story how this 'similarity.pkl' file is made

#importing the required libraries

import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#loading the table data
df=pd.read_csv('movies_2.csv')

#making all the content in tags column in lowercase
df.tags=df.tags.apply(lambda x:x.lower())

#now using CountVectorizer() function

tfidf=TfidfVectorizer(stop_words='english')
vectors=tfidf.fit_transform(df.tags).toarray()
ps=PorterStemmer()

def stem(text):
  y=[]
  for i in text.split():
    y.append(ps.stem(i))
  return " ".join(y)

#applying stem function in all the values in the 'tags' column
df.tags=df.tags.apply(stem)

#now using cosine_similarity() to find the similarity of all data with each other
sim=cosine_similarity(vectors)
pickle.dump(sim,open('similarity.pkl','wb'))
