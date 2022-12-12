# nameTartan

This command line script generates a PNG representation of a tartan pattern based on a full name.

usage: python nameTartanHSV.py \[first\] \[middle\] \[last\]

### Notes:
- use only lower-case letters in the names
- use exactly three names
- the colors are interpretted using the HSV color representation
    - the last name specifies the hue (H)
    - the middle name specifies the saturation (S)
    - the first name specifies the value (V)
- the two shorter names are repeated to match the length of the longest name
