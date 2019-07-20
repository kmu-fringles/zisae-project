from django.shortcuts import render,redirect,get_object_or_404
from .models import Find
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    
    finds = Find.objects.all()
    find_list = Find.objects.all()
    paginator = Paginator(find_list, 3)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request,'FindTHeRoom/home.html',{'finds':finds, 'page_posts' : page_posts})

def new(reqest):
    return render(request,'FindTHeRoom/new.html')

def detail(request, find_id) :
    find_detail = get_object_or_404(Board, pk = find_id) #pk는 모델에서 찍어낸 객체 구분자
    return render(request, 'detail.html', {'find' : find_detail})


def create(request):
   find=Find()
   find.title=request.GET['title']
   find.body = request.GET['body']
   find.pub_date = timezone.datetime.now()
   find.writer = request.GET['writer']
   find.save()
   return redirect('/find/' + str(find.id)) #redirect는 요청이 오면 저쪽 url로 보내줘


def update(request,find_id):
    update_find = Find.objects.get(id = find_id)
    update_find.title = request.POST['title']
    update_find.body = request.POST['body']
    update_find.writer = request.POST['writer'] 
    update_find.save()
    return redirect('findtheroom_home')


def delete(request,find_id):
    delete_post = Find.objects.get(id=find_id)
    delete_post.delete()
    return redirect('findtheroom_home')

def edit(request, find_id) :
    edit_post = Board.objects.get(id=find_id)
    return render(request, 'FindTHeRoom/edit.html', {'find' : edit_find})
