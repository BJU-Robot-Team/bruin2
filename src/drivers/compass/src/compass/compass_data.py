#!/usr/bin/env python

# -------------------------------------------
# Compass Data object, corresponds to Compass_Data.h in old code
# -------------------------------------------
class CompassData:
    def __init__(self, head=0):
        self.heading = head
        self.pitch = 0
        self.roll = 0
        self.temperature = 0
        self.check_sum = 0
