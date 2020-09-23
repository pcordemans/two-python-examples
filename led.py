class Led:
    def __init__(self, pin):
        self.__pinNumber = pin
        self.__isOn = False
    
    def on(self):
        self.__isOn = True
    
    def off(self):
        self.__isOn = False
    
    def get_state(self):
        return self.__isOn
    
    def toggle(self):
        self.__isOn = not self.get_state()

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

# name mangling is used to obfuscate members which start with a double underscore
print(myLed._Led__isOn)
