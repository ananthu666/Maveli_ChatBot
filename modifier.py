import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


# nltk.download('stopwords')
# nltk.download('punkt')

stemmer = SnowballStemmer('english')

# buzzwords = ['you', 'why', 'what', 'during', 'a', 'to', 'and', 'the', 'of','how']
buzzwords  = ['you', 'during', 'a', 'to', 'and', 'the', 'of', 'in', 'on', 'with', 'as', 'at', 'for', 'an', 'it', 'by', 'that', 'this', 'from', 'but', 'not', 'we', 'can', 'your', 'will', 'has']

def preprocess_sentences(sentences):
        words = nltk.word_tokenize(sentences.lower())
        
        words = [stemmer.stem(word) for word in words if word not in stopwords.words('english') and word not in buzzwords]
        
        

        preprocessed_sentence = ' '.join(words)
        
        
        if(preprocessed_sentence==""):
            
            return sentences
        else:
            return preprocessed_sentence

