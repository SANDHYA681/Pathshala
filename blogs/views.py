from django.shortcuts import render,redirect
from django.contrib import messages

def addBlogPage(request):
    return render(request, 'pages/blogs/addBlogPage.html')

def validate_blog(data):
    errors={}
    title= data.get('title')
    content= data.get('content')
    tags= data.get('tags')
    image= data.get('image')
    attachment= data.get('attachment')
    if len(title)<3 or len(title)>50:
        errors['title']= 'The title should be minimum 3 and maximum 50 characters long'
    if len(content)<10:
        errors['content']="The content must be minimum 10 characters long "
    if tags == "":
        errors['tags']= "Atleast one tag in required"
        
    else:
        splitted_tags = tags.split(',')
        for tag in splitted_tags:
            if len(tag)<3 or len(tag)>1:
                errors['tags']= "Tag must be at least 3 and max 15 char long"
    if image:
        allowed_extensions = ['.jpg', '.png', '.jpeg']
        if image.size> 5*1024*1024:
            errors['profile_image'] = "Image size should be less than 5MB."
        image_extension = image.name.split('.')[-1] # splits the data by '.' and gets the last part
        if image_extension.lower () not in allowed_extensions:
            errors['profile_image']= f"{image_extension} is not allowed, allowed extensions are .jpg .png, .jpeg"
    if attachment and attachment.size>10*1024*1024:
        errors['attachment'] = "Attachment size should not be gretaer than 10 MB"
    return errors
    

def createBlog(request):
    if request.method =="POST":
        data=request.POST.copy()
        data['image']= request.FILES.get('image')
        data['attachment']=request.FILES.get('attachment')
        errors= validate_blog(data)
        if errors:
            return render (request, 'pages/blogs/addBlogPage.html',{"errors":errors })
        
        messages.success(request, "Blog Created succesfully")
        return redirect('/blogs')