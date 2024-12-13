import tkinter as tk
import tkinter.font as tkFont
from tkcalendar import Calendar

root = tk.Tk()
root.geometry("1300x500")
root.title("THÔNG TIN NHÂN VIÊN")

font = tkFont.Font(size=11, weight="bold")


Tieude = tk.Label(root, text="THÔNG TIN NHÂN VIÊN", font=font)
Tieude.place(x=0, y=20, width=320, height=30)


box_1 = tk.Text()
box_1.place(x=290, y=20, width=15, height=15)

box_2 = tk.Text()
box_2.place(x=450, y=20, width=15, height=15)

box_3 = tk.Entry()
box_3.place(x=50, y=70, width=200, height=30)

box_4 = tk.Entry()
box_4.place(x=290, y=70, width=300, height=30)

box_5 = tk.Entry(root)
box_5.place(x=650, y=70, width=200, height=30)


def show_calendar(event):

    calendar_window = tk.Toplevel(root)
    calendar_window.geometry("250x250")
    calendar_window.title("Chọn ngày")

    calendar = Calendar(calendar_window, selectmode='day', year=2023, month=12, day=13)
    calendar.pack(pady=20)

    def select_date():
        selected_date = calendar.get_date()
        box_5.delete(0, tk.END)  # Xóa dữ liệu cũ trong box_5
        box_5.insert(0, selected_date)  # Hiển thị ngày được chọn
        calendar_window.destroy()  # Đóng cửa sổ lịch


    tk.Button(calendar_window, text="Chọn", command=select_date).pack()


box_5.bind("<Button-1>", show_calendar)

box_6 = tk.Entry()
box_6.place(x=50, y=140, width=539, height=30)

box_7 = tk.Entry()
box_7.place(x=50, y=215, width=539, height=30)

box_8 = tk.Entry()
box_8.place(x=650, y=140, width=340, height=30)

box_9 = tk.Entry()
box_9.place(x=1020, y=140, width=200, height=30)

box_10 = tk.Entry()
box_10.place(x=650, y=215, width=539 + 30, height=30)

tk.Label(root, text="Là khách hàng", font=("Arial", 10)).place(x=300, y=20, width=120, height=20)
tk.Label(root, text="Là nhà cung cấp", font=("Arial", 10)).place(x=460, y=20, width=120, height=20)
tk.Label(root, text="Mã", font=("Arial", 10, "bold")).place(x=40, y=50, width=50, height=20)
tk.Label(root, text="Tên", font=("Arial", 10, "bold")).place(x=280, y=50, width=50, height=20)
tk.Label(root, text="Ngày sinh", font=("Arial", 10, "bold")).place(x=650, y=50, width=80, height=20)
tk.Label(root, text="Đơn vị", font=("Arial", 10, "bold")).place(x=40, y=120, width=80, height=20)
tk.Label(root, text="Số CMND", font=("Arial", 10, "bold")).place(x=650, y=120, width=80, height=20)
tk.Label(root, text="Chức danh", font=("Arial", 10, "bold")).place(x=54, y=195, width=80, height=20)
tk.Label(root, text="Nơi cấp", font=("Arial", 10, "bold")).place(x=642, y=194, width=80, height=20)
root.mainloop()
