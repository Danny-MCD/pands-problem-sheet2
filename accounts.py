# accepts a 10 digit account number and prints it with characters 1-6 replaced with X's
# Author: Daniel Mc Donagh

AccNo = str(input("Please enter account no: "))
print(AccNo.replace(AccNo[0:6], "XXXXXX"))