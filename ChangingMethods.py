class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email Address: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}\r")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("NOTICE User already a member")
        else: self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
        else: print("Insufficient Points")
        return self

Hermon = User("Hermon", "Rigsby", "hermon@msn.com", 25)
Hermon.spend_points(50).display_info()

Moby = User("Moby", "Dick", "mo-d@msn.com", 150)
Moby.enroll().spend_points(80).display_info().enroll().display_info()

Chris = User("Chris", "Rock", "crock@msn.com", 51)
Chris.spend_points(40).display_info()