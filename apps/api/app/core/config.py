from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "HypeeAI API"
    api_version: str = "v1"
    
    # Base URL for the application (used for OAuth redirects)
    base_url: str = "http://localhost:8000"
    
    # JWT Configuration
    jwt_secret_key: str = "supersecretkey"  # Should be in .env file in production
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    
    # Facebook OAuth Configuration
    facebook_client_id: Optional[str] = "701021539179419" 
    facebook_client_secret: Optional[str] = "da418cb6d980d3ef52773392697e13ec"
    facebook_oauth_scopes: str = "email,public_profile,pages_show_list,pages_read_engagement,pages_manage_posts"
    
    # Callback URLs
    oauth_redirect_path: str = "/api/v1/auth/callback/facebook"
    frontend_callback_url: str = "http://localhost:3000/auth/callback"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
