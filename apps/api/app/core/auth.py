from datetime import datetime, timedelta
from typing import Optional, Dict, Any

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from app.core.config import settings

# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"/{settings.api_version}/auth/token")

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class TokenData(BaseModel):
    sub: str
    provider: str
    exp: Optional[datetime] = None


class UserAuth(BaseModel):
    """User authentication information"""
    id: str
    email: str
    provider: str
    provider_user_id: str
    name: Optional[str] = None
    picture: Optional[str] = None
    

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token
    
    Args:
        data: Data to encode in the token
        expires_delta: Optional expiration time delta
        
    Returns:
        JWT token string
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.jwt_access_token_expire_minutes))
    to_encode.update({"exp": expire})
    
    return jwt.encode(
        to_encode, 
        settings.jwt_secret_key, 
        algorithm=settings.jwt_algorithm
    )


def verify_token(token: str = Depends(oauth2_scheme)) -> TokenData:
    """
    Verify a JWT token and extract its data
    
    Args:
        token: JWT token to verify
        
    Returns:
        Token data
        
    Raises:
        HTTPException: If token is invalid
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(
            token, 
            settings.jwt_secret_key, 
            algorithms=[settings.jwt_algorithm]
        )
        
        # Ensure required fields are present
        if "sub" not in payload or "provider" not in payload:
            raise credentials_exception
            
        return TokenData(
            sub=payload["sub"],
            provider=payload["provider"],
            exp=datetime.fromtimestamp(payload["exp"]) if "exp" in payload else None
        )
        
    except JWTError:
        raise credentials_exception 