import sqlite3
import tkinter as tk
from tkinter import messagebox

# Kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('sinhVien.db')

# Tạo bảng nếu chưa tồn tại
conn.execute('''
CREATE TABLE IF NOT EXISTS SINHVIEN
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50));
''')
print("Table created successfully")

# Tạo giao diện người dùng
window = tk.Tk()
window.title("Quản lý hồ sơ sinh viên")

def add_student():
    # Thêm sinh viên vào cơ sở dữ liệu
    conn.execute(f"INSERT INTO SINHVIEN (ID,NAME,AGE,ADDRESS) \
        VALUES (1, 'Nguyen Van A', 20, 'Hanoi' )");
    conn.commit()
    messagebox.showinfo("Thông báo", "Đã thêm sinh viên thành công")

add_button = tk.Button(window, text="Thêm sinh viên", command=add_student)
add_button.pack()

window.mainloop()

# Đóng kết nối
conn.close()
