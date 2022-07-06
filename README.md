# Third Hand

## Overview
Third hand is a simple backdoor generator with a REPL interface.

## Installation
`cd` to the project directory and then run:
```
sudo make build
```
To run the program, use this command:
```
python3 -m thirdhand
```
Or if you just want to test it, you can use this command
```
sudo make run
```
which equals to `sudo make build` and then `python3 -m thirdhand`.  
  
After starting the program, type `help` to see the help message.

## Translation

We officially support `zh_CN`, `en_US` and `ja_JP` translations. If you are interested in translating this software into other languages, just fork it, and go to the `src/thirdhand/Strings.py`, and edit the dictionary `STRINGS`. After doing that, please give us a pull request, and use `[i18n]` as the prefix of your pull request's title.  
Please translate the following text as the content of `str_third_party_warn` when translating as a third-party translator:
```
This translation is offered by a third-party translator.
The translation may be not 100% accurate.
```
