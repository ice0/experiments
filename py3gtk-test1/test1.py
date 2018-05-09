import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#builder = Gtk.Builder()
#builder.add_from_file("ExportDialog.glade")
builder = Gtk.Builder.new_from_file("ExportDialog2.glade")
class Handler:
    def on_destroy(self, *args):
        print("Close!")
        Gtk.main_quit()

    def onButtonPressed(self, button):
        print("Hello World!")

builder.connect_signals(Handler())

def quit():
    x = 5
    print("Quit!")

#builder.connect_signals(
#    {
#        "on_close": quit
#    })

window = builder.get_object("window1")
window.show_all()

Gtk.main()

#win = Gtk.Window()
#win.connect("destroy", Gtk.main_quit)
#win.show_all()
#Gtk.main()