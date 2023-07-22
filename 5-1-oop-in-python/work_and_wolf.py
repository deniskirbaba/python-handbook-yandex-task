class Programmer():

    pos_info = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.hours = 0
        self.wage = Programmer.pos_info[pos]
        self.total = 0

    def work(self, time):
        self.hours += time
        self.total += self.wage * time

    def rise(self):
        match self.pos:
            case 'Junior':
                self.pos = 'Middle'
                self.wage = Programmer.pos_info[self.pos]
            case 'Middle':
                self.pos = 'Senior'
                self.wage = Programmer.pos_info[self.pos]
            case 'Senior':
                self.wage += 1
    
    def info(self):
        return f'{self.name} {self.hours}ч. {self.total}тгр.'


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
