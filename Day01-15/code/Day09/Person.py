class Person():
    
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def add_property(self,pro):
        self._pro = pro
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value
    
    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行器' % self._name)
        else:
            print('%s正在玩斗地主' % self._name)

def main():
    person = Person('yann', 12)
    person.play()
    person.age = 18
    # person._name = 'qu' # 也可以直接访问该属性。毕竟不是真正的私有
    person.play()
    person.add_property(123)

if __name__ == '__main__':
    main()