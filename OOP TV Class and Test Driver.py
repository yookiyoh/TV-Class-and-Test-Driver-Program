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
    
    # method that sets the volume level
    def setVolume(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel
    
    # method that increases the channel number by 1
    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    # method that decreases the channel number by 1
    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1
    
    # method that increases the volume level by 1
    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
            self.channel += 1

    # method that decreases the volume level by 1
    def volumeDown(self):
        if self.on and self.volumeLevel > 1:
            self.channel -= 1


# define TestTV class
class TestTV:
    
    # have TestTV constructor/s
    def __init__ (self):
        # create two TV objects
        self.tv1 = TV()
        self.tv2 = TV()
        # set the channel, volume level, and turn on both TVs
        self.tv1.setChannel(30)
        self.tv1.setVolume(3)
        self.tv1.turnon()
        self.tv2.setChannel(3)
        self.tv2.setVolume(2)
        self.tv2.turnon()
        
    # enable methods for TestTV class
    def display(self):
        print ("tv1's channel is", self.tv1.getChannel(), "and volume level is", self.tv1.getVolume())
        print ("tv2's channel is", self.tv2.getChannel(), "and volume level is", self.tv2.getVolume())
        
    def menu(self):
        while True:   # use while True looping
            # print menu options
            print("Select an option here:")
            print("1. Turn on TV")
            print("2. Turn off TV")
            print("3. Set channel")
            print("4. Set volume level")
            print("5. Channel up")
            print("6. Channel down")
            print("7. Volume up")
            print("8. Volume down")
            print("9. Display TV info")
            print("0. Exit")
            # have the user enter a choice from the menu
            choice = input("Enter your choice: ")
            
            # have the conditionals
            if choice == '1':
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.turnon()
                elif tv == '2':
                    self.tv2.turnon()
            
            if choice == '2':
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.turnoff()
                elif tv == '2':
                    self.tv2.turnoff()
                    
            if choice == '3':
                tv = input("Select TV (1 or 2): ")
                channel = int(input("Enter new channel (1-120): "))
                if tv == '1':
                    self.tv1.setChannel()
                elif tv == '2':
                    self.tv2.setChannel()
            
            if choice == '4':
                tv = input("Select TV (1 or 2): ")
                volume = int(input("Enter new volume level (1-7): "))
                if tv == '1':
                    self.tv1.setVolume()
                elif tv == '2':
                    self.tv2.setVolume()
                    
            if choice == '5':
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.channelUp()
                elif tv == '2':
                    self.tv2.channelUp()
                    
            if choice == '6':
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.channelDown()
                elif tv == '2':
                    self.tv2.channelDown()
                    
            if choice == '7':
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.volumeUp()
                elif tv == '2':
                    self.tv2.volumpeUp()
            
            if choice == '8':
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.volumeDown()
                elif tv == '2':
                    self.tv2.volumeDown()
                    
            if choice == '9':
                self.display()
                
            if choice == '10':
                print("Exiting program...")
                break
            
            else:
                print("Invalid input. Please try again.")

# create instance of TestTV
if __name__ == '__main__':
    test = TestTV()
    test.menu()

# initial trial testing
# trial error, "_name_" undefined
# edited name error
# another trial failed output
# fixed major indentation errors
# retrial 
# blank output, program failed
# re-editing, insertion of parentheses
# retrial
# retrial failed
# mass re-editing of code 
# retrial commenced, program is working