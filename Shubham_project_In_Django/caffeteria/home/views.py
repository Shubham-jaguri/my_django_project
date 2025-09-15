from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Order_Menu, Contact
from django.contrib import messages

# Email sending the import the file
# from django.conf import settings
# from django.core.mail import send_mail
# from django.core.mail.message import EmailMessage
# from django.core import mail

# Create your views here.

def index(request):
    
    return render(request, 'index.html')


#SignUP Coding
def SignUp(request):
    
    if request.method == 'POST':
        uname = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        # print(uname,email,password)
        try :
            if User.objects.get(username=uname):
                messages.error(request,"USERNAME IS TAKEN")
                return redirect('/signup')
        
        except:
            pass

        try :
            if User.objects.get(email=email):
                messages.success(request,"Email IS TAKEN")
                return redirect('/signup')
        
        except:
            pass

        myuser = User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,'signup successful')  
        return redirect('/signin') 

    return render(request, 'SignUp_SignIn.html')

# Sign-IN coding
def SignIn(request):
    if request.method == 'POST':
        uname = request.POST.get("name")
        pass1 = request.POST.get("pass")
        myuser = authenticate(username=uname, password=pass1)
        if myuser is not None:
            login(request,myuser)
            
            messages.success(request, 'Login Successfully')
            return redirect('/ind')
        else:
            messages.error(request, 'Invalid Credentails')
            return redirect('/signin')
    return render(request, 'SignUp_SignIn.html')

# Logout 

def LogoutUser(request):
    logout(request)
    messages.info(request,"Logout success")
    return redirect('/signin')

#Show into in the Index1

def index1(request):
    return render(request, 'index1.html')


# Show Menu
def Menu(request):
    return render(request,"Menu.html")

def OrderMenu_Now(request):
    if request.method == "POST":
        fid = request.POST.get("identi")
        fname = request.POST.get("name")
        item = request.POST.get("item")
        address = request.POST.get("address")
        Mob = request.POST.get("mob")
        date_time = request.POST.get("dt")
        query = Order_Menu(User_id=fid, name=fname, select_product=item,Address=address,  Mob_num=Mob, date=date_time )
        query.save()
        messages.success(request, 'Successfully Order ')
    return render(request, 'OrderForm.html')


# Update data in table

def Update_Data(request, id):
    allposts = Order_Menu.objects.get(User_id=id)
    return render(request, 'UpdateForm.html',{'allposts':allposts})

def Upgrade(request):
    if request.method == 'POST':
        data_id = request.POST.get('data_id')
        fname = request.POST.get('name')
        item = request.POST.get('item')
        address = request.POST.get('address')
        mob = request.POST.get('mob')
        dt = request.POST.get('dt')

        obj_update = Order_Menu.objects.get(User_id=data_id)
        obj_update.name = fname
        obj_update.select_product = item
        obj_update.Address = address
        obj_update.Mob_num = mob
        obj_update.date = dt
        obj_update.save()
        messages.success(request, 'Successfully Update ')
        return redirect("/table")

# Delete in table of data
def Delete(request,id):
    allposts=Order_Menu.objects.get(User_id=id)
    allposts.delete()
    return redirect("/table")

# table in show data
def Table_data(request):
    allposts = Order_Menu.objects.all()
    context = {'allposts':allposts}
    return render(request, 'SearchTable.html',context)


# Search in the table

def Table_Search(request):
    allposts = Order_Menu.objects.all()
    if request.method == 'GET':
        st = request.GET.get('search')
        if st!=None:
            n1=Order_Menu.objects.filter(name__icontains=st)
            n2 =Order_Menu.objects.filter(User_id__icontains=st)
            allposts= n1.union(n2)

    return render(request, 'SearchTable.html',{'allposts':allposts })

def ContactUs(request):
    if request.method =="POST":
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        fdes=request.POST.get("txt1")
        query=Contact(name=fname, email=femail, description=fdes)
        query.save()
        #Email sending start from here
        # from_email =settings.EMAIL_HOST_USER
        # connection=mail.get_connection()
        # connection.open()
        # email_message = mail.EmailMessage(f'Email from {fname}', f'UserEmail:{femail}\n\n QUERY:{fdes}',from_email,['err.shivani@gmail.com.com','err.amitjaguri@gmail.com'],connection=connection)
        # connection.send_messages([email_message])
        # connection.close()

        messages.success(request,"Thanks For Reaching Us! We will get back you soon.")
        return redirect('/contact')
    

    return render(request,'Contact.html')
#email coding



