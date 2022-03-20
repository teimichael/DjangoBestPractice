from django.core.files.storage import FileSystemStorage

from core.controllers import ViewBaseController


class UploadViewController(ViewBaseController):
    template = 'upload.html'

    def post(self):
        image_file = self.request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        self.context['image_url'] = image_url
        print(image_url)
