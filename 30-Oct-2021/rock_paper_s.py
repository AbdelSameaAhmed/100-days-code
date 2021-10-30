import random
def play():
    user = input(f"'r'--> Rock\n'p'--> paper\n's'--> Scissors: \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f"It's a tie"
    
    if is_win(user, computer):
        return 'you won! '
    return 'you lost'
    

def is_win(player, oponet):
    if (player=='r' and oponet=='s') or (player=='s' and oponet=='p')\
        or (player=='p' and oponet=='r'):
        return True

print(play())