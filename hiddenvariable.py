class User:
    #hidden to variable
    __Password = 125
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def getPassword(self):
        print(self.__Password)


obj = User("jaanvi", "Jammy", "jkala")

print(obj.username) 

#print(obj.__Password)

obj.getPassword()