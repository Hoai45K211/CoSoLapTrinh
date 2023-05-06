#bai1
# n=input()
# h=t=s=k=0
# for i in n:
#     if i.isupper():
#         h+=1
#     elif i.islower():
#         t+=1
#     elif i.isnumeric():
#         s+=1
#     else:
#         k+=1
# print('In hoa:',h,'\nIn thuong:',t,'\nChu so:',s,'\nKhac:',k)



#bai 2
# n=input()
# n=n.strip()
# a=n[0].upper()+n[1:].lower()
# a=a.split()
# n=''
# for i in a:
#     if i==',' or i==':' or i==';' or i=='.':
#         n=n.strip()+i+' '
#     else: n=n+i+' '
# print(n.strip())

#cach2
# import re
# n=input()
# n=' '.join(n.split())
# n=n[0].upper()+n[1:].lower()
# a=re.search('[.,:;]',n).group()
# i=n.find(a)
# if n[i-1]==' ':
#     n=n[:i-1]+n[i:]
# print(n)



#bai 3
# n=input()
# x=0
# if len(n)<6 or len(n)>17 or n.islower() or n.isupper() or n.isalnum():
#         print(False)
# else:
#     for i in n:
#         if i=='$' or i=='#' or i=='@':
#                 x=1
#                 break
#     if x==1:
#         print(True)
#     else: print(False)
#cach 2
# import re
# n=input()
# k=re.search('[a-z]',n)
# i=re.search('[0-9]',n)
# m=re.search('[A-Z]',n)
# a=re.search('[$#@]',n)
# if k!=None and i!=None and m!=None and a!=None and len(n)>=6 and len(n)<=17:
#     print(True)
# else: print(False)


#bai 4
# n=input()
# n=n.split(',')
# m=[]
# for i in n:
#     if i not in m:
#         m=m+[i]
# m.sort()
# print(','.join(m))


#bai 5
# n=input()
# n=n.split()
# X=int(input())
# x=[]
# for i in range(len(n)):
#     if int(n[i])==X:
#         x=x+[i+1]
# if x==[]:
#     print(0)
# else:
#     for i in x:
#         print(i)


#bai 6
# n=input()
# n=n.split(',')
# m=[]
# for i in n:
#     if int(i,2)%3==0:
#         m=m+[i]
# print(','.join(m))


#bai 7
# n=input()
# n=n.split()
# if n[-1]!='Email:':
#     print(n[-1])
# else:print('')   
   



# st1=input('st1=')
# st2=input('st2=')
# st3=input('st3=')
# def checkstring(st1,st2,st3):
#     if st1.startswith(st2) or st1.endswith(st3):
#         print(True)
#     else: print(False)
# checkstring(st1,st2,st3)



# st='''--Người---đâu-gặp---gỡ-làm-chi---
# Trăm----năm-biết-có---duyên---gì--hay--không.
# Ngổn-ngang---trăm-mối---bên---lòng----
# ----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''
# while '-' in st:
#     st=st.split('-')
# l=' '.join(st)
# l=l.split()
# for i in l:
#     if i.istitle():
#         print('\n',i,end=' ')
#     else: print(i,end=' ')



#l=[]
#cach1
# for i in range(4):
#     a=input('Mon: ')
#     b=input('So luong: ')
#     l=l+[a]+[b]
#cach2
# for i in range(4):
#     a,b=[i for i in input().split()]
#     l=l+[a]+[b]



# for i in range(0,len(l),2):
#     print(l[i].ljust(20,'.'),l[i+1].rjust(10),sep='')



# data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# atpos=data.find('@')
# sppos=data.find(' ',atpos)
# host=data[atpos+1:sppos]
# print(host)

# st1=input('st1=')
# st2=input('st2=')
# st3=input('st3=')
# print('Vi tri xuat hien st2:',st1.find(st2))
# print('Xau ket qua:',st1.replace(st2,st3))



# st1='''Người---đâu-gặp---gỡ-làm-chi---
# Trăm----năm-biết-có---duyên---gì--hay--không.
# Ngổn-ngang---trăm-mối---bên---lòng----
# ----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''
 
# L=st1.split("\n")
# for i in range(len(L)):
#     s=' '.join(L[i].split("-"))
#     s=' '.join(s.split())
#     print(s)




# n=input()
# a=input()
# n=n.split()
# b=[]
# for i in n:
#     b=b+[a]+[i]
# print(b)


# n=input()
# a=input()
# b=[]
# a=a.split()
# n=n.split()
# for i in n:
#     if i in a:
#         b=b+[i]
# print(b)


n=input()
n=n.split()