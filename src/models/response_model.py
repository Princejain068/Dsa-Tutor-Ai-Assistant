from pydantic import BaseModel
from typing import List


class AnalyzeResponse(BaseModel):
    correctness: str
    time_complexity: str
    space_complexity: str
    better_approach: str
    edge_cases: List[str]
    hints: List[str]
    teaching: str