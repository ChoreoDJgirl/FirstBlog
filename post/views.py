from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from post.models import Post 
from django.views.generic.edit import FormView
from post.forms import PostForm 

# Create your views here.
class Home(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostDetail(DetailView):
    template_name = 'post.html'
    context_object_name = 'post'
    model = Post

class NewPost(FormView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)