# lagrange-polynomial-interpolation
This is a personal passion project I created as a delve into Lagrange polynomials and interpolation. The program is designed for matplotlib, however notably the graph will only show with some sort of GUI. The 'main' function returns the Lagrange function from a number of points, that can be inputted by a user or by calling it with the option.

The key point of Lagrange interpolation is to create a polynomial that goes through every point. The polynomial that 'main' returns is not pretty, but works if evaluated: I may add in the future a 'prettified' version of the polynomial.

The 'li()' function also returns a polynomial for a specific point as part of the visualization of Lagrange's idea.

It's worth noting that, because of the steps in the for loop, floating point numbers cannot be inputted.
I do think however it's still possible to receive a polynomial for a set of these, if you scale all of them up accordingly, and then scale down the resulting polynomial. For example, the co-ordinates (1, 0.1) become (10, 1).
