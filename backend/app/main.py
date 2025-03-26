from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.routes import tenants, users, projects, me

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)