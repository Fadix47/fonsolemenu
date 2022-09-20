# fonsolemenu
Simple console menu for windows

How to install 
```
pip install fonsolemenu
```

# Classes

### fonsoleMenu - base menu
### fonsoleOption - option for `fonsoleMenu`

# Parameters for fonsoleOption

| Name  | Type  |       Default   |                        Information                               |
|:-----:|:-----:|:---------------:|:----------------------------------------------------------------:|
| name  | `str` |                 |                        The option name                           |
| index | `int` | `Autoincrement` | Index of option from list, you should not setting it by yourself |

# Parameters for fonsoleMenu

|   Name    |  Type  |  Default|         Information       |
|:---------:|:------:|:-------:|:-------------------------:|
|    title  |  `str` |         |         Menu name         |
|  options  | `list` |         | List of `fonsoleOption`s  |

### Methods
### start - sends the menu. Return type `fonsoleOption`

# Usage example

```py
from fonsolemenu import fonsoleMenu, fonsoleOption

def main():
    print("Correct button")

option1 = fonsoleOption(name='Option 1')
option2 = fonsoleOption(name='Option 2')

menu = fonsoleMenu(title='Choose your option:', options=[option1, option2])
response = menu.start()

if response.index == 0:
    main()
```
