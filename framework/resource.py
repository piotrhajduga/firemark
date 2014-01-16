class APIResource(object):
    def __init__(self, request):
        self.request = request

    def get(self):
        raise NotImplementedError()

    def post(self):
        raise NotImplementedError()

    def put(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()
