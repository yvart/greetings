print("Hello, Noella!")
print("Welcome to the Python scripting world.")

class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}! Nice to meet you."

if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    greeter = Greeter(user_name)
    print(greeter.greet())

    