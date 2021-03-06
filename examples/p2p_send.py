#!/usr/bin/python
# -*- coding: UTF-8 -*-

import traceback
import time

from wssx126 import sx1268

if __name__ == '__main__':
  controller = sx1268.Controller()

  try:

    controller.initialize(serialPipe = "/dev/ttyAMA0")

    controller.channel = 0x1
    controller.address = 0xB8
    controller.networkId = 0x10
    controller.mode = sx1268.OperatingMode.Transmission

    while True:
      controller.sendMessage(str(time.time()))

  except:
    print(traceback.format_exc())
  finally:
    controller.cleanup()
