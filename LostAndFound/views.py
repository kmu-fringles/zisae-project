from django.shortcuts import render, get_object_or_404, redirect
from .models import LostAndFound
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import CommentForm

# Create your views here.
def home(request) :
    losts = LostAndFound.objects
    lost_list = LostAndFound.objects.all()
    paginator = Paginator(lost_list, 9)
    page = request.GET.get('page')
    page_losts = paginator.get_page(page)
    return render(request, 'lostandfound/home.html', {'losts' : losts, 'page_losts' : page_losts})

def detail(request, lost_id) :
    lost_detail = get_object_or_404(LostAndFound, pk = lost_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.instance.lost_id = lost_id
        if comment_form.is_valid():
            comment = comment_form.save()

    comment_form = CommentForm()
    comments = lost_detail.comments.all()

    return render(request, 'lostandfound/detail.html', {'lost': lost_detail, "comments" :comments, "comment_form":comment_form})

def new(request) :
    return render(request, 'lostandfound/new.html')

def create(request) :
    if request.method == 'POST' and request.FILES['image']:
        lost = LostAndFound()
        lost.title = request.POST['title']
        lost.writer = request.POST['writer']
        lost.pub_date = request.POST['pub_date']
        lost.body = request.POST['body']
        lost.image= request.FILES['image']
        lost.save()
    return redirect('/lostandfound/'+str(lost.id))

def delete(request, lost_id) :
    delete_lost = LostAndFound.objects.get(id=lost_id)
    delete_lost.delete()
    return redirect('lostandfound_home')

def edit(request, lost_id) :
    edit_lost = LostAndFound.objects.get(id = lost_id)
    return render(request, 'lostandfound/edit.html', {'lost': edit_lost})

def update(request, lost_id) :
    if request.method == 'POST' and request.FILES['image']:
        update_lost = LostAndFound.objects.get(id = lost_id)
        update_lost.title = request.POST['title']
        update_lost.writer = request.POST['writer']
        update_lost.pub_date = request.POST['pub_date']
        update_lost.body = request.POST['body']
        update_lost.image = request.FILES['image']
        update_lost.save()
        return redirect('lostandfound_home')
