from .models import Topic

def navbar_data(request):
    topics = Topic.objects.all()
    return {'topics': topics}

