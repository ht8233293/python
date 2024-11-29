import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import Frame, Button, Label, Entry

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_management"
)
def show_student_ui(root, content_frame):
    clear_frame(content_frame)

    # Hiển thị thông tin sinh viên
    Label(content_frame, text="Tên:").grid(row=0, column=0)
    global entry_name
    entry_name = Entry(content_frame)
    entry_name.grid(row=0, column=1)

    Label(content_frame, text="Ngày sinh (YYYY-MM-DD):").grid(row=1, column=0)
    global entry_dob
    entry_dob = Entry(content_frame)
    entry_dob.grid(row=1, column=1)

    Label(content_frame, text="Giới tính (male/female):").grid(row=2, column=0)
    global entry_gender
    entry_gender = Entry(content_frame)
    entry_gender.grid(row=2, column=1)

    Label(content_frame, text="Địa chỉ:").grid(row=3, column=0)
    global entry_address
    entry_address = Entry(content_frame)
    entry_address.grid(row=3, column=1)

    Label(content_frame, text="Email:").grid(row=4, column=0)
    global entry_email
    entry_email = Entry(content_frame)
    entry_email.grid(row=4, column=1)

    Label(content_frame, text="SĐT:").grid(row=5, column=0)
    global entry_phone
    entry_phone = Entry(content_frame)
    entry_phone.grid(row=5, column=1)

    Label(content_frame, text="ID lớp:").grid(row=6, column=0)
    global entry_class_id
    entry_class_id = Entry(content_frame)
    entry_class_id.grid(row=6, column=1)

    # Nút thêm sinh viên
    btn_add = tk.Button(content_frame, text="Thêm sinh viên", command=add_student)
    btn_add.grid(row=7, column=0, columnspan=2)

    # Nút hiển thị danh sách sinh viên
    btn_show_students = tk.Button(content_frame, text="Xem sinh viên", command=show_students)
    btn_show_students.grid(row=8, column=0, columnspan=2)
def show_students():
    try:
        conn = db
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sinhvien")
        students = cursor.fetchall()

        top = tk.Toplevel()
        top.title("Danh sách sinh viên")

        for idx, sinhvien in enumerate(students):
            Label(top, text=f"ID: {sinhvien[0]}").grid(row=idx, column=0)
            Label(top, text=f"Họ và Tên: {sinhvien[1]}").grid(row=idx, column=1)
            Label(top, text=f"Ngày sinh: {sinhvien[2]}").grid(row=idx, column=2)
            Label(top, text=f"Giới tính: {sinhvien[3]}").grid(row=idx, column=3)
            Label(top, text=f"Địa chỉ: {sinhvien[4]}").grid(row=idx, column=4)
            Label(top, text=f"Email: {sinhvien[5]}").grid(row=idx, column=5)
            Label(top, text=f"SĐT: {sinhvien[6]}").grid(row=idx, column=6)
            Label(top, text=f"ID lớp: {sinhvien[7]}").grid(row=idx, column=7)

    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()
def add_student():
    try:
        conn = db
        cursor = conn.cursor()
        sql = "INSERT INTO sinhvien (ten, ngay_sinh, gioi_tinh, dia_chi, email, sdt, lop_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (entry_name.get(), entry_dob.get(), entry_gender.get(), entry_address.get(), entry_email.get(),
               entry_phone.get(), entry_class_id.get())
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Thành công", "Thêm sinh viên thành công!")
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def show_khoa_ui(root, content_frame):
    clear_frame(content_frame)

    # Hiển thị thông tin khoa
    Label(content_frame, text="Tên khoa:").grid(row=0, column=0)
    global entry_khoa_name
    entry_khoa_name = Entry(content_frame)
    entry_khoa_name.grid(row=0, column=1)

    Label(content_frame, text="Trưởng khoa:").grid(row=1, column=0)
    global entry_khoa_head
    entry_khoa_head = Entry(content_frame)
    entry_khoa_head.grid(row=1, column=1)

    # Nút thêm khoa
    btn_add_khoa = tk.Button(content_frame, text="Thêm khoa", command=add_khoa)
    btn_add_khoa.grid(row=2, column=0, columnspan=2)

    # Nút hiển thị danh sách khoa
    btn_show_khoa = tk.Button(content_frame, text="Xem danh sách khoa", command=show_khoa)
    btn_show_khoa.grid(row=3, column=0, columnspan=2)
