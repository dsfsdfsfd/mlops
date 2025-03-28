import requests
import io
from PIL import Image
from utils import plot_bbox

BACKEND_URL = "http://0.0.0.0:8000"

def ocr_api(uploaded_file):
    try:
        image = Image.open(uploaded_file)
        img_name = uploaded_file.name  

        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')
        img_byte = img_byte_arr.getvalue()

        url = f"{BACKEND_URL}/ocr/predict"
        files = {'file_upload': (img_name, img_byte, 'image/jpeg')}
        headers = {'accept': 'application/json'}

        response = requests.post(url, headers=headers, files=files)
        response.raise_for_status()  

        json_results = response.json().get('data')
        if json_results is None:
            return "Error: 'data' key not found in response.", None

        if image.mode != 'RGB':
            image = image.convert('RGB')

        image_with_bbox, _, _, _ = plot_bbox(json_results, image)
        return "Success", image_with_bbox
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}", None
    except Exception as e:
        return f"Error: {str(e)}", None