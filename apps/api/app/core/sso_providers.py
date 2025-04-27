from typing import Dict, Optional, Any
from fastapi import Request
from fastapi_sso.sso.facebook import FacebookSSO
from app.core.config import settings

class FacebookSSOProvider():
    """
    Facebook SSO provider implementation
    """
    
    def __init__(self):
        """Initialize the Facebook SSO provider"""
        self._sso: Optional[FacebookSSO] = None
        
    @property
    def sso(self) -> FacebookSSO:
        """
        Get the configured FacebookSSO instance
        
        Returns:
            FacebookSSO: The configured SSO instance
        
        Raises:
            ValueError: If the Facebook SSO is not properly configured
        """
        if self._sso is None:
            if not settings.facebook_client_id or not settings.facebook_client_secret:
                raise ValueError(
                    "Facebook SSO is not configured. Please set facebook_client_id and facebook_client_secret in the environment."
                )
            
            self._sso = FacebookSSO(
                client_id=settings.facebook_client_id,
                client_secret=settings.facebook_client_secret,
                redirect_uri=f"{settings.base_url}{settings.oauth_redirect_path}",
                allow_insecure_http=True,
            )
        
        return self._sso
    
    def get_login_url(self) -> str:
        """
        Get the Facebook OAuth login URL
        
        Returns:
            str: The login URL
        """
        return self.sso.get_login_redirect()
    
    async def verify_and_process(self, request: Request) -> Dict[str, Any]:
        """
        Verify the OAuth code and process the user information
        
        Args:
            code: The OAuth authorization code
            
        Returns:
            Dict: The user information from Facebook
            
        Raises:
            HTTPException: If the code verification fails
        """
        # Get user information from Facebook
        user = await self.sso.verify_and_process(request)
        
        return user



facebook_sso_provider = FacebookSSOProvider()
