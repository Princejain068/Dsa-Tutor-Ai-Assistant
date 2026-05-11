from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    problem: str
    code: str