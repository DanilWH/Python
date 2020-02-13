vasilok = " cat "
vasilok.rsplit()
' cat' # rstrip() удаляет пробелы с правой стороны текста!
vasilok.lstrip()
'cat ' # lstrip() удаляет пробелы с левой стороны текста!
vasilok.strip()
'cat' # strip() удаляет пробелы с обеих сторон текста!
vasilok = vasilok.strip()
vasilok
'cat'
# Это пример удаление пропусков из книги (не работает здесь как программа, это просто для примера)


print("\tPython") # \t делает отступ от левого края, так называется "табуляция"!
      Python
print("semya:\nmama\npapa\nchigik\nme") # \т делает перенос следующего слова на следующую строку, так называется "разрыв строки"!
semya:
mama
papa
chigik
me
print("semya:\n\tmama\n\tpapa\n\tchigik\n\tme") # \n\t приказывает Python начать текст с новой строки, в начале которой распологается табуляция!
semya:
    mama
    papa
    chigik
    me
# Это примет табуляции и разрывы строк!
