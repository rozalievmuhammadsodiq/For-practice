# 1
# def k(n: int):
#     return n ** 2
# numbers = [1,2,3,4,5,6,7,8,9,10]
# result = map(k,numbers)
# print(list(result))


# 2
# def A(a: str):
#     if a.istitle():
#         return a
# a = ["A", "a", "B", "b", "C", "c", "D", "d"]
# c = filter(A,a)
# print(list(c))


# 3
# def number(num: str):
#     if num.startswith("+998"):
#         return f"Uzbekis {num}"
#     elif num.startswith("+7"):
#         return f"Russia {num}"
#     elif num.startswith("+14"):
#         return f"America {num}"
# phone_numbers = ["+998991234567", "+79454874459", "+14385001031"]
# res = map(number,phone_numbers)
# print(list(res))


# 4
# def Strat_big(s: str):
#     return s.title()
# names = ['alfred', 'tabitha', 'william', 'arla']
# rres = map(Strat_big, names)
# print(list(rres))

# 5
# def Than_75_big_numbers(n: int):
#     if n >= 75:
#         return n
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# s = filter(Than_75_big_numbers, scores)
# print(list(s))


# 6
# def palindrom(a: str):
#     if a.lower() == a[::-1].lower():
#         return a
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# s = filter(palindrom, words)
# print(list(s))


# 7
# def lenn(l: str):
#     return len(l)
# s = ("Muhammadsodiq","Abdulloh","Abubakir")
# res = map(lenn, s)
# print(list(res))

# 8
# def s(a,s):
#     return a + s
# d = ['apple', 'banana', 'cherry']
# c = ['orange', 'lemon', 'pineapple']
# v = map(s,d,c)
# print(list(v))

# 9
# def Listt(a, b):
#     return a + b
# s =  ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# c = [" Sobir", " Bakir", " Jalil", " Toxir"]
# v = map(Listt, s, c)
# print(list(v))


# 10
# def lis(lst: list, element):
#     return lst.count(element)
#
# c = ["1", "2", "3", "1"]
# unique_elements = set(c)
# res = map(lambda element: (element, lis(c, element)), unique_elements)
# for element, count in res:
#     print(f"Element '{element}' ro'yxatda {count} marotaba takrorlanadi.")


# 11
# def s(a,b):
#     return a + b
# c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# res = map(s,c,v)
# print(list(res))


# 12
# def s(a: str):
#     if len(a) % 2 == 1:
#         return a
#
# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# res = filter(s,programming_languages)
# print(list(res))

# 13
# def python(a: str):
#     return a
# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# start = programming_languages.index("Basic")
# result = programming_languages[start:]
# res = map(python,result)
# print(list(res))


# 14
# from collections import namedtuple
# Talaba = namedtuple("Talaba",["Name","Team","Grade"])
# talabalr = [
#     Talaba(Name="Muhammadsodiq",Team="Unity",Grade=5),
#     Talaba(Name="Muhammadziyo",Team="Unity", Grade=6),
#     Talaba(Name="Ibrohimjon",Team="Unity",Grade=5)
# ]
# s = max(talabalr)
# print(f"Eng kotta va ortachasi {s} ")

# 15
# def generator():
#     for i in range(1,20+1):
#         s = i ** 2
#         yield s
# for i in generator():
#     print(i)



# 16
# def s():
#     def inner(matin):
#         return len(matin)
#     return inner
# c = s()
# print(c("Alisher"))


# 17
# def s():
#     def inner(a):
#         return f"Assalomu alekum {a}"
#     return inner
# c = s()
# print(c("Muhammadsodiq"))