sandwich_orders = ['bokadilo', 'pastrami', 'arepa', 'crok-madam', 'pastrami', 'kazu-sando', 'vada-pav', 'pastrami']
finished_sandvich = []

print("Sory, but 'pastrami' is no more.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	sandwich_order = sandwich_orders.pop()
	print("I made your " + sandwich_order + " sandwich.")

	finished_sandvich.append(sandwich_order)

for finished_sandvich in finished_sandvich:
	print(finished_sandvich)
# Упражнение 7-8 с элементам 7-9.

vacation = {}

while True:
	name = input("\nWhat is your name? ")
	place = input("Where you want to rest? ")

	vacation[name] = place

	question = input("Do you want to ask your friends? ")
	if question == 'no':
		break
print("\n---Thanks for your anwer---")
for name, place in vacation.items():
	print(name.title() + " want to rest " + place.title())
