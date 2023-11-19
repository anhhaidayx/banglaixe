import cv2
import requests
import numpy as np

# Khởi tạo đối tượng VideoCapture để kết nối với webcam máy tính
cap = cv2.VideoCapture(0)

# Kiểm tra xem webcam có khả dụng không
if not cap.isOpened():
    print("Không thể kết nối với webcam.")
    exit()

# Đọc khung hình từ webcam
ret, frame = cap.read()

# Lưu ảnh vào một mảng NumPy
_, img_encoded = cv2.imencode('.png', frame)
img_array = np.array(img_encoded).tobytes()

# Gửi ảnh lên server
url = 'http://127.0.0.1:5000/upload'  # Thay thế bằng địa chỉ server của bạn
files = {'file': ('image.png', img_array)}
response = requests.post(url, files=files)

# Kiểm tra xem yêu cầu đã thành công không
if response.status_code == 200:
    print("Ảnh đã được gửi thành công.")
else:
    print("Gửi ảnh thất bại. Mã trạng thái:", response.status_code)

# Giải phóng tài nguyên
cap.release()