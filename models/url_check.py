import pickle
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(current_directory, "model.pkl")
with open(model_path, 'rb') as file:
    your_model = pickle.load(file)

new_data = ['http://adzbux.com']


# Assuming you have a new data point for prediction stored in a variable 'new_data'
prediction = your_model.predict(new_data)
