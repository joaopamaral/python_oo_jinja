class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("I'm a", self.name)


class Fish(Animal):
    def move(self):
        print("I'm swimming")


# ADD YOUR CODE HERE
if __name__ == '__main__':
    tuna = Fish('Tuna')
    tuna.info()
    tuna.move()
    guppy = Fish('Guppy')
    guppy.info()
    guppy.move()
