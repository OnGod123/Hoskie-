from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
import os

@login_required  # Restrict access to logged-in users
def create_blog_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        # Generate a unique filename (optional)
        filename = f"{title}.txt"  # Example: using title with .txt extension

        # Create a temporary directory to store the file (optional for security)
        # temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
        # os.makedirs(temp_dir, exist_ok=True)  # Create directory if it doesn't exist

        # Create the text file with the content
        with open(filename, 'w', encoding='utf-8') as text_file:
            text_file.write(content)

        # Save the filename (path) to a field in your model (optional)
        # new_post = BlogPost.objects.create(
        #     author=request.user,
        #     title=title,
        #     content=content,
        #     content_file=filename  # Assuming you have a 'content_file' field
        # )

        # Alternatively, store the file path elsewhere (e.g., database)

        # Redirect to a success page or blog detail page after successful creation
        return redirect('blog_detail', slug=new_post.slug)  # Assuming you have a 'blog_detail' URL pattern
    else:
        # Render the form for creating a new blog post
        return render(request, 'create_post.html')

