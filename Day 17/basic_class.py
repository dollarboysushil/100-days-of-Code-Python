class User:
    def __init__ (self , user_id, username ):
        self.id = user_id
        self.username = username
        self.default = 0


user_1 = User("001" , "angela")
user_2 = User("002" , "Jack")


print(f"Username = {user_1.username}")
print(f"Default = {user_1.default}")



