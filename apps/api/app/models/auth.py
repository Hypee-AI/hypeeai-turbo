from typing import Optional, List
from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    """JWT token response model"""
    access_token: str
    token_type: str
    expires_in: int
    user_id: str
    email: str
    name: Optional[str] = None
    picture: Optional[str] = None


class SSOLoginResponse(BaseModel):
    """Response model for SSO login URL"""
    login_url: str


class OAuthCallback(BaseModel):
    """OAuth callback request model"""
    code: str
    state: Optional[str] = None


class FacebookPage(BaseModel):
    """Facebook page model"""
    id: str
    name: str
    access_token: str
    category: str
    picture_url: Optional[str] = None


class FacebookPagesResponse(BaseModel):
    """Response model for Facebook pages list"""
    pages: List[FacebookPage] 