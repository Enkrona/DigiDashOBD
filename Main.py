# -*- coding: utf-8 -*-

########################################################################
#                                                                      #
# DigiDashOBD: A python digital dash  module derived from Python-OBD   #
#                                                                      #
# Copyright 2004 Donour Sizemore (donour@uchicago.edu)                 #
# Copyright 2009 Secons Ltd. (www.obdtester.com)                       #
# Copyright 2009 Peter J. Creath                                       #
# Copyright 2016 Brendan Whitfield (brendan-w.com)                     #
# Copyright 2016-2017 Bradley Taylor                                   #
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
# import subprocess
import time

connection = obd.OBD()  # auto-connects to USB or RF port

# Commands we wish to utilize/query later on
# Core/Base Info you would want on your dash
cmd_KPH = obd.commands.SPEED  # select an OBD command (sensor) [Speed (I believe it is originally fed in KPH)]
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
""" These queries are a one time query and do NOT automatically update.
    For auto update we must utilize a method that constantly is calling queries.   """
in_KPH = connection.query(cmd_KPH)  # send the command, and parse the response
in_RPM = connection.query(cmd_RPM)
in_FUEL_LEVEL = connection.query(cmd_FUEL)
in_TEMP_OUTSIDE = connection.query(cmd_TEMP_OUTSIDE)
in_OIL_TEMP = connection.query(cmd_OIL_TEMP)
in_MPG = connection.query(cmd_FUEL_RATE)


# print(in_MPH.value.to("mph"))
# ------------------------------------------------------------------------------------------------------------------- #

# Handy method to print CURRENT_VALUE (or CV) of the object we feed it -- note you must perform a query before feeding

def printout_cv(query):
    print str(query)

# ------------------------------------------------------------------------------------------------------------------- #

# Conversion method from KPH to MPH

def kph_to_mph(kph):
    return kph * 0.621371


# ------------------------------------------------------------------------------------------------------------------- #

while in_RPM > 1:
    print ""
    print str(in_RPM) + " RPMs"  # Purely for Debugging ATM to test RPM Changes
    printout_cv(in_KPH)
    printout_cv(in_FUEL_LEVEL)
    print ""
    # getting new values to return
    in_MPH = connection.query(cmd_KPH)  # send the command, and parse the response
    in_RPM = connection.query(cmd_RPM)
    in_FUEL_LEVEL = connection.query(cmd_FUEL)

# print(response.value.to("mph"))  # user-friendly unit conversions  #! Throws an error will investigate in later build!

# Very simply shuts down the Pi if the RPMs = 0, i.e. car is off & has been 3 secs #! dilapadated - will update in later
# builds
timeout = time.time() + 3.0
print type(timeout)
"""
if in_RPM == 0 & time.time() > timeout:
    subprocess.call("./shutdown.sh", shell=True)
    print "Shutting Down Pi"
    """
