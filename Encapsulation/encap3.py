class TV:
    def __init__(self):
        self.__status = "off"
        self.__channel_no = 1
        self.__volume = 10
        
    def __str__(self):
        return f"TV Status : {self.__status}\nChannel : {self.__channel_no}\nVolume : {self.__volume}"

    def get_status(self):
        return self.__status
    
    def get_channel_no(self):
        return self.__channel_no

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        if volume > 0 and volume <= 100:
            self.__volume = volume
        else:
            raise ValueError("Value provided does not fall in the range of 0 to 100")
        
    def set_channel_no (self, channel_no):
        if channel_no >= 1 and channel_no <= 10:
            self.__channel_no = channel_no
        else:
            raise ValueError("Value provided does not fall in the range of 1 to 10")

    ## USING THE PROPERTY METHOD TO CONVERT GETTERS AND SETTERS INTO ATTRIBUTES / OBJECTS

    volume = property(get_volume, set_volume)
    channel = property(get_channel_no, set_channel_no)

                                                                                                                          
TV1 = TV()
# print(TV1.get_channel_no())
# print(TV1.get_status())
# TV1.set_volume(200)
# TV1.set_channel_no(11)
# TV1.set_volume(20) 
# TV1.set_channel_no(10)
## THE ABOVE TWO LINES ARE BY PASSED BY THE USE PROPERTY METHOD
TV1.volume = 90
TV1.channel = 10
print(TV1)