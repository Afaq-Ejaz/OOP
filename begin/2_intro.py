class User:
    def __init__(self, username , email , password) -> None:
        self.username = username
        "We can make the methods Private using underscore , like self._"
        self._email = email # method is protected
        self.password = password
    
    def sayhi(self , user):
        print(f"Sending message to {user.username} : Hi , {user.username} , it is {self.username} ")
    

user1 = User("Eugene" , "UG@xyz" , "Lahore")

