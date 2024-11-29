import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import Frame, Button, Label, Entry

# Establish database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_management"
)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def create_label_entry_pair(frame, text, row, column=0, entry_var=None):
    label = Label(frame, text=text, padx=5, pady=5)
    label.grid(row=row, column=column, sticky='e')
    entry = Entry(frame, textvariable=entry_var)
    entry.grid(row=row, column=column+1, padx=5, pady=5)
    return entry

def show_student_ui(root, content_frame):
    clear_frame(content_frame)

    global entry_name, entry_dob, entry_gender, entry_address, entry_email, entry_phone, entry_class_id

    entry_name = create_label_entry_pair(content_frame, "Tên:", 0)
    entry_dob = create_label_entry_pair(content_frame, "Ngày sinh (YYYY-MM-DD):", 1)
    entry_gender = create_label_entry_pair(content_frame, "Giới tính (male/female):", 2)
    entry_address = create_label_entry_pair(content_frame, "Địa chỉ:", 3)
    entry_email = create_label_entry_pair(content_frame, "Email:", 4)
    entry_phone = create_label_entry_pair(content_frame, "SĐT:", 5)
    entry_class_id = create_label_entry_pair(content_frame, "ID lớp:", 6)

    Button(content_frame, text="Thêm sinh viên", command=add_student).grid(row=7, column=0, columnspan=2, pady=10)
    Button(content_frame, text="Xem sinh viên", command=show_students).grid(row=8, column=0, columnspan=2, pady=10)

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

def show_students():
    try:
        conn = db
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sinhvien")
        students = cursor.fetchall()

        top = tk.Toplevel()
        top.title("Danh sách sinh viên")

        headers = ["ID", "Họ và Tên", "Ngày sinh", "Giới tính", "Địa chỉ", "Email", "SĐT", "ID lớp"]
        for col, header in enumerate(headers):
            Label(top, text=header, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=0, column=col)

        for idx, sinhvien in enumerate(students):
            for col, value in enumerate(sinhvien):
                Label(top, text=value, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=idx+1, column=col)

    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()

def show_khoa_ui(root, content_frame):
    clear_frame(content_frame)

    global entry_khoa_name, entry_khoa_head

    entry_khoa_name = create_label_entry_pair(content_frame, "Tên khoa:", 0)
    entry_khoa_head = create_label_entry_pair(content_frame, "Trưởng khoa:", 1)

    Button(content_frame, text="Thêm khoa", command=add_khoa).grid(row=2, column=0, columnspan=2, pady=10)
    Button(content_frame, text="Xem danh sách khoa", command=show_khoa).grid(row=3, column=0, columnspan=2, pady=10)

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

def show_khoa():
    try:
        conn = db
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM khoa")
        faculties = cursor.fetchall()

        top = tk.Toplevel()
        top.title("Danh sách khoa")

        headers = ["ID", "Tên khoa", "Trưởng khoa"]
        for col, header in enumerate(headers):
            Label(top, text=header, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=0, column=col)

        for idx, faculty in enumerate(faculties):
            for col, value in enumerate(faculty):
                Label(top, text=value, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=idx+1, column=col)

    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()

def show_lop_ui(root, content_frame):
    clear_frame(content_frame)

    global entry_lop_name, entry_khoa_id

    entry_lop_name = create_label_entry_pair(content_frame, "Tên lớp:", 0)
    entry_khoa_id = create_label_entry_pair(content_frame, "ID Khoa:", 1)

    Button(content_frame, text="Thêm lớp", command=add_lop).grid(row=2, column=0, columnspan=2, pady=10)
    Button(content_frame, text="Xem danh sách lớp", command=show_lop).grid(row=3, column=0, columnspan=2, pady=10)

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

def show_lop():
    try:
        conn = db
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Lop")
        classes = cursor.fetchall()

        top = tk.Toplevel()
        top.title("Danh sách lớp")

        headers = ["ID", "Tên lớp", "ID Khoa"]
        for col, header in enumerate(headers):
            Label(top, text=header, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=0, column=col)

        for idx, lop in enumerate(classes):
            for col, value in enumerate(lop):
                Label(top, text=value, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=idx+1, column=col)

    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()

def show_giay_to_ui(root, content_frame):
    clear_frame(content_frame)

    global entry_document_name, entry_document_description

    entry_document_name = create_label_entry_pair(content_frame, "Tên giấy tờ:", 0)
    entry_document_description = create_label_entry_pair(content_frame, "Mô tả:", 1)

    Button(content_frame, text="Thêm giấy tờ", command=add_document).grid(row=2, column=0, columnspan=2, pady=10)
    Button(content_frame, text="Xem danh sách giấy tờ", command=show_documents).grid(row=3, column=0, columnspan=2, pady=10)