def show_khoa():
    try:
        conn = db
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM khoa")
        faculties = cursor.fetchall()

        top = tk.Toplevel()
        top.title("Danh sách khoa")

        for idx, faculty in enumerate(faculties):
            Label(top, text=f"ID: {faculty[0]}").grid(row=idx, column=0)
            Label(top, text=f"Tên khoa: {faculty[1]}").grid(row=idx, column=1)
            Label(top, text=f"Trưởng khoa: {faculty[2]}").grid(row=idx, column=2)

    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()
def add_khoa():
    try:
        conn = db
        cursor = conn.cursor()
        sql = "INSERT INTO khoa (ten, truong_khoa) VALUES (%s, %s)"
        val = (entry_khoa_name.get(), entry_khoa_head.get())
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Thành công", "Thêm khoa thành công!")
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()
def show_lop_ui(root, content_frame):
    clear_frame(content_frame)

    # Hiển thị thông tin lớp
    Label(content_frame, text="Tên lớp:").grid(row=0, column=0)
    global entry_lop_name
    entry_lop_name = Entry(content_frame)
    entry_lop_name.grid(row=0, column=1)

    Label(content_frame, text="ID Khoa:").grid(row=1, column=0)
    global entry_khoa_id
    entry_khoa_id = Entry(content_frame)
    entry_khoa_id.grid(row=1, column=1)

    # Nút thêm lớp
    btn_add_lop = tk.Button(content_frame, text="Thêm lớp", command=add_lop)
    btn_add_lop.grid(row=2, column=0, columnspan=2)

    # Nút hiển thị danh sách lớp
    btn_show_lop = tk.Button(content_frame, text="Xem danh sách lớp", command=show_lop)
    btn_show_lop.grid(row=3, column=0, columnspan=2)
def show_lop():
    try:
        conn = db
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Lop")
        classes = cursor.fetchall()

        top = tk.Toplevel()
        top.title("Danh sách lớp")

        for idx, lop in enumerate(classes):
            Label(top, text=f"ID: {lop[0]}").grid(row=idx, column=0)
            Label(top, text=f"Tên lớp: {lop[1]}").grid(row=idx, column=1)
            Label(top, text=f"ID Khoa: {lop[2]}").grid(row=idx, column=2)

    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()
def add_lop():
    try:
        conn = db
        cursor = conn.cursor()
        sql = "INSERT INTO Lop (ten, khoa_id) VALUES (%s, %s)"
        val = (entry_lop_name.get(), entry_khoa_id.get())
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Thành công", "Thêm lớp thành công!")
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()
def show_giay_to_ui(root, content_frame):
    clear_frame(content_frame)
    # TODO: Thêm logic để hiển thị giao diện quản lý giấy tờ nhập trường
def show_nhan_than_ui(root, content_frame):
    clear_frame(content_frame)
    # TODO: Thêm logic để hiển thị giao diện quản lý thông tin nhân thân

def show_lien_he_ui(root, content_frame):
    clear_frame(content_frame)
    # TODO: Thêm logic để hiển thị giao diện quản lý thông tin liên hệ
def main():
    root = tk.Tk()
    root.title("Hệ thống quản lý sinh viên")
    root.geometry("800x600")

    button_frame = Frame(root)
    button_frame.pack(side=tk.TOP, fill=tk.X)

    content_frame = Frame(root)
    content_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    student_button = Button(button_frame, text="Quản lý sinh viên",
                            command=lambda: show_student_ui(root, content_frame))
    student_button.pack(side=tk.LEFT)

    faculty_button = Button(button_frame, text="Quản lý khoa", command=lambda: show_khoa_ui(root, content_frame))
    faculty_button.pack(side=tk.LEFT)

    class_button = Button(button_frame, text="Quản lý lớp", command=lambda: show_lop_ui(root, content_frame))
    class_button.pack(side=tk.LEFT)

    admission_button = Button(button_frame, text="Quản lý giấy tờ nhập trường",
                              command=lambda: show_giay_to_ui(root, content_frame))
    admission_button.pack(side=tk.LEFT)

    result_button = Button(button_frame, text="Quản lý thông tin nhân thân",
                           command=lambda: show_nhan_than_ui(root, content_frame))
    result_button.pack(side=tk.LEFT)

    contact_button = Button(button_frame, text="Quản lý thông tin liên hệ",
                            command=lambda: show_lien_he_ui(root, content_frame))
    contact_button.pack(side=tk.LEFT)

    root.mainloop()
if __name__ == "__main__":
    main()
