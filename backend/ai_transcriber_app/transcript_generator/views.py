from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import json
from pytube import YouTube
import os
import assemblyai as aa
import dotenv
from dotenv import load_dotenv
import openai

# Create your views here.
load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

@login_required
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method =='POST':
      username=request.POST['username']
      password=request.POST['password'] 

      user = authenticate(request,username=username,password=password)
      if user is not None:
          login(request,user)
          return redirect('/')
      else:
            error_message = "No such user found recheck credentials"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request,'login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message':error_message})
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html', {'error_message':error_message})
        
    return render(request, 'signup.html')

@csrf_exempt
def generate_transcript(request):
    if request.method=='POST':
        try:
            data=json.loads(request.body)
            yt_link = data['link']
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error':'Invalid data sent'}, status=400)
        
        title=yt_title(yt_link)
        #getting the transcript from the audio file
        transcript=get_transcription(yt_link)
        if not transcript:
            return JsonResponse({'error':'Transcription failed'}, status=500)
        
        summary_content=generate_article(transcript)
        if not summary_content:
            return JsonResponse({'error':'Article generation failed'}, status=500)
        

        return JsonResponse({'content':summary_content})


    else:
        return JsonResponse({'error':'Ivalid request method'}, status=405)




@login_required
def all_scripts(request):
    return render(request,'all-scripts.html')


def user_logout(request):
    logout(request)
    return redirect('/')


def yt_title(link):
    yt=YouTube(link)
    title=yt.title
    return title

def get_transcription(link):
    audio_file=download_audio(link)
    aa.settings.api_key= ASSEMBLYAI_API_KEY
    transcriber=aa.Transcriber()
    transcript=transcriber.transcribe(audio_file)
    os.remove(audio_file)
    return transcript.text



def download_audio(link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=settings.MEDIA_ROOT)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file


def generate_article(transcript):
    openai.api_key =  OPENAI_API_KEY

    prompt = f"Based on the following transcript, write a comprehensive summary and mention key points but do not make it look like a youtube video make it look like a blog article on the topic of the video. \n\n {transcript}\n\nArticle:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )
    generated_content=response.choices[0].text.strip()
    return generated_content
