grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]

def display_grades(book):
    print("\n--- BẢNG ĐIỂM HỌC SINH ---")
    print(f"{'Mã SV':<6}| {'Tên Học Sinh':<20}| {'Điểm Toán':<10}| {'Điểm Anh':<10}| {'ĐTB':<5}")
    print("-" * 70)
    for student in book:
        math, eng = student["info"]
        avg = (math + eng) / 2
        print(f"{student['id']:<6}| {student['name']:<20}| {math:<10}| {eng:<10}| {avg:<5.2f}")
    print("-" * 70)

def add_student(book):
    while True:
        new_id = input("Nhập mã học sinh mới: ").strip()
        if any(s["id"] == new_id for s in book):
            print(f"Lỗi: Mã học sinh {new_id} đã tồn tại! Vui lòng nhập mã khác.")
        else:
            break
    new_name = input("Nhập tên học sinh: ").strip()
    math_score = float(input("Nhập điểm Toán: "))
    eng_score = float(input("Nhập điểm Anh: "))
    book.append({"id": new_id, "name": new_name, "info": (math_score, eng_score)})
    print(f"Thành công: Đã thêm học sinh {new_id} vào hệ thống!")

def update_scores(book):
    student_id = input("Nhập mã học sinh cần cập nhật: ").strip()
    for student in book:
        if student["id"] == student_id:
            math_score = float(input("Nhập điểm Toán mới: "))
            eng_score = float(input("Nhập điểm Anh mới: "))
            student["info"] = (math_score, eng_score)
            print(f"Thành công: Đã cập nhật điểm cho học sinh {student_id}!")
            return
    print(f"Lỗi: Không tìm thấy học sinh có mã {student_id}!")

def delete_student(book):
    student_id = input("Nhập mã học sinh cần xóa: ").strip()
    for student in book:
        if student["id"] == student_id:
            book.remove(student)
            print(f"Thành công: Đã xóa hồ sơ học sinh {student_id} khỏi hệ thống!")
            return
    print(f"Lỗi: Không tìm thấy học sinh có mã {student_id}!")

def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===")
        print("1. Xem bảng điểm học sinh")
        print("2. Thêm hồ sơ học sinh mới")
        print("3. Cập nhật điểm số")
        print("4. Xóa hồ sơ học sinh")
        print("5. Thoát chương trình")
        print("================================")
        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            display_grades(grade_book)
        elif choice == "2":
            add_student(grade_book)
        elif choice == "3":
            update_scores(grade_book)
        elif choice == "4":
            delete_student(grade_book)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập từ 1 đến 5.")

main()
