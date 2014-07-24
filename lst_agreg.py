#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools
import commons
import plugins_agreg

myRequest = LaTeXparser.PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash

# L'ordre dans les plugin est important parce que set_isAgreg retourne un code latex sans les commentaires
# alors que keep_script_marks compte dessus pour faire sa sélection.
myRequest.add_plugin(plugins_agreg.accept_all_input,"medicament")
myRequest.add_plugin(plugins_agreg.keep_script_marks(plugins_agreg.agreg_mark_list),"after_pytex")
myRequest.add_plugin(plugins_agreg.set_isAgreg,"after_pytex")
myRequest.add_plugin(plugins_agreg.set_commit_hexsha,"after_pytex")
myRequest.add_plugin(plugins_agreg.ultimate_git,"before_compilation")

myRequest.original_filename="mazhe.tex"
