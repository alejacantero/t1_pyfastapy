from src .templates.controlles import create_trainee, get_all_trainees, get_trainee_by_id, update_trainee, delete_trainee

from src.models.model import TraineeModel, TraineeUpdateModel
from fastapi import FastAPI, HTTPException, status

app = FastAPI(
    title = "API de aprendices",
    description = "API simple con fastapi para onsumir los datos de los aprendices",
    version = "1.0.0",
)

#mensaje bievenida
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de aprendices"}

#registrar aprendices
@app.post(
    "/trainee", response_description="Registrar un nuevo aprendiz", 
    status_code=status.HTTP_201_CREATED,
)

def create_trainee_api(trainee: TraineeModel):
    #validar si ya existe el documento
    return create_trainee (trainee)

#obtener la lista de aprendices
@app.get(
    "/trainee", response_description="listar todos los aprendices"   
)

def get_all_trainee_api():
    return get_all_trainees()

#obtener un aprendiz porsu id
@app.get(
    "/trainee/{id}", response_description="obtener un aprendiz porsu id"
)

def get_trainee_by_id_api(id: str):
    trainee = get_trainee_by_id (id)
    if not trainee: 
        raise HTTPException (
            status_code= status.HTTP_404_NOT_FOUND, detail="aprendiz no encontrado")
    return trainee

#editar aprendiz por su id
@app.put(
    "/trainee/{id}", response_description="actualizar un aprendiz por su ID"
)

def update_trainee_api(id: str , trainee: TraineeUpdateModel):
    trainee= update_trainee (id, trainee)
    if not trainee:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND, detail="aprendiz no encontrado o sin datos a actualizar",
        )
    return update_trainee

#eliminar un aprendiz
@app.delete(
    "/trainee/{id}", response_description="eliminar un aprendiz por su ID"
)
def delete_trainee_api(id= str):
    trainee = delete_trainee(id)
    if not trainee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail= "aprendiz no encontrado"
        )
    return {"message": "aprendiz eliminadp"}