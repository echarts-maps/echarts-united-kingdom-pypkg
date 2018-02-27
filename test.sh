pip freeze
nosetests --with-coverage --cover-package echarts_united_kingdom_pypkg --cover-package tests  tests docs/source echarts_united_kingdom_pypkg && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
