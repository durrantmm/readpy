# `readpy` - A simple python package designed to syntactically mimic the readr package in R. 


Install the package with pip:

    pip install readpy
    
Load the functions into your script with:

    from readpy import *
    
You will then have access to the functions

    read_csv(f, col_names = True)
    read_tsv(f, col_names = True)
    read_delim(f, delim, col_names = True)
    
    write_csv(x, path, col_names = True)
    write_tsv(x, path, col_names = True)
    write_delim(x, path, delim, col_names = True)
    
The syntax is designed to resemble that of the R package `readr` as closely as possible. 
All of the functionality is not yet fully implemented, but the basics are there.

This returns a `DplyFrame`, which is a class written in the `dplython` package. This means that you
can use the `>>` to pipe data between `dplython` functions. (see [`dplython`](https://pythonhosted.org/dplython/) 
for more information).

This is intended to be syntactically similar, but also functionally similar to the `readr` R package
where possible. For example, when the parameter `col_names = False` is passed, the header resembles
the `readr` default: 

         X1       X2 X3   X4    X5    X6   X7    X8    X9   X10
    0  0.23    Ideal  E  SI2  61.5  55.0  326  3.95  3.98  2.43
    1  0.21  Premium  E  SI1  59.8  61.0  326  3.89  3.84  2.31
    2  0.23     Good  E  VS1  56.9  65.0  327  4.05  4.07  2.31
    3  0.29  Premium  I  VS2  62.4  58.0  334  4.20  4.23  2.63
    4  0.31     Good  J  SI2  63.3  58.0  335  4.34  4.35  2.75


This package is currently in development, please visit the github page if you'd like to contribute: 
https://github.com/durrantmm/readpy