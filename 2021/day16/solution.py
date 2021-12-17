from reader import PacketReader

def parse_packet(reader: PacketReader)->int:
    if reader.finished():
        return 0

    version = reader.read(3)
    type = reader.read(3)

    # type 4 means literal
    if type == 4:
        while True:
            is_last = reader.read(1) == 0
            _ = reader.read(4)

            if is_last:
                return version
    else:
        length_type = reader.read(1)

        v = version
        if length_type == 0:
            total_bits_len = reader.read(15)
            limit = reader.pos + total_bits_len
            while reader.pos < limit:
                v += parse_packet(reader)
        elif length_type == 1:
            count_packets = reader.read(11)
            for _ in range(count_packets):
                v += parse_packet(reader)

        return v

with open("input.txt", "r") as f:
    input = f.readline()

reader = PacketReader(input)

resp = parse_packet(reader)
print(resp)
