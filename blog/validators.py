from django.core.exceptions import ValidationError

def valid_images(value):
    file = str(value)
    if file.endswith('.jpg') != True and file.endswith('.png') != True and file.endswith('.vmw') != True:
        raise ValidationError(f"Your file type ->({file[file.find('.'):]}) | Valid file types ->(.jpg, .png, .vmw)")
    else:
        return file