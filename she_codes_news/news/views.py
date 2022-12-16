from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .models import NewsStory
from .forms import StoryForm, SearchForm

USER = get_user_model()

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'all_stories'
    # model = NewsStory
    # ordering = ['-pub_date']

    def get_queryset(self):
        '''Return all news stories.'''
        qs = NewsStory.objects.all()

        form = SearchForm(self.request.GET)
        if form.is_valid():
            if author := form.cleaned_data.get('with_author'):
                qs = qs.filter(author=author)
            if search_text := form.cleaned_data.get('search'):
                qs = qs.filter(
                    Q(title__icontains=search_text) |
                    Q(content__icontains=search_text)
                    )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = NewsStory.objects.order_by('-pub_date')
        context['latest_stories'] = news[:4]
        # context['all_stories'] = news
        context['author_list'] = USER.objects.all()
        context['form'] = SearchForm(self.request.GET)
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = "news/story.html"
    context_object_name = "story"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        story_on = get_object_or_404(NewsStory, id=self.kwargs['pk'])
        total_favourites = story_on.total_favourites()

        favourited = False
        if story_on.favourites.filter(id=self.request.user.id).exists():
            favourited = True

        context['total_favourites'] = total_favourites
        context['favourited'] = favourited
        return context

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
    favourited = False
    if story.favourites.filter(id=request.user.id).exists():
        story.favourites.remove(request.user)
        favourited = False
    else:
        story.favourites.add(request.user)
        favourited = True

    return HttpResponseRedirect(reverse("news:story", args=[str(pk)]))