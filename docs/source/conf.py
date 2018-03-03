# -*- coding: utf-8 -*-
DESCRIPTION = (
    'pyecharts map extension - united kingdom maps - python package' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'echarts-united-kingdom-pypkg'
copyright = u'2018 pyecharts dev team'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'echarts-united-kingdom-pypkgdoc'
latex_elements = {}
latex_documents = [
    ('index', 'echarts-united-kingdom-pypkg.tex',
     'echarts-united-kingdom-pypkg Documentation',
     'pyecharts dev team', 'manual'),
]
man_pages = [
    ('index', 'echarts-united-kingdom-pypkg',
     'echarts-united-kingdom-pypkg Documentation',
     [u'pyecharts dev team'], 1)
]
texinfo_documents = [
    ('index', 'echarts-united-kingdom-pypkg',
     'echarts-united-kingdom-pypkg Documentation',
     'pyecharts dev team', 'echarts-united-kingdom-pypkg',
     DESCRIPTION,
     'Miscellaneous'),
]
