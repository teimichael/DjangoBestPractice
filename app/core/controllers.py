from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render


class BaseController:
    """ Base Controller

    Attributes:
        template : HTML template
        context: Context
    """
    template = ''
    context = {}

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
        return render(self.request, self.template, self.context)

    def get(self):
        pass

    def post(self):
        pass

    def forbidden(self):
        return HttpResponseForbidden("Method not allowed")

    def page_not_found(self):
        """ 存在しないページへのリクエスト

        Returns:
            HttpResponseNotFound:
        """
        return HttpResponseNotFound()
