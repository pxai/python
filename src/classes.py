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


class ChildGreet(Greet):
    def childish(self):
        print("Hey mummy, ", self.msg)

cg = ChildGreet()
cg.childish()


class ChildGreetOverride(BetterGreet):
    def __init__(self, msg):
        self.msg = "Look ma: " + msg

    def prefix(self):
        return "Child Message: "

cgo = ChildGreetOverride("I love you")
print(cgo.say())
