#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Author: Peter Nadrah
## License: GNU GPL v3
## Description: Software controller of ThorLabs LED controller 4100

import ledcontroller4100
import time

def main():
  ret = ledcontroller4100.LEDConnect()
  print ('Description:', ret['description'])

  ledcontroller4100.LEDSetCurrent(0, 0.02)
  ledcontroller4100.LEDSetCurrent(1, 0.03)
  
  ledcontroller4100.LEDTurnOnOff(0, True)
  time.sleep(2)  
  ledcontroller4100.LEDTurnOnOff(0, False)
  time.sleep(2)
  
  ledcontroller4100.LEDTurnOnOff(1, True)
  time.sleep(2)  
  ledcontroller4100.LEDTurnOnOff(1, False)
  
if __name__ == '__main__':
  main()