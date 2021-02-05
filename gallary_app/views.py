from django.shortcuts import render
from .forms import ImageForm, CategoryForm
from .models import Image, ImageCategory

# Create your views here.
add_image = 1

def image_upload_view(request):
    global add_image
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_objects = form.instance
            # Image.objects.all().delete()
            # img_objects = Image.objects.all().values()
            # print(img_objects)
            # print(img_objects[0]['image'])
            return render(request, 'index.html', {'add_image': add_image,'form': form, 'img_objects': img_objects})
    else:
        # Image.objects.all().delete()
        img_obj = Image.objects.all().values()
        # print(len(img_obj)) 
        # print(img_obj)
        form = ImageForm()
        add_image = 1
    return render(request, 'index.html', {'add_image': add_image, 'form': form, 'zero_user' : len(img_obj)})


def add_category(request):
    global add_image
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            # img_obj = form.instance
            # Image.objects.all().delete()
            img_objects = ImageCategory.objects.all().values()
            # print(img_objects)
            # print(img_objects[0]['image'])
            add_image = 1
            return render(request, 'index.html', {'add_image': add_image,'form': form, 'cat_objects': img_objects})
    else:
        # Image.objects.all().delete()
        add_image = 0
        img_obj = ImageCategory.objects.all().values()
        # cat = ImageCategory.objects.all().values()
        # print(cat)

        # print(len(img_obj)) 
        print(img_obj)
        # form = ImageForm()
        c_form = CategoryForm()
    return render(request, 'index.html', {'add_image': add_image, 'c_form':c_form, 'zero_user' : len(img_obj)})

def view_image(request):
    cat_obj = ImageCategory.objects.all().values()

    if request.method == 'POST':
        cat_code = request.POST['category_code']
        img_objects = Image.objects.filter(category_id = cat_code).order_by('-image_id').values()

        context = {'add_image':add_image, 'img_objects':img_objects, 'cat_obj':cat_obj}
        return render(request, 'view_images.html', context=context)
    img_objects = Image.objects.order_by('-image_id').all().values()
    context = {'add_image':add_image, 'img_objects':img_objects, 'cat_obj':cat_obj}
    return render(request, 'view_images.html', context=context)