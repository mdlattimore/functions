# A Collection of Useful(ish) Functions
This is a collection of functions I created when first learning Python, 
simply as an exercise to test my understanding of the underlying skills. 
They are basically useless but still fun little exercises.

## binary_to_dec.py
Converts user input binary number to base 10

## countdown.py
A no-frills countdown timer. Starting time is currently hard-coded 
at 10 seconds. Feel free to modify

## dec_to_binary.py
Converts user input base 10 number to binary.

## key_gen.py
Produces a pseudo-random key using the os module's urandom function,
and saves the key as a text file in the working directory.
DO NOT use for creating encryption keys. This function was originally
written to support the random_key_tester.py file which measures how 
long it takes to generate a key collision of n length keys.

## key_generation_function.py
The function underlying key_gen.py

## random_key_tester.py
A short program that measures the time it takes to generate a key
collision of n length using the key_generation_function in this repo.

## math_functions.py
A collection of mostly unnecessary math functions. Functions for
calculating area of a circle, area of a triangle, area of a rectangle,
volume of a cube, volume of a sphere, and the hypotenuse of a right
triangle.

## simple_calc.py
Currently inoperative gui calculator for calculating various 
values and conversions. It remains in the repo pending revisions.

## str_functions.py
A collection of functions used for manipulating strings. See the docstring
for each function for its operation

## teletype.py
Prints text one letter at a time with n seconds between letters
using a for loop. Designed to resemble old style teletype machines