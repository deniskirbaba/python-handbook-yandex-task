class GreetingFormal():

    def __init__(self):
        self.formal_greeting = 'Good afternoon,'

    def greet_formal(self, name):
        return f'{self.formal_greeting} {name}!'
    

class GreetingInformal():

    def __init__(self):
        self.informal_gretting = 'Hello,'

    def greet_informal(self, name):
        return f'{self.informal_gretting} {name}!'
    

class GreetingMix(GreetingFormal, GreetingInformal):

    def __init__(self):
        GreetingFormal.__init__(self)
        GreetingInformal.__init__(self)


mixed_greeting = GreetingMix()
print(mixed_greeting.greet_formal("User"))
print(mixed_greeting.greet_informal("User"))
