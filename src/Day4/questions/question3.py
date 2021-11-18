"""
Exercise: Add Fish Class
Add a Fish class that inherits from the Animal class so that the code below produces the given output.

```
→
I'm a Tuna
I'm swimming
I'm a Guppy
I'm swimming
```
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("I'm a", self.name)


# ADD YOUR CODE HERE
if __name__ == '__main__':
    tuna = Fish('Tuna')
    tuna.info()
    tuna.move()
    guppy = Fish('Guppy')
    guppy.info()
    guppy.move()
