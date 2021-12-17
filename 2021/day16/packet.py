from reader import PacketReader

class Packet:
    def __init__(self, reader: PacketReader):
        self.version = reader.read(3)
        self.sum_version = self.version
        self.type_id = reader.read(3)
        self.value = 0

        if self.is_literal():
            self.__read_literal(reader)
        else:
            self.__read_operator(reader)
    
    def is_literal(self) -> bool:
        return self.type_id == 4
    
    def __read_literal(self, reader: PacketReader):
        bin_val = ""
        while True:
            is_last = reader.read(1) == 0
            bin_val += reader.read_raw(4)

            if is_last:
                self.value = int(bin_val, 2)
                return
    
    def __read_operator(self, reader: PacketReader):
        children = self.__read_children(reader)
        
        if self.type_id == 0:
            self.value = sum(c.value for c in children)
        elif self.type_id == 1:
            self.value = 1
            for c in children:
                self.value *= c.value
        elif self.type_id == 2:
            self.value = min(c.value for c in children)
        elif self.type_id == 3:
            self.value = max(c.value for c in children)
        elif self.type_id == 5:
            self.value = 1 if children[0].value > children[1].value else 0
        elif self.type_id == 6:
            self.value = 1 if children[0].value < children[1].value else 0
        elif self.type_id == 7:
            self.value = 1 if children[0].value == children[1].value else 0
    
    def __read_children(self, reader: PacketReader)->"list[Packet]":
        length_type = reader.read(1)
        children: list[Packet] = []

        if length_type == 0:
            total_bits_len = reader.read(15)
            limit = reader.pos + total_bits_len
            while reader.pos < limit:
                p = Packet(reader)
                self.sum_version += p.sum_version
                children.append(p)
        elif length_type == 1:
            count_packets = reader.read(11)
            for _ in range(count_packets):
                p = Packet(reader)
                self.sum_version += p.sum_version
                children.append(p)
        
        return children
