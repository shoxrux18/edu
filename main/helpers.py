import os,datetime,random

def video_upload_to(instance,filename):

    _,ext = os.path.splitext(filename)
    
    
    
    return "{:%Y}/{:%m}/{:%Y-%m-%d-%H-%M-%S-%f}{}{}".format(
        datetime.datetime.now(),
        datetime.datetime.now(),
        datetime.datetime.now(),
        random.randint(10000000,999999999),
        ext.lower()
    )

def image_upload_to(instance,filename):
    
    _,ext = os.path.splitext(filename)
    
    
    
    return "{:%Y}/{:%m}/{:%Y-%m-%d-%H-%M-%S-%f}{}{}".format(
        datetime.datetime.now(),
        datetime.datetime.now(),
        datetime.datetime.now(),
        random.randint(10000000,999999999),
        ext.lower()
    )