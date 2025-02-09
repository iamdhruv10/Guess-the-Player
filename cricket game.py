from Dictionary import players
import random

score = 0
running = True

while running:
    random_player = random.choice(list(players.keys()))
    stats = players[random_player]
    print(stats)
    player_guess = input('Who is this player?')
    if player_guess == random_player:
        print('You are correct')
        score += 1
        players.pop(random_player)
    else:
        print(player_guess +" is incorrect. The correct answer was " + random_player)
        running = False

print('Your final score is '+ str(score))
