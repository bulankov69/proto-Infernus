import webbrowser
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


class WebItem(BaseModel):
    url: str
    
app = FastAPI()

@app.get("/")
def first_example():
    return {"message": "Hello, FastAPI!"}

@app.post("/tools/open_link")
def open_Web(item: WebItem):
    if not item.url:
        return "URL is required"
    webbrowser.open(item.url)
    return item.url

@app.post("/tools/open_link")
def open_App(AppName):
    print(f"Opening {AppName} application")

@app.post("/tools/open_link")
def change_Volume(Mode, Amount):
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")