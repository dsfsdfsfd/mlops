import easyocr
import numpy as np
from PIL import Image
from schemas import ocr_output

def build_extract_ocr(languages):
    easy_ocr = easyocr.Reader(languages, gpu=False)
    return easy_ocr

def extract_ocr(img_path, languages: list=['en']) -> list[ocr_output]:
    try:
        easy_ocr = build_extract_ocr(languages)
    except Exception as e:
        raise Exception(f"Error during OCR processing: {e}")
    
    try:
        pil_img = Image.open(img_path).convert("RGB")
        array_img = np.asarray(pil_img)
        ocr_result = easy_ocr.readtext(array_img, slope_ths=0.5, height_ths=1.0, width_ths=1.5)

        return_data = []
        for line in ocr_result:
            bbox = [[int(x) for x in sublist] for sublist in line[0]]
            text = str(line[1])
            score = float(line[2])
            return_data.append(
                ocr_output(
                    bbox=bbox,
                    text=text,
                    score=score
                )
            )
        return return_data
    except Exception as e:
        raise Exception(f"Error during OCR processing: {e}")
