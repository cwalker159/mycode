#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 IP address:")
    
    # display the input back to the user.
    print("You told me the IPv4 address is: " + user_input)
    
# this calls main
main()
#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   CHALLENGE 01 - Solution"""    

def main():

    user_input = input("Please enter an IPv4 IP address: ")
    
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is:" + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)
    
    # asking user for 'vendor name'
    vendor = input("Please input the vendor name: ")
    print(vendor)

main()

