from django.http import StreamingHttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Feed, Blog, Video, Image

class StreamData(APIView):
    def get(self, request):
        # Function to generate data in chunks
        def generate_data():
            # Accessing all blogs
            blogs = Blog.objects.all()
            for blog in blogs:
                yield f"Blog: {blog.title} - {blog.content}\n"

            # Accessing all videos
            videos = Video.objects.all()
            for video in videos:
                yield f"Video: {video.title} - {video.video_url}\n"

            # Accessing all images
            images = Image.objects.all()
            for image in images:
                yield f"Image: {image.title} - {image.image.url}\n"

            # Accessing all feeds
            feeds = Feed.objects.all()
            for feed in feeds:
                yield f"Feed: User {feed.user.username} at {feed.timestamp}\n"
                if feed.blog:
                    yield f" - Blog: {feed.blog.title}\n"
                if feed.video:
                    yield f" - Video: {feed.video.title}\n"
                if feed.image:
                    yield f" - Image: {feed.image.title}\n"

        # Stream data using StreamingHttpResponse
        response = StreamingHttpResponse(generate_data(), content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="data.txt"'
        return response

# Instantiate your models (this part would typically be done elsewhere, such as in a management command or an initial data setup script)
user = User.objects.first()  # Assuming you have at least one user
if user:
    blog = Blog.objects.create(title='My Blog', content='This is a blog post.')
    video = Video.objects.create(title='My Video', video_url='http://example.com/video.mp4')
    image = Image.objects.create(title='My Image', image='path/to/image.jpg')

    feed = Feed.objects.create(user=user, blog=blog, video=video, image=image)

