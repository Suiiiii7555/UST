class TV:
    def __init__(self):
        self.__Status = "off"
        self.__channel_no = 1
        self.__volume = 10
        
    def __str__(self):
        return f"TV Status :{self.__Status}\nChannel : {self.__channel_no}\nVolume : {self.__volume}"
    
TV1 = TV()
print(TV1.__dir__())
print(TV1._TV__volume)
print(TV1._TV__channel_no)
print(TV1)