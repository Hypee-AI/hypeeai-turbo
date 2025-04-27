from datetime import timedelta
from typing import Dict, Any

from fastapi import APIRouter, Depends, HTTPException, Request, status 
from fastapi.responses import RedirectResponse

from app.core.auth import create_access_token, verify_token, TokenData, UserAuth
from app.core.config import settings
from app.core.sso_providers import facebook_sso_provider
from app.models.auth import SSOLoginResponse 

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.get("/login/facebook", response_model=SSOLoginResponse)
async def login_social():
    """
    Get login URL for a social provider
    
    Args:
        provider: The name of the SSO provider (e.g., "facebook")
    
    Returns:
        Dict: Login URL object
        
    Raises:
        HTTPException: If the provider is not supported or not configured
    """
    try:
        return await facebook_sso_provider.get_login_url()

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting login URL: {str(e)}"
        )


@router.get("/callback/facebook")
async def facebook_callback(request: Request):
    """
    Handle OAuth callback from any supported provider
    
    Args:
        code: The authorization code
        state: The state parameter for CSRF protection
        
    Returns:
        RedirectResponse: Redirect to frontend with the token
    """
    try:
        # Get the appropriate SSO provider
        sso_provider = facebook_sso_provider()
        
        # Verify and get user info
        user_data = await sso_provider.verify_and_process(request)
        
        return user_data
        
    except Exception as e:
        # Redirect to frontend with error
        error_url = f"{settings.frontend_callback_url}?error=authentication_failed&message={str(e)}"
        return RedirectResponse(url=error_url)


@router.post("/token/validate", response_model=UserAuth)
async def validate_token(token_data: TokenData = Depends(verify_token)):
    """
    Validate a JWT token
    
    Args:
        token_data: The verified token data
        
    Returns:
        UserAuth: The user authentication information
    """
    # In a real application, you would fetch the user from a database
    # using the token_data.sub (user ID) and token_data.provider
    
    # For this example, we'll just return basic information
    return UserAuth(
        id=token_data.sub,
        email="example@example.com",  # This would come from the database
        provider=token_data.provider,
        provider_user_id=token_data.sub
    )


def create_token_from_sso_data(user_data: Dict[str, Any]) -> str:
    """
    Create a JWT token from SSO user data
    
    Args:
        user_data: User data from the SSO provider
        
    Returns:
        str: JWT token
    """
    # Set the token payload
    token_data = {
        "sub": user_data["id"],
        "provider": user_data["provider"],
        "email": user_data["email"]
    }
    
    # Create the token with expiration time
    expires_delta = timedelta(minutes=settings.jwt_access_token_expire_minutes)
    return create_access_token(token_data, expires_delta) 