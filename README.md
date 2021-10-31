# Validate user entered IP address is valid or not and print whether it's a class A, class B, or class C IP address.

Created a Python file to run this program.
IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots (".")
e.g.,172.16.254.1                             

## Steps
1. Validate the input string is valid IP address or not.            
2. If it is a valid IP address check which class does the IP address belongs to.                                         
3. If the IP address is invalid, the program raises a ValueError. 

## Below are some of the test written to validate the program. 
1. test_validIP - Verify if the IP address is valid. e.g., IP address 223.10.10.10 is valid.
2. test_validate_invalidIP - Verify if the IP address is invalid. e.g., IP address .10.10.10 is invalid
3. test_validate_classA - Verify if the IP address belongs to class A. e.g., IP address 127.10.10.10 belongs to class A
4. test_validate_classB - Verify if the IP address belongs to class B. e.g., IP address 191.10.10.10 belongs to class B
5. test_validate_classC - Verify if the IP address belongs to class C. e.g., IP address 223.10.10.10 belongs to class C
6. test_invalid_class - Verify if the IP address does not belongs to class A, B or C. e.g., IP address 255.10.10.10 does not belongs to class A, B or C