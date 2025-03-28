from pydantic import BaseModel

class ocr_output(BaseModel):
    bbox: list[list[int]]
    text: str
    score: float

class ocr_response(BaseModel):
    data: list[ocr_output]
    status_code: int
