from flask import Flask, request, jsonify
import pyodbc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ Cấu hình kết nối SQL Server
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-JFRFT8R;'
        'DATABASE=QLySinhVien;'     # ← sửa tên DB của bạn
        'UID=sa;'
        'PWD=sa'
    )

# ✅ API: Lấy tất cả sinh viên
@app.route('/api/sinhvien', methods=['GET'])
def get_sinhvien():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MaSV, TenSV, TenLop, QueQuan FROM Sinhvien")
    rows = cursor.fetchall()
    result = []

    for row in rows:
        result.append({
            "MaSV": row.MaSV,
            "TenSV": row.TenSV,
            "TenLop": row.TenLop,
            "QueQuan": row.QueQuan
        })

    conn.close()
    return jsonify(result)

# ✅ API: Thêm sinh viên
@app.route('/api/sinhvien', methods=['POST'])
def add_sinhvien():
    data = request.json
    ma_sv = data.get("MaSV")
    ten_sv = data.get("TenSV")
    ten_lop = data.get("TenLop")
    que_quan = data.get("QueQuan")

    if not ma_sv or not ten_sv or not ten_lop or not que_quan:
        return jsonify({"error": "Thiếu thông tin"}), 400

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Sinhvien (MaSV, TenSV, TenLop, QueQuan)
            VALUES (?, ?, ?, ?)
        """, (ma_sv, ten_sv, ten_lop, que_quan))
        conn.commit()
        conn.close()
        return jsonify({"message": "Thêm sinh viên thành công"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ API: Xóa sinh viên theo MaSV
@app.route('/api/sinhvien/<ma_sv>', methods=['DELETE'])
def delete_sinhvien(ma_sv):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Sinhvien WHERE MaSV = ?", (ma_sv,))
        conn.commit()
        conn.close()
        return jsonify({"message": f"Đã xóa sinh viên {ma_sv}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# PUT: Cập nhật sinh viên
@app.route('/api/sinhvien/<ma_sv>', methods=['PUT'])
def update_sinhvien(ma_sv):
    data = request.json
    ten_sv = data.get("TenSV")
    ten_lop = data.get("TenLop")
    que_quan = data.get("QueQuan")

    if not ten_sv or not ten_lop or not que_quan:
        return jsonify({"error": "Thiếu thông tin"}), 400

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Sinhvien
            SET TenSV = ?, TenLop = ?, QueQuan = ?
            WHERE MaSV = ?
        """, (ten_sv, ten_lop, que_quan, ma_sv))
        conn.commit()
        conn.close()
        return jsonify({"message": "Cập nhật sinh viên thành công"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/api/sinhvien/<ma_sv>', methods=['GET'])
def get_sinhvien_by_id(ma_sv):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT MaSV, TenSV, TenLop, QueQuan FROM Sinhvien WHERE MaSV = ?", (ma_sv))
        row = cursor.fetchone()
        conn.close()

        if row:
            return jsonify({
                "MaSV": row.MaSV,
                "TenSV": row.TenSV,
                "TenLop": row.TenLop,
                "QueQuan": row.QueQuan
            })
        else:
            return jsonify({"error": "Không tìm thấy sinh viên"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
