from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from pydantic import BaseModel

app = FastAPI(
    title="JWT Authentication API",
    description="FastAPI JWT Authentication Demo with Login, Logout and Protected Routes",
    version="1.0"
)

SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Dummy user database
fake_users_db = {
    "admin": {
        "username": "admin",
        "password": "admin123"
    }
}

# Token Model
class Token(BaseModel):
    access_token: str
    token_type: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Create JWT Token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Verify JWT Token
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or Expired Token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    return username

# Home Route
@app.get("/")
def home():
    return {"message": "JWT Authentication Demo"}

# Login Route
@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    user = fake_users_db.get(form_data.username)

    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token({"sub": user["username"]})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# Protected Route
@app.get("/profile")
def profile(current_user: str = Depends(get_current_user)):
    return {
        "message": f"Welcome {current_user}",
        "access": "Authorized"
    }

# Another Protected Route
@app.get("/dashboard")
def dashboard(current_user: str = Depends(get_current_user)):
    return {
        "message": f"{current_user} can access Dashboard"
    }

# Logout Route (Client removes JWT)
@app.post("/logout")
def logout():
    return {
        "message": "Logout successful. Please remove the JWT token from the client."
    }
