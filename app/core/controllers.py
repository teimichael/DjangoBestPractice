from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


class BaseController(ModelViewSet):
    """
    Base Controller for restful APIs
    """
    pass


class ViewBaseController:
    """ View Base Controller

    Attributes:
        template : HTML template
        context: Context
    """
    template = ''
    context = {}
    status_code = 200

    def __init__(self, request, **kwargs):
        """ Init BaseController

        Args:
            request: HTTP Request
            **kwargs: Parameters
        """
        self.request = request
        for key in kwargs.keys():
            setattr(self, key, kwargs.get(key))

    @classmethod
    def view(cls, request, **kwargs):
        this = cls(request, **kwargs)
        if request.method == 'GET':
            this.get()
        elif request.method == 'POST':
            this.post()
        return this.response()

    def response(self):
        if self.status_code == 200:
            return render(self.request, self.template, self.context)
        elif self.status_code == HttpResponseBadRequest.status_code:
            return render(self.request, 'error/400.html')
        elif self.status_code == HttpResponseForbidden.status_code:
            return render(self.request, 'error/403.html')
        elif self.status_code == HttpResponseNotFound.status_code:
            return render(self.request, 'error/404.html')
        else:
            return render(self.request, 'error/400.html')

    def get(self):
        pass

    def post(self):
        pass

    def bad_request(self):
        self.status_code = HttpResponseBadRequest.status_code

    def forbidden(self):
        self.status_code = HttpResponseForbidden.status_code

    def not_found(self):
        self.status_code = HttpResponseNotFound.status_code
