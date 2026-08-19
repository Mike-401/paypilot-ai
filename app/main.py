from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "PayPilot AI is running!"}