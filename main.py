from fastapi import FastAPI
from src.forms.router import router_forms

app = FastAPI()

app.include_router(router_forms)



