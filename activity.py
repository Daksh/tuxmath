# -*- coding: UTF-8 -*-
# Copyright 2007-2008 One Laptop Per Child
# Copyright 2007 Gerard J. Cerchio <www.circlesoft.com>
# Copyright 2008 Andrés Ambrois <andresambrois@gmail.com>
# Copyright 2010 Marcos Orfila <www.marcosorfila.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import logging
import sugar.logger
import gtk
import pygtk
from gettext import gettext as _
from sugar.activity.activity import Activity, ActivityToolbox
import pango
import os
import commands
import sys


logger = logging.getLogger('Tuxmath')


class TuxmathStart(Activity):

    def __init__(self, handle):
        # Initialize the parent
        Activity.__init__(self, handle)
        logger.debug('Initiating Tuxmath')
     
        # Set the activity toolbox
        toolbox = ActivityToolbox(self)
        self.set_toolbox(toolbox)

        self.ceibaljam_icon_path = os.getenv("SUGAR_BUNDLE_PATH") + "/images/ceibaljam.png"

	#
	# There's a good explanation of the use of boxes in PyGTK here:
	# http://www.pygtk.org/pygtk2tutorial/sec-DetailsOfBoxes.html
	#
 
        box_canvas = gtk.VBox(False, 0)
        self.set_canvas(box_canvas)


        # Title

        box_title = gtk.VBox(False, 0)
        label_title = gtk.Label(_("Tuxmath"))
        label_title.set_justify(gtk.JUSTIFY_CENTER)
        label_title.modify_font(pango.FontDescription("Arial 22"))

        box_title.add(gtk.Label("\n\n\n"))
        box_title.add(label_title)
        box_title.add(gtk.Label("\n"))

        # Author

        box_author = gtk.VBox(False, 0)
        box_author.add(gtk.Label(""))
        box_author.add(gtk.Label(_("Created by Tux4kids")))
        label_author_url = gtk.Label('<b>http://tux4kids.alioth.debian.org</b>')
        label_author_url.set_use_markup(True)
        box_author.add(label_author_url)

        # Options box

        box_options = gtk.VBox(False, 0)
        label_options = gtk.Label(_("Options:"))
        label_options.set_justify(gtk.JUSTIFY_LEFT)
        self.checkbtn_sound = gtk.CheckButton(label=_("No sound"))
        self.checkbtn_sound.set_active(True)
        self.checkbtn_negatives = gtk.CheckButton(label=_("Include negative numbers"))
        self.checkbtn_negatives.set_active(False)
	# Pack the checkboxes in HBoxes to center them
	hbox1 = gtk.HBox(False, 0)
	hbox1.add(gtk.Label(""))
	hbox1.add(gtk.Label(""))
	hbox1.add(gtk.Label(""))
	hbox1.add(gtk.Label(""))
	hbox1.add(gtk.Label(""))
	hbox1.add(gtk.Label(""))
	hbox1.add(gtk.Label(""))
	hbox1.add(self.checkbtn_sound)
	hbox1.add(gtk.Label(""))
	hbox1.add(gtk.Label(""))
	hbox1.add(gtk.Label(""))
	hbox1.add(gtk.Label(""))
	hbox1.add(gtk.Label(""))
	hbox1.add(gtk.Label(""))
	box_options.add(hbox1)
        #box_options.add(gtk.Label(""))
        #box_options.add(label_options)
        #box_options.add(self.checkbtn_sound)
        #box_options.add(self.checkbtn_negatives)

        # Credits

        box_credits = gtk.VBox(False, 0)
        box_credits.add(gtk.Label(""))
        box_credits.add(gtk.Label(_('Spanish translation and pedagogical evaluation by %(TEACHER)s') % { 'TEACHER': 'Ana Cichero' }))
        label_teacher_email= gtk.Label('<b>ana.cichero@gmail.com</b>')
        label_teacher_email.set_use_markup(True)
        box_credits.add(label_teacher_email)
        box_credits.add(gtk.Label(_('Sugarized by %(SUGARIZER)s') % { 'SUGARIZER': 'Marcos Orfila' }))
        label_sugarizer_website = gtk.Label('<b>http://www.marcosorfila.com</b>')
        label_sugarizer_website.set_use_markup(True)
        box_credits.add(label_sugarizer_website)
        box_credits.add(gtk.Label(""))

        # Footer box (Activities on CeibalJAM! website)

        box_footer = gtk.VBox(False, 0)
        box_footer.add(gtk.Label(""))
        box_footer.add(gtk.Label(_('Find more activities on %(CEIBALJAM)s website:') % { 'CEIBALJAM': 'CeibalJAM!'}))
        label_ceibaljam_website = gtk.Label('<b>http://activities.ceibaljam.org</b>')
        label_ceibaljam_website.set_use_markup(True)
        box_footer.add(label_ceibaljam_website)
        box_footer.add(gtk.Label(""))

        # CeibalJAM! image

        box_ceibaljam_image = gtk.VBox(False, 0)
        image_ceibaljam = gtk.Image()
        image_ceibaljam.set_from_file(self.ceibaljam_icon_path)
        box_ceibaljam_image.pack_end(image_ceibaljam, False, False, 0)

        # Buttons box

        box_buttons = gtk.HBox(False, 0)
        self.button_play = gtk.Button(_("Play"))
        self.button_play.connect("clicked", self._button_play_clicked_cb)
        self.button_exit = gtk.Button(_("Exit"))
        self.button_exit.connect("clicked", self._button_exit_clicked_cb)
        box_buttons.add(gtk.VBox())
        box_buttons.add(self.button_play)
        box_buttons.add(gtk.VBox())
        box_buttons.add(self.button_exit)
        box_buttons.add(gtk.VBox())


	# Get all the boxes together

        box_canvas.pack_start(box_title, False, False, 0)
        box_canvas.pack_start(box_options, False, False, 0)
        box_canvas.pack_end(gtk.Label("\n\n"), False, False, 0)
        box_canvas.pack_end(box_buttons, False, False, 0)
        box_canvas.pack_end(gtk.Label("\n"), False, False, 0)
        box_canvas.pack_end(box_footer, False, False, 0)
        box_canvas.pack_end(box_ceibaljam_image, False, False, 0)
        box_canvas.pack_end(box_credits, False, False, 0)
        box_canvas.pack_end(box_author, False, False, 0)


        self.button_play.grab_focus()
        self.show_all()


    def create_script(self, script_path):
       """Create the script to run the program"""

       # In the future, some options to be included in the tuxmath script (like "--nosound")
       # could be selected by the user.
       script_text = "exec $SUGAR_BUNDLE_PATH/bin/tuxmath --homedir $TUX_HOMEDIR --fullscreen"

       if (self.checkbtn_sound.get_active()):
           script_text += " --nosound "
       """
       if (self.checkbtn_negatives.get_active()):
           script_text += " --allownegatives "
       """

       f = open(script_path, 'w')
       f.write(script_text)
       f.close()
       os.chmod(script_path, 0755)

 
    def _button_play_clicked_cb(self, widget):
       self.create_script(os.getenv("TUXMATH_SCRIPT"))
       sys.exit(0)


    def _button_exit_clicked_cb(self, widget):
       sys.exit(0)


