from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import User_input
from schema.predicted_output import Predicted_output
from model.predict import predict_output,model,MODEL_Version

app = FastAPI()


@app.get('/')
def home():
    return {"message":"Insurance Premium Predictor API"}

# machine-readable
@app.get("/health")
def health_check():
    return {
        "status":"ok",
        "version":MODEL_Version,
        "model_loaded": model is not None,
    }

@app.post("/predict", response_model=Predicted_output)
def predict_premium(data: User_input):

    user_input = {
        "income_lpa": data.income_lpa,
        "occupation": data.occupation,
        "BMI": data.BMI,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,

    }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={"Predicted_Category": prediction})

    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
