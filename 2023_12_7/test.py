class Sports:
    def __init__(self,name):
        self.name=name

class Land(Sports):
    def __init__(self,name):
        super().__init__(name)

class Water(Sports):
    def __init__(self,name):
        super().__init__(name)

class Balls(Land):
    def __init__(self,name):
        super().__init__(name)

class NonBalls(Land):
    def __init__(self,name):
        super().__init__(name)

class SwimmingPool(Water):
    def __init__(self,name):
        super().__init__(name)

class Maritime(Water):
    def __init__(self,name):
        super().__init__(name)

def main():
    swimming=SwimmingPool("swimming")
    print(swimming.name)

if __name__=="__main__":
    main()