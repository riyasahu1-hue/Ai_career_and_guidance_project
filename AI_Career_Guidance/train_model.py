# train_model.py

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("Loading dataset...")

# Required columns from dataset
columns = [
    'Profession',
    'Industry',
    'Required_Skills',
    'Preferred_Education',
    'Experience_Level'
]

# Load dataset
df = pd.read_csv(
    'ai_career_guidance_dataset.csv',
    usecols=columns,
    low_memory=False
)

# Reduce dataset size for faster training
df = df.sample(30000, random_state=42)

print("Dataset Loaded Successfully")

# Fill missing values
df.fillna('', inplace=True)

# Combine columns into single text feature
X = (
    df['Required_Skills'].astype(str) + ' ' +
    df['Preferred_Education'].astype(str) + ' ' +
    df['Industry'].astype(str) + ' ' +
    df['Experience_Level'].astype(str)
)

# Target column
y = df['Profession']

print("Splitting dataset...")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training model...")

# Machine Learning Pipeline
model = Pipeline([
    (
        'tfidf',
        TfidfVectorizer(
            stop_words='english',
            max_features=3000
        )
    ),
    (
        'classifier',
        LogisticRegression(max_iter=1000)
    )
])

# Train model
model.fit(X_train, y_train)

print("Model Training Completed")

# Accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, 'model.pkl')

print("Model Saved Successfully")