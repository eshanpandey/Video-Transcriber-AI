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
from dotenv import load_dotenv
import requests
import google.generativeai as genai
from .models import ArticlePost
# Create your views here.
load_dotenv()

ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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

# @csrf_exempt
# def generate_transcript(request):
#     if request.method=='POST':
#         try:
#             data=json.loads(request.body)
#             yt_link = data['link']
#         except (KeyError, json.JSONDecodeError):
#             return JsonResponse({'error':'Invalid data sent'}, status=400)
        
#         title=yt_title(yt_link)
#         #getting the transcript from the audio file
#         transcript=get_transcription(yt_link)
#         if not transcript:
#             return JsonResponse({'error':'Transcription failed'}, status=500)
        
#         summary_content=generate_article(transcript)
#         if not summary_content:
#             return JsonResponse({'error':'Article generation failed'}, status=500)
        

#         return JsonResponse({'content':summary_content})


#     else:
#         return JsonResponse({'error':'Ivalid request method'}, status=405)


prompt="""You are a notes maker You will be taking the transcript text
and summarizing the entire video's crux without making it look like a video but a blog article
and providing the important topics and their explanation in points use simple text only like 
 try to write simple paragraphs and points.
 make the language easy to understand for everyone."""


@csrf_exempt
def generate_transcript(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            yt_link = data['link']
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data sent'}, status=400)


        # getting video title
        title = yt_title(yt_link)

        # getting transcript for the video
        transcription = get_transcription(yt_link)
        if not transcription:
            return JsonResponse({'error': " Failed to get transcript"}, status=500)


       
        article_content = generate_article(transcription, prompt)
        if not article_content:
            return JsonResponse({'error': " Failed to generate blog article"}, status=500)

        # save article to database
        new_article_post = ArticlePost.objects.create(
            user=request.user,
            youtube_title=title,
            youtube_link=yt_link,
            generated_content=article_content,
        )
        new_article_post.save()

        # return blog article as a response
        return JsonResponse({'content': article_content})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



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


def generate_article(transcript,prompt):
 model=genai.GenerativeModel("gemini-pro")
 response=model.generate_content(prompt+transcript)
 return response.text


