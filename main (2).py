from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            name = results[0]['annotations']['currency']['name']
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}"

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {
                "coordinates": f"Широта: {lat}, Долгота: {lon} \n Страна: {country}.\n Регион: {region}. \n Валюта: {name}",
                "map_url": osm_url
                        }
            else:
                return  {
                "coordinates": f"Широта: {lat}, Долгота: {lon} \n Страна: {country}.",
                "map_url": osm_url
                        }
        else :
            return  "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"


def show_coordinates(event=None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n {result['coordinates']}")
    map_url = result['map_url']

def show_map():
    if map_url:
        webbrowser.open(map_url)


def delete():
    entry.delete(0, END,)


key = "8f34e7c28e0d43b19f20c8fc0d09e4e9"
map_url = ""

window=Tk()
window.title("Координаты городов")
window.geometry("350x190")

entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)

button = Button(text="Поиск координат", command=show_coordinates)
button.pack()

label = Label(text= "Введите город и нажмите на кнопку")
label.pack()

map_button = Button(text="Показать карту", command=show_map)
map_button.pack()

button = Button(text="Очистить", command=delete)
button.pack()

window.mainloop()