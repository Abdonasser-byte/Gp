from django.shortcuts import render
from .forms import ImageForm
from matplotlib import pyplot as plt
from PIL import Image
import cv2
import numpy as np
from .savedmode import predict
import io
def image_upload_view(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            curimage = request.FILES['image']
            ret = Image.open(curimage)
            retanother = predict(ret)            
            img_obj = form.instance
            return render(request,"image_form.html", {'form': form, 'img_obj': img_obj })
    else:
        form = ImageForm()
    return render(request,"image_form.html", {'form': form})