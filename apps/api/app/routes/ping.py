from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/")
async def ping():
    """
    Health check endpoint
    
    Returns:
        Dict: Simple health check response
    """
    return {"status": "healthy", "message": "pong"}
