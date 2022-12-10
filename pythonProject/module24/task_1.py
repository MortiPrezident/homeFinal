class MyUser:
    user_name = "Admin"
    password = "qwerty"
    is_banned = False
    frends = []

    def print_info(self):
        print(
            "name - {}\npasssword - {}\nBan status - {}".format(
                self.user_name,
                self.password,
                self.is_banned
            ))
    def add_frend(self, frend):

        if isinstance(frend, MyUser):
            self.frends.append(frend.user_name)
        else:
            self.frends.append(frend)

user_1 = MyUser()  # Экземпляр класса

user_1.user_name = 'pasha'
user_2 = MyUser()
user_2.user_name = "Katy"
user_1.print_info()
user_1.add_frend("Masha")
user_1.add_frend(user_2)

print(user_1.frends)