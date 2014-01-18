from json import dumps
from pyramid.view import view_config


class APIResource(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET')
    def _read(self):
        return self.read(self.request)

    @view_config(request_method='POST')
    def _create(self):
        return self.create(self.request)

    @view_config(request_method='PUT')
    def _update(self):
        return self.update(self.request)

    @view_config(request_method='DELETE')
    def _delete(self):
        return self.delete(self.request)

    def read(self, request):
        raise NotImplementedError()

    def create(self, request):
        raise NotImplementedError()

    def update(self, request):
        raise NotImplementedError()

    def delete(self, request):
        raise NotImplementedError()

    def _prepare_response(response_dict):
        return dumps(response_dict)
