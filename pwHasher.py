#!/usr/bin/env python
#
#
#    pwHasher - Easily hash text
#    Copyright (C) 2015 Gabe Guillen - gabe@lovesmeat.com
#
#    ####################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import signal
import crypt
import getpass


def program():
    while True:
        print "Available hash methods:"

        for i in range(len(crypt.methods)):
            print str(i) + '. ', crypt.methods[i].name
        try:
            raw_selection = raw_input("Choose a hash method [0]: ")

            if len(raw_selection) == 0:
                selection = 0
            else:
                selection = int(raw_selection)

            if len(crypt.methods) > selection >= 0:
                break
            else:
                raise Exception()
        except Exception:
            print "Invalid selection, try again\n"

    password = getpass.getpass()

    print "Hash:", crypt.crypt(password,
                               crypt.mksalt(crypt.methods[selection]))


def exit_gracefully(signal, frame):
    print ""
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_gracefully)
    program()
