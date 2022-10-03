class TV:
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False

    def turn_on(self):
        self.on = True
    
    def turn_off(self):
        self.on = False

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def get_volume_level(self):
        return self.volumeLevel

    def set_volume_level(self, volume_level):
        self.volumeLevel = volume_level

    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    def volume_down(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1
