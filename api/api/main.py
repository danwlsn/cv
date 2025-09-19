from fastapi import FastAPI

from api.routes import ROUTER as APIROUTES


app = FastAPI()

app.include_router(APIROUTES)
