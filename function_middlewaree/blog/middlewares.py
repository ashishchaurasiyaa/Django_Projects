def my_middleware(get_response):
    print("One time initilization")

    def my_function(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response

    return my_function


class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization")

    def __call__(self, request):
        print("This is Before View")
        response = self.get_response(request)
        print("This is after view")
        return response

class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Middleware Initialization brother")

    def __call__(self, request):
        print("This is Brother before view")
        response = self.get_response(request)
        print("This is Brother after view")
        return response

class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Middleware Initialization Father")

    def __call__(self, request):
        print("This is Father Before View")
        response = self.get_response(request)
        print("This is Father after view")
        return response
class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Middleware Initialization Mother")

    def __call__(self, request):
        print("This is Mother Before View")
        response = self.get_response(request)
        print("This is Mother after view")
        return response

