# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Map, online


def create_uk_map():
    map = Map('UK', width=800, height=600)
    map.add('', [], [], maptype='UK_electoral_2016',
            is_visualmap=True, visual_text_color="#000")
    return map


def test_jupyter_display():
    map = create_uk_map()
    html = map._repr_html_()
    assert "UK" in html
    assert "nbextensions/echarts-united-kingdom-js" in html


def test_embeded_html():
    map = create_uk_map()
    html = map.render_embed()
    assert "UK_electoral_2016" in html


def test_jupyter_online_display():
    online()
    map = create_uk_map()
    html = map._repr_html_()
    assert "UK_electoral_2016" in html
    assert "'echarts': 'https://pyecharts.github.io/jupyter-echarts/echarts/echarts.min'" in html  # flake8: noqa
    print(html)
    assert "https://echarts-maps.github.io/echarts-united-kingdom-js/echarts-united-kingdom-js/westminster_2016_uk" in html  # flake8: noqa
