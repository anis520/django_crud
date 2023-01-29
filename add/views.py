from django.shortcuts import render,redirect
from .forms import Shop_add
from .models import Shop_data
from django.contrib import messages
# Create your views here.
def add(req):
   if req.method=='POST':
    fm=Shop_add(req.POST)
    name=req.POST['name']
    brand=req.POST['brand']
    slug=req.POST['slug']
    price=req.POST['price']
    add=Shop_data(name=name,brand=brand,slug=slug,price=price)
    add.save()
    fm=Shop_add()

    


   else:
    fm=Shop_add()
   data=Shop_data.objects.all()
   return render(req,'add/add.html',{'form':fm,'da':data})

# delete veiws fun
def delete_data(req,id):
  de=Shop_data(id=id)
  de.delete()
  fm=Shop_add()
  data=Shop_data.objects.all()
  # messages.add_message(req,messages.SUCCESS,f'you data{de.name} has been deleted')
  messages.info(req,'data deleted !!')
  return redirect(add)


# veiw data 

def see_data(req,id):
  si=Shop_data.objects.get(id=int(id))
  fm=Shop_add()
  data=Shop_data.objects.all()
  print(si)
  
  return render(req,'add/single.html',{'form':fm,'da':data,'si':si})



# edit data 

def edit_data(req,id):
  if req.method =="POST":       
   pi =Shop_data.objects.get(id=int(id))
   fm=Shop_add(req.POST,instance=pi)
   fm.save()
   return redirect(add) 
  else:
   ed=Shop_data.objects.get(id=int(id))
   fm=Shop_add(instance=ed)
  data=Shop_data.objects.all()
  return render(req,'add/add.html',{'form':fm,'da':data})
    