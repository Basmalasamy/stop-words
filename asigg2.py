

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt')

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

file_path =( r"D:\\cloud computing\\paragraphs.txt")  
text = read_text_file(file_path)
if text:
    print("File contents:")
    print(text)



    

def remove_stopwords(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Load English stopwords
    stop_words = set(stopwords.words("english"))
    
    # Remove stopwords and convert words to lowercase
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    
    # Join the filtered words back into a single string
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text



# Remove stopwords from the text
text_without_stopwords = remove_stopwords(text)

print("Text without stopwords:")
print(text_without_stopwords)



from collections import Counter

def count_word_frequency(text):
    # Tokenize the text into words
    words = text.split()
    
    # Count the frequency of each word
    word_freq = Counter(words)
    
    return word_freq



# Count word frequency
word_freq = count_word_frequency(text_without_stopwords)

# Display word frequency count
print("Word frequency count:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

