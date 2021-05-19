from GoogleNews import GoogleNews                       #Подключаем библиотекку

google_news = GoogleNews(period ="12h", lang = "eng")   #Период новостей
google_news.search("Android 12")                        #Что искать
result = google_news.result()                           #Результат

for item in result:                                     #Цикл
    print(f"title: {item['title']}")                    #Название заголовка
    print(f"date/Time: {item['date']}")                 #Дата и время
    print(f"description: {item['desc']}")               #Самое описание
    print(f"link: {item['link']}")                      #Сама ссылка на источник
    print("*" * 150)                                    #Отделить строчку
