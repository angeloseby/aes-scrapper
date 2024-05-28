from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "Hello World"


@app.get("/user")
def get_user(username: str, password: str):
    return {
        "username": username.upper(),
        "password": password
    }
