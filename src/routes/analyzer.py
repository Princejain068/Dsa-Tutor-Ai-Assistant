from fastapi import APIRouter

from src.models.request_model import AnalyzeRequest
from src.models.response_model import AnalyzeResponse

from src.services.ai_service import analyze_solution

router = APIRouter()


@router.post(
    "/analyze-solution",
    response_model=AnalyzeResponse
)
async def analyze_solution_api(
    data: AnalyzeRequest
):

    result = analyze_solution(
        problem=data.problem,
        code=data.code
    )

    return result