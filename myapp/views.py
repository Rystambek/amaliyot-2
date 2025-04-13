from django.shortcuts import render

# Yangiliklar ma'lumotlari
news_data = [
    {"id": 1, "title": "Yangilik 1", "content": "Bu Yangilik 1 ning to'liq matni."},
    {"id": 2, "title": "Yangilik 2", "content": "Bu Yangilik 2 ning to'liq matni."},
    {"id": 3, "title": "Yangilik 3", "content": "Bu Yangilik 3 ning to'liq matni."},
]

def news_list(request):
    return render(request, 'news_list.html', {'news_list': news_data})

def news_detail(request, news_id):
    news = next((item for item in news_data if item["id"] == news_id), None)
    if not news:
        return render(request, '404.html', status=404)
    return render(request, 'news_detail.html', {'news': news})
