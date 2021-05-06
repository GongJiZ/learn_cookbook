class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Programer(object):

    def __new__(cls, *args, **kwargs):
        print('call __new__ method')
        print(args)
        return super(Programer, cls).__new__(cls)

    def __init__(self, name, age):
        print('call __init__ method')
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('GONGJ', 23)
    programer = Programer('GONGJ', 23)
    print(programer.__dict__)
