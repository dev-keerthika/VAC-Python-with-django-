class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram", self.ram)
        print("processor:", self.processor)

hp=laptop()
dell= laptop()

hp.ram="6ig"
hp.processor="545"

dell.ram="5yu"
dell.processor="54"

hp.display()
dell.display()
