from django.db import models
# from django.core.files.storage import default_storage
# class User(models.Model): 
#     name = models.CharField(max_length=50) 
#     userProfileImage = models.ImageField(upload_to='profileImages/') 

from storages.backends.gcloud import GoogleCloudStorage
storages = GoogleCloudStorage()
class Upload:
    @staticmethod
    def upload_image(file, filename):
        try:
            target_path = '/images/profilePictures/' + filename
            path = storages.save(target_path, file)
            return storages.url(path)
        except Exception as e:
            print("Failed to upload!")