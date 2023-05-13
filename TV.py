# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 6
# OOP TV Class File


# Define a TV class with its properties and methods
class TV:
    # Enable TV class constructor/s
    # Constructor that initializes the TV object
    def __init__ (self):
        # Default values for channel, volume level, and on/off status
        self.channel = 1
        self.volumeLevel = 1
        self.on = False
    
    # Execute TV class methods
    
    # Method that turns on the TV
    def turnon(self):
        self.on = True

    # Method that turns off the TV
    def turnoff(self):
        self.on = False
    
    # Method that returns the current channel
    def getChannel(self):
        return self.channel
    
    # Method that sets the channel to a new value if the TV is on and the channel value is valid
    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel
    
    # Method that returns the current volume level
    def getVolume(self):
        return self.volumeLevel
    
    # Method that sets the volume level to a new value if the TV is on and the volume level value is valid
    def setVolume(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel
    
    # Method that increases the channel number by 1 if the TV is on and the channel is not at its maximum value
    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    # Method that decreases the channel number by 1 if the TV is on and the channel is not at its minimum value
    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1
    
    # Method that increases the volume level by 1 if the TV is on and the volume level is not at its maximum value
    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    # Method that decreases the volume level by 1 if the TV is on and the volume level is not at its minimum value
    def volumeDown(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1