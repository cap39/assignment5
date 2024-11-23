import unittest

#to run from terminal (inside folder directory):
#python -m unittest question6.py

class Coupon:
    def __init__(self, discount):
        self.discount = discount
    def get_discount(self):
        return self.discount

class Observer:
    def __init__(self, name):
        self.name = name
        pass
    def update(self, coupon):
        print(f'{self.name} has been notified of the discount: {coupon.get_discount()}%')
        return f'{self.name} has been notified of the discount: {coupon.get_discount()}%'

class Subject:
    def __init__(self):
        self.observers = []
        self.coupon = None
    def add_observer(self, observer):
        self.observers.append(observer)
    def remove_observer(self, observer):
        self.observers.remove(observer)
    def notify_observers(self, coupon):
        for observer in self.observers:
            observer.update(coupon)

def main():
    subject = Subject()
    observer1 = Observer('Observer 1')
    observer2 = Observer('Observer 2')
    subject.add_observer(observer1)
    subject.add_observer(observer2)
    subject.notify_observers(coupon = Coupon(20))

if __name__ == '__main__':
    main()


class TestObserver(unittest.TestCase):
    def test_observer_update(self):
        subject = Subject()
        observer1 = Observer('Observer 1')
        observer2 = Observer('Observer 2')
        subject.add_observer(observer1)
        subject.add_observer(observer2)
        self.assertEqual(observer1.update(Coupon(20)), 'Observer 1 has been notified of the discount: 20%')
        self.assertEqual(observer2.update(Coupon(20)), 'Observer 2 has been notified of the discount: 20%')
        
    def test_subject_notify_observers(self):
        subject = Subject()
        observer1 = Observer('Observer 1')
        observer2 = Observer('Observer 2')
        subject.add_observer(observer1)
        subject.add_observer(observer2)
        self.assertEqual(subject.notify_observers(Coupon(20)), None)