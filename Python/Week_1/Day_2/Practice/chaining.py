class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points= 0
    def display_info(self, first_name,last_name,email,age,):
        print(f"the user information:{self.first_name},\n{self.last_name},\n{self.email},\n{self.age},\n{self.is_rewards_member},\n{self.gold_card_points}")
        return self
    def enroll(self):
        if self.is_rewards_member== True:
            print("User already a member")
            return False
        else:    
            print(f"is the status of the user is a member?  {self.is_rewards_member} \n gold card points : {self.gold_card_points}")
            self.is_rewards_member=True
            self.gold_card_points= 200
            return True
    def spend_points(self,amount):
        if amount <= self.gold_card_points :
            spend=self.gold_card_points -amount
            print (f"Your current points : {spend}")
        else :
            print("Sorry! You don't have enough points.")
first_user=User('Omar', 'Miss', 'omar@gamil.com',23)
print(first_user)
second_user=User('layla', 'smith', 'layla@gamil.com',30)
first_user.display_info('Omar', 'Miss', 'omar@gamil.com',23).spend_points(50)
second_user.display_info('layla', 'smith', 'layla@gamil.com',30).spend_points(80)
second_user.enroll()