import re
from logging import getLogger

from scarab.web.resources import render_template


logger = getLogger(__name__)


def test_engine():
    """Test that the template engine is working"""
    
    template_str = render_template("status.html")
    assert type(template_str) is str
    logger.info(f"Rendered html: {template_str}")
    assert re.findall(r"<html.*>", template_str)
