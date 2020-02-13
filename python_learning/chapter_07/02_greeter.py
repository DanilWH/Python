name = input("Please enter your name: ")
print("Hello " + name + "!")
# Необходимо делать содержательные подсказки при вводе.
# В конец подсказки нужно ставить пробел, чтобы точно показать, где должен вводиться текст.

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
# Если подсказка слишком длинная, то её можно сохронить в переменную, а затем использовать в input().
# Оператор += объединяет текст, хранящийся в prompt, с новым фрагментом текста.
