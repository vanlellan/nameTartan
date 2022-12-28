# nameTartan

![name tartan generator image](./)

This command line script generates a PNG representation of a tartan pattern based on a full name.

usage: python nameTartanHSV.py \[first\] \[middle\] \[last\]

### Notes:
- generated pattern is not case sensitive
- special characters are removed
- must use exactly three names/words
- the colors are interpreted using the HSV color representation
    - the first name specifies the hue (H)
    - the middle name specifies the saturation (S)
    - the last name specifies the value (V)
- the size of each block of color is determined from the last name letters, times two (a=2, b=4, etc)
- the two shorter names are repeated to match the length of the longest name
- a simple flask app is provided as a GUI

## To Do
- [X] graphical user interface (webapp with flask!)
    - [X] one text input with an image display above
    - [ ] toggle radio buttons for assigning H, S, V, and count to first, middle, and last names in any combination
- [ ] split name format checking and tartan generation into two functions
- [X] add extra flask stuff (gunicorn script, systemd config, wsgi.py, ...) to repo
