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
            FOREIGN KEY (khoa_id) REFERENCES Khoa(id) ON DELETE CASCADE
        );
        ''')

        # Tạo bảng Sinh viên (Student)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS SinhVien (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ten VARCHAR(100),
            ngay_sinh DATE,
            gioi_tinh ENUM('male', 'female'),
            dia_chi VARCHAR(255),
            email VARCHAR(100),
            sdt VARCHAR(20),
            lop_id INT,
            FOREIGN KEY (lop_id) REFERENCES Lop(id) ON DELETE CASCADE
        );
        ''')

        # Tạo bảng Giấy tờ (Document)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS GiayTo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ten VARCHAR(100),
            mo_ta VARCHAR(255)
        );
        ''')

        # Tạo bảng Nhân thân (Relative)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS NhanThan (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ten VARCHAR(100),
            quan_he VARCHAR(100),
            lien_he VARCHAR(100)
        );
        ''')

        # Tạo bảng Liên hệ (Contact)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS LienHe (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ten VARCHAR(100),
            email VARCHAR(100),
            sdt VARCHAR(20)
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
