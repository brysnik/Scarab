import falcon

from .resources.status import StatusResource

api = falcon.API()
api.add_route('/status', StatusResource())
