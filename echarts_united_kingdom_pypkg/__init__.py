# flake8: noqa
import os

from echarts_united_kingdom_pypkg._version import __version__
from echarts_united_kingdom_pypkg._version import __author__
from echarts_united_kingdom_pypkg.constants import NM_WESTMINSTER_2016_UK

from lml.plugin import PluginInfo


@PluginInfo('pyecharts_js_extension', tags=['custom'])
class Pypkg():
    def __init__(self):
        __package_path__ = os.path.dirname(__file__)
        self.js_extension_path = os.path.join(
            __package_path__, "resources")
