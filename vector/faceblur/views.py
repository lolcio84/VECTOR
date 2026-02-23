import cv2
import os
import json
import base64
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def blur(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        
        # Zapis tymczasowy
        filename = fs.save(uploaded_file.name, uploaded_file)
        path = fs.path(filename)
        
        try:
            img = cv2.imread(path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces_detected = face_cascade.detectMultiScale(gray, 1.1, 4)

            faces_list = []
            for (x, y, w, h) in faces_detected:
                faces_list.append({'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)})

            # Zamiana obrazu na tekst (Base64)
            _, buffer = cv2.imencode('.jpg', img)
            encoded_string = base64.b64encode(buffer).decode('utf-8')
            
            context['faces_json'] = json.dumps(faces_list)
            context['image_base64'] = f"data:image/jpeg;base64,{encoded_string}"

        finally:
            # Usuwamy plik natychmiast - obrazek "żyje" już tylko w zmiennej context
            if os.path.exists(path):
                os.remove(path)

    return render(request, 'blur.html', context)

def hub(request):
    return render(request, "hub.html")