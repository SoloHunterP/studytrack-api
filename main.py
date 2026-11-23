from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
class MateriaCreate(BaseModel):
    nome: str
    meta_horas: int
materias = [{"id":1,"nome":"Python Backend", "meta_horas": 5},
            {"id": 2, "nome": "Ingles", "meta_horas": 4},
            ]
@app.get("/")
def inicio():
    return {"mensagem":"Meu primeiro servidor esta no ar!"}
@app.get("/materias")
def listar_materias():
    return materias
@app.get("/materias/{materia_id}")
def buscar_materia(materia_id:int):
    for materia in materias:
        if materia["id"] == materia_id:
            return materia
        raise HTTPException(status_code=404, detail="materia não encontrada")
@app.post("/materias", status_code=201)
def criar_materia(materia: MateriaCreate):
    novo_id = len(materias)+1
    nova_materia ={
        "id": novo_id,
        "nome":materia.nome,
        "meta_horas": materia.meta_horas,
    } 
    materias.append(nova_materia)
    return nova_materia