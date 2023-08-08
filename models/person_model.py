from pydantic import BaseModel

class PersonModel(BaseModel):
    name: str
    specie: str