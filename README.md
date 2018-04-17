# Install
To install django-modeltocsv, just clone this repo in your computer and copy modeltocsv folder to your django project.

### Something like this:
```
$ git clone https://github.com/andrelramos/django-modeltocsv.git
$ mv django-modeltocsv/modeltocsv/ your-project-dir/
```

# Usage
In your view write:
```
from .models import MyModel
from modeltocsv import modeltocsv

def myview(request):
	return modeltocsv(model=MyModel, filename='file', exclude_fields=['id'], queryset=MyModel.objects.all()
```
