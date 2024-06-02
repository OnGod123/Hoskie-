# views.py

from django.shortcuts import render, redirect
from django.conf import settings
import os
from .models import Video
from .utils import save_video_with_quality

def upload_video(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        
        # Use the original file name
        original_filename = myfile.name
        
        # Create the input file path
        input_file_path = os.path.join(settings.MEDIA_ROOT, original_filename)
        
        # Save the uploaded file to the input path
        with open(input_file_path, 'wb+') as destination:
            for chunk in myfile.chunks():
                destination.write(chunk)
        
        # Create the output file path (same as input in this case)
        output_file_path = input_file_path
        
        # Use the utility function to save the video with quality preserved
        save_video_with_quality(input_file_path, output_file_path)
        
        # Save the video record in the database
        video = Video(title=original_filename, file_path=output_file_path)
        video.save()
        
        # Optionally, remove the temporary input file if you want to process it differently
        # if os.path.exists(input_file_path):
        #     os.remove(input_file_path)
        
        return redirect('video_list', video_id=video.id)
    
    return render(request, 'upload.html')

def video_list(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video_list.html', {'video': video})

