# Ứng dụng nhập thông tin sửa chữa xe (Streamlit + Excel)

Ứng dụng web đơn giản dùng **Streamlit** để nhập thông tin sửa chữa xe và lưu dữ liệu vào file **Excel**.

## 1. Chức năng chính

- **Nhập thông tin khách hàng và xe**:
  - Tên khách hàng  
  - Số điện thoại  
  - Biển số xe  
  - Hiệu xe / Model  
  - Ngày nhận xe  
  - Mô tả hư hỏng / yêu cầu sửa chữa  
  - Chi phí dự kiến
- **Lưu dữ liệu vào Excel**: mỗi lần bấm nút sẽ ghi thêm một dòng vào file `du_lieu_sua_chua.xlsx`.
- **Xem lại dữ liệu đã lưu** ngay trên web.
- **Tải file Excel** về máy.

## 2. Cấu trúc file chính

- `app.py`: Mã nguồn ứng dụng Streamlit.
- `requirements.txt`: Danh sách thư viện Python cần cài.
- `du_lieu_sua_chua.xlsx`: File Excel lưu dữ liệu (tự tạo sau khi lưu dữ liệu lần đầu).

## 3. Yêu cầu môi trường

- Python 3.8+ đã cài sẵn trên máy.
- Hệ điều hành: Windows (đang sử dụng PowerShell).

## 4. Cài đặt thư viện

Mở **PowerShell** tại thư mục project:

```powershell
cd "d:\SETUP\Python\Tự học\Bài Tập\Bài tập phần 2_1_Nhập thông tin sửa chữa xe"
```

Khuyến nghị tạo môi trường ảo (có thể bỏ qua nếu không cần):

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

Cài đặt các thư viện cần thiết:

```powershell
pip install -r requirements.txt
```

## 5. Chạy ứng dụng

Trong thư mục project, chạy lệnh:

```powershell
streamlit run app.py
```

Sau khi chạy:

- Trình duyệt sẽ tự mở giao diện web (hoặc bạn truy cập đường link mà Streamlit in ra, dạng `http://localhost:8501`).
- Nhập thông tin sửa chữa xe.
- Bấm **"Lưu vào Excel"** để ghi dữ liệu.
- Bên dưới sẽ hiển thị bảng dữ liệu và nút **"Tải file Excel"**.

## 6. Tuỳ chỉnh thêm

- Bạn có thể chỉnh sửa các trường nhập liệu trong `app.py` để phù hợp với nhu cầu thực tế (thêm cột, đổi tên cột, định dạng ngày tháng, v.v.).
- Nếu muốn lưu file Excel vào thư mục khác hoặc đổi tên file, sửa biến `EXCEL_FILE` trong `app.py`.

