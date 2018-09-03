# This package is for desktop app at Pi
# install those package
# sudo apt-get install python-gtk2
# sudo apt-get install python-webkit
# sudo apt-get install python-gobject


#!/usr/bin/env python
import gtk
import webkit
import gobject

gobject.threads_init()
win = gtk.Window()
bro = webkit.WebView()
bro.open("http://www.google.com")
win.add(bro)
win.show_all()
win.set_title('Drawing Test')
win.set_size_request(640,480)
gtk.main()