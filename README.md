# LEDController4100

## About

A Python library and a CLI interface for controlling of [ThorLabs LED controller DC4100](https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=3832) through USB interface.

## Requirements

It requires `visa32.dll` and `TLDC4100_32.dll` dynamic libraries and `ctypes` Python library to run. The DLL files can be obtained by installing GUI controlling software from ThorLabs website.

## Use

Use it in you program by importing `ledcontroller4100.py` or use directly from command line by running `cli.py`.

### CLI use
Run `python main.py` and follow the instruction.

Example of use:
```
> python main.py
Controller: ASRL5  (COM5 - DC4104 - 4 Channel LED Driver)
Select channel (0-3):2
Specify current (0-1 A, 0.001 A resolution):0.380
Specify on or off:on
Select channel (0-3):1
Specify current (0-1 A, 0.001 A resolution):0.150
Specify on or off:on
Select channel (0-3):2
Specify current (0-1 A, 0.001 A resolution):0.1
Specify on or off:off
Select channel (0-3):2
Specify current (0-1 A, 0.001 A resolution):0
Specify on or off:off
```

### Function reference

#### LEDConnect (searchPattern=DC4100_FIND_PATTERN)
Connects to the physical LED controller 4100 by searching for a specified name pattern. The default value works for most situation, but you can specify you own. On success, it returns dictionary type with two keys: 'success' set to True and 'description' set to the description of the device.

#### LEDSetCurrent(channel, current)
Set the current (floating number in Ampers (A)) to the channel (intiger, starting from 0). Please, refer to the [ThorLabs website](https://www.thorlabs.com/NewGroupPage9.cfm?ObjectGroup_ID=3836) for information on available curernt for you LEDs. Not all LEDs support the range 0 to 1 A as supported by the controller. Some support only 0.35 A or 0.7 A! The available resolution is 0.001 A (1 mA).
  
#### LEDTurnOnOff(channel, state)
Turn or or off the LED at the correspoding channel (intiger, starting from 0). State (boolean) set to True turns the LED on, while set to False turns it off.

## Authorship
Created by Peter Nadrah on 04/01/2023.
