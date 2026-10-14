diem = float(input("Nhập điểm trung bình: "))
if diem < 0 or diem > 10:
    print("Điểm không hợp lệ")
elif diem >= 9.0:
    print("Xếp loại Xuất sắc")
elif diem >= 8.0:
    print("Xếp loại Giỏi")
elif diem >= 7.0:
    print("Xếp loại Khá")
elif diem >= 5.0:
    print("Xếp loại Trung Bình")
else:
    print("Xếp loại Yếu")
