from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import schemas, database, models
from sqlalchemy.orm import Session
from hashing import Hash
from jwt_token import create_access_token
router = APIRouter()

@router.post('/login', tags= ['authenticate'])
def login(request:OAuth2PasswordRequestForm  = Depends(), db: Session = Depends(database.get_db)): 
    
    user = db.query(models.User).filter(models.User.name == request.username).first()
    
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "invalid credentials")
    if not Hash.verify(user.password, request.password):
    # if (user.password != request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "invalid password")
    # return user
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer", "user_details": {"user_id": user.id, "user_name": user.name}}
