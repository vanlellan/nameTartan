# nameTartan

This command line script generates a PNG representation of a tartan pattern based on a full name.

usage: python nameTartanHSV.py \[first\] \[middle\] \[last\]

### Notes:
- generated pattern is not case sensitive
- no special characters!
- use exactly three names
- the colors are interpreted using the HSV color representation
    - the last name specifies the hue (H)
    - the middle name specifies the saturation (S)
    - the first name specifies the value (V)
- the size of each block of color is determined from the last name letters, x2 (a=2, b=4, etc)
- the two shorter names are repeated to match the length of the longest name
