"""
botNLP Module

Create decision tree and attempts to find function

Functions:
    1. parse_message(message): Attempts to use NLP to parse the message

Authors: Michael Vlatko
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
import re

#Import the dataset
train_data = pd.read_csv(r"train.csv")

#remove stop words and lowercase the set
tfidf_vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)

#partition the set into training and test data
X = tfidf_vectorizer.fit_transform(train_data['message'])
y = train_data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Create the tree
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

def parse_message(message):
    """
    Attempts to use NLP to parse the message

    Parameters:
        message (string): The message to parse

    Returns:
        (string, string)|(None, None): The function and parameter, or None

    """

    #Remove the guids and split the message into function_call and params
    guid_pattern = r'[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}'
    minusguids = re.sub(guid_pattern, '', message)
    function_call = minusguids.strip()
    params = re.findall(guid_pattern, message)

    # Extract parameters if there are any
    if len(params) == 0:
        params_str = None
        params = None
    else:
        params = list(set(params))
        params_str = ', '.join(params)
    
    # Vectorize the message and predict using the trained classifier
    message_vec = tfidf_vectorizer.transform([function_call])
    # Take first element
    predicted_fun = clf.predict(message_vec)[0]

    return (str(predicted_fun), params_str)