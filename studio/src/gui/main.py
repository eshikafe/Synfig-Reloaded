#!/usr/bin/env python
#
# 	wxSynfig: main.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
# 
#  wxSynfig/main.py: 	Copyright (c) 2017 Austin Aigbe
#  
#  Synfig/main.cpp: 	Copyright (c) 2002-2005 Robert B. Quattlebaum Jr., Adrian Bentley
#  						Copyright (c) 2007, 2008 Chris Moore


import os
import sys
import wx

from app import App
from general import *

if sys.platform == 'win32':
	import locale


# Entry point
if __name__ == '__main__':

	argc = len(sys.argv)

	binary_path = os.path.dirname(os.path.abspath(sys.argv[0]))
	locale_dir = os.path.dirname(os.path.dirname(binary_path)) + os.path.sep + "share" + os.path.sep + "locale"
	if sys.platform == 'win32':
		locale_dir = locale_from_utf8(locale_dir)
	
	#locale.setlocale(locale.LC_ALL, "")
	#gettext.bindtextdomain(GETTEXT_PACKAGE,  locale_dir)
	#gettext.bind_textdomain_codeset(GETTEXT_PACKAGE, "UTF-8")
	#gettext.textdomain(GETTEXT_PACKAGE)


	
	# {
	# 	SmartFILE file(IPC::make_connection());
	# 	if(file)
	# 	{
	# 		print("\n")
	# 		print("   " + _("synfig studio is already running") + "\n\n")
	# 		print("   " + _("the existing process will be used") + "\n\n")
	# 		#// Hey, another copy of us is open!
	# 		#// don't bother opening us, just go ahead and
	# 		#// tell the other copy to load it all up
	# 		if (argc > 1)
	# 			fprintf(file.get(),"F\n");
	# 		while(--argc)
	# 			if((argv)[argc] && (argv)[argc][0]!='-')
	# 				fprintf(file.get(),"O %s\n",etl::absolute_path((argv)[argc]).c_str());
	# 		fprintf(file.get(),"F\n");
	# 		return 0;
	# 	}
	# }
	
	#print("\n")
	#print("   " + _(APP_NAME + " -- starting up application...") + "\n\n")

	try:
		#studio::App app(etl::dirname(binary_path), &argc, &argv);
		app = wx.App(False)
		App(os.path.dirname(binary_path), argc, sys.argv)
		app.MainLoop()

	except Exception, e:
		print(APP_NAME + " Exception: " + "[" +__file__ + "] " + str(e) + "\n")
		sys.exit()
