company = ["валя", "аня", "лена", "таня", "ирина"]

first_guest = company[0].title() + ", приглашаю тебя на обед!"
second_guest = "Приглашаю тебя " + company[1].title() + " на обед!"
third_guest = "От всего сердца приглашаю тебя " + company[2].title() + " на обед!"
fourth_guest = company[3].title() + ", приглашаю тебя на обед!"
fifth_guest = "Дорогая " + company[-1].title() + ", приглашаю тебя на званный обед!"
print(first_guest)
print(second_guest)
print(third_guest)
print(fourth_guest)
print(fifth_guest)
print(len(company))# Подсчёт приглашённых гостей.

print(" ")

new = "ирина"
company[-1] = "павел"

first_guest = company[0].title() + ", приглашаю тебя на обед!"
second_guest = "Приглашаю тебя " + company[1].title() + " на обед!"
third_guest = "От всего сердца приглашаю тебя " + company[2].title() + " на обед!"
fourth_guest = company[3].title() + ", приглашаю тебя на обед!"
fifth_guest = "Дорогой " + company[-1].title() + ", приглашаю тебя на званный обед!"
print(first_guest)
print(second_guest)
print(third_guest)
print(fourth_guest)
print(fifth_guest)
print(new.title() + " не придет.")
print(len(company)

print(" ")

company.insert(0, "саша")
company.insert(3, "маша")
company.append("ольга")
# Только что мы добавили ещё трёх людей.
first_guest = company[1].title() + ", приглашаю тебя на обед!"
second_guest = "Приглашаю тебя " + company[2].title() + " на обед!"
third_guest = "От всего сердца приглашаю тебя " + company[4].title() + " на обед!"
fourth_guest = company[5].title() + ", приглашаю тебя на обед!"
fifth_guest = "Дорогой " + company[6].title() + ", приглашаю тебя на званный обед!"
sixth_guest = "Я хочу пригласить тебя " + company[0].title() + " на обед!"
seventh_guest = company[3].title() + ", приглашаю тебя на обед!"
eight_guests = "Я приглашаю тебя " + company[-1].title() + " на обед!"
print(first_guest)
print(second_guest)
print(third_guest)
print(fourth_guest)
print(fifth_guest)
print(sixth_guest)
print(seventh_guest)
print(eight_guests)
print("В нашу компанию добавляется: " + company[0].title() +", " + company[3].title() + " и " + company[-1].title() + ".")
print(company.__len__())

print(" ")

# Стол не привозят. Нужно удалить те имена, которые не придут на обед.
print("К сожалению приглашаются только два гостя так как стол не успевают привезти вовремя! Извените!")
# Начинаем удалять имена и отсылать им сообщения об отмене застолья.
sasha = company.pop(0)
print("Сожалею об неприглашении на обед " + sasha.title() + "!")
anya = company.pop(1)
print("Дорогая " + anya.title() + " извини, но обед отменяется!")
masha = company.pop(1)
print(masha.title() + ", обед отменяется!")
lena = "лена"
company.remove(lena)
print("Не огорчайся " + lena.title() + ", но из-за непривизённого стола обед отменяется!")
pasha = company.pop(-2)
print(pasha.title() + ", извини но назначенный обед отменяется!")
olga = company.pop(-1)
print("Извини " + olga.title() + ", но сегодня не получится по обедать!")

print(" ")

print(company[0].title() + ", для тебя обед не отменяется!")
print("Дорогая " + company[1].title() + ", мы решили не отказывать тебе в приглашении на обед!")
print("Количество приглашённых гостей: " + str(len(company)) + "!")
del company[0]
del company[0]
print(company)
