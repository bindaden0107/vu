# from tkinter import *
#
# window = Tk()
#
# btn_add = Button(text = 'Add Two Number')
# btn_add.pack()
#
# window.mainloop()
from nhan_vien_demo import Nhan_Vien

#Gán thông tin dữ liệu cho 1 đối tượng nv1
nv1 = Nhan_Vien(ma_nv= "NV01", ten_nv= "Tran Van A", luong_nv= 2000) #tạo đối tượng
# nv1.ma_nhan_vien = "NV01" #gán thông tin
# nv1.ten_nhan_vien = "Tran Van A"
# nv1.luong_nhan_vien = 2000

#Gán thông tin dữ liệu cho 1 đối tượng nv2
nv2 = Nhan_Vien()
nv2.ma_nhan_vien = "NV02"
nv2.ten_nhan_vien = "Tran Van Vu"
nv2.luong_nhan_vien = 3000

nv3 = Nhan_Vien("NV03", "Nguyen Van Vu", 4000)

#truy xuất thông tin của đối tượng
# print(nv1.ten_nhan_vien, nv2.ten_nhan_vien)
# print(nv1.ma_nhan_vien, nv2.ma_nhan_vien)

#Truy xuất thuộc tính phần tử thông qua danh sách
ds_nhan_vien = [nv1, nv2, nv3]

# for i in range(0, len(ds_nhan_vien)):
#     print(ds_nhan_vien[i].ten_nhan_vien)

def xoa_nhan_vien():
    flag = 0
    ten_xoa = input("Vui long nhap vao ten nhan vien muon xoa: ")
    ds_con_lai = []
    for i in range(0, len(ds_nhan_vien)):
        if ten_xoa not in ds_nhan_vien[i].ten_nhan_vien:
            ds_con_lai.append(ds_nhan_vien[i])
        else:
            flag = 1

    if flag == 0:
        print("Khong tim thay", ten_xoa)

    return ds_con_lai

ds_con_lai = xoa_nhan_vien()

for i in range(0, len(ds_con_lai)):
    print(ds_con_lai[i].ten_nhan_vien)


