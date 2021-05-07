class Programer(object):

    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('Age type must be int')

    def __repr__(self):
        return f'{self.name} is {self.age} years old'

    def __dir__(self):
        return self.__dict__.keys()


if __name__ == '__main__':
    p = Programer('GONGJ', 22)
    print(p)
    print(dir(p))
