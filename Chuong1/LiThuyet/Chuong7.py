#Chuỗi ghi trong ' ' hoặc " "
#VD: str1="Thanh Hoai"

#\': 
#\":
#\t: tạo một khoảng cách trong chuỗi
#\n: xuống dòng
#\\: ngắt 2 chuỗi

#print(r"Hello!\Hi") --> Hello!\Hi (sử dụng r để giữ lại 
# kí tự ĐB)

#''': Dùng cặp dấu nháy đơn 3 để gõ chuỗi nhiều dòng

#TOÁN TỬ

##upper(): viết hoa
##spam="Hello Word" - spam=spam.upper() --> HELLO WORD
##lower(): viết thường
##spam="Hello Word" - spam=spam.lower() --> hello word

##isupper(): trả về TRUE nếu viết hoa toàn bộ xâu
##spam="Hello Word" - spam.isupper() --> FALSE
##islower(): trả về TRUE nếu viết thường toàn bộ xâu
##spam="Hello Word" - spam.islower() --> FALSE

##isalpha(): trả về TRUE nếu chỉ chứa CHỮ CÁI và 
# KHÔNG KHOẢNG CÁCH

##isnumeric() / isdecimail(): trả về TRUE nếu chỉ chứa CHỮ SỐ
# và KHÔNG KHOẢNG CÁCH

##isalnum(): trả về TRUE nếu chỉ chứ SỐ và CHỮ (KHÔNG CÓ KC)

##isspace(): trả về TRUE nếu chỉ chứa KHOẢNG CÁCH

##istitle(): trả về TRUE nếu viết hoa MỖI CHỮ ĐẦU 

##startswith(str): trả về TRUE nếu chuỗi bắt đầu bằng chuỗi str
##endswith(str): trả về TRUE nếu chuỗi kết thúc bằng chuỗi str

##join(): nối các phần tử trong LIST bằng 1 chuỗi tương ứng
##', '.join(['cats','rats','bats']) --> 'cats, rats, bats'

##split(): tách mỗi từ thành một LIST
##'My name is Hoai',split() --> ['My','name','is','Hoai']

## rjust(n,ch): (bên phải) trả về chuỗi mới và thêm các ký tự
# "ch" sao cho chiều dài của chuỗi bằng n ký tự 
##Ví dụ: 'Hello'.rjust(10, '*') --> '*****Hello'

## ljust(n,ch): (bên trái) trả về chuỗi mới và thêm các ký tự
# "ch" sao cho chiều dài của chuỗi bằng n ký tự 
##Ví dụ: 'Hello'.ljust(10, '*') --> 'Hello*****'

## center (n,ch): (ở giữa) trả về chuỗi mới và thêm các ký tự
# "ch" sao cho chiều dài của chuỗi bằng n ký tự 
##Ví dụ: 'Hello'.center(10, '*') --> '**Hello***'

## strip(str): Xóa ký tự trắng ở 2 đầu chuỗi
## spam = ' Hello Word  ' --> spam.strip() --> 'Hello Word'

## lstrip(str): Xóa ký tự trắng bên trái chuỗi
## spam = ' Hello Word  ' --> spam.lstrip() --> 'Hello Word '

## rstrip(str): Xóa ký tự trắng bên phải chuỗi
## spam = ' Hello Word  ' --> spam.rstrip() --> ' Hello Word'

##find(str,n): tìm chuỗi str trong chuỗi gốc, bắt đầu từ số
#chỉ mục n (n trống thì n=0)
#Kết quả trả về vị trí lần đầu được tìm thấy từ trái -> phải.
#Nếu không tìm thấy thì trả về -1
## a=banana
## a.find('a') -> 1

##replace(giá trị cũ, giá trị mới, n): tìm và thay thế các 
# chuỗi giá trị cũ trong chuỗi gốc bằng giá trị mới, với n
#lần tìm và thay thế. Nếu n=0 mặc định là tất cả lần