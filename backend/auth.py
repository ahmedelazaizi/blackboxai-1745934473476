from fastapi import APIRouter, HTTPException, Response, Cookie
from pydantic import BaseModel
from typing import Optional
import hashlib
import secrets
from backend.db import get_db_connection

router = APIRouter()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/register")
async def register(user: UserRegister):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (user.username, hash_password(user.password)))
        conn.commit()
    except Exception:
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists")
    conn.close()
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: UserLogin, response: Response):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (user.username,))
    db_user = cursor.fetchone()
    conn.close()
    if db_user is None or db_user["password_hash"] != hash_password(user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    session_token = secrets.token_hex(16)
    response.set_cookie(key="session_token", value=session_token, httponly=True)
    return {"message": "Login successful", "session_token": session_token}

@router.get("/me")
async def get_current_user(session_token: Optional[str] = Cookie(None)):
    if session_token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"username": "demo_user", "message": "Authenticated user (mock)"}
