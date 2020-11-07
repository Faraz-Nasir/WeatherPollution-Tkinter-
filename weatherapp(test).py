from tkinter import *
import requests
import json
from PIL import ImageTk,Image

root=Tk()
root.title("Pollution Check")
root.geometry('1000x1000')
root.resizable(0,0)
#34101
#98003
#21201
def ziplookup():

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode_entry_text.get()+"&distance=25&API_KEY=B8445E1C-2107-4110-BAAB-0191C37C5B18")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']

        if category == 'Good':
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = "#ff9900"
        elif category == 'Unhealthy':
            weather_color = "#FF0000"
        elif category == 'Very Unhealthy':
            weather_color = "990066"
        elif category == 'Hazardous':
            weather_color = "#660000"

        category=api[0]['Category']['Name']

        my_label=Label(root,text=f'{city} \n\n\n {str(quality)} \n\n\n {category}',bg=weather_color)
        my_label.config(width=35,height=10)
        my_label.config(font=("Helvetica",12))
        my_label.grid(row=5,column=0,pady=20)
    except Exception as e:
        api="Error"




background_image=PhotoImage(file="C:\\Users\\faraz\\PycharmProjects\\Tkinter\\WeatherCast Faraz\\Background.png")
background_label=Label(root,image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

title_img=PhotoImage(file="WeatherCast Faraz/Title.png")
title_label=Label(root,image=title_img)
title_label.config(width=220)
title_label.grid(row=0,column=0,pady=(80,130))

zipcode_image=PhotoImage(file="WeatherCast Faraz/Zipcode.png")
zipcode_label=Label(root,image=zipcode_image)
zipcode_label.config(width=150)
zipcode_label.grid(row=1,column=0,sticky=W)

zipcode_entry=PhotoImage(file="WeatherCast Faraz/Rectangle 1.png")
zipcode_entry_label=Label(root,image=zipcode_entry)
zipcode_entry_label.config(width=150)
zipcode_entry_label.grid(row=2,column=0,pady=20,sticky=W)

zipcode_entry_text=Entry(root)
zipcode_entry_text.config(width=20)
zipcode_entry_text.grid(row=2,column=0,sticky=W)

btn_submit=Button(root,bg="green",text="LookUp",font=("Helvetica",25),command=ziplookup)
btn_submit.config(width=7)
btn_submit.grid(row=3,column=0,sticky=W)


root.mainloop()