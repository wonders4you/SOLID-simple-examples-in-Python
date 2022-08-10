# SOLID cz. 5 SOLI%D%
# 
# D - Dependency inversion principle

# Depend upon abstractions, not concretions.

from abc import ABC, abstractmethod


class Speakers:
    
    def turn_on(self):
        print('speakers ON')

    def turn_off(self):
        print('speakers OFF')
        

class USBSwitch():
    def __init__(self, s: Speakers):
        self.speaker = s
        self.on = False
        
    def press(self):
        if self.on:
            self.speaker.turn_off()
            self.on = False
        else:
            self.speaker.turn_on()
            self.on = True
        

s=Speakers()
switch=USBSwitch(s)

switch.press()
switch.press()    
switch.press()    


# The above solution breaks the rules of Dependency inversion principle

# We have to assign dependencies to abstractions to satisfy principle D/
# The example below follows this principle:



class Switchable(ABC):
    """
    What does it means that something is switchable?    
    """
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
        

class USBSpeakers(Switchable):
    
    def turn_on(self):
        print('speakers ON')

    def turn_off(self):
        print('speakers OFF')        


# Thanks to this solution we can add more devices:

class USBCamera(Switchable):
    
    def turn_on(self):
        print('camera ON')

    def turn_off(self):
        print('camera OFF')        



class PowerSwitch:
    def __init__(self, s: Switchable):
        self.client = s
        self.on = False
        
    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True     



    
camera=USBCamera()
switch=PowerSwitch(camera)

switch.press()
switch.press()    
switch.press()    



