# Copyright (c) 2020 Trong Viet Dao & Dennis Walter
# The RevolverHeadPlugin is released under the terms of the AGPLv3 or higher.

from . import RevolverHeadPlugin

def getMetaData():
    return {}

def register(app):
    return {"extension": RevolverHeadPlugin.RevolverHeadPlugin()}