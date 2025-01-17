import mysql.connector
from mysql.connector import errorcode

# Hàm kết nối tới cơ sở dữ liệu MySQL mà không cần database cụ thể
def ket_noi_csdl():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
    except mysql.connector.Error as err:
        print(f"Lỗi kết nối cơ sở dữ liệu: {err}")
        exit(1)

# Hàm tạo cơ sở dữ liệu 'student_management'
def tao_csdl():
    conn = ket_noi_csdl()
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS student_management")
        print("Tạo cơ sở dữ liệu thành công.")
    except mysql.connector.Error as err:
        print(f"Tạo cơ sở dữ liệu thất bại: {err}")
        exit(1)
    finally:
        cursor.close()
        conn.close()

# Hàm kết nối tới cơ sở dữ liệu 'student_management'
def ket_noi_csdl_sinh_vien():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_management"
        )
    except mysql.connector.Error as err:
        print(f"Lỗi kết nối cơ sở dữ liệu: {err}")
        exit(1)

# Hàm tạo các bảng cần thiết
def tao_bang():
    conn = ket_noi_csdl_sinh_vien()
    cursor = conn.cursor()

    try:
        # Tạo bảng Khoa (Department)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Khoa (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ten VARCHAR(100),
            truong_khoa VARCHAR(100)
        );
        ''')

        # Tạo bảng Lớp (Class)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lop (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ten VARCHAR(100),
            khoa_id INT,
            FOREIGN KEY (khoa_id) REFERENCES Khoa(id)
        );
        ''')

        # Tạo bảng Sinh viên (Student)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS SinhVien (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ten VARCHAR(100),
            ngay_sinh DATE,
            gioi_tinh ENUM('M', 'F'),
            dia_chi VARCHAR(255),
            email VARCHAR(100),
            sdt VARCHAR(20),
            lop_id INT,
            FOREIGN KEY (lop_id) REFERENCES Lop(id)
        );
        ''')

        # Tạo bảng Giấy tờ (Document)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS GiayTo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            sinhvien_id INT,
            loai_giayto ENUM('BC', 'DIP', 'TRC', 'IDP'),
            trang_thai BOOLEAN,
            FOREIGN KEY (sinhvien_id) REFERENCES SinhVien(id)
        );  
        ''')

        # Tạo bảng Liên hệ (Contact)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS LienHe (
            id INT AUTO_INCREMENT PRIMARY KEY,
            sinhvien_id INT,
            ten_nguoi_giam_ho VARCHAR(100),
            sdt_khan_cap VARCHAR(20),
            FOREIGN KEY (sinhvien_id) REFERENCES SinhVien(id)
        );
        ''')

        conn.commit()
        print("Tạo bảng thành công.")
    except mysql.connector.Error as err:
        print(f"Lỗi tạo bảng: {err}")
    finally:
        cursor.close()
        conn.close()

# Khởi tạo cơ sở dữ liệu
tao_csdl()

# Khởi tạo các bảng
tao_bang()
