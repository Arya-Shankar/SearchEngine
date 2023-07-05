import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_stopwords(text):
    # Download punkt from nltk
    # nltk.download('punkt')
    # Download the stopwords corpus if not already downloaded
    # nltk.download('stopwords')

    # Get the list of stop words
    stop_words = set(stopwords.words('english'))

    # Tokenize the text into words
    words = word_tokenize(text)

    # Filter out the stop words
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Join the filtered words back into a sentence
    filtered_text = ' '.join(filtered_words)

    return filtered_text

