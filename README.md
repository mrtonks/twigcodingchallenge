# Twig Coding Challenge

This code was developed using a version of Python 3 and VSCode. 

It can be obtained either by downloading zip or by typing git clone https://github.com/mrtonks/twigcodingchallenge.git.

To run it you can simply open a terminal window and navigate to the folder that contains the .py file, and type:
```
python -c 'import challenge; challenge.helperPrintArray([1, 2, 3, 4, 5], 3)'
```
The values inside ```challenge.helperPrintArray([1, 2, 3, 4, 5], 3)``` can be changed to any other similar values (array and integer). You must also make sure you have any version of Python 3 installed in your computer.

The challenge.py file contains two functions:
1. groupArrayElements
2. helperPrintArray

### groupArrayElements
This function will take as input an array and an integer (N). It will divide the array into N sub-arrays. It uses the function ```divmod``` to extract the quotient and the remainder from a division. Those two values are used to create chucks from the original array and create the sub-arrays with the correct number of values inside a for-loop. The chucks are appended into another array and finally returned when the loop ends.

### helperPrintArray
This function has the only purpose to print the array created by the function __groupArrayElements__.
