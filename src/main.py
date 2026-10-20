from fastapi import FastAPI, HTTPException, status
from pymongo.errors import PyMongoError

from src.templates.controlles import (
    create_trainee,
    get_all_trainees,
    get_trainee_by_id,
    update_trainee,
    delete_trainee,
)
from models.models import TraineeModel, TraineeUpdateModel

# Ejecutar desde la carpeta tll_fastapi:
# uvicorn src.main:app --reload
app = FastAPI(
    title="Gestion de datos de aprendices",
    description="Api simple para la gestion de datos de aprendices",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {"mensaje": "Hello World"}


# Registrar aprendices
@app.post(
    "/Trainees/",
    response_description="registrar un aprendiz",
    status_code=status.HTTP_201_CREATED,
)
def create_trainee_api(trainee: TraineeModel):
    try:
        return create_trainee(trainee)
    except PyMongoError as exc:
        raise HTTPException(status_code=503, detail="No se pudo acceder a MongoDB") from exc


# Obtener lista de aprendices
@app.get(
    "/Trainees/",
    response_description="listar todos los aprendices",
)
def get_all_trainee_api():
    try:
        return get_all_trainees()
    except PyMongoError as exc:
        raise HTTPException(status_code=503, detail="No se pudo acceder a MongoDB") from exc


# Obtener aprendiz por su ID
@app.get(
    "/Trainees/{id}",
    response_description="obtener aprendiz por su ID",
)
def get_trainee_by_id_api(id: str):
    try:
        trainee = get_trainee_by_id(id)
    except PyMongoError as exc:
        raise HTTPException(status_code=503, detail="No se pudo acceder a MongoDB") from exc
    if not trainee:
        raise HTTPException(status_code=404, detail="Aprendiz no encontrado")
    return trainee


@app.put("/Trainees/{id}", response_description="actualizar un aprendiz")
def update_trainee_api(id: str, data: TraineeUpdateModel):
    try:
        trainee = update_trainee(id, data)
    except PyMongoError as exc:
        raise HTTPException(status_code=503, detail="No se pudo acceder a MongoDB") from exc
    if not trainee:
        raise HTTPException(status_code=404, detail="Aprendiz no encontrado")
    return trainee


@app.delete("/Trainees/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_trainee_api(id: str):
    try:
        deleted = delete_trainee(id)
    except PyMongoError as exc:
        raise HTTPException(status_code=503, detail="No se pudo acceder a MongoDB") from exc
    if not deleted:
        raise HTTPException(status_code=404, detail="Aprendiz no encontrado")
    return None
