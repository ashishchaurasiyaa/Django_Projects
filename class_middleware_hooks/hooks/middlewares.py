from django.shortcuts import HttpResponse

class MyProcessMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_view(self, *args,**kwargs):
        print("This is Process View - Before view")
        # if we will not pass return NOne the don't will go cloued.
        return None
class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_exception(self,request,exception):
        print("Exception occured")
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        return HttpResponse(msg)

class MyTemplateResponsiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_template_response(self,request,response):
        print("Process Template Response From Middleware")
        response.context_data['name'] = 'Ashish'
        return response