# Hệ Thống Quản Lý Kho Hàng & Doanh Thu (TechStore Inventory)

inventory_stock = 100
total_revenue = 0.0

menu = """
========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================
"""


def add_stock(amount):
    global inventory_stock

    print(f"Đã nhập thành công {amount} sản phẩm.")
    inventory_stock += amount
    print(f"Tồn kho hiện tại: {inventory_stock}")


def process_sale(quantity):
    global inventory_stock

    if quantity > inventory_stock:
        print(
            f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}"
        )
        return False

    return True


def calculate_final_price(quantity, price):
    global inventory_stock, total_revenue

    discount = 0

    total_temp = quantity * price

    if total_temp >= 1000:
        discount = total_temp * 0.1

    vat = (total_temp - discount) * 0.08

    final_total = total_temp - discount + vat

    inventory_stock -= quantity

    total_revenue += final_total

    bill = f"""
-> Hóa đơn chi tiết:
Số lượng: {quantity} | Đơn giá: ${price:.2f}
Tạm tính: ${total_temp:.2f}
Giảm giá (10%): ${discount:.2f}
Thuế VAT (8%): ${vat:.2f}
Tổng thanh toán: ${final_total:.2f}
Đã bán thành công!
"""

    print(bill)


def print_report():
    global inventory_stock, total_revenue

    report = f"""
--- BÁO CÁO KINH DOANH ---
Tồn kho hiện tại: {inventory_stock} sản phẩm
Tổng doanh thu: ${total_revenue:.2f}
"""

    print(report)


while True:
    print(menu)

    # Kiểm tra nhập menu
    try:
        select = int(input("Chọn chức năng (1-4): "))

        if select < 1 or select > 4:
            print("Lỗi: Chỉ được chọn từ 1 đến 4!")
            continue

    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên từ 1 đến 4!")
        continue

    if select == 1:
        print("--- NHẬP HÀNG ---")

        try:
            amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))

            if amount <= 0:
                print("Lỗi: Số lượng nhập kho phải lớn hơn 0!")
                continue

            add_stock(amount)

        except ValueError:
            print("Lỗi: Số lượng phải là số nguyên!")
            continue

    elif select == 2:
        print("--- BÁN HÀNG ---")

        try:
            quantity = int(input("Nhập số lượng mua: "))

            if quantity <= 0:
                print("Lỗi: Số lượng mua phải lớn hơn 0!")
                continue

            price = float(input("Nhập đơn giá ($): "))

            if price <= 0:
                print("Lỗi: Đơn giá phải lớn hơn 0!")
                continue

            if process_sale(quantity):
                calculate_final_price(quantity, price)

        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng số!")
            continue

    elif select == 3:
        print_report()

    elif select == 4:
        print("Thoát chương trình thành công!")
        break