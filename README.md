# Maveli Chat Bot


<img src="https://github.com/ananthu666/Maveli_ChatBot/blob/main/Screenshot/mav_chat.png"/>

# [Link To Video](https://www.youtube.com/watch?v=jl1FaTkBfA8)

# [Chat with Bot](./)

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites And Installation](#prerequisites-and-installation)
- [Working](#working)
- [How to Run](#how-to-run)

## Features


- **Natural Language Understanding (NLU):** The chatbot can understand and process user input in natural language, making interactions more conversational.

- **User Intent Recognition:** It can recognize the intent behind user messages to determine what the user wants or needs.

- **Scalability:** The chatbot can handle a large number of concurrent users and interactions.

- **Emotion Recognition:** It can detect user emotions and respond empathetically when appropriate.

- **User Education:** The chatbot can educate users about its capabilities and how to interact effectively.

## Getting Started

``` Clone The Repo Maveli_ChatBot```

### Prerequisites And Installation

```
streamlit==1.22.0 
openai==0.28.0
requests==2.31.0
nltk==3.8.1  
spacy==3.6.1 
streamlit-chat==0.1.1
json5==0.9.11
python-dotenv
en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.6.0/en_core_web_sm-3.6.0-py3-none-any.whl#sha256=83276fc78a70045627144786b52e1f2728ad5e29e5e43916ec37ea9c26a11212
```
```bash
pip install -r requirements.txt
```

## Working
Maveli Chat Bot is a versatile conversational agent that seamlessly blends two core functionalities. It starts by searching a backend CSV file to identify and deliver responses to user queries, measuring the similarity between the input and pre-existing questions. If the user's query closely matches any stored questions, Maveli Chat Bot retrieves the corresponding response from the CSV file. However, what sets it apart is its capacity to adapt and learn. If a user's query doesn't closely align with existing questions, the chatbot gracefully switches to leveraging OpenAI's text generation capabilities to provide relevant and context-aware responses. Moreover, Maveli Chat Bot actively updates its knowledge base by appending new questions and responses to the CSV file based on interactions, allowing it to continually improve its effectiveness and respond effectively to a growing array of queries. This dynamic approach ensures that users receive informative and engaging answers, whether they're seeking information readily available in the CSV file


## How to run
```bash
$ streamlit run Maveli_chat_bot.py
```


