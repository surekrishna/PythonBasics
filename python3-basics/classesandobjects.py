# Creating empty class
class Snake:
    pass

snake = Snake()
print(snake)
print('--------------------------------------------')
# Creating class with attribute 
class Snake1:
    name = 'python'

snake1 = Snake1()
print(snake1.name)
print('--------------------------------------------')
class Snake2:
    name = 'python'

    def change_name(self, new_name):
        self.name = new_name

snake2 = Snake2()
print(snake2.name)
snake2.change_name('anakonda')
print(snake2.name)
print('--------------------------------------------')
# Instance attributes
class Snake3:
    def __init__(self, name):
        self.name = name

python = Snake3('python')
anakonda = Snake3('anakonda')
print(python.name)
print(anakonda.name)
