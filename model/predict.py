import pickle
import pandas as pd

with open("model/model3.pkl", "rb") as f:
    model = pickle.load(f)

MODEL_Version = "1.0.0"

class_labels = model.classes_.tolist()

def predict_output(user_input: dict):

    input_df = pd.DataFrame([user_input])
    output = model.predict(input_df)[0]
    probabilities =  model.predict_proba(input_df)[0]
    confidence = max(probabilities)
    class_prob = dict(zip(class_labels,map(lambda p: round(p,4),probabilities)))
    return {
        "predicted_category":output,
        "confidence":round(confidence,4),
        "class_probabilities":class_prob
    }
