# demo.py
from implement_router import Router

ops = ["Router","addPacket","addPacket","addPacket","addPacket","addPacket","forwardPacket","addPacket","getCount"]
args = [[3],[1,4,90],[2,5,90],[1,4,90],[3,5,95],[4,5,105],[],[5,2,110],[5,100,110]]

result = []
obj = None

for op, arg in zip(ops, args):
    if op == "Router":
        obj = Router(*arg)
        result.append(None)
    elif op == "addPacket":
        val = obj.addPacket(*arg)
        result.append(val)
    elif op == "forwardPacket":
        val = obj.forwardPacket()
        result.append(val)
    elif op == "getCount":
        val = obj.getCount(*arg)
        result.append(val)

print("Results:", result)
