class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name=first_name   
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name,self.last_name,self.email,self.age)
    def enroll(self):
        if self.is_rewards_member==True:
            print(f"{self.first_name} is already a rewards member")
        else:    
            self.is_rewards_member=True
            self.gold_card_points=200
            print(f"{self.first_name} has been enrolled and received {self.gold_card_points} points.")
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount

omar=User("Omar","smith","omar@gmail.com","42")
layla=User("Layla","Smith","layla@gmail.com","30")   
omar.display_info()
omar.enroll()
omar.spend_points(50)
print(omar.gold_card_points)
layla.display_info()
layla.enroll()
layla.spend_points(80)
print(layla.gold_card_points)