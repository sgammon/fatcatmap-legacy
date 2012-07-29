# -*- coding: utf-8 -*-
## Project Models Init

###### ====== Shortcuts ====== ######
from google.appengine.ext import ndb
from google.appengine.api import files
from google.appengine.ext import blobstore
from google.appengine.ext.ndb import polymodel


class Model(ndb.Model):
	pass


class Expando(ndb.Expando):
	pass


PolyModel = polymodel.PolyModel
