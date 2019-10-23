class Greet:
    def __init__(self):
        self.msg = "Hello"

    def greet(self):
        print(self.msg)


g = Greet()
g.greet()

class BetterGreet:
    def __init__(self, msg):
        self.msg = msg

    def say(self):
        return self.prefix() + self.msg

    def prefix(self):
        return "Message: "

bg = BetterGreet("Hey!")
print(bg.say())
