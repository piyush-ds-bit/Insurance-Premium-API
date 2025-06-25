from pydantic import BaseModel,Field
from typing import Dict

class Predicted_output(BaseModel):
    predicted_category: str = Field(...,description="Premium category",example="medium")
    confidence: float = Field(..., description="Model's Confidence score for the predicted class range: (0 to 1)", example="0.99")
    class_probabilities: Dict[str , float] = Field(...,description="Class probabilities for each category",example={"low":0.07,"medium":0.03,"high":0.99})
