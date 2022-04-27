from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PostCreate, AddPostForm
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage

def index(request):
    return render(request, 'Shop_app/index.html')

def about(request):
    return render(request, 'Shop_app/about.html')

def comment(request):
    comments = Comment.objects.all()
    return render(request, 'Shop_app/comment.html', {'comments': comments})

def report(request):
    sell = Sell.objects.all()
    return render(request, 'Shop_app/report.html', {'sell': sell})

def Bekzatolla(request):
    products = Product.objects.all()
    return render(request, 'Shop_app/Bekzatolla.html', {'products': products})

def secret(request):
    return render(request, 'Shop_app/secret.html')

def create(request):
    uoload = PostCreate()
    if request.method == 'POST':
        uoload = PostCreate(request.POST, request.FILES)
        if uoload.is_valid():
            uoload.save()
            return redirect('comment')
        else:
            return HttpResponse("""Error, reload on <a href = "{{ url: 'comment' }}">reload</a> """)
    else:
        return render(request, 'Shop_app/create.html', {'create': uoload, 'title': 'Create'})

def update_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Comment.objects.get(id = post_id)
    except Comment.DoesNotExist:
        return redirect('comment')
    post_form = PostCreate(request.POST or None, instance = post_sel)
    if post_form.is_valid():
        post_form.save()
        return redirect('comment')
    return render(request, 'Shop_app/create.html', {'create': post_form, 'title': 'Update'})

def delete_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Comment.objects.get(id = post_id)
    except Comment.DoesNotExist:
        return redirect('comment')
    post_sel.delete()
    return redirect('comment')

def show_comment(request, post_slug):
    comment = get_object_or_404(Post, slug = post_slug)
    return render(request, 'Shop_app/comment_number.html', {'comment': comment})

def page(request):
    made_page = Made_Page.objects.all()
    return render(request, 'Shop_app/pages.html', {'made_page': made_page})

def page_slug(request, post_slug):
    made_page = get_object_or_404(Made_Page, slug = post_slug)
    return render(request, 'Shop_app/page.html', {'made_page': made_page})

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('page')
            except:
                form.add_error(None, "Возникла ошибка при добавлении страницы")
    else:
        form = AddPostForm()
    return render(request, "Shop_app/addpage.html", {"form": form})

def send_message(request):
    send_mail("Bekzatolla", "Hello from Shop.kz", "bekzatolla100@gmail.com", ["200103138@stu.sdu.edu.kz"], fail_silently=False, html_message="<b>Hello</b><i> world!</i>")
    return render(request, 'Shop_app/successfull.html')

def send_message_seccond(request):
    email = EmailMessage(
        "Hello",
        "I don/'t understand",
        "bekzatolla100@gmail.com",
        ["bekzatolla200@gmail.com", "200103138@stu.sdu.edu.kz"],
        headers={"Message-ID": "foo"}
    )
    email.attach_file("media/All_Might_hero_half_body.jpg")
    email.send(fail_silently=False)
    return render(request, 'Shop_app/successfull.html')