import time
import random

print('-'*65)
print()

print('I am the Magic Eight Ball!' )
question = input('Please ask your question!: ')

print()

time.sleep(1/3)
print(' ...Shaking... ')
time.sleep(1/3)
print(' ...Shaking... ')
time.sleep(1/3)
print(' ...Shaking... ')

print()

choice = random.randint(1,6)

if choice == 1:
	print('It be like that ')
elif choice == 2:
	print('Go for it! ')
elif choice == 3:
	print('Uh, no.')
elif choice == 4:
	print('Possibly')
elif choice == 5:
	print('Are you dumb? ')
else:
	print('Ya okay' )
