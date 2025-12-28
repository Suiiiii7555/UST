class TV:
    def __init__(self):
        self.TV_Status = "off"
        self.channel_no = 1
        self.TV_volume = 10
        
    def __str__(self):
        return f"TV Status :{self.TV_Status}\nChannel : {self.channel_no}\nVolume : {self.TV_volume}"
    
TV1 = TV()
print(TV1)