from django.core.exceptions import ValidationError

def validate_minimum_size(width=None, height=None):
    def validator(image):
        error = False
        if width is not None and image.width < width:
            error = True
        if height is not None and image.height < height:
            error = True
        if error:
            raise ValidationError(
                [f'Size should be at least {width} x {height} pixels.']
            )

    return validator


def validate_video_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.MPEG-4', '.WEBM', '.WMV', '.AVI', '.AVCHD', '.FLV']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


