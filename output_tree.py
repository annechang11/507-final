
from tree import tree

def play(tree):
    """Accept a tree consists of tomato variety data, 
    ask for user's preference of tomato's color and size, 
    and recommend a type of tomato to the user based on input.
    Provide the tomato variety's name, size, shape, maturity day information, as well as a link to an image of it.
    """
    if len(tree) == 2: # is leaf
        print('============')
        print(f'Based on your preference, I recommend you grow this tomato variety...')
        print(f'\n"{tree[1][0]}"')
        print(f"This {tree[1][1]['Color']}, {tree[1][1]['Size']} tomaoto has a {tree[1][1]['Shape']} shape and takes {tree[1][1]['Maturity']} days to grow.")
        print(f"{tree[1][1]['MoreInfo']}")
        print(f'Click the link to see how it looks like --> "{tree[1][2]}"')
        print('============')
        return(tree[1])
    else:
        ask_user = input(f'Do you like {tree[1][0]}, {tree[2][0]}, or {tree[3][0]} tomato?')
        if ask_user.lower() == tree[1][0].lower():
            return play(tree[1])
        if ask_user.lower() == tree[2][0].lower():
            return play(tree[2])
        if ask_user.lower() == tree[3][0].lower():
            return play(tree[3])
        else: # invalid input
            print(f'Invalid input. Please type {tree[1][0]}, {tree[2][0]}, or {tree[3][0]}.')
            return play(tree)

def yes(prompt):
    """Check if the user say yes or no
    Return True if yes. False if no. Ask again if neither yes nor no"""
    user_answer = input(prompt)
    if user_answer in ['yes','Yes','y','Y','yup','Yup','sure','Sure','Correct','correct','Right','right',"It is",'it is',"That's right","that's right","That's correct","that's correct"]:
        return True
    elif user_answer in ['No','no','not','Not','Wrong','wrong','Nah','nah', "It's not", "it's not"]:
        return False
    else:
        return yes('Invalid answer. Try again. Yes or No?')

def playAndAgain(tree):
    """Play a tree. If the user say yes to play again, recursively plan the tree. 
    Parameter
    ----------
    tree: an initial tree to be played
    Return
    ----------
    a new tree which is the result from the game
    """
    new_tree = play(tree)
    if yes('Would you like another recommendation?'): 
        new_tree = playAndAgain(tree)
    return new_tree


def main():
    """Make a tomato recommendation based on user input of tomato color and size. 
    The result will show the info of the tomato variety as well as a link to an image of it
    The user can ask for recommendation again and agin.
    """
    print('\n')
    print('Welcome to Tomato Recommender!')
    print('Tell me your preference of tomatoes, and I will recommend a tomato variety to you.')
    print('\n')
    initial_tree = tree
    output_tree = playAndAgain(initial_tree)
    print('Bye!')



if __name__ == '__main__':
    main()

