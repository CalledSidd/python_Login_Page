from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if 'username' in request.session:  
        print("IN username")          
        return redirect(home)
    if request.method == 'POST':
        print("Request method")
        pass_wrd = request.POST['pwd']
        u_name = request.POST['un']
        user = authenticate(username=u_name, password=pass_wrd)
        if user is not None:
            request.session['username'] = u_name
            return redirect(home)
    return render(request,'index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'username' in request.session:
        print("redirect home is working")
        return render(request,'home.html')
    else:
          print("redirect index is working")
          return redirect(index)

def logout(request):
    request.session.flush()
    print("This is working or maybe not...")
    return redirect(index)