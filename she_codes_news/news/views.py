from django.views import generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .models import NewsStory
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    # model = NewsStory
    # ordering = ['-pub_date']

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = NewsStory.objects.order_by('-pub_date')
        context['latest_stories'] = news[:4]
        context['all_stories'] = news[4:]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = "news/story.html"
    context_object_name = "story"

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = "storyForm"
    template_name = "news/createStory.html"
    success_url = reverse_lazy("news:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def FavouriteView(request, pk):
    story = get_object_or_404(NewsStory, id=request.POST.get("news_id"))
    story.favourites.add(request.user)
    return HttpResponseRedirect(reverse("news:story", args=[str(pk)]))