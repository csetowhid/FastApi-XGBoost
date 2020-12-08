from pydantic import BaseModel

class Corona(BaseModel):
	age: int
	temperature: float
	pulse: float
	rr: float
	rhonchi: int
	wheezes: int
	cough: int
	fever: int
	loss_of_smell: int
	loss_of_taste: int