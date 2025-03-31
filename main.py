from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import User
from .crud import create_user, get_user
from fastapi.security import OAuth2PasswordBearer
from .auth import create_access_token, get_password_hash, verify_password
from .logging_config import logger


Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def add_user(name: str, email: str, db: Session = Depends(get_db)):
    return create_user(db, name, email)

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

@app.post("/token")
def login(username: str, password: str):
    hashed_password = get_password_hash(password)
    if verify_password(password, hashed_password):
        access_token = create_access_token(data={"sub": username}, expires_delta=timedelta(minutes=30))
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Invalid credentials")

@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    return response  # Ensure this line is indented with exactly 4 space