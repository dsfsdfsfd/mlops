from PIL import ImageDraw

def plot_bbox(easy_ocr_result, image):
    # Lấy danh sách các giá trị, sử dụng get() để tránh lỗi nếu khóa không tồn tại
    boxes = [data.get("bbox") for data in easy_ocr_result]
    texts = [data.get("text") for data in easy_ocr_result]
    scores = [data.get("score") for data in easy_ocr_result]

    draw = ImageDraw.Draw(image)
    rectangle_width = 2
    font_size = 20
    width, height = image.size  # Lấy kích thước ảnh

    for box, text in zip(boxes, texts):
        if box is None or text is None:  # Bỏ qua nếu dữ liệu không hợp lệ
            continue
        try:
            # Lấy tọa độ và giới hạn trong kích thước ảnh
            top_left = (max(0, min(width, int(box[0][0]))), max(0, min(height, int(box[0][1]))))
            bottom_right = (max(0, min(width, int(box[2][0]))), max(0, min(height, int(box[2][1]))))

            # Đảm bảo top_left và bottom_right đúng thứ tự
            if top_left[0] > bottom_right[0]:
                top_left, bottom_right = (bottom_right[0], top_left[1]), (top_left[0], bottom_right[1])
            if top_left[1] > bottom_right[1]:
                top_left, bottom_right = (top_left[0], bottom_right[1]), (bottom_right[0], top_left[1])

            # Đảm bảo vị trí văn bản không âm
            text_pos = (top_left[0], max(0, top_left[1] - font_size - rectangle_width))

            draw.rectangle([top_left, bottom_right], outline="green", width=rectangle_width)
            draw.text(text_pos, text, fill="blue")
        except Exception as e:
            print(f"Error drawing box: {e}")
            continue

    return image, boxes, texts, scores