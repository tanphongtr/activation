
from django.utils.deprecation import MiddlewareMixin

# middleware test
class TestMiddleware(MiddlewareMixin):
    # def __init__(self, get_response):
    #     self.get_response = get_response
    #     print('TestMiddleware init')

    # def __call__(self, request):
    #     print('TestMiddleware call')
    #     response = self.get_response(request)
    #     return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print('TestMiddleware process_view')
    #     return None

    # def process_exception(self, request, exception):
    #     print('TestMiddleware process_exception')
    #     return None

    # def process_template_response(self, request, response):
    #     print('TestMiddleware process_template_response')
    #     return response

    def process_response(self, request, response):
        print('TestMiddleware process_response')
        return response

    def process_request(self, request):
        print('TestMiddleware process_request')
        return None
