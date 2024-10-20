from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from PIL import Image
from CancerDiagnoser import Prediction
from mental_health import testing
from disease import chatbot_diagnose

def index(request):
    return render(request,'index.html')
def result(request):
    return render(request,'result.html')
def disease(request):

    if request.method == "POST":
        # Extract the message from the POST request
        message = request.POST.get("message")
        
        # # Process the message and generate a response
        # # Here you can add logic to handle the message and create a response
        response_message = chatbot_diagnose.predictor(message)  # Example response
        # # Return the response as JSON
        return JsonResponse({'response': response_message})
    return render(request,'disease.html')
def mental(request):

    if request.method == "POST":
        # Extract the message from the POST request
        message = request.POST.get("message")
        
        # Process the message and generate a response
        # Here you can add logic to handle the message and create a response
        response_message = testing.predictor(message)  # Example response
        # Return the response as JSON
        return JsonResponse({'response': response_message})
    return render(request,'mental.html')
def brain_cancer(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()

            # Optionally, open and process the uploaded image using Pillow
            img = Image.open(image_instance.image.path)

            # Do any image processing here (e.g., resizing, filtering)
            img = img.resize((300, 300))  # Resize as an example

            # Save the processed image back (overwrites the original)
            img.save(image_instance.image.path)

            result=Prediction.predict_brain_cancer(image_instance.image.path)
            if result[1] > 0.75:
                type=f'Brain Tumor Prediction: {result[0]} (Confidence: {result[1]:.2f})'
            else:
                type=f'Brain Tumor Prediction: Confidence too low (Confidence: {result[1]:.2f})'
            return render(request,'result.html',{'type':type,'details':result[2]})# Redirect to a success page
    else:
        form = ImageUploadForm()
    return render(request,'brain_cancer.html', {'form': form})
def blood_cancer(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()

            # Optionally, open and process the uploaded image using Pillow
            img = Image.open(image_instance.image.path)

            # Do any image processing here (e.g., resizing, filtering)
            img = img.resize((300, 300))  # Resize as an example

            # Save the processed image back (overwrites the original)
            img.save(image_instance.image.path)

            result=Prediction.predict_blood_cancer(image_instance.image.path)
            if result[1] > 0.70:
                type=f'Blood Cancer Prediction: {result[0]} (Confidence: {result[1]:.2f})'
            else:
                type=f'Blood Cancer Prediction: Confidence too low (Confidence: {result[1]:.2f})'
            return render(request,'result.html',{'type':type,'details':result[2]})# Redirect to a success page
    else:
        form = ImageUploadForm()
    return render(request,'blood_cancer.html', {'form': form})
def lung_cancer(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()

            # Optionally, open and process the uploaded image using Pillow
            img = Image.open(image_instance.image.path)

            # Do any image processing here (e.g., resizing, filtering)
            img = img.resize((300, 300))  # Resize as an example

            # Save the processed image back (overwrites the original)
            img.save(image_instance.image.path)
            result=Prediction.predict_lung_cancer(image_instance.image.path)
            if result[1] > 0.80:
                type=f'Lung Cancer Prediction: {result[0]} (Confidence: {result[1]:.2f})'
            else:
                type=f'Lung Cancer Prediction: Confidence too low (Confidence: {result[1]:.2f})'
            return render(request,'result.html',{'type':type,'details':result[2]})# Redirect to a success page
    else:
        form = ImageUploadForm()
    return render(request,'lung_cancer.html', {'form': form})
def kidney_cancer(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()

            # Optionally, open and process the uploaded image using Pillow
            img = Image.open(image_instance.image.path)

            # Do any image processing here (e.g., resizing, filtering)
            img = img.resize((300, 300))  # Resize as an example

            # Save the processed image back (overwrites the original)
            img.save(image_instance.image.path)

            result=Prediction.predict_kidney_cancer(image_instance.image.path)
            if result[1] > 0.80:
                type=f'Kidney Cancer Prediction: {result[0]} (Confidence: {result[1]:.2f})'
            else:
                type=f'Kidney Cancer Prediction: Confidence too low (Confidence: {result[1]:.2f})'
            return render(request,'result.html',{'type':type,'details':result[2]})# Redirect to a success page
    else:
        form = ImageUploadForm()
    return render(request,'kidney_cancer.html', {'form': form})
def skin_cancer(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()

            # Optionally, open and process the uploaded image using Pillow
            img = Image.open(image_instance.image.path)

            # Do any image processing here (e.g., resizing, filtering)
            img = img.resize((300, 300))  # Resize as an example

            # Save the processed image back (overwrites the original)
            img.save(image_instance.image.path)

            result=Prediction.predict_skin_cancer(image_instance.image.path)
            if result[1] > 0.70:
                type=f'Skin Cancer Prediction: {result[0]} (Confidence: {result[1]:.2f})'
            elif result[1]<0.30:
                type=f'Skin Cancer Prediction: Benign (Confidence: {result[1]:.2f})'
            else:
                type=f'Skin Cancer Prediction: Confidence too low (Confidence: {result[1]:.2f})'
            return render(request,'result.html',{'type':type,'details':result[2]})# Redirect to a success page
    else:
        form = ImageUploadForm()
    return render(request,'skin_cancer.html', {'form': form})
def hospitals_nearby(request):
    return render(request,'hospitals_nearby.html')
