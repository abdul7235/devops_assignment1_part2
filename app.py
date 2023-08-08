from fastapi import FastAPI
from models.person_model import PersonModel

app = FastAPI()


@app.get('/api/greeting/')
async def get_greeting(name: str, specie: str):
    PersonModel.name = name
    PersonModel.specie = specie

    if PersonModel.specie.lower() == 'human':
        return {"greeting": f"Hello {PersonModel.name}"}
    else:
        return {"greeting": f"Hello Animal"}