from abc import ABC, abstractmethod
import unittest

#to run from terminal (inside folder directory):
#python -m unittest question7.py


# Mediator Interface
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event: str):
        pass

# Concrete Mediator Class
class ChatMediator(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def notify(self, sender, event: str):
        for user in self.users:
            if user != sender:
                user.receive(event, sender.name)

# Component Base Class
class User:
    def __init__(self, name, mediator: Mediator):
        self.name = name
        self.mediator = mediator
        self.mediator.add_user(self)

        self.sent_message = ""
        self.received_message = ""

    def send(self, message: str):
        #print(f"{self.name} sends message: {message}")
        self.mediator.notify(self, message)
        self.sent_message = message

    def receive(self, message: str, sender_name: str):
        #print(f"{self.name} receives message from {sender_name}: {message}")
        self.received_message = message

# Client Code
if __name__ == "__main__":
    mediator = ChatMediator()
    
    user1 = User("User1", mediator)
    user2 = User("User2", mediator)

    user1.send("Hello User2!")
    user2.send("Hi User1, how was your car ride?")

    print("User 1 sends: ", user2.received_message)
    print("User 2 sends: ", user1.received_message)




######## Test cases for Mediator pattern ########

class TestMediator(unittest.TestCase):      #need to actually write this one now

    def test_send_function(self):
        #assume
        myMediator = ChatMediator()
    
        user1 = User("User1", myMediator)
        user2 = User("User2", myMediator)

        user1.send("Hello User2!")
        user2.send("Hi User1, how was your car ride?")
        
        #assert
        self.assertEqual(user1.sent_message, "Hello User2!")
        self.assertEqual(user2.sent_message, "Hi User1, how was your car ride?")


    def test_receive_function(self):
        myMediator = ChatMediator()
    
        user1 = User("User1", myMediator)
        user2 = User("User2", myMediator)

        user1.send("Hello User2!")
        user2.send("Hi User1, how was your car ride?")

        #assert
        self.assertEqual(user1.received_message, "Hi User1, how was your car ride?")
        self.assertEqual(user2.received_message, "Hello User2!")
