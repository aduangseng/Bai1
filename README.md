1. Bài làm về ứng dụng quản lý sinh viên
Đề tài của bài làm là "Xây dựng hệ thống quản lý sinh viên đơn giản sử dụng Flask và SQL Server".
Mục tiêu chính của hệ thống là tạo ra một ứng dụng cho phép người dùng thực hiện các thao tác cơ bản như:
+ Thêm mới sinh viên
+ Cập nhật thông tin sinh viên
+ Xóa sinh viên
+ Tìm kiếm sinh viên theo mã số
Ứng dụng được chia làm hai phần:
+ Backend (App1) cung cấp các API để thao tác với cơ sở dữ liệu.
+ Frontend (App2) là một ứng dụng web đơn giản hiển thị thông tin sinh viên từ API.
2.Công nghệ, thuật toán, ngôn ngữ lập trình
Ngôn ngữ lập trình: Python (với Flask), HTML, CSS, JavaScript
Framework: Flask (Python Web Framework đơn giản, nhẹ)
Cơ sở dữ liệu: Microsoft SQL Server
Giao tiếp giữa frontend và backend: Sử dụng RESTful API (GET, POST, PUT, DELETE)
Thư viện hỗ trợ:
+ pyodbc: Kết nối Python với SQL Server
+ flask-cors: Cho phép frontend truy cập API từ domain khác (bật CORS)
Không sử dụng thuật toán phức tạp, vì hệ thống chủ yếu thao tác CRUD với dữ liệu.
3. Một số giao diện cơ bản
Dưới đây là mô tả một số giao diện người dùng đã xây dựng:
  + Giao diện danh sách sinh viên:
  Bảng hiển thị các thông tin: Mã SV, Tên SV, Lớp, Quê quán, kèm các nút Sửa / Xóa
<img width="673" height="172" alt="image" src="https://github.com/user-attachments/assets/f673ce34-17de-4270-a9b9-4ded99a2c7df" />
  + Giao diện tìm kiếm sinh viên theo mã:
  Người dùng nhập mã sinh viên → nhấn "Tìm kiếm" → thông tin sinh viên hiện ra bên dưới.
<img width="393" height="248" alt="image" src="https://github.com/user-attachments/assets/8b44c48c-135b-425c-bd33-808c48b85eca" />
  + Giao diện thêm và cập nhật sinh viên:
  Form gồm các trường: Mã SV, Tên SV, Tên lớp, Quê quán → nút "Thêm mới"
  Khi nhấn "Sửa", thông tin hiện ra để chỉnh sửa → nhấn "Lưu"
<img width="536" height="403" alt="image" src="https://github.com/user-attachments/assets/cf7682b9-7675-48bf-82ee-99cf754c22ac" />

