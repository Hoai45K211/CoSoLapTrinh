def add(L, x, k):
    n = len(L)  # Số phần tử của List L
    if k > n:
        L.append(x)  # Thêm x vào cuối List L nếu k lớn hơn n
    else:
        L.insert(k, x)  # Thêm x vào vị trí k trong List L
    return L