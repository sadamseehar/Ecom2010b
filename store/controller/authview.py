from django.shortcuts import render,redirect

from django.contrib import messages

from store.forms import CustomUserForm

from django.contrib.auth import authenticate,login,logout


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Succesfullt registerd")
            return redirect('/')
    
    
    context = {'form':form}
    return render(request,"store/auth/register.html",context)



def loginpage(request):
    if request.user.is_authenticated:
        messages.success(request,"already logged in ")
        return redirect("/")

    else :
        if request.method == "POST":
            name = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = name , password = password)

            if user is not None:
                login(request, user)
                messages.success(request,"login successfully")
                return redirect("/")
            else : 
                messages.success(request,"incalid credentials")
                return redirect('/login')
            

        return render(request,"store/auth/login.html")




def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out")
        return redirect("/")

    return redirect("/")