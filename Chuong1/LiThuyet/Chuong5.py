#SỐ CHỈ MỤC:
#Số 0: Chỉ phần tử đầu tiên
#Số -1: Chỉ phần tử áp cuối

#spam[1:4]: Lấy từ phần tử 1 đến 3
#spam[:2]: Lấy từ 0 đến 2
#spam [1:]: Lấy từ 1 đến cuối List
#spam [:]: Lấy toàn bộ List

#List có thể thực hiện toán tử + / *

#in / in not: KIỂM TRA PHẦN TỬ TRONG LIST
#myPets = ['Zophie', 'Pooka', 'Fat-tail']
#print('Enter a pet name:')
#name = input()
#if name not in myPets:
#print('I do not have a pet named ' + name)
#else:
#print(name + ' is my pet.')

#len(): KIỂM TRA CHIỀU DÀI CỦA LIST
#spam=[1,2,3]
#len(spam) --> Output: 3

#TRẢ VỀ PHẨN TỪ LỚN/ NHỎ NHẤT TRONG LIST
#numbers = [5, 3, 8, 2, 9]
#print(max(numbers)) --> 9
#print(min(numbers)) --> 3

#XÓA PHẦN TỬ TRONG LIST
#spam=[1,2,3,4,5]
#del(spam[2])
#print(spam)  --> [1,2,4,5]
#del(spam[1])
#print(spam)  --> [1,4,5]

#CÁC PHƯƠNG THỨC CỦA LIST:

##index(x): Trả về số chỉ mục của phần tử cần tìm
##L=[1,2,3]
##print(L.index(2)) --> 3

##append(x): Thêm phần tử x vào cuối LIST
##insert(i,x): Chèn x vào vị trí có số chỉ mục i trong LIST

##remove(x): Xóa phần tử x đầu tin tìm thấy trong LIST
##del(): Xóa 1PT khi biết index // remove(): Biết giá trị

##sort(): Sắp xếp các PT trong LIST
##sort(reverse=True): SX giảm dần

##reverse(): Thực hiện đảo ngược thứ tự các phần tử trong LIST

##clear(): Xóa tất cả các phần tử trong LIST

##count(x): Đếm số phần tử x xuất hiện trong LIST

##copy(): Tạo ra một bản sao mới

##pop(i): Xóa và lấy ra giá trị của phần tử có số chỉ mục i
##Nếu i để trống thì mặc định là lấy phần tử cuối.abs