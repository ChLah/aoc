class PacketReader():
    def __init__(self, input: str):
        self.data = "".join([bin(int(x, 16))[2:].zfill(4) for x in list(input)])
        self.pos = 0
    
    def finished(self)->bool:
        return self.pos >= len(self.data)

    def read(self, count: int)->int:
        self.pos += count
        return int(self.data[self.pos - count:self.pos] , 2)
        