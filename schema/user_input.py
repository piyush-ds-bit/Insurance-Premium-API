from pydantic import BaseModel, computed_field, Field, field_validator
from typing import List, Dict, Literal, Annotated
from config.cities import tier_1,tier_2

# Pydantic model to validate incoming data
class User_input(BaseModel):
    age: Annotated[int, Field(...,gt=0, lt=120, description="age of the user")]
    weight: Annotated[float, Field(...,gt=0, description="weight of the user")]
    height: Annotated[float, Field(...,gt=0, lt=2.5, description="height of the user")]
    income_lpa: Annotated[float, Field(...,gt=0, description="income_lpa of the user")]
    smoker: Annotated[bool, Field(..., description="is user a smoker")]
    city: Annotated[str, Field(..., description="the city user belongs to")]
    occupation: Annotated[Literal['Civil Servant', 'Startup Founder', 'Nurse', 'Electrician',
    'Data Scientist', 'Cab Driver', 'Farmer', 'Teacher',
    'Software Engineer', 'Architect', 'Artist', 'Doctor',
    'Construction Worker', 'Fitness Trainer', 'Banker', 'Craftsperson',
    'Delivery Executive', 'Journalist', 'Mechanic', 'Shopkeeper'
    ], Field(..., description="occupation of the user")]

    @computed_field
    @property
    def BMI(self) -> float:
        return self.weight/(self.height**2)



    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        else:
            return ("senior")

    @field_validator("city")
    @classmethod
    def normalise_city(cls, v:str) ->str:
        v = v.strip().title()
        return v

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.BMI > 30:
            return "high"
        elif self.smoker or self.BMI > 27:
            return "medium"
        else:
            return "low"


    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1:
            return 1
        elif self.city in tier_2:
            return 2
        else:
            return 3