def add_document():
    try:
        conn = db
        cursor = conn.cursor()
        sql = "INSERT INTO giayto (ten, mo_ta) VALUES (%s, %s)"
        val = (entry_document_name.get(), entry_document_description.get())
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Thành công", "Thêm giấy tờ thành công!")
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()

def show_documents():
    try:
        conn = db
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM giayto")
        documents = cursor.fetchall()

        top = tk.Toplevel()
        top.title("Danh sách giấy tờ")

        headers = ["ID", "Tên giấy tờ", "Mô tả"]
        for col, header in enumerate(headers):
            Label(top, text=header, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=0, column=col)

        for idx, document in enumerate(documents):
            for col, value in enumerate(document):
                Label(top, text=value, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=idx+1, column=col)

    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()

def show_nhan_than_ui(root, content_frame):
    clear_frame(content_frame)

    global entry_relative_name, entry_relative_relation, entry_relative_contact

    entry_relative_name = create_label_entry_pair(content_frame, "Tên nhân thân:", 0)
    entry_relative_relation = create_label_entry_pair(content_frame, "Quan hệ:", 1)
    entry_relative_contact = create_label_entry_pair(content_frame, "Liên hệ:", 2)

    Button(content_frame, text="Thêm nhân thân", command=add_relative).grid(row=3, column=0, columnspan=2, pady=10)
    Button(content_frame, text="Xem danh sách nhân thân", command=show_relatives).grid(row=4, column=0, columnspan=2, pady=10)

def add_relative():
    try:
        conn = db
        cursor = conn.cursor()
        sql = "INSERT INTO nhanthan (ten, quan_he, lien_he) VALUES (%s, %s, %s)"
        val = (entry_relative_name.get(), entry_relative_relation.get(), entry_relative_contact.get())
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Thành công", "Thêm nhân thân thành công!")
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()

def show_relatives():
    try:
        conn = db
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nhanthan")
        relatives = cursor.fetchall()

        top = tk.Toplevel()
        top.title("Danh sách nhân thân")

        headers = ["ID", "Tên nhân thân", "Quan hệ", "Liên hệ"]
        for col, header in enumerate(headers):
            Label(top, text=header, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=0, column=col)

        for idx, relative in enumerate(relatives):
            for col, value in enumerate(relative):
                Label(top, text=value, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=idx+1, column=col)

    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()

def show_lien_he_ui(root, content_frame):
    clear_frame(content_frame)

    global entry_contact_name, entry_contact_email, entry_contact_phone

    entry_contact_name = create_label_entry_pair(content_frame, "Tên liên hệ:", 0)
    entry_contact_email = create_label_entry_pair(content_frame, "Email:", 1)
    entry_contact_phone = create_label_entry_pair(content_frame, "SĐT:", 2)

    Button(content_frame, text="Thêm liên hệ", command=add_contact).grid(row=3, column=0, columnspan=2, pady=10)
    Button(content_frame, text="Xem danh sách liên hệ", command=show_contacts).grid(row=4, column=0, columnspan=2, pady=10)

def add_contact():
    try:
        conn = db
        cursor = conn.cursor()
        sql = "INSERT INTO lienhe (ten, email, sdt) VALUES (%s, %s, %s)"
        val = (entry_contact_name.get(), entry_contact_email.get(), entry_contact_phone.get())
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Thành công", "Thêm liên hệ thành công!")
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()

def show_contacts():
    try:
        conn = db
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lienhe")
        contacts = cursor.fetchall()

        top = tk.Toplevel()
        top.title("Danh sách liên hệ")

        headers = ["ID", "Tên liên hệ", "Email", "SĐT"]
        for col, header in enumerate(headers):
            Label(top, text=header, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=0, column=col)

        for idx, contact in enumerate(contacts):
            for col, value in enumerate(contact):
                Label(top, text=value, borderwidth=2, relief='groove', padx=5, pady=5).grid(row=idx+1, column=col)

    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        cursor.close()

def main():
    root = tk.Tk()
    root.title("Hệ thống quản lý sinh viên")
    root.geometry("900x600")

    button_frame = Frame(root, padx=10, pady=10)
    button_frame.pack(side=tk.TOP, fill=tk.X)

    content_frame = Frame(root, padx=10, pady=10)
    content_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    buttons = [
        ("Quản lý sinh viên", show_student_ui),
        ("Quản lý khoa", show_khoa_ui),
        ("Quản lý lớp", show_lop_ui),
        ("Quản lý giấy tờ nhập trường", show_giay_to_ui),
        ("Quản lý thông tin nhân thân", show_nhan_than_ui),
        ("Quản lý thông tin liên hệ", show_lien_he_ui)
    ]

    for text, command in buttons:
        Button(button_frame, text=text, command=lambda cmd=command: cmd(root, content_frame), width=20).pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
