from core.controllers import BaseController
from service.models.user import User


class UserController(BaseController):
    template = 'user.html'

    def post(self):
        name = self.request.POST.get('name', '')
        age = self.request.POST.get('age', '0')
        try:
            age = int(age)
        except ValueError:
            return self.forbidden()
        user = User(name=name, age=age)
        user.save()

    def get(self):
        query_fields = ['id', 'name', 'age']
        self.context['users'] = list(User.objects.values(*query_fields))
