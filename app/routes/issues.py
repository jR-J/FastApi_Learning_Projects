from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/issues", tag=["issues"])

@router.get("/")
def get_issues():
    return []