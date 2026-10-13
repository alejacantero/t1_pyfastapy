from bson import ObjectId
from src.models.database import collection
from src.models.model import TraineeModel, TraineeUpdateModel

def helper_trainee(trainne) -> dict:
    return {
        "id": str(trainne["_id"]),
        "document": str (trainne["document"]),
        "name": trainne["name"],
        "last_name": trainne["last_name"],
        "email": trainne["email"],
        "age": trainne["age"],
        "program": trainne["program"],
        "record_number": trainne["record_number"]
    }
