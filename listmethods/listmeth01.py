#!/usr/bin/env python3
"""Alta3 Research | CRWalker
Messing aroung with List Objects and Methods"""

def main():

 proto = ["ssh", "http", "https"]
 print(proto)
 print(proto[1])

 ## this line will add "dns" to the end of our list
 proto.extend("dns")
 print(proto)


#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

main()
