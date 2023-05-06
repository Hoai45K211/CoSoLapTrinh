#Viết một hàm có tên priority trả về một số nguyên đại diện cho
#giá trị của một toán tử toán học. Một chuỗi chứa toán tử sẽ được chuyển đến
#chức năng như là tham số duy nhất của nó. Hàm của bạn sẽ trả về 1 cho + và -, 2 cho *
#và /, và 3 cho ˆ. Nếu chuỗi được truyền cho hàm không phải là một trong những toán tử này
#thì hàm sẽ trả về -1. Bao gồm một chương trình chính đọc toán tử
#từ người dùng và hiển thị quyền ưu tiên của người vận hành hoặc chỉ báo lỗi
#thông báo rằng đầu vào không phải là toán tử. Chương trình chính của bạn chỉ nên chạy khi
#tệp chứa giải pháp của bạn chưa được nhập vào chương trình khác.
#Trong bài tập này, cùng với những bài tập khác xuất hiện ở phần sau của cuốn sách, chúng ta sẽ sử dụng ˆ để
#biểu diễn lũy thừa. Sử dụng ˆ thay vì lựa chọn ** của Python sẽ khiến
#những bài tập này dễ dàng hơn vì toán tử sẽ luôn là một ký tự đơn.


def precedence(operator):
    if operator=='+' or operator=='-':
        op=1
    elif operator=='*' or operator == "/":
        op=2
    elif operator=='^':
        op=3
    else:
        op=('-1.This is not an operator!')
    return op
def main():
    operator=input('Enter the operator:')
    print('The precedence is',precedence(operator))
main()