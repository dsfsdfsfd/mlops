from fastapi import APIRouter, File, UploadFile, status
from controllers import extract_ocr
from schemas import ocr_response

router = APIRouter()

@router.post("/ocr/predict")
async def predict_ocr(file_upload: UploadFile = File(...)):
    ocr_result = extract_ocr(file_upload.file)
    return ocr_response(
        data=ocr_result,
        status_code=status.HTTP_200_OK
    )