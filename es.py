# program to read the number of e's in a txt file
# Author: Daniel Mc Donagh

import sys
 # import sys module to use sys.argv function to use name of txt file from command line
def main():
    name = sys.argv[1]
    print(f'The number of times the letter e is used in {name}')
 
 
if __name__ == "__main__":
    main()



# function to count the frequency of letter e in a txt file
def letter_frequency(file_name, letter):
   
    # open file in read mode
    file = open(file_name, 'r')
 
    # store content of the file in a variable
    text = file.read()
 
    # using count()
    return text.count(letter)
# sets command line argument containing txt file name to be used as variable file_name 
file_name = sys.argv[1] 
# call the function and display the letter count
print(letter_frequency(file_name, 'e'))