This implements a tool which outputs a canonical Euclidean rhythm when given inputs of n time steps and k beats, 
as well as an offset (rotation) of offset time steps.

I also keep a few functions I wrote down at the bottom, including an alternate implementation of the Euclidean algorithm

I'm a bassist. Playing Bad Bunny (Baile Inolvidable, which, by the by, has an amazing bass line!) made me really
appreciate polyrhythms. Although I suppose Erykah Badu and Rochelle Jordan share some of the blame.

I started playing with Strudel and had a blast. Euclidean rhythm notation blew my mind: I wanted to use it, but lacked
an easy visual guide to help me interpret Euclidean rhythms without just hearing them. I built this so I could test 'em.

I used Claude as a design partner: designing a few tests/edge cases, providing some guidance, and helping identify
libraries and some "glue" to make things work a little better. But I wrote all the code myself, and didn't use any lines
I couldn't completely understand. 

My personal use case/setup: I added the following line to .zshrc: 

`alias euclidean='/path/to/python /path/to/euclidean.py'`

Basically, I can now call this wherever. This will last until I write something else which has to do with Euclidean
anything...
