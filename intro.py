


#print('My name is Ryan')

'''def namelen(name):
    nchars = len(name)
    print('My name is Ryan')
    return nchars

nchars = namelen('Ryan')
print(nchars)'''

class person:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def introduction(self):
        print("My name is "f"{self.name}"
              f" and I am {self.age}  "
              f"years old and work as a {self.occupation}")


Ryan = person("Ryan",27,"MRI Physicist")
Ryan.introduction()