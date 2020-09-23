class Led:
    def __init__(self, pin):
        self.pinNumber = pin
        self.isOn = False
    
    def on(self):
        self.isOn = True
    
    def off(self):
        self.isOn = False
    
    def get_state(self):
        return self.isOn
    
    def toggle(self):
        self.isOn = not self.get_state()

myLed = Led(1)
print(myLed.get_state())
myLed.on()
print(myLed.get_state())
myLed.off()
print(myLed.get_state())
myLed.toggle()
print(myLed.get_state())
myLed.toggle()
print(myLed.get_state())