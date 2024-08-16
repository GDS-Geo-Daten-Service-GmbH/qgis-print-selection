# -*- coding: utf-8 -*-
"""
PrintSelection

 Outputs selected features ordered by layer to text console.
                              -------------------
        begin                : 2024-07-30
        copyright            : (C) 2024 by Andreas Steffens (GDS Geo Daten Service GmbH)
        email                : a.steffens@gds-team.de
 /***************************************************************************
"""

__author__ = 'Andreas Steffens'
__date__ = '30/7/2024'
__copyright__ = 'Copyright 2024, Andreas Steffens (GDS Geo Daten Service GmbH)'

import os
import locale
import re
from enum import Enum
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtGui import *
from qgis.PyQt import uic
from qgis.gui import *
from qgis.core import *

class PrintSelection(QWidget):

    def __init__(self, iface):
        super().__init__()

        self.iface = iface

    def initGui(self):
        self.iface.mapCanvas().selectionChanged.connect(self.onSelectionChanged)

    def unload(self):
        self.iface.mapCanvas().selectionChanged.connect(self.onSelectionChanged)

    def onSelectionChanged(self, layer):
        QgsMessageLog.logMessage(str(layer.selectedFeatureCount()) + " in Ebene '" + layer.name()  + "' ausgewählt!", tag="Print Selection", level=Qgis.MessageLevel.Info)

