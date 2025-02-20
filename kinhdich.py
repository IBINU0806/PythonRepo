# Mô tả: Chương trình bói quẻ Kinh Dịch
# Nhập số phù hợp để bói quẻ
def get_number(prompt):
    while True:
        number = input(prompt)
        if number.isdigit() and int(number) > 0:
            return int(number)
        else:
            print("Invalid input! Please enter a positive number.")

# Nhập các số để bói quẻ           
the_upper_number = get_number("Please enter the upper number: ")
the_below_number = get_number("Please enter the below number: ")
the_dynamic_number = get_number("Please enter the dynamic number: ")

# Tìm phần của quẻ
def get_hexagram_part(num):
    hexagram_parts = ["Càn (☰)", "Đoài (☱)", "Ly (☲)", "Chấn (☳)",
                      "Tốn (☴)", "Khảm (☵)", "Cấn (☶)", "Khôn (☷)"]
    return hexagram_parts[(num % 8) - 1]

# Tìm phần của quẻ
the_upper_hexagram = get_hexagram_part(the_upper_number)
the_below_hexagram = get_hexagram_part(the_below_number)

# Bảng quẻ và nghĩa của quẻ
hexagram_dict = {
    ("Càn (☰)", "Càn (☰)"): (1, "Thuần Càn"),
    ("Khôn (☷)", "Khôn (☷)"): (2, "Thuần Khôn"),
    ("Khảm (☵)", "Chấn (☳)"): (3, "Thuỷ Lôi Truân"),
    ("Cấn (☶)", "Khảm (☵)"): (4, "Sơn Thuỷ Mông"),
    ("Khảm (☵)", "Càn (☰)"): (5, "Thuỷ Thiên Nhu"),
    ("Càn (☰)", "Khảm (☵)"): (6, "Thiên Thuỷ Tụng"),
    ("Khôn (☷)", "Khảm (☵)"): (7, "Địa Thuỷ Sư"),
    ("Khảm (☵)", "Khôn (☷)"): (8, "Thuỷ Địa Tỷ"),
    ("Tốn (☴)", "Càn (☰)"): (9, "Phong Thiên Tiểu Súc"),
    ("Càn (☰)", "Đoài (☱)"): (10, "Thiên Trạch Lý"),
    ("Khôn (☷)", "Càn (☰)"): (11, "Địa Thiên Thái"),
    ("Càn (☰)", "Khôn (☷)"): (12, "Thiên Địa Bĩ"),
    ("Càn (☰)", "Ly (☲)"): (13, "Thiên Hoả Đồng Nhân"),
    ("Ly (☲)", "Càn (☰)"): (14, "Hoả Thiên Đại Hữu"),
    ("Khôn (☷)", "Cấn (☶)"): (15, "Địa Sơn Khiêm"),
    ("Chấn (☳)", "Khôn (☷)"): (16, "Lôi Địa Dự"),
    ("Đoài (☱)", "Chấn (☳)"): (17, "Trạch Lôi Tuỳ"),
    ("Cấn (☶)", "Tốn (☴)"): (18, "Sơn Phong Cổ"),
    ("Khôn (☷)", "Đoài (☱)"): (19, "Địa Trạch Lâm"),
    ("Tốn (☴)", "Khôn (☷)"): (20, "Phong Địa Quan"),
    ("Ly (☲)", "Chấn (☳)"): (21, "Hoả Lôi Phệ Hạp"),
    ("Cấn (☶)", "Ly (☲)"): (22, "Sơn Hoả Bí"),
    ("Cấn (☶)", "Khôn (☷)"): (23, "Sơn Địa Bác"),
    ("Khôn (☷)", "Chấn (☳)"): (24, "Địa Lôi Phục"),
    ("Càn (☰)", "Chấn (☳)"): (25, "Thiên Lôi Vô Vọng"),
    ("Cấn (☶)", "Càn (☰)"): (26, "Sơn Thiên Đại Súc"),
    ("Cấn (☶)", "Chấn (☳)"): (27, "Sơn Lôi Di"),
    ("Đoài (☱)", "Tốn (☴)"): (28, "Trạch Phong Đại Quá"),
    ("Khảm (☵)", "Khảm (☵)"): (29, "Thuần Khảm"),
    ("Ly (☲)", "Ly (☲)"): (30, "Thuần Ly"),
    ("Đoài (☱)", "Cấn (☶)"): (31, "Trạch Sơn Hàm"),
    ("Chấn (☳)", "Tốn (☴)"): (32, "Lôi Phong Hằng"),
    ("Càn (☰)", "Cấn (☶)"): (33, "Thiên Sơn Độn"),
    ("Càn (☰)", "Chấn (☳)"): (34, "Thiên Lôi Đại Tráng"),
    ("Ly (☲)", "Khôn (☷)"): (35, "Hoả Địa Tấn"),
    ("Khôn (☷)", "Ly (☲)"): (36, "Địa Hoả Minh Di"),
    ("Tốn (☴)", "Ly (☲)"): (37, "Phong Hoả Gia Nhân"),
    ("Ly (☲)", "Đoài (☱)"): (38, "Hoả Trạch Khuê"),
    ("Khảm (☵)", "Cấn (☶)"): (39, "Thuỷ Sơn Kiển"),
    ("Chấn (☳)", "Khảm (☵)"): (40, "Lôi Thuỷ Giải"),
    ("Cấn (☶)", "Đoài (☱)"): (41, "Sơn Trạch Tổn"),
    ("Tốn (☴)", "Chấn (☳)"): (42, "Phong Lôi Ích"),
    ("Đoài (☱)", "Càn (☰)"): (43, "Trạch Thiên Quải"),
    ("Càn (☰)", "Tốn (☴)"): (44, "Thiên Phong Cấu"),
    ("Đoài (☱)", "Khôn (☷)"): (45, "Trạch Địa Tuỵ"),
    ("Khôn (☷)", "Tốn (☴)"): (46, "Địa Phong Thăng"),
    ("Đoài (☱)", "Khảm (☵)"): (47, "Trạch Thuỷ Khốn"),
    ("Khảm (☵)", "Tốn (☴)"): (48, "Thuỷ Phong Tỉnh"),
    ("Đoài (☱)", "Ly (☲)"): (49, "Trạch Hoả Cách"),
    ("Ly (☲)", "Tốn (☴)"): (50, "Hoả Phong Đỉnh"),
    ("Chấn (☳)", "Chấn (☳)"): (51, "Thuần Chấn"),
    ("Cấn (☶)", "Cấn (☶)"): (52, "Thuần Cấn"),
    ("Tốn (☴)", "Cấn (☶)"): (53, "Phong Sơn Tiệm"),
    ("Chấn (☳)", "Đoài (☱)"): (54, "Lôi Trạch Quy Muội"),
    ("Chấn (☳)", "Ly (☲)"): (55, "Lôi Hoả Phong"),
    ("Ly (☲)", "Cấn (☶)"): (56, "Hoả Sơn Lữ"),
    ("Tốn (☴)", "Tốn (☴)"): (57, "Thuần Tốn"),
    ("Đoài (☱)", "Đoài (☱)"): (58, "Thuần Đoài"),
    ("Tốn (☴)", "Khảm (☵)"): (59, "Phong Thuỷ Hoán"),
    ("Khảm (☵)", "Đoài (☱)"): (60, "Thuỷ Trạch Tiết"),
    ("Tốn (☴)", "Đoài (☱)"): (61, "Phong Trạch Trung Phu"),
    ("Chấn (☳)", "Cấn (☶)"): (62, "Lôi Sơn Tiểu Quá"),
    ("Khảm (☵)", "Ly (☲)"): (63, "Thuỷ Hoả Ký Tế"),
    ("Ly (☲)", "Khảm (☵)"): (64, "Hoả Thuỷ Vị Tế"),
}

