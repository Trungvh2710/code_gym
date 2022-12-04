def them(chi_tieu, khoan_chi):
    chi_tieu.append(khoan_chi)
    
def xem(chi_tieu):
    for khoan_chi in chi_tieu:
        print(khoan_chi)

def xoa(chi_tieu, ten_chi_tieu):
    #Duyệt qua tất cả các chi tiêu
    index = -1
    for i in range(len(chi_tieu)):
        if ten == chi_tieu[i]["ten"]:
            index = i
            break
    if index == -1:
        print("Không tìm thấy khoản chi: ", ten)
    else:
        chi_tieu.remove(chi_tieu[index])

def sua_ten(chi_tieu, ten_chi_tieu):
    index = -1
    for i in range(len(chi_tieu)):
        if ten == chi_tieu[i]["ten"]:
            index = i
            break
    if index == -1:
        print("Không tìm thấy khoản chi: ", ten)
    else:
        chi_tieu[i]["ten"] = input("Nhập vào tên bạn cần thay đổi: ")
    
chi_tieu = []

while True:
    yeu_cau = int(input("Ấn 1 để xem chi tiêu\
                        ấn 2 để thêm chi tiêu\
                        ấn 3 để xóa chi tiêu\
                        ấn 4 để sửa tên chi tiêu"))
    if (yeu_cau) == 1:
        print("Hiển thị các chi tiêu")
        xem(chi_tieu)
    elif (yeu_cau) == 2:
        print("Thêm 1 chi tiêu mới")
        ten = input("Nhập vào tên khoản chi: ")
        so_tien = int(input("Nhập vào số tiền: "))
        ngay = input("Nhập vào ngày chi: ")
        khoan_chi = {
            "ten" : ten,
            "so_tien" : so_tien,
            "ngay" : ngay
        }
        them(chi_tieu, khoan_chi)
    elif (yeu_cau) == 3:
        print("Xóa 1 chỉ tieu")
        ten = input("Nhập vào tên chỉ tiêu cần xóa: ")
        xóa(chi_tieu, ten)
    elif (yeu_cau) == 4:
        print("Sửa tên chi tiêu")
        ten = input("Nhập vào tên chi tiêu cần sửa: ")
        sua_ten(chi_tieu,ten) 
    else:
        print("Bạn nhập không đúng yêu cầu")
    y_o_n = input("Bạn muốn tiếp tục(Y/N)?: ")
    if y_o_n.upper() == "N":
        break