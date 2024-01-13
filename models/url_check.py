import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained MultiOutputClassifier model
with open('model_1.pkl', 'rb') as file:
    rf_model = pickle.load(file)

# Load the TfidfVectorizer used during training
with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Input data for prediction
new_url = ['questar.net/comm_dorsey.html']

# Transform the new URL using the loaded vectorizer
new_url_transformed = vectorizer.transform(new_url)
# legit webistes url
# questar.net/comm_dorsey.html,
# donsworld.com/Michele_Scarabelli.html,
# facebook.com/pages/Jon-Niese/107385165950598,


# suspicious website
# lnterac-refund.com
# laserstrength.com


# Ensure the number of features in the input data matches the trained model
if new_url_transformed.shape[1] != rf_model.estimators_[0].n_features_in_:
    print(f"Number of features in the input data ({new_url_transformed.shape[1]}) does not match the model's expectations ({rf_model.estimators_[0].n_features_in_}).")

# Make predictions using the loaded model
new_url_prediction = rf_model.predict(new_url_transformed)

# Check if the prediction matches either of the specified patterns
if any((new_url_prediction == pattern).all() for pattern in [[1, 0, 0, 0], [0, 1, 0, 0]]):
    print("Prediction: Legit")
else:
    print("Prediction: Suspicious")
