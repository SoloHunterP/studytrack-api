from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
class MateriaCreate(BaseModel):
    nome: str
    meta_horas: int
materias = [{"id":1,"nome":"Python Backend", "meta_horas": 5},
            {"id": 2, "nome": "Ingles", "meta_horas": 4},
            ]
class SessaoCreate(BaseModel):
    materia_id: int
    horas: float
    observacao: str = ""

sessoes = []
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
@app.put("/materias/{materia_id}")
def atualizar_materia(materia_id:int, dados: MateriaCreate):
    for materia in materias:
        if materia["id"] == materia_id:
            materia["nome"] = dados.nome
            materia["meta_horas"] = dados.meta_horas
            return materia
    raise HTTPException(status_code=404, detail= "materia não encontrada")
@app.delete("/materias/{materia_id}", status_code=204)
def deletar_materia(materia_id: int): 
    for indice, materia in enumerate(materias):
        if materia["id"] == materia_id:
            materias.pop(indice)
            return
    raise HTTPException(status_code=404, detail="materia não encontrada")
    
@app.post("/sessoes", status_code=201, tags=["Sessoes"])
def registrar_sessao(sessao: SessaoCreate):
    materia_existe = False
    for materia in materias:
        if materia["id"] == sessao.materia_id :
            materia_existe = True
            break
    if not materia_existe:
        raise HTTPException(status_code=404, detail="Materia não encontrada.")
    nova_sessao = {
        "id": len(sessoes) + 1,
        "materia_id": sessao.materia_id,
        "horas": sessao.horas,
        "observacao": sessao.observacao,
    }
    sessoes.append(nova_sessao)
    return nova_sessao
@app.get("/sessoes", tags= ["Sessoes"])
def listar_sessoes():
    return sessoes