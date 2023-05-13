# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 6
# OOP TV Class and Test Driver Program

# Pseudocode

# create a class for TV
class TV:

    # enable TV class constructor/s

    # constructor that initializes the TV object
    def __init__ (self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False
    
    # execute TV class methods
    
    # method that turns on the TV
    def turnon(self):
        self.on = True

    # method that turns off the TV
    def turnoff(self):
        self.off = True
    
    # method that returns the channel
    def getChannel(self):
        return self.channel
    
    # method that sets the channel
    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel
    
    # method that returns the volume level
    def getVolume(self):
        return self.volumeLevel


# define TestTV class
# have TestTV constructor/s
# enable methods for TestTV class
# create instance of TestTV