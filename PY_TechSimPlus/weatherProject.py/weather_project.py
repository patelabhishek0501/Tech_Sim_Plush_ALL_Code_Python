import requests
from tkinter import Tk,Entry,StringVar,Button,Label
def get_weather(city):
    api_key = "77213f031cd22011bbc5b3c9eb3415d1"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    return response.json()

def show_weather_details():
    city = city_text.get()
    weather = get_weather(city)
    try:
        weather_details['text'] = f"City: {weather['name']}\nTemperature: {weather['main']['temp']}°C\nWeather: {weather['weather'][0]['description']}"
    except:
        weather_details['text'] = "Something went wrong!"

app = Tk()

app.title("MY First APP")
app.geometry("500x300")


title = Label(app,text="Weather APP",fg = "green", font=("TimesNewRomen",20,'bold'))
title.pack(pady=20)
city_text = StringVar()
city_input_box = Entry(app, textvariable=city_text, width=30, font=('Arial', 16), bg='lightblue', fg='darkblue', bd=2, relief='solid')
city_input_box.pack(pady=10)

search_btn = Button(app,text="Search",font=('Arial',16),command=show_weather_details,bg="black", fg="white")
search_btn.pack(pady=10)

weather_details = Label(app,text="",font=('Arial',16))
weather_details.pack(pady=10)

app.mainloop()