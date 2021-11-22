# 2 Напишите функцию, которая проверяет: является ли слово палиндромом:
def is_palindrome(word):
    return word[::-1] == word


while True:
    w = input("Input the word for check for palindrome : \n")
    print(f"{w} - this word is a palindrome!" if is_palindrome(w) else "this word isn`t a palindrome")