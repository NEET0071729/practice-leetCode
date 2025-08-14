# Language Detection using Naive Bayes

# 1. Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 2. Load Dataset
# Example dataset (You can replace this with a larger one like 'Language Detection' from Kaggle)
data = {
    "Text": [
        "Hello, how are you?",  # English
        "Bonjour, comment ça va?",  # French
        "Hola, ¿cómo estás?",  # Spanish
        "Hallo, wie geht es dir?",  # German
        "Ciao, come stai?",  # Italian
        "नमस्ते, आप कैसे हैं?",  # Hindi
        "こんにちは、お元気ですか？",  # Japanese
        "Привет, как дела?",  # Russian
        "안녕하세요, 어떻게 지내세요?",  # Korean
        "Merhaba, nasılsın?"  # Turkish
    ],
    "Language": [
        "English", "French", "Spanish", "German", "Italian",
        "Hindi", "Japanese", "Russian", "Korean", "Turkish"
    ]
}

df = pd.DataFrame(data)

# 3. Split Data
X = df["Text"]
y = df["Language"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Vectorization
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5. Model Training
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 6. Predictions
y_pred = model.predict(X_test_vec)

# 7. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 8. Test on Custom Input
custom_text = ["Buongiorno, come va?", "How's the weather today?", "नमस्कार, आप कहाँ जा रहे हैं?"]
custom_vec = vectorizer.transform(custom_text)
predictions = model.predict(custom_vec)

for text, lang in zip(custom_text, predictions):
    print(f"Text: {text} --> Predicted Language: {lang}")