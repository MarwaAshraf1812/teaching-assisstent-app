from fastapi import FASTAPI
app= FASTAPI()

@app.get("/welcome")
def welcome():
    return {"message": "Welcome to the teaching assistant app!"}