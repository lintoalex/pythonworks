from abc import ABC,abstractmethod

class car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelarate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class swift(car):

    def start(self):
        print("swift start method")

    def accelarate(self):
        print("swift accelarate method")

    def stop(self):
        print("swift stop method")

car_instance=swift()

car_instance.start()

car_instance.accelarate()

car_instance.stop()