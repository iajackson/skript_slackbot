import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def basic_interpret(message):

    #Tokenize the text
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(message)

    #Create a frequency table
    freqTable = dict()

    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
       
    return (freqTable)