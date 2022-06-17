from fastapi import FastAPI

app =  FastAPI()

vendas =

@app.get("/")
def home():
    return "Minha API está no ar"