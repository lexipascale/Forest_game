print('Once upon a time...')

class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  #adds interactive choices
  def add_child(self, node):
    self.choices.append(node)

  #allows user to go through the story
  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    #loop will run as long as story_node.choices is not empty
    while len(story_node.choices) > 0:
      choice = input('Enter 1 or 2 to continue... ')
      #checks for valid response
      if choice not in ['1', '2']:
        print('Not a valid response... ')
      else:
        chosen_index = int(choice)
        #set indexes of choices 1 and 2 to 0 and 1
        chosen_index -= 1
        chosen_child = story_node.choices[chosen_index]
        print(chosen_child.story_piece)
        story_node = chosen_child


story_root = TreeNode('''
Your story begins at a forest clearing. You take a path to the left.
All of a sudden a bear emerges from the trees and roars!
Do you: 
1) Roar back!
2) Run away!...
''')
choice_a = TreeNode('''
The bear is startled and runs away.
Do you:
1) Shout 'Sorry bear!'
2) Yell 'Hooray!'
''')

choice_b = TreeNode('''
You come across a clearing full of flowers. 
The bear follows1 you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
''')


story_root.story_piece
story_root.add_child(choice_a)
story_root.add_child(choice_b)


choice_a_1 = TreeNode('''
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS!!!
''')

choice_a_2 = TreeNode('''
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.
 
YOU REMAIN LOST!!!
''')

choice_b_1 = TreeNode ('''
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
 
YOU REMAIN LOST.
''')

choice_b_2 = TreeNode ('''
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
''')

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
story_root.traverse()