# In kết quả quẻ chủ
print(f"Thượng quái: {the_upper_hexagram}")
print(f"Hạ quái: {the_below_hexagram}")
main_hexagram = hexagram_dict.get((the_upper_hexagram, the_below_hexagram), ("?", "Không tìm thấy"))
print(f"Quẻ chủ: {main_hexagram[0]}. {main_hexagram[1]}")

# Mã nhị phân của các quẻ
bagua_binary = {
    "Càn (☰)": "111", "Đoài (☱)": "011", "Ly (☲)": "101", "Chấn (☳)": "011",
    "Tốn (☴)": "110", "Khảm (☵)": "010", "Cấn (☶)": "100", "Khôn (☷)": "000"
}

# Tách main_hexagram thành upper_binary và below_binary
upper_binary = bagua_binary[the_upper_hexagram]
below_binary = bagua_binary[the_below_hexagram]
main_binary = upper_binary + below_binary

# Tách main_binary thành upper_support và below_support
upper_support = main_binary[1:4]
below_support = main_binary[2:5]
main_support_binary = upper_support + below_support

# Chuyển từ mã nhị phân về tên quẻ
def binary_to_bagua(binary_code):
    for name, code in bagua_binary.items():
        if code == binary_code:
            return name
    return "Không tìm thấy"

# Chuyển upper_support và below_support thành chữ + kí hiệu
upper_support_name = binary_to_bagua(upper_support)
below_support_name = binary_to_bagua(below_support)

# Tìm quẻ hỗ trong bảng hexagram_dict
support_hexagram = hexagram_dict.get((upper_support_name, below_support_name), ("?", "Không tìm thấy"))

# In kết quả quẻ hỗ
print(f"Thượng quái hỗ: {upper_support_name}")
print(f"Hạ quái hỗ: {below_support_name}")
print(f"Quẻ hỗ: {support_hexagram[0]}. {support_hexagram[1]}")

# Chuyển main_binary thành một danh sách để dễ dàng thay đổi hào động
main_binary_list = list(main_binary)

# Xác định vị trí hào động (đếm từ dưới lên, nhưng Python index từ 0)
dynamic_index = 6 - ((the_dynamic_number - 1) % 6 + 1)  # Chuyển hào động thành index đúng trong Python

# Đảo bit tại vị trí hào động
main_binary_list[dynamic_index] = "1" if main_binary_list[dynamic_index] == "0" else "0"

# Cập nhật lại mã nhị phân sau khi thay đổi
changed_binary = "".join(main_binary_list)

# Chia lại thành thượng quái và hạ quái sau khi biến đổi
changed_upper_binary = changed_binary[:3]  # 3 bit đầu là Thượng quái
changed_below_binary = changed_binary[3:]  # 3 bit cuối là Hạ quái

# Chuyển từ nhị phân về tên quái
changed_upper_name = binary_to_bagua(changed_upper_binary)
changed_below_name = binary_to_bagua(changed_below_binary)

# Tìm quẻ biến trong hexagram_dict
changed_hexagram = hexagram_dict.get((changed_upper_name, changed_below_name), ("?", "Không tìm thấy"))

# In kết quả quẻ biến
print(f"Thượng quái biến: {changed_upper_name}")
print(f"Hạ quái biến: {changed_below_name}")
print(f"Quẻ biến: {changed_hexagram[0]}. {changed_hexagram[1]}")