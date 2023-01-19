#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Author: Peter Nadrah
## License: GNU GPL v3
## Description: Software controller of ThorLabs LED controller 4100

import ledcontroller4100

def main():
  ret = ledcontroller4100.LEDConnect()
  print ('Controller:', ret['description'])
  
  showMenu()
  
def showMenu():
  ch = int(input('Select channel (0-3):'))
  current = float(input('Specify current (0-1 A, 0.001 A resolution):'))
  stateStr = input('Specify on or off:')
  state = False
  if stateStr == 'on':
    state = True
  
  ledcontroller4100.LEDSetCurrent(ch, current)
  ledcontroller4100.LEDTurnOnOff(ch, state)
  
  showMenu()

if __name__ == '__main__':
  main()