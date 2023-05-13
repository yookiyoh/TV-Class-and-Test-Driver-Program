# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 6
# OOP TV Class


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


# Define a TestTV class
class TestTV:
    # Have TestTV constructor/s
    # Constructor that initializes two TV objects with their properties and methods
    def __init__ (self):
        # Create two TV objects
        self.tv1 = TV()
        self.tv2 = TV()
        # Set the channel, volume level, and turn on both TVs
        self.tv1.setChannel(30)
        self.tv1.setVolume(3)
        self.tv1.turnon()
        self.tv2.setChannel(3)
        self.tv2.setVolume(2)
        self.tv2.turnon()
        
    # Enable methods for TestTV class
    # Method that displays the current channel and volume level for both TVs
    def display(self):
        print ("tv1's channel is", self.tv1.getChannel(), "and volume level is", self.tv1.getVolume())
        print ("tv2's channel is", self.tv2.getChannel(), "and volume level is", self.tv2.getVolume())
        
    # Method that displays a menu of options for the user to interact with both TVs
    def menu(self):
        while True:   # Use while True looping
            # Print the menu options
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
            # Get the user's input for the chosen option
            choice = input("Enter your choice: ")
            # Have the conditionals
            # Loop through the user's selected TV options
            # Turn on TV if user selects option 1
            if choice == '1':
                # Prompt user to select a TV and turn it on if valid option is chosen
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.turnon()
                elif tv == '2':
                    self.tv2.turnon()
            
            # Turn off TV if user selects option 2
            elif choice == '2':
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.turnoff()
                elif tv == '2':
                    self.tv2.turnoff()
                    
            # Change channel of selected TV if user selects option 3
            elif choice == '3':
                tv = input("Select TV (1 or 2): ")
                channel = int(input("Enter new channel (1-120): "))
                if tv == '1':
                    self.tv1.setChannel(channel)
                elif tv == '2':
                    self.tv2.setChannel(channel)
            
            # Adjust volume of selected TV if user selects option 4
            elif choice == '4':
                tv = input("Select TV (1 or 2): ")
                volume = int(input("Enter new volume level (1-7): "))
                if tv == '1':
                    self.tv1.setVolume(volume)
                elif tv == '2':
                    self.tv2.setVolume(volume)
                    
            # Increase channel of selected TV if user selects option 5
            elif choice == '5':
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.channelUp()
                elif tv == '2':
                    self.tv2.channelUp()
                    
            # Decrease channel of selected TV if user selects option 6
            elif choice == '6':
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.channelDown()
                elif tv == '2':
                    self.tv2.channelDown()
                    
            # Increase volume of selected TV if user selects option 7
            elif choice == '7':
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.volumeUp()
                elif tv == '2':
                    self.tv2.volumeUp()
            
            # Decrease volume of selected TV if user selects option 8
            elif choice == '8':
                tv = input("Select TV (1 or 2): ")
                if tv == '1':
                    self.tv1.volumeDown()
                elif tv == '2':
                    self.tv2.volumeDown()
                    
            # Display current state of all TVs if user selects option 9
            elif choice == '9':
                print("\nLoading info...\n")
                for i in tqdm(range(100)):
                    time.sleep(0.01)

                time.sleep(2)
                print("\n[TV Info Loaded Successfully!]\n")
                self.display()
                
            # Exit the program is user selects option 0
            elif choice == '0':
                print("\nThank you for using this program!")
                print("Exiting program in...")
                for i in range(3, 0, -1):
                    print(f"{Fore.CYAN}{Back.WHITE}{Style.BRIGHT}{i}{Style.RESET_ALL}")
                    time.sleep(0.8)
                exit()
            
            # Prompt user to select a valid option if an invalid option is selected and or inputted
            else:
                print("Invalid input. Please try again.")



# Create an instance of TestTV and call the menu method if the file is being run as the main program
if __name__ == '__main__':
    test = TestTV()
    test.menu()