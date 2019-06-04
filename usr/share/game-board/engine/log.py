#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  log.py
#  
#  Copyright 2019 Thomas Castleman <contact@draugeros.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
import sys
import os
log_type = sys.argv[1]
log_type = str(log_type)
log_type = log_type.upper()
log_message = sys.argv[2]
log_message = str(log_message)
logging_file = sys.argv[3]
logging_file = str(logging_file)
if not os.path.exists('/tmp/game-board'):
	os.makedirs("/tmp/game-board")
if log_type == "ERROR":
	error = open('/tmp/game-board/error.log', "a")
	error.write("%s from %s: %s\n" % (log_type,logging_file,log_message))
	error.close()
	print("%s from %s: %s\n" % (log_type,logging_file,log_message))
elif log_type == "GENERIC" or log_type == "LOG":
	log = open('/tmp/game-board/generic.log', "a")
	log.write("%s from %s: %s\n" % (log_type,logging_file,log_message))
	log.close()
	print("%s from %s: %s\n" % (log_type,logging_file,log_message))
elif log_type == "WARNING":
	warn = open('/tmp/game-board/warnings.log', "a")
	warn.write("%s from %s: %s\n" % (log_type,logging_file,log_message))
	warn.close()
	print("%s from %s: %s\n" % (log_type,logging_file,log_message))
else:
	log = open('/tmp/game-board/generic.log', "a")
	log.write("%s from %s: %s\n" % (log_type,logging_file,log_message))
	log.close()
	print("%s from %s: %s\n" % (log_type,logging_file,log_message))
