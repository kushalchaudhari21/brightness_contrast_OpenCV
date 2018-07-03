Theory

A general image processing operator is a function that takes one or more input images and produces an output image.
In pixel image processing transformation, each output pixel's value depends on only the corresponding input pixel value (plus, potentially, some globally collected information or parameters).Examples of such operator include brightness and contrast adjustments as well as color correction and transformations.

Two commonly used point processes are multiplication and addition with a constant:
g(x)=αf(x)+β
The parameters α>0 and β are often called the gain and bias parameters; sometimes these parameters are said to control contrast and brightness respectively.
You can think of f(x) as the source image pixels and g(x) as the output image pixels. Then, more conveniently we can write the expression as:
g(i,j)=α⋅f(i,j)+β
where i and j indicates that the pixel is located in the i-th row and j-th column.

    
