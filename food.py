class Food:
    #class declaration
    def  __init__(self):
       self.data = {}

    # adder method
    def add(self, key, value):
        if key not in self.data.keys():
            self.data[key] = value
        else:
            self.data[key] = value


