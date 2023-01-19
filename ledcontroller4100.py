#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Author: Peter Nadrah
## License: GNU GPL v3
## Description: Software controller of ThorLabs LED controller DC4100

import ctypes

visa = ctypes.CDLL('visa32.dll')
TLDC = ctypes.CDLL(r'C:\Program Files (x86)\IVI Foundation\VISA\WinNT\Bin\TLDC4100_32.dll')

instr = ctypes.c_uint32()
OFF = 0
ON = 1
VI_FIND_BUFLEN = 256
DC4100_BUFFER_SIZE = 256
DC4100_ERR_DESCR_BUFFER_SIZE = 512
# Name pattern is usually 'ASRL?*' or 'ASRL5?*' in case of multiple devices.
DC4100_FIND_PATTERN = b"ASRL5?*"
DC4100_ERR_DESCR_BUFFER_SIZE = 512
VI_ATTR_INTF_INST_NAME = ctypes.c_ulong(0xBFFF00E9)
VI_NULL = ctypes.c_int32(0)

def LEDConnect(searchPattern=DC4100_FIND_PATTERN):
  # It has to be created with  create_string_buffer, not c_wchar_p to function properly.
  cSearchPattern = ctypes.create_string_buffer(searchPattern)
  
  resMgr = ctypes.c_uint32()
  findList = ctypes.c_uint32()
  cnt = ctypes.c_uint32(0)
  rscStr = ctypes.create_string_buffer(VI_FIND_BUFLEN)
  
  ret = visa.viOpenDefaultRM(ctypes.byref(resMgr))
  if ret < 0:
    errorExit(ret)
  
  ret = visa.viFindRsrc(resMgr, cSearchPattern, ctypes.byref(findList), ctypes.byref(cnt), rscStr)
  if ret < 0:
    errorExit(ret)
    
  id_query = ctypes.c_bool()
  reset_instr = ctypes.c_bool()
  ret = TLDC.TLDC4100_init(rscStr, id_query, reset_instr, ctypes.byref(instr));
  if ret < 0:
    errorExit(ret)
  
  lockState = ctypes.c_uint32()
  name = rscStr = ctypes.create_string_buffer(DC4100_BUFFER_SIZE)
  descr = rscStr = ctypes.create_string_buffer(DC4100_BUFFER_SIZE)
  #ret = visa.readInstrData(resMgr, rscStr, name, alias, ctypes.byref(lockState))
  
  intfType = ctypes.c_uint16()
  intfNum = ctypes.c_uint16()
  err = visa.viParseRsrcEx(resMgr, rscStr, ctypes.byref(intfType), ctypes.byref(intfNum), VI_NULL, VI_NULL, name)

  if ret < 0:
    errorExit(ret)
  
  err = visa.viGetAttribute(instr, VI_ATTR_INTF_INST_NAME, descr);

  if ret < 0:
    errorExit(ret)
  
  return ({
    'success': True,
    'description': descr.value.decode('UTF-8')
  })
  
def LEDDisconnect():
  visa.viClose(instr)
 
def LEDSetCurrent(channel, current):
  _channel = ctypes.c_int32(channel)
  # if defined a c_double it gives to low current, even though ViReal64 is defined as double in visatype.h
  _current = ctypes.c_float(current)
  ret = TLDC.TLDC4100_setConstCurrent(instr, _channel, _current)
  if ret < 0:
    errorExit(ret)

def LEDTurnOnOff(channel, state):
  _channel = ctypes.c_int32(channel)
  if state:
    ret = TLDC.TLDC4100_setLedOnOff(instr, _channel, ON);
  else:
    ret = TLDC.TLDC4100_setLedOnOff(instr, _channel, OFF);
  if ret < 0:
    errorExit(ret)
  
def errorExit(err):
  DC4100_ERR_DESCR_BUFFER_SIZE = 512
  
  ebuf = ctypes.create_string_buffer(DC4100_ERR_DESCR_BUFFER_SIZE)
  
  # Print error
  TLDC.TLDC4100_error_message(instr, err, ebuf)
  print('ERROR:', ebuf.value)

	# Close instrument handle if open
  if instr != None:
    TLDC.TLDC4100_close(instr)
  
  exit()
 