# -*- coding: utf-8 -*-
"""Disaster_tweet.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T3fEnS8ab3BVw8HhJrXmwtOtaHyJqsbm
"""

import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("/content/disaster_tweets.csv")

df.head()

df.tail()

df.shape

df.info()

df.describe()

df['target'].value_counts()

df.drop(['id'], axis = 1, inplace = True)
df.drop(['keyword'], axis = 1, inplace = True)
df.drop(['location'], axis = 1, inplace = True)

df.head()

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stem_port = PorterStemmer()

import nltk
nltk.download('stopwords')

def stemming(content):
  # Convert content to string to handle non-string values
  content = str(content)
  stemmed_content = re.sub('[^a-zA-Z]',' ',content)
  stemmed_content = stemmed_content.lower()
  stemmed_content = stemmed_content.split()
  stemmed_content = [stem_port.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
  stemmed_content = ' '.join(stemmed_content)
  return stemmed_content

df['text'] = df['text'].apply(stemming)

df['text']

x= df['text'].values
y= df['target'].values

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
vectorizer.fit(x)
x = vectorizer.transform(x)

print(x)

#bar chart

plt.figure(figsize=(10,5))
sns.barplot(x=df['target'].value_counts().index,y=df['target'].value_counts())
plt.show()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred

from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_pred)

df.columns