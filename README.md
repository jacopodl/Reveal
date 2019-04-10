# Reveal #
This is a experimental tool to recursive detect and decode encoded strings, it's also can encode strings recursively.

## Installation
Reveal package can be installed through following procedure:

    $ git clone https://github.com/jacopodl/reveal
    $ cd reveal
    $ python setup.py install
    
## Usage ##
Let's take this encoded string:

    ODIsNDksODYsOTcsODEsNDgsNzAsNzksODEsMTA4LDkwLDcwLDgxLDg0LDc0LDg1LDg0LDg1LDEwOCw2Nyw4Niw4NSwxMDAsODYsODUsODUsODIsNzQsODQsODUsMTEyLDY2LDgyLDQ5LDc0LDgzLDg1LDg0LDQ4LDU3LDgwLDg0LDQ4LDYx

and supply it to revel:

    $> reveal "ODIsNDksODYsOTcsODEsNDgsNzAsNzksODEsMTA4LDkwLDcwLDgxLDg0LDc0LDg1LDg0LDg1LDEwOCw2Nyw4Niw4NSwxMDAsODYsODUsODUsODIsNzQsODQsODUsMTEyLDY2LDgyLDQ5LDc0LDgzLDg1LDg0LDQ4LDU3LDgwLDg0LDQ4LDYx"
        b64 -> n2c -> b64 -> b32 -> hex = REVEAL
        Encode with: hex,b32,b64,n2c,b64

Reveal automatically detects the encoding formats and decodes it recursively.

If option --quiet was not provided, Reveal also print a list of used decoders, in this way you can use this list with  --encode option to re encode string to original encoded format.

    $> reveal --encode hex,b32,b64,n2c,b64 "REVEAL"
        ODIsNDksODYsOTcsODEsNDgsNzAsNzksODEsMTA4LDkwLDcwLDgxLDg0LDc0LDg1LDg0LDg1LDEwOCw2Nyw4Niw4NSwxMDAsODYsODUsODUsODIsNzQsODQsODUsMTEyLDY2LDgyLDQ5LDc0LDgzLDg1LDg0LDQ4LDU3LDgwLDg0LDQ4LDYx
        
   
## Support ##
Supported encoders/decoders

- base32
- base64
- hex (space separated hex: 67 69 75 6c 69 61 ...)
- n2c (ascii to comma separated numbers: 106,97,99,111,112,111,...)
- urlEncoding
- jwt
