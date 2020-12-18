class Friendships:

    def __init__(self):
        self.dict = {}

    def add_friend(self, person, friend):
        if type(person) is not str or type(friend) is not str:
            raise TypeError("Wrong type")
        if person in self.dict:
            self.dict[person].append(friend)
        else:
            self.dict[person] = [friend]

    def make_friends(self, person1, person2):
        if type(person1) is not str or type(person2) is not str:
            raise TypeError("Wrong type")
        self.add_friend(person1, person2)
        self.add_friend(person2, person1)

    def get_friends_list(self, person):
        if type(person) is not str:
            raise TypeError("Wrong type")
        elif person in self.dict:
            return self.dict[person]
        else:
            return "Person doesn't exist"

    def are_friends(self, person1, person2):
        if type(person1) is not str or type(person2) is not str:
            raise TypeError("Wrong type")
        elif person1 in self.dict[person2] and person2 in self.dict[person1]:
            return True
        else:
            return False