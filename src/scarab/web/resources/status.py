"""
Default status.html resource
"""


from scarab.web.resources import render_template


class StatusResource:
    def on_get(self, req, resp):
        """Returns the status.html page"""
        resp.content_type = 'text/html'
        resp.media = render_template('status.html')