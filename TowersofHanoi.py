from node import Node
from stacks import Stack

print("\nLet's play Towers of Hanoi!!\n::Your goal:: \nMove the stack of disks from the leftmost stack to the rightmost stack.")
print("\n::Rules::")
print("1) Only one disk can be moved at a time.")
print("2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.")
print("3) No disk may be placed on top of a smaller disk.\n")
#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)


#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disks in range(num_disks, 0, -1):
  left_stack.push(disks)

num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {moves} moves".format(moves = num_optimal_moves)) 
#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {L} for {N}.".format(L = letter, N = name))
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]

#Rules for the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  left_stack.print_items()
  middle_stack.print_items()
  right_stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again.")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again.")   
print("\n\nYou completed the game in {move} moves, and the optimal number of moves is {opt}".format(move = num_user_moves, opt = num_optimal_moves))