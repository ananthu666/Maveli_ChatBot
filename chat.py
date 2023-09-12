import spacy
from collections import Counter
from modifier import preprocess_sentences
import csv
from ai_support import maveli


nlp = spacy.load("en_core_web_sm")


def analyze_message(message):
    message_prev = message
    csv_file='onam.csv'
    conversation = []
    with open(csv_file, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            conversation.append({'Question': row['Question'], 'Answer': row['Answer']})

    message = message.lower()
    message = preprocess_sentences(message)
    doc = nlp(message)
    word_counts = Counter(token.text for token in doc if token.is_alpha)

    best_match = None
    best_probability = 0.0
  
    user_words = set(token.text for token in doc if token.is_alpha)
    ranger=len(doc)
    best_match = None
    best_row = None
    best_word_count = 0
        
    for entry in conversation:
        key_lower = entry['Question'].lower()
        key_lower = preprocess_sentences(key_lower)
        
        key_words = set(key_lower.split())
        
        common_words = user_words.intersection(key_words)
        
        if len(common_words) > best_word_count:
            best_match = entry['Question']
            best_row = entry
            best_word_count = len(common_words)

# # ***********************************************************************************
    
    if best_match and (best_word_count/ranger)>=0.75:
        return best_row['Answer']
    else:
        msg=maveli(message_prev)
        new_row = {'Question': message_prev, 'Answer': msg}
        with open(csv_file, 'a', newline='') as csvfile:
            fieldnames = ['Question', 'Answer']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(new_row)
            return msg
    

def chater(user_text):
        user_input = user_text
        response = analyze_message(user_input)
        return response

