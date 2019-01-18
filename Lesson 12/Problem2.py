import time

print('-'*65)

print('Your current health is 100. ')



print()

time.sleep(1/2)
print(' ...Walking... ')
time.sleep(1/2)
print(' ...Walking... ')
time.sleep(1/2)
print(' ...Walking... ')

print()

print('You have encountered an enemy. Get ready for a fight! ')
print('-'*10)
print('Actions: ')
print('Fight ')
print('Block ')
print('Heal ')
print('-'*10)

player_hp = 100
enemy_hp = 100

while player_hp > 0 and enemy_hp > 0: 
	print()
	print('Your health: ' + str(player_hp))
	print('Enemy health: ' + str(enemy_hp))
	print()

	print('-'*65)
	action = input('Choose your next action! ')
	print('-'*65)
	if action == 'Fight':
		player_hp = player_hp - 35
		enemy_hp = enemy_hp - 30

	elif action == 'Block': 
		player_hp = player_hp - 20


	elif action == 'Heal':
		player_hp = player_hp + 15
		if player_hp > 100:
			player_hp = 100

	elif action not in ['Block', 'Fight', 'Heal']:
		print('That is not a valid action! Choose an action!')
print()

print('          You have died!       ')
print('-'* 65)



