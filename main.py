from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def inicio():
    return {"mensagem":"Meu primeiro servidor esta no ar!"}
