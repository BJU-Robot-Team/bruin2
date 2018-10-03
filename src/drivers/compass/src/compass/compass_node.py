#!/usr/bin/env python

# -------------------------------------------
# Manipulate Data object, builds on top of compass_data to form interface with options selected
# -------------------------------------------

import compass_data

class ManipulateData:
    
    def parse_data(self, raw_data):
        new_data = compass_data.CompassData(0)
        length = len(raw_data)
        finished = False
        for i in range(0, length):
            if finished:
                break
            option = raw_data[i]
            if (option == 'C'):
                new_data.heading = self.pull_data(raw_data, i)
                new_data.heading = 9 - new_data.heading - (6 + 37 / 60)
                if (new_data.heading < 0):
                    new_data.heading = new_data.heading + 360
            elif (option == 'P'):
                new_data.pitch = self.pull_data(raw_data, i)
            elif (option == 'R'):
                new_data.roll = self.pull_data(raw_data, i)
            elif (option == '*'):
                new_data.check_sum = self.pull_data(raw_data, i)
            else:
                #TODO: handle invalid option?
                continue
        return new_data



    def pull_data(self, raw_data, start_index):
        stop = False
        i = start_index + 1
        temp_string = ""

        while(stop != True and i < int(len(raw_data))):
            ialpha = raw_data[i].isalpha()

            if (ialpha == True or raw_data[i] == '*'):
                stop = True
            else:
                temp_string += raw_data[i]
            i = i + 1
        return float(temp_string)

    def send_data(self, compass_data):
        # this file was outputting to an outfile, and I don't think it's necessary anymore
        print("Unimplemented")

    def load_data(self):
        # TODO: this should be coming from the compass itself, this is just temporary
        with open("sample_data.txt") as sample_data:
            test_data = sample_data.readline()
            return test_data
