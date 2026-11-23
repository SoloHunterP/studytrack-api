from fastapi import FastAPI
app = FastAPI()
materias = [{"id":1,"nome":"Python Backend", "meta_horas": 5},
            {"id": 2, "nome": "Ingles", "meta_horas": 4},
            ]
@app.get("/")
def inicio():
    return {"mensagem":"Meu primeiro servidor esta no ar!"}
@app.get("/materias")
def çistar_materias():
    return materias