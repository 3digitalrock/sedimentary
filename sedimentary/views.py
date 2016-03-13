from django.shortcuts import render
import services

def AboutView(request):
    return render(request, 'about.html')

def ChannelsListView(request):
    channels = services.get_channels()
    
    # This really should be solved in the API
    # For now it works
    for idx, channel in enumerate(channels):
        videos = services.get_channelvideos(channel['uid'])
        channels[idx]['videos'] = videos
        
    template_vars = {
      'pageTitle': 'Channels - 3 Digital Rock Studios',
      'channels': channels,
    }
    return render(request, 'channels_list.html', template_vars)

def HomeView(request):
    trailers = services.get_trailers('home')
    template_vars = {
      'pageTitle': '3 Digital Rock Studios',
      'at_homepage': True,
      'trailers': trailers
    }
    return render(request, 'home.html', template_vars)
