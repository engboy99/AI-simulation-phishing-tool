import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load phishing dataset (assumed CSV file with 'text' & 'label' columns)
df = pd.read_csv("phishing_dataset.csv")

# Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = MultinomialNB()
model.fit(X, y)

# Save model
with open("phishing_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

def analyze_email(email_text):
    """Predict if the email is phishing or not"""
    with open("phishing_model.pkl", "rb") as f:
        vectorizer, model = pickle.load(f)

    email_vectorized = vectorizer.transform([email_text])
    prediction = model.predict(email_vectorized)

    return "Phishing" if prediction == 1 else "Legitimate"
