import re

from scarab.web.resources import render_template


def test_engine():
    template_str = render_template("status.html")
    assert type(template_str) is str
    assert re.findall(r"<html.*>", template_str)
