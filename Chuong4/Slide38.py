def spam(divideby):
    try:
        result = 42 / divideby
    except: #0 chạy được
        print("Sorry ! You are dividing by zero ")
    else:   #nếu chạy được
        print("Yeah ! Your answer is :",result)

print(spam(1))
print(spam(0))