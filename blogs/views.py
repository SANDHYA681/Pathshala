from django.shortcuts import render, redirect
from django.contrib import messages
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/log-in')
def addBlogPage(request):
    categories = Category.objects.all()
    return render(request, "pages/blogs/addBlogPage.html", {"categories": categories})


def validate_blog(data):
    errors = {}
    title = data.get("title")
    content = data.get("content")
    tags = data.get("tags")
    image = data.get("image")
    attachment = data.get("attachment")

    if len(title) < 3 or len(title) > 50:
        errors["title"] = (
            "The title should be minimum 3 and maximum 50 characters long."
        )

    if len(content) < 10:
        errors["content"] = "The content must be minimum 10 characters long."

    if tags == "":
        errors["tags"] = "At least one tag in required"
    else:
        splitted_tags = tags.split(",")
        for tag in splitted_tags:
            if len(tag.strip()) < 2 or len(tag.strip()) > 15:
                errors["tags"] = "Tag must be at least 3 and maximum 15 character long."
            if len(splitted_tags) > 5:
                errors["tags"] = "Tag must not be more than 5. "

    if image:
        allowed_extensions = ["jpg", "png", "jpeg"]
        if image.size > 5 * 1024 * 1024:
            errors["image"] = "Image size should be less than 5MB."

        image_extension = image.name.split(".")[-1]  # splits the data by '.' and gets the last part

        if image_extension.lower() not in allowed_extensions:
            errors["image"] = (
                f"{image_extension} is not allowed, allowed extensions are .jpg, .png, .jpeg"
            )

    if attachment and attachment.size > 10 * 1024 * 1024:
        errors["attachment"] = "Attachment size should not be greater than 10 MB."

    return errors


def createBlog(request):
    if request.method == "POST":
        data = request.POST.copy()
        data["image"] = request.FILES.get("image")
        data["attachment"] = request.FILES.get("attachment")
        errors = validate_blog(data)
        if errors:
            return render(request, "pages/blogs/addBlogPage.html", {"errors": errors})
        category = Category.objects.get( pk = data['category'] )
        blog = Blog.objects.create(
            title=data["title"],
            content=data["content"],
            image=data["image"],
            attachment=data["attachment"],
            author = request.user, 
            category = category,
        )
        # blog.tags.add(*data['tags'].split(",")) # split() seperates the data and keeps in list and * unwraps the list
        #Alternative Way
        blog.tags.add(*[tag.strip() for tag in data['tags'].split(',')])
        messages.success(request, "Blog Created Successfully!")
        return redirect("/blogs")

def blogDetails(request,id):
    blog = Blog.objects.get(id=id)
    return render( request, 'pages/blogs/blogDetails.html', {"blog": blog})

def editBlog(request, id):
    blog = Blog.objects.get(id=id)
    categories = Category.objects.all()
    tags = "," .join(blog.tags.names())
    return render(request, 'pages/blogs/editBlog.html', {"blog": blog, "categories": categories, 'tags': tags})


def updateBlog(request, id):
  if request.method == "POST":
      data = request.POST.copy()
      data["image"] = request.FILES.get("image")
      data["attachment"] = request.FILES.get("attachment")
      errors = validate_blog(data)
      if errors:
          categories = Category.objects.all()
          tags = data['tags']
          data['category']= Category.objects.get(name = data['category'])
          context= {"errors": errors, "blog":data, "categories":categories, 'tags':tags}
          return render(request, "pages/blogs/editBlog.html",context)
      else:
          blog = Blog.objects.get(pk=id)
          blog.title = data["title"]
          blog.content = data["content"]
          if data['image']:
              blog.image = data["image"]
          if data['attachment']:
              blog.attachment = data["attachment"]
              
          category = Category.objects.get( name = data['category'] )
          blog.category = category
          blog.tags.set([tag.strip() for tag in data['tags'].split(',')])
          blog.save()
          messages.success(request, "Blog Updated Successfully!")
          return redirect(f'/blog/{blog.id}')
          
     