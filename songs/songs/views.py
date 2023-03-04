from django.shortcuts import render
from django.shortcuts import redirect
from . models import *
from  django.core.files.storage import FileSystemStorage
from django.conf import settings

def home(request):
    m_id=request.session.get('uid')
    song=add_song.objects.filter(pk=m_id)
    return render(request,'index.html',{'song':song})

def register(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        place=request.POST.get('place')
        img=request.FILES['img']
        a=FileSystemStorage()
        b=a.save(img.name,img)
        if password1 == password2:
            reg=user_register(name=name , email=email,password1=password1 ,password2=password2, place=place,img=img)
            reg.save()
            return redirect(loguser)
    return render(request, 'register.html')

def loguser(request):
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    if email == 'admin@gmail.com' and password1 =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] ='admin'
        return render(request,'index.html')

    elif user_register.objects.filter(email=email,password1=password1).exists():
        udetails=user_register.objects.get(email=request.POST['email'],password1=password1)
        if udetails.password1 == request.POST['password1']:
            request.session['uid'] = udetails.id
            request.session['name'] = udetails.name
            request.session['email'] = email
            request.session['user'] = 'user'
            return render(request,'index.html')

    else:
        return render(request, 'login.html')

def userlogout(request):
    request.session.delete()
    return redirect("/")


    

def addsong(request):
    m_id=request.session['uid']
    if request.method == 'POST':
        songname=request.POST.get('songname')
        descp=request.POST.get('descp')
        artistname=request.POST.get('artistname')
        audio=request.FILES['audio']
        cover=request.FILES['cover']
        a=FileSystemStorage()
        b=a.save(audio.name,audio)
        c=a.save(cover.name,cover)

        reg=add_song(songname=songname ,descp=descp,artistname=artistname,m_id=m_id,audio=audio,cover=cover)
        reg.save()
        return redirect("/")
    return render(request,'addsong.html')

def songdetails(request,id):
    dsong=add_song.objects.get(pk=id)
    return render(request,'songdetails.html',{'dsong':dsong})

def songupdate(request,id):
    upsong=add_song.objects.get(pk=id)
    return render(request,'updatesong.html',{'upsong':upsong})
    
def songuupdate(request,id):
    m_id=request.session['uid']
    if request.method == 'POST':
        songname=request.POST.get('songname')
        descp=request.POST.get('descp')
        artistname=request.POST.get('artistname')
        audio=request.POST.get('audio')
        cover=request.POST.get('cover')
    
        reg=add_song(songname=songname ,descp=descp,artistname=artistname,m_id=m_id,audio=audio,cover=cover,id=id)
        reg.save()
        return redirect("/")
    
def songdelete(request,id):
    song=add_song.objects.get(pk=id)
    song.delete()
    return redirect("/")

def profile(request):
    m_id=request.session['uid']
    user=user_register.objects.get(pk=m_id)
    return render(request,'profile.html',{'user':user})