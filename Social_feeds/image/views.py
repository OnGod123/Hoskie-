# views.py

from django.shortcuts import render, redirect
from django.conf import settings
import os
from .models import Document
from .utils import save_image_with_quality

def upload_document(request):
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
        
        # Use the utility function to save the image with quality preserved
        save_image_with_quality(input_file_path, output_file_path)
        
        # Save the document record in the database
        document = Document(title=original_filename, file_path=output_file_path)
        document.save()
        
        # Optionally, remove the temporary input file if you want to process it differently
        # if os.path.exists(input_file_path):
        #     os.remove(input_file_path)
        
        return redirect('document_list')
    
    return render(request, 'upload.html')

