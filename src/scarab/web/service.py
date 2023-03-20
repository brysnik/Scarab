"""Implementation of the Scarab web service."""
from fastapi import FastAPI


def create_app():
    app = FastAPI()
    return app


def init_app(app):

    @app.get("/")
    async def root():
        return {"message": "Hello World"}
