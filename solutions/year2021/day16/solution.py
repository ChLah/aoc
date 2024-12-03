from packet import Packet
from reader import PacketReader

with open("input.txt", "r") as f:
   input = f.readline()

reader = PacketReader(input)
packet = Packet(reader)
print(packet.sum_version, packet.value)
