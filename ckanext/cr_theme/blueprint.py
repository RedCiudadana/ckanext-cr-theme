# encoding: utf-8

import ckan.lib.base as base
import ckan.lib.helpers as helpers
from flask import Blueprint
render = base.render

cr_theme = Blueprint(u'cr_theme', __name__)
