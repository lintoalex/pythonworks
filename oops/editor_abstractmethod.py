from abc import ABC,abstractmethod

class editor(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class visualstudio(editor):
 
    def open(self):
        print("open method")

    def execute(self):
        print("execute method")

    def debug(self):
        print("debug method")

editor_instance=visualstudio()

editor_instance.open()

editor_instance.execute()

editor_instance.debug()

