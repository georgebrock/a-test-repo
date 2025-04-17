class Hello:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f'Hello, {self.name}')
