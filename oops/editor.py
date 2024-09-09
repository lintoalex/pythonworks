
class Editor:

    def __init__(self,name,vendor):

        self.name=name

        self.vendor=vendor

    def open(self):

        print(f"{self.name} open")

    def execute(self):

        print(f"{self.name} execute")

class vscode(Editor):

    def __init__(self,name,vendor):

        super().__init__(name,vendor)

vsc_instance=vscode("visual studio","vscvendor")

vsc_instance.open()


class pycharm(Editor):

    def __init__(self,name,vendor):

        super().__init__(name,vendor)

pycharms_instance=pycharm("pycharm","pycharmvendor")

pycharms_instance.execute()

