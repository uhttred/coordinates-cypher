# Coordinates' Cypher

This is a cryptographic algorithm based on the way text messages were written using cellphones with buttons numbered from 1 to 9, cellphones like Nokia 3310. 

It is very simple to understand the algorithm, just ask yourself the following question:
> How many times would I hit the button numbered "2" until I get a "c"?

That technique is the algorithm basis, however it is easily extensible using things such as `functions` to increase the level of security. You can customize it to fit your own needs.

The reason why I call it __coordinates' cypher__ is because of the `'` which reminds me of GPS coordinates. 

To encode a file, you type `python3 main.py -e 'file.extension'`, the output file will be `file.nje`

To decode a file, you type `python3 main.py -d 'file.nje'`, the output file will be `file.njd`

Check the folder `example` to see the results.
