# -*- coding: utf-8 -*-

########################################################################
#                                                                      #
# DigiDashOBD: A python digital dash  module derived from Python-OBD   #
#                                                                      #
# Copyright 2004 Donour Sizemore (donour@uchicago.edu)                 #
# Copyright 2009 Secons Ltd. (www.obdtester.com)                       #
# Copyright 2009 Peter J. Creath                                       #
# Copyright 2016 Brendan Whitfield (brendan-w.com)                     #
# Copyright 2016 Bradley Taylor                                        #
#                                                                      #
########################################################################
#                                                                      #
# Main.py                                                              #
#                                                                      #
# This file implements python-OBD, and probably later other things     #
#                                                                      #
# DigiDashOBD is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# DigiDashOBD is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with DigiDashOBD.  If not, see <http://www.gnu.org/licenses/>. #
#                                                                      #
########################################################################



# Main Method for invoking an OBD Object and detecting sensors
import obd

connection = obd.OBD()  # auto-connects to USB or RF port

# Commands we wish to utilize/query later on
# Core/Base Info you would want on your dash
cmd_MPH = obd.commands.SPEED  # select an OBD command (sensor) [Speed (I believe it is originally fed in KPH)]
cmd_RPM = obd.commands.RPM
cmd_FUEL = obd.commands.FUEL_LEVEL

# Temperature Commands
cmd_TEMP_OUTSIDE = obd.commands.AMBIANT_AIR_TEMP
cmd_OIL_TEMP = obd.commands.OIL_TEMP

# MPG Calculation Command
# At this time I am unsure if all vehicles support this command or only ones that already have an MPG on radio,etc
cmd_FUEL_RATE = obd.commands.FUEL_RATE

# ------------------------------------------------------------------------------------------------------------------- #

# Stores the query as an object that we can print, read from, etc
in_MPH = connection.query(cmd_MPH)  # send the command, and parse the response
in_RPM = connection.query(cmd_RPM)
in_FUEL_LEVEL = connection.query(cmd_FUEL)
in_TEMP_OUTSIDE = connection.query(cmd_TEMP_OUTSIDE)
in_OIL_TEMP = connection.query(cmd_OIL_TEMP)
in_MPG = connection.query(cmd_FUEL_RATE)


# ------------------------------------------------------------------------------------------------------------------- #

# Handy method to print CURRENT_VALUE (or CV) of the object we feed it -- note you must perform a query before feeding

def printout_cv(query):
    for i in range(5):  # Prints the first 5 values -- DEBUGGING TOOL
        print(query.value)
    return


# ------------------------------------------------------------------------------------------------------------------- #

printout_cv(in_RPM)  # Purely for Debugging ATM to test RPM Changes
# print(response.value.to("mph"))  # user-friendly unit conversions  #! Throws an error will investigate in later build!

# Very basic for debug runs
print("End of program")
