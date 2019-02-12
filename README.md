# Removing-Noise-Using-Morphological-Operations

Erosion:
The erosion of a binary image f by a structuring element s (denoted f s) produces a new
binary image g = f s with ones in all locations (x,y) of a structuring element's origin at
which that structuring element s fits the input image f, i.e. g(x,y) = 1 is s fits f and 0 otherwise,
repeating for all pixel coordinates (x,y).
-In this part we have implemented erosion using a structuring element with 5 rows and 5
columns of ones I.e rectangle.


Dilation:
The dilation of an image f by a structuring element s (denoted f s) produces a new binary
image g = f s with ones in all locations (x,y) of a structuring element's orogin at which that
structuring element s hits the the input image f, i.e. g(x,y) = 1 if s hits f and 0 otherwise,
repeating for all pixel coordinates (x,y). Dilation has the opposite effect to erosion -- it adds a
layer of pixels to both the inner and outer boundaries of regions.


Opening:
The opening of an image f by a structuring element s (denoted byf s) is an erosion followed
by a dilation:
f s= (f s) s
opening is so called because it can open up a gap between objects connected by a thin bridge
of pixels. Any regions that have survived the erosion are restored to their original size by the
dilation
opening is an idempotent operation: once an image has been opened, subsequent openings
with the same structuring element have no further effect on that image:
(f s) s) = f s.


Closing:
The closing of an image f by a structuring element s (denoted by f • s) is a dilation followed
by an erosion:
f • s= (f srot) srot
In this case, the dilation and erosion should be performed with a rotated by 180 degree
structuring element. Typically, the latter is symmetrical, so that the rotated and initial versions
of it do not differ.


-In our case the structuring element is kept symmetrical.
In all the operations we are using a structuring element of size 5x5 having all values 1.It is a
rectangle having the origin at index (2,2)



In the fig res_noise1.jpg the two morphological operations performed are
opening and then closing.
-In the fig res_noise2.jpg the two morphological operations performed are
closing and then opening.
-From the above two outputs we can see that the results of the two
different morphological operations are almost similar.
-There is a very minute difference along the boundaries of the object this
is affected based on what morphological operation are performed first that
is erosion is performed first or dilation



-In the fig res_bound1.jpg we are first performing erosion of image res_noise1.jpg and then
subtracting the eroded image from res_noise1.jpg to get the final boundaries.
-In the fig res_bound2.jpg we are first performing dilation of image res_noise2.jpg and then
subtracting the image res_noise2.jpg from the dilated image to get the final boundary output


RUN 
python task3.1.py
