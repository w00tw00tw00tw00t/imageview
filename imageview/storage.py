from django.core.files.storage import FileSystemStorage
import os


# Credits http://stackoverflow.com/a/15900958
# noinspection PyAbstractClass
class MediaFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        return name

    def _save(self, name, content):
        if self.exists(name):
            # if the file exists, do not call the superclasses _save method
            return name
        # if the file is new, DO call it
        return super(MediaFileSystemStorage, self)._save(name, content)


def media_file_name(instance, filename):
    h = instance.md5sum
    basename, ext = os.path.splitext(filename)
    return os.path.join('mediafiles', h[0:1], h[1:2], h + ext.lower())
