import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkcalendar import Calendar

# Create Object

root=Tk()
# Set geometry
root.geometry("400x400")

# Add Calendar
cal = Calendar(root, selectmode = 'day',
			year = 2020, month = 5,
			day = 22)

cal.pack(pady = 20)

def grad_date():
	date.config(text = "Selected Date is: " + cal.get_date())

# Add Button and Label
Button(root, text = "Get Date",
	command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)



root = tk.Tk()


root.geometry("1300x300")
font = tkFont.Font(None,weight=tk.font.BOLD)
font1 = tkFont.Font(None,size=11)
font2 = tkFont.Font(None, size=11,weight=tk.font.BOLD)

Tieude=tk.Label(root,text="THÔNG TIN NHÂN VIÊN",width=90,font=font)
Tieude.place(x=0 ,y=20 ,width=320 , height=20)

box_1 = tk.Text()
box_1.place (x=290 , y=20 , width=15 , height=15)

box_2 = tk.Text()
box_2.place (x=450 , y=20 , width=15 , height=15)

box_3 = tk.Text()
box_3.place (x=50 , y=70 , width=200 , height=30)

box_4 = tk.Text()
box_4.place (x=290 , y=70 , width=300 , height=30)

box_5 = tk.Entry(root)
box_5.place(x=650, y=70, width=200, height=30)
def show_calendar(event):
    # Tạo cửa sổ pop-up để hiển thị lịch
    calendar_window = tk.Toplevel(root)
    calendar_window.geometry("250x250")
    calendar_window.title("Chọn ngày")

    # Tạo lịch
    calendar = Calendar(calendar_window, selectmode='day', year=2023, month=12, day=13)
    calendar.pack(pady=20)

    # Hàm để lấy ngày được chọn và đóng cửa sổ lịch
    def select_date():
        selected_date = calendar.get_date()
        box_5.delete(0, tk.END)  # Xóa dữ liệu cũ trong box_5
        box_5.insert(0, selected_date)  # Hiển thị ngày được chọn
        calendar_window.destroy()  # Đóng cửa sổ lịch

    # Nút "Chọn"
    tk.Button(calendar_window, text="Chọn", command=select_date).pack()


# Gắn sự kiện nhấn chuột trái (Left-Click) vào box_5 để hiển thị lịch
box_5.bind("<Button-1>", show_calendar)

box_6 = tk.Text()
box_6.place (x=50 , y=140 , width=539 , height=30)

box_7 = tk.Text()
box_7.place (x=50 , y=215 , width=539 , height=30)

box_8 = tk.Text()
box_8.place (x=650 , y=140 , width=340 , height=30)

box_9 = tk.Text()
box_9.place (x=1020 , y=140 , width=200 , height=30)

box_10 = tk.Text()
box_10.place (x=650 , y=215 , width=539+30 , height=30)

name_box_1=tk.Label(root,text="Là khách hàng",width=10,font=font1)
name_box_1.place(x=300 ,y=20 ,width=120 , height=20)

name_box_2=tk.Label(root,text="Là nhà cung cấp",width=10,font=font1)
name_box_2.place(x=460 ,y=20 ,width=120 , height=20)

name_box_3=tk.Label(root,text="Mã",width=10,font=font2)
name_box_3.place(x=40 ,y=50 ,width=50 , height=20)

name_box_4=tk.Label(root,text="Tên",width=90,font=font2)
name_box_4.place(x=280 ,y=50 ,width=50 , height=20)

name_box_5=tk.Label(root,text="Ngày sinh",width=90,font=font2)
name_box_5.place(x= 648,y=50 ,width=80 , height=20)

name_box_6=tk.Label(root,text="Đơn vị",width=0,font=font2)
name_box_6.place(x=40 ,y=120 ,width=80 , height=20)

name_box_8=tk.Label(root,text="Số CMND",width=90,font=font2)
name_box_8.place(x=648 ,y=120 ,width=80 , height=20)

name_box_7=tk.Label(root,text="Chức danh",width=90,font=font2)
name_box_7.place(x=54 ,y=195 ,width=80 , height=20)

name_box_9=tk.Label(root,text="Nơi cấp",width=90,font=font2 )
name_box_9.place(x=642 ,y=194 ,width=80 , height=20)

name_box_10=tk.Label(root,text="Nơi cấp",width=90,font=font2 )
name_box_10.place(x=642 ,y=194 ,width=80 , height=20)
root.mainloop()