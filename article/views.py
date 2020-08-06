from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,redirect,get_object_or_404
from .models import article
from django.http import HttpResponse
from .form import addar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
def listarticles(request):
    x=article.objects.all().order_by('-date')
    query=request.GET.get('Q')
    if(query):
        x=x.filter(Q(title__icontains=query)|
                   Q(body__icontains=query) )
    paginator = Paginator(x, 3)
    page = request.GET.get('page')
    x = paginator.get_page(page)
    return render(request,'articles.html',{'x':x})

def art(request,id):
    x=article.objects.get(id=id)
    return render(request,'article.html',{'x':x})


@login_required(login_url='system:login')
def deletear(request,id):
    x=article.objects.get(id=id)
    x.delete()
    return redirect('/articles/')

@login_required(login_url='system:login')
def editar(request,id):
    x=article.objects.get(id=id)
    if request.method=='GET':
        form=addar(instance=x)
    else:
        form=addar(request.POST,request.FILES,instance=x)
        try:
            if form.is_valid():
                form.save()
                return redirect('/articles/')
        except Exception as e:
            return HttpResponse(e)
    return render(request,'edit.html',{'form':form})

@login_required(login_url='system:login')
def addart(request):
    if request.method=='GET':
        form=addar()
    else:
        form=addar(request.POST,request.FILES)
        if form.is_valid():
            u=form.save(commit=False)
            u.User=request.user
            u.save()
            return redirect('/articles/')
    return render(request,'addart.html',{'form':form})


def searart(request):
    query=request.GET.get('q',None)
    qs=article.objects.all()
    if query is not None:
        qs=qs.filter(title___icontains=query)
    return render(request,'articles.html',{'query':qs})
