import tkinter as tk
import requests
import datetime
import pytz
from PIL import ImageTk, Image
from tkinter import messagebox

win = tk.Tk()
win.geometry("400x650")
win.title("Weather Forecast")
win.iconbitmap("logo.ico")
dt = datetime.datetime.now()
hour=dt.hour
def unix_to_ist(unix_timestamp):
    utc_datetime = datetime.datetime.fromtimestamp(unix_timestamp, tz=pytz.utc)
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_datetime = utc_datetime.astimezone(ist_timezone)
    return  ist_datetime.strftime("%H:%M")
def add(e)  :
     global l1,l2,l3,e1
     l1.destroy()
     canvas.destroy()
     e1=tk.Entry(win,width=41,font=("arial", 19),bg='white')
     e1.place(x=0,y=20)
     e1.bind('<Return>',show) 
def show(e) :
    global bg_img, canvas,l1, l2, l3,e1,la,temp,temp1,name

    city=e1.get()
    if city == "":
            messagebox.showerror("Error", "City not found")
            return
    api_key='3b98271fc0fe8a28a43944faa37ddcf9'
    res2= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
    temp2=res2.json()
   
    if temp2.get("cod") != 200:
            messagebox.showerror("Error", temp2.get("message", "City not found"))
            e1.delete(0, tk.END)
            return
    if 6 <= hour and hour < 9:
              img = Image.open("earlymorning.png").resize((400, 650))
              bg_img = ImageTk.PhotoImage(img)
              canvas=tk.Canvas(win, width=img.width, height=img.height)  
              canvas.pack()
              canvas.create_image(0, 0, anchor="nw", image=bg_img)
              name=e1.get().capitalize()
              l1 = tk.Label(win, text=f"{name}", font=("Arial", 27, "bold"), bg="#8D91D4", fg="white")
              l1.place(x=15, y=20)
              api_key='3b98271fc0fe8a28a43944faa37ddcf9'
              city=e1.get()
              res= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
              temp=res.json()['main']['temp']
              rect1=canvas.create_rectangle(25,265,375,360, fill="#5E63AC", outline="white", width=2)
              resda = requests.get ("https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.20&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto")
              mn=resda.json()['daily']['temperature_2m_min'][0]
              mx=resda.json()['daily']['temperature_2m_max'][0]
              da0 = resda.json()['daily']['time'][1]
              d0=da0.split('-')
              mn1=resda.json()['daily']['temperature_2m_min'][1]
              mx1=resda.json()['daily']['temperature_2m_max'][1]
              da1 = resda.json()['daily']['time'][2]
              d1=da1.split('-')
              mn2=resda.json()['daily']['temperature_2m_min'][2]
              mx2=resda.json()['daily']['temperature_2m_max'][2]
              da2 = resda.json()['daily']['time'][3]
              d2=da2.split('-')
              mn3=resda.json()['daily']['temperature_2m_min'][3]
              mx3=resda.json()['daily']['temperature_2m_max'][3]
              da3 = resda.json()['daily']['time'][4]
              d3=da3.split('-')
              mn4=resda.json()['daily']['temperature_2m_min'][4]
              mx4=resda.json()['daily']['temperature_2m_max'][4]
              canvas.create_text(55, 285, text=f"Today", font=("Arial", 10), fill="white")
              canvas.create_text(60, 313, text=f"{int(temp)}°", font=("Arial", 20, "bold"), fill="white")
              canvas.create_text(55, 340, text=f"{int(mn)}°/{int(mx)}°", font=("Arial", 8), fill="white")
              canvas.create_text(125, 285, text=f"{d0[1]}/{d0[2]}", font=("Arial", 10, "bold"), fill="white")
              canvas.create_text(130, 313, text=f"{int((int(mn1)+int(mx1))/2)}°", font=("Arial", 20, "bold"), fill="white")
              canvas.create_text(125, 340, text=f"{int(mn1)}°/{int(mx1)}°", font=("Arial", 8), fill="white")
              canvas.create_text(195, 285, text=f"{d1[1]}/{d1[2]}", font=("Arial", 10, "bold"), fill="white")
              canvas.create_text(200, 313, text=f"{int((int(mn2)+int(mx2))/2)}°", font=("Arial", 20, "bold"), fill="white")
              canvas.create_text(195, 340, text=f"{int(mn2)}°/{int(mx2)}°", font=("Arial", 8), fill="white")
              canvas.create_text(265, 285, text=f"{d2[1]}/{d2[2]}", font=("Arial", 10, "bold"), fill="white")
              canvas.create_text(270, 313, text=f"{int((int(mn3)+int(mx3))/2)}°", font=("Arial", 20, "bold"), fill="white")
              canvas.create_text(265, 340, text=f"{int(mn3)}°/{int(mx3)}°", font=("Arial", 8), fill="white")
              canvas.create_text(335, 285, text=f"{d3[1]}/{d3[2]}", font=("Arial", 10, "bold"), fill="white")
              canvas.create_text(340, 313, text=f"{int((int(mn4)+int(mx4))/2)}°", font=("Arial", 20, "bold"), fill="white")
              canvas.create_text(335, 340, text=f"{int(mn4)}°/{int(mx4)}°", font=("Arial", 8), fill="white")
              canvas.create_text(200,200, text=f"{int(temp)}°", font=("Arial", 35, "bold"), fill="white")
              temp1=res.json()['weather'][0]['description']
              lon=res.json()['coord']['lon']
              lat=res.json()['coord']['lat']
              res1= requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}")
              aqi=res1.json()['list'][0]['main']['aqi']
              if aqi == 1 :
                    aqi_value='good'
              elif aqi == 2 :
                    aqi_value='Fair'
              elif aqi == 3 :
                    aqi_value='Moderate '
              elif aqi == 4 :
                    aqi_value='Poor' 
              else :
                    aqi_value='Very Poor'    
              canvas.create_text(200,237, text=f"{temp1} {int(mn)}°/{int(mx)}°  Air quality: {aqi_value} ", font=("Arial", 10, "bold"), fill="white")
              rect2=canvas.create_rectangle(25,380,133,443,fill="#5E63AC", outline='white',width=2)
              rect3=canvas.create_rectangle(155,380,252,443, fill="#5E63AC", outline="white", width=2)
              rect4=canvas.create_rectangle(275,380,375,443, fill="#5E63AC", outline="white", width=2)
              rect5=canvas.create_rectangle(25,460,133,523, fill="#5E63AC", outline="white", width=2)
              rect6=canvas.create_rectangle(155,460,252,523, fill="#5E63AC", outline="white", width=2)
              rect7=canvas.create_rectangle(275,460,375,523, fill="#5E63AC", outline="white", width=2)

              humidity=res.json()['main']['humidity']
              canvas.create_text(65, 400, text=f"Humidity", font=("Arial",12),fill="#C7C7C7",)
              canvas.create_text(55, 423, text=f"{humidity}%", font=("Arial", 12),fill="white")
       
              like=res.json()['main']['feels_like'] 
              like=res.json()['main']['feels_like'] 
              like=abs(like)  
              canvas.create_text(196, 400, text=f"Feels like", font=("Arial", 12),fill="#C7C7C7")
              canvas.create_text(180, 423, text=f"{int(like)}°", font=("Arial", 12),fill="white")
       
              pre=res.json()['main']['pressure']  
              canvas.create_text(315, 400, text=f"Pressure", font=("Arial", 12),fill="#C7C7C7")
              canvas.create_text(315, 423, text=f"{pre}hPa", font=("Arial", 12),fill="white")
     
              vis=res.json()['visibility']
              vis=int(vis /1000) 
              canvas.create_text(195, 480, text=f"Visibility", font=("Arial", 12),fill="#C7C7C7")
              canvas.create_text(188, 500, text=f"{vis}km", font=("Arial", 12),fill="white")
       

              wind=res.json()['wind']['speed']
              canvas.create_text(75, 480, text=f"Wind speed", font=("Arial", 12),fill="#C7C7C7")
              canvas.create_text(65, 500, text=f"{wind}m/s", font=("Arial", 12),fill="white")  
       
 
              co2=res1.json()['list'][0]['components']['co'] 
              canvas.create_text(315, 480, text=f"Co2 level", font=("Arial", 12),fill="#C7C7C7")
              canvas.create_text(310, 500, text=f"{int(co2)}ppm", font=("Arial", 12),fill="white") 
              rect7=canvas.create_rectangle(25,543,375,613, fill="#5E63AC", outline="white", width=2) 
              t1=res.json()['sys']['sunrise']
              t2=res.json()['sys']['sunset']
              canvas.create_text(70, 563, text= unix_to_ist(t1), font=("Arial", 8), fill="white")
              canvas.create_text(327, 563, text= unix_to_ist(t2), font=("Arial", 8), fill="white")
              canvas.create_line(60, 580, 340, 580, fill="#000020", width=6, capstyle=tk.ROUND)  
              if hour == 6 :
                   canvas.create_oval(61, 575, 71, 585, fill="grey", outline="grey")
              elif hour == 7 :  
                   canvas.create_oval(81, 575, 91, 585, fill="grey", outline="grey") 
              else :
                   canvas.create_oval(101, 575, 111, 585, fill="grey", outline="grey")         

              canvas.create_text(72, 595, text=f"Sunrise", font=("Arial", 8), fill="white")
              canvas.create_text(327, 595, text=f"Sunset", font=("Arial", 8), fill="white")
     
              l1.bind('<Button-3>',add)
              l1.bind('<Button-1>',add)
    elif 9 <= hour and hour < 15:
             img = Image.open("sunny.png").resize((400, 630))
             bg_img = ImageTk.PhotoImage(img)
             canvas=tk.Canvas(win, width=img.width, height=img.height)  
             canvas.pack()
             canvas.create_image(0, 0, anchor="nw", image=bg_img)
             name=e1.get().capitalize()
             l1 = tk.Label(win, text=f"{name}", font=("Arial", 27, "bold"), bg="#146CAB", fg="white")
             l1.place(x=15, y=20)
             api_key='3b98271fc0fe8a28a43944faa37ddcf9'
             city=e1.get()
             res= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
             temp=res.json()['main']['temp']
             canvas.create_text(200, 200, text=f"{int(temp)}°", font=("Arial", 35, "bold"), fill="white")
             temp1=res.json()['weather'][0]['description']
             lon=res.json()['coord']['lon']
             lat=res.json()['coord']['lat']
             res1= requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}")
             aqi=res1.json()['list'][0]['main']['aqi']
             if aqi == 1 :
                aqi_value='good'
             elif aqi == 2 :
                aqi_value='Fair'
             elif aqi == 3 :
                aqi_value='Moderate '
             elif aqi == 4 :
                aqi_value='Poor' 
             else :
                aqi_value='Very Poor'    
             rect1=canvas.create_rectangle(25,265,375,360, fill="#0C5985", outline="grey", width=2)
             resda = requests.get (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto")
             mn=resda.json()['daily']['temperature_2m_min'][0]
             mx=resda.json()['daily']['temperature_2m_max'][0]
             da0 = resda.json()['daily']['time'][1]
             d0=da0.split('-')
             mn1=resda.json()['daily']['temperature_2m_min'][1]
             mx1=resda.json()['daily']['temperature_2m_max'][1]
             da1 = resda.json()['daily']['time'][2]
             d1=da1.split('-')
             mn2=resda.json()['daily']['temperature_2m_min'][2]
             mx2=resda.json()['daily']['temperature_2m_max'][2]
             da2 = resda.json()['daily']['time'][3]
             d2=da2.split('-')
             mn3=resda.json()['daily']['temperature_2m_min'][3]
             mx3=resda.json()['daily']['temperature_2m_max'][3]
             da3 = resda.json()['daily']['time'][4]
             d3=da3.split('-')
             mn4=resda.json()['daily']['temperature_2m_min'][4]
             mx4=resda.json()['daily']['temperature_2m_max'][4]
             canvas.create_text(55, 285, text=f"Today", font=("Arial", 10), fill="white")
             canvas.create_text(60, 313, text=f"{int(temp)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(55, 340, text=f"{int(mn)}°/{int(mx)}°", font=("Arial", 8), fill="white")
             canvas.create_text(125, 285, text=f"{d0[1]}/{d0[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(130, 313, text=f"{int((int(mn1)+int(mx1))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(125, 340, text=f"{int(mn1)}°/{int(mx1)}°", font=("Arial", 8), fill="white")
             canvas.create_text(195, 285, text=f"{d1[1]}/{d1[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(200, 313, text=f"{int((int(mn2)+int(mx2))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(195, 340, text=f"{int(mn2)}°/{int(mx2)}°", font=("Arial", 8), fill="white")
             canvas.create_text(265, 285, text=f"{d2[1]}/{d2[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(270, 313, text=f"{int((int(mn3)+int(mx3))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(265, 340, text=f"{int(mn3)}°/{int(mx3)}°", font=("Arial", 8), fill="white")
             canvas.create_text(335, 285, text=f"{d3[1]}/{d3[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(340, 313, text=f"{int((int(mn4)+int(mx4))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(335, 340, text=f"{int(mn4)}°/{int(mx4)}°", font=("Arial", 8), fill="white")


             canvas.create_text(200, 237, text=f"{temp1} {int(mn)}°/{int(mx)}°  Air quality: {aqi_value} ", font=("Arial", 10, "bold"), fill="white")
             rect2=canvas.create_rectangle(25,380,133,443,fill="#0C5985", outline='grey',width=2)
             rect3=canvas.create_rectangle(155,380,252,443, fill="#0C5985", outline="grey", width=2)
             rect4=canvas.create_rectangle(275,380,375,443, fill="#0C5985", outline="grey", width=2)
             rect5=canvas.create_rectangle(25,460,133,523, fill="#0C5985", outline="grey", width=2)
             rect6=canvas.create_rectangle(155,460,252,523, fill="#0C5985", outline="grey", width=2)
             rect7=canvas.create_rectangle(275,460,375,523, fill="#0C5985", outline="grey", width=2)

             humidity=res.json()['main']['humidity']
             canvas.create_text(65, 400, text=f"Humidity", font=("Arial",12),fill="grey",)
             canvas.create_text(55, 423, text=f"{humidity}%", font=("Arial", 12),fill="white")
       
             like=res.json()['main']['feels_like'] 
             like=res.json()['main']['feels_like'] 
             like=abs(like)  
             canvas.create_text(196, 400, text=f"Feels like", font=("Arial", 12),fill="grey")
             canvas.create_text(180, 423, text=f"{int(like)}°", font=("Arial", 12),fill="white")
       
             pre=res.json()['main']['pressure']  
             canvas.create_text(315, 400, text=f"Pressure", font=("Arial", 12),fill="grey")
             canvas.create_text(315, 423, text=f"{pre}hPa", font=("Arial", 12),fill="white")
     
             vis=res.json()['visibility']
             vis=int(vis /1000) 
             canvas.create_text(195, 480, text=f"Visibility", font=("Arial", 12),fill="grey")
             canvas.create_text(188, 500, text=f"{vis}km", font=("Arial", 12),fill="white")
       

             wind=res.json()['wind']['speed']
             canvas.create_text(75, 480, text=f"Wind speed", font=("Arial", 12),fill="grey")
             canvas.create_text(65, 500, text=f"{wind}m/s", font=("Arial", 12),fill="white")  
       
 
             co2=res1.json()['list'][0]['components']['co'] 
             canvas.create_text(315, 480, text=f"Co2 level", font=("Arial", 12),fill="grey")
             canvas.create_text(310, 500, text=f"{int(co2)}ppm", font=("Arial", 12),fill="white") 
             rect7=canvas.create_rectangle(25,543,375,613, fill="#0C5985", outline="grey", width=2) 
             t1=res.json()['sys']['sunrise']
             t2=res.json()['sys']['sunset']
             canvas.create_text(70, 563, text= unix_to_ist(t1), font=("Arial", 10), fill="white")
             canvas.create_text(327, 563, text= unix_to_ist(t2), font=("Arial", 10), fill="white")
             canvas.create_line(60, 580, 340, 580, fill="#E8F71C", width=7, capstyle=tk.ROUND)  
             if hour == 9 or hour == 10  :
                  canvas.create_oval(121, 575, 131, 585, fill="white", outline="grey")
             elif hour == 11 or hour == 12  :  
                  canvas.create_oval(151, 575, 161, 585, fill="white", outline="grey") 
             else :
                  canvas.create_oval(181, 575, 191, 585, fill="white", outline="grey")         

             canvas.create_text(72, 595, text=f"Sunrise", font=("Arial", 10), fill="white")
             canvas.create_text(327, 595, text=f"Sunset", font=("Arial", 10), fill="white")
     
             l1.bind('<Button-3>',add)
             l1.bind('<Button-1>',add)
    elif 15 <= hour and hour < 18:
             img = Image.open("morning.png").resize((400, 650))
             bg_img = ImageTk.PhotoImage(img)
             canvas=tk.Canvas(win, width=img.width, height=img.height)  
             canvas.pack()
             canvas.create_image(0, 0, anchor="nw", image=bg_img)
             name=e1.get().capitalize()
             l1 = tk.Label(win, text=f"{name}", font=("Arial", 27, "bold"), bg="#5FCBAF", fg="white")
             l1.place(x=15, y=20)

             api_key='3b98271fc0fe8a28a43944faa37ddcf9'
             city=e1.get()
             res= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
             temp=res.json()['main']['temp']
             canvas.create_text(200,200,text=f"{int(temp)}°", font=("Arial", 35, "bold"), fill="white")
             temp1=res.json()['weather'][0]['description']
             lon=res.json()['coord']['lon']
             lat=res.json()['coord']['lat']
             res1= requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}")
             aqi=res1.json()['list'][0]['main']['aqi']
             if aqi == 1 :
                aqi_value='good'
             elif aqi == 2 :
                aqi_value='Fair'
             elif aqi == 3 :
                aqi_value='Moderate '
             elif aqi == 4 :
                aqi_value='Poor' 
             else :
                aqi_value='Very Poor'    

             rect1=canvas.create_rectangle(25,265,375,360, fill="#F6EC6C", outline="grey", width=2)
             resda = requests.get ("https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.20&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto")
             mn=resda.json()['daily']['temperature_2m_min'][0]
             mx=resda.json()['daily']['temperature_2m_max'][0]
             da0 = resda.json()['daily']['time'][1]
             d0=da0.split('-')
             mn1=resda.json()['daily']['temperature_2m_min'][1]
             mx1=resda.json()['daily']['temperature_2m_max'][1]
             da1 = resda.json()['daily']['time'][2]
             d1=da1.split('-')
             mn2=resda.json()['daily']['temperature_2m_min'][2]
             mx2=resda.json()['daily']['temperature_2m_max'][2]
             da2 = resda.json()['daily']['time'][3]
             d2=da2.split('-')
             mn3=resda.json()['daily']['temperature_2m_min'][3]
             mx3=resda.json()['daily']['temperature_2m_max'][3]
             da3 = resda.json()['daily']['time'][4]
             d3=da3.split('-')
             mn4=resda.json()['daily']['temperature_2m_min'][4]
             mx4=resda.json()['daily']['temperature_2m_max'][4]
             canvas.create_text(55, 285, text=f"Today", font=("Arial", 10), fill="white")
             canvas.create_text(60, 313, text=f"{int(temp)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(55, 340, text=f"{int(mn)}°/{int(mx)}°", font=("Arial", 8), fill="white")
             canvas.create_text(125, 285, text=f"{d0[1]}/{d0[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(130, 313, text=f"{int((int(mn1)+int(mx1))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(125, 340, text=f"{int(mn1)}°/{int(mx1)}°", font=("Arial", 8), fill="white")
             canvas.create_text(195, 285, text=f"{d1[1]}/{d1[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(200, 313, text=f"{int((int(mn2)+int(mx2))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(195, 340, text=f"{int(mn2)}°/{int(mx2)}°", font=("Arial", 8), fill="white")
             canvas.create_text(265, 285, text=f"{d2[1]}/{d2[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(270, 313, text=f"{int((int(mn3)+int(mx3))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(265, 340, text=f"{int(mn3)}°/{int(mx3)}°", font=("Arial", 8), fill="white")
             canvas.create_text(335, 285, text=f"{d3[1]}/{d3[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(340, 313, text=f"{int((int(mn4)+int(mx4))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(335, 340, text=f"{int(mn4)}°/{int(mx4)}°", font=("Arial", 8), fill="white")

             canvas.create_text(200, 237, text=f"{temp1} {int(mn)}°/{int(mx)}°  Air quality: {aqi_value} ", font=("Arial", 10, "bold"), fill="white")
        
             rect2=canvas.create_rectangle(25,380,133,443,fill="#F6EC6C", outline='grey',width=2)
             rect3=canvas.create_rectangle(155,380,252,443, fill="#F6EC6C", outline="grey", width=2)
             rect4=canvas.create_rectangle(275,380,375,443, fill="#F6EC6C", outline="grey", width=2)
             rect5=canvas.create_rectangle(25,460,133,523, fill="#F6EC6C", outline="grey", width=2)
             rect6=canvas.create_rectangle(155,460,252,523, fill="#F6EC6C", outline="grey", width=2)
             rect7=canvas.create_rectangle(275,460,375,523, fill="#F6EC6C", outline="grey", width=2)

             humidity=res.json()['main']['humidity']
             canvas.create_text(65, 400, text=f"Humidity", font=("Arial",12),fill="grey",)
             canvas.create_text(55, 423, text=f"{humidity}%", font=("Arial", 12),fill="white")
       
             like=res.json()['main']['feels_like'] 
             like=res.json()['main']['feels_like'] 
             like=abs(like)  
             canvas.create_text(196, 400, text=f"Feels like", font=("Arial", 12),fill="grey")
             canvas.create_text(180, 423, text=f"{int(like)}°", font=("Arial", 12),fill="white")
       
             pre=res.json()['main']['pressure']  
             canvas.create_text(315, 400, text=f"Pressure", font=("Arial", 12),fill="grey")
             canvas.create_text(315, 423, text=f"{pre}hPa", font=("Arial", 12),fill="white")
     
             vis=res.json()['visibility']
             vis=int(vis /1000) 
             canvas.create_text(195, 480, text=f"Visibility", font=("Arial", 12),fill="grey")
             canvas.create_text(188, 500, text=f"{vis}km", font=("Arial", 12),fill="white")
       

             wind=res.json()['wind']['speed']
             canvas.create_text(75, 480, text=f"Wind speed", font=("Arial", 12),fill="grey")
             canvas.create_text(65, 500, text=f"{wind}m/s", font=("Arial", 12),fill="white")  
       
 
             co2=res1.json()['list'][0]['components']['co'] 
             canvas.create_text(315, 480, text=f"Co2 level", font=("Arial", 12),fill="grey")
             canvas.create_text(310, 500, text=f"{int(co2)}ppm", font=("Arial", 12),fill="white") 
             rect7=canvas.create_rectangle(25,543,375,613, fill="#F6EC6C", outline="grey", width=2) 
             t1=res.json()['sys']['sunrise']
             t2=res.json()['sys']['sunset']
             canvas.create_text(70, 563, text= unix_to_ist(t2), font=("Arial", 10), fill="white")
             canvas.create_text(327, 563, text= unix_to_ist(t1), font=("Arial", 10), fill="white")
             canvas.create_line(60, 580, 340, 580, fill="#F8BC09", width=7, capstyle=tk.ROUND)  
             if hour == 15  :
                 canvas.create_oval(201, 575, 211, 585 ,fill="grey", outline="grey")
             else :
                  canvas.create_oval(221, 575, 231, 585, fill="grey", outline="grey")         

             canvas.create_text(72, 595, text=f"Sunset", font=("Arial", 10), fill="white")
             canvas.create_text(327, 595, text=f"Sunrise", font=("Arial", 10), fill="white")
     
             l1.bind('<Button-3>',add)
             l1.bind('<Button-1>',add)
    elif 18 <= hour and hour < 20:
             img = Image.open("sunset.png").resize((400, 650))
             bg_img = ImageTk.PhotoImage(img)
             canvas=tk.Canvas(win, width=img.width, height=img.height)  
             canvas.pack()
             canvas.create_image(0, 0, anchor="nw", image=bg_img)
             name=e1.get().capitalize()
             l1 = tk.Label(win, text=f"{name}", font=("Arial", 27, "bold"), bg="#D44A10", fg="white")
             l1.place(x=15, y=20)
             api_key='3b98271fc0fe8a28a43944faa37ddcf9'
             city=e1.get()
             res= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
             temp=res.json()['main']['temp']
             canvas.create_text(200,200 ,text=f"{int(temp)}°", font=("Arial", 35, "bold"), fill="white")
             temp1=res.json()['weather'][0]['description']
             lon=res.json()['coord']['lon']
             lat=res.json()['coord']['lat']
             res1= requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}")
             aqi=res1.json()['list'][0]['main']['aqi']
             if aqi == 1 :
                 aqi_value='good'
             elif aqi == 2 :
                 aqi_value='Fair'
             elif aqi == 3 :
                 aqi_value='Moderate '
             elif aqi == 4 :
                aqi_value='Poor' 
             else :
               aqi_value='Very Poor'    
    
             rect1=canvas.create_rectangle(25,265,375,360, fill="#FF7D05", outline="grey", width=2)
             resda = requests.get ("https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.20&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto")
             mn=resda.json()['daily']['temperature_2m_min'][0]
             mx=resda.json()['daily']['temperature_2m_max'][0]
             da0 = resda.json()['daily']['time'][1]
             d0=da0.split('-')
             mn1=resda.json()['daily']['temperature_2m_min'][1]
             mx1=resda.json()['daily']['temperature_2m_max'][1]
             da1 = resda.json()['daily']['time'][2]
             d1=da1.split('-')
             mn2=resda.json()['daily']['temperature_2m_min'][2]
             mx2=resda.json()['daily']['temperature_2m_max'][2]
             da2 = resda.json()['daily']['time'][3]
             d2=da2.split('-')
             mn3=resda.json()['daily']['temperature_2m_min'][3]
             mx3=resda.json()['daily']['temperature_2m_max'][3]
             da3 = resda.json()['daily']['time'][4]
             d3=da3.split('-')
             mn4=resda.json()['daily']['temperature_2m_min'][4]
             mx4=resda.json()['daily']['temperature_2m_max'][4]
             canvas.create_text(55, 285, text=f"Today", font=("Arial", 10), fill="white")
             canvas.create_text(60, 313, text=f"{int(temp)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(55, 340, text=f"{int(mn)}°/{int(mx)}°", font=("Arial", 8), fill="white")
             canvas.create_text(125, 285, text=f"{d0[1]}/{d0[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(130, 313, text=f"{int((int(mn1)+int(mx1))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(125, 340, text=f"{int(mn1)}°/{int(mx1)}°", font=("Arial", 8), fill="white")
             canvas.create_text(125, 285, text=f"{d0[1]}/{d0[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(130, 313, text=f"{int((int(mn1)+int(mx1))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(125, 340, text=f"{int(mn1)}°/{int(mx1)}°", font=("Arial", 8), fill="white")
             canvas.create_text(195, 285, text=f"{d1[1]}/{d1[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(200, 313, text=f"{int((int(mn2)+int(mx2))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(195, 340, text=f"{int(mn2)}°/{int(mx2)}°", font=("Arial", 8), fill="white")
             canvas.create_text(265, 285, text=f"{d2[1]}/{d2[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(270, 313, text=f"{int((int(mn3)+int(mx3))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(265, 340, text=f"{int(mn3)}°/{int(mx3)}°", font=("Arial", 8), fill="white")
             canvas.create_text(335, 285, text=f"{d3[1]}/{d3[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(340, 313, text=f"{int((int(mn4)+int(mx4))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(335, 340, text=f"{int(mn4)}°/{int(mx4)}°", font=("Arial", 8), fill="white")

             canvas.create_text(200, 237, text=f"{temp1} {int(mn)}°/{int(mx)}°  Air quality: {aqi_value} ", font=("Arial", 10, "bold"), fill="white")
             rect2=canvas.create_rectangle(25,380,133,443,fill="#FF7D05", outline='grey',width=2)
             rect3=canvas.create_rectangle(155,380,252,443, fill="#FF7D05", outline="grey", width=2)
             rect4=canvas.create_rectangle(275,380,375,443, fill="#FF7D05", outline="grey", width=2)
             rect5=canvas.create_rectangle(25,460,133,523, fill="#FF7D05", outline="grey", width=2)
             rect6=canvas.create_rectangle(155,460,252,523, fill="#FF7D05", outline="grey", width=2)
             rect7=canvas.create_rectangle(275,460,375,523, fill="#FF7D05", outline="grey", width=2)

             humidity=res.json()['main']['humidity']
             canvas.create_text(65, 400, text=f"Humidity", font=("Arial",12),fill="grey",)
             canvas.create_text(55, 423, text=f"{humidity}%", font=("Arial", 12),fill="white")
       
             like=res.json()['main']['feels_like'] 
             like=res.json()['main']['feels_like'] 
             like=abs(like)  
             canvas.create_text(196, 400, text=f"Feels like", font=("Arial", 12),fill="grey")
             canvas.create_text(180, 423, text=f"{int(like)}°", font=("Arial", 12),fill="white")
       
             pre=res.json()['main']['pressure']  
             canvas.create_text(315, 400, text=f"Pressure", font=("Arial", 12),fill="grey")
             canvas.create_text(315, 423, text=f"{pre}hPa", font=("Arial", 12),fill="white")
     
             vis=res.json()['visibility']
             vis=int(vis /1000) 
             canvas.create_text(195, 480, text=f"Visibility", font=("Arial", 12),fill="grey")
             canvas.create_text(188, 500, text=f"{vis}km", font=("Arial", 12),fill="white")
       

             wind=res.json()['wind']['speed']
             canvas.create_text(75, 480, text=f"Wind speed", font=("Arial", 12),fill="grey")
             canvas.create_text(65, 500, text=f"{wind}m/s", font=("Arial", 12),fill="white")  
       
 
             co2=res1.json()['list'][0]['components']['co'] 
             canvas.create_text(315, 480, text=f"Co2 level", font=("Arial", 12),fill="grey")
             canvas.create_text(310, 500, text=f"{int(co2)}ppm", font=("Arial", 12),fill="white") 
             
             rect7=canvas.create_rectangle(25,543,375,613, fill="#FF7D05", outline="grey", width=2) 
             t1=res.json()['sys']['sunrise']
             t2=res.json()['sys']['sunset']
             canvas.create_text(70, 563, text= unix_to_ist(t1), font=("Arial", 10), fill="white")
             canvas.create_text(327, 563, text= unix_to_ist(t2), font=("Arial", 10), fill="white")
             canvas.create_line(60, 580, 340, 580, fill="#000020", width=7, capstyle=tk.ROUND)  
             if hour == 18 :
                  canvas.create_oval(251, 575, 261, 585, fill="grey", outline="grey")
             else :
                  canvas.create_oval(331, 575,341 , 585, fill="grey", outline="grey")         

             canvas.create_text(72, 595, text=f"Sunrise", font=("Arial", 10), fill="white")
             canvas.create_text(327, 595, text=f"Sunset", font=("Arial", 10), fill="white")
     
             l1.bind('<Button-3>',add)
             l1.bind('<Button-1>',add)
    else:
             img = Image.open("night.png").resize((400, 650))
             bg_img = ImageTk.PhotoImage(img)
             canvas=tk.Canvas(win, width=img.width, height=img.height)  
             canvas.pack()
             canvas.create_image(0, 0, anchor="nw", image=bg_img)
             name=e1.get().capitalize()
             l1 = tk.Label(win, text=f"{name}", font=("Arial", 27, "bold"), bg="#000a41", fg="white")
             l1.place(x=15, y=20)
             api_key='3b98271fc0fe8a28a43944faa37ddcf9'
             city=e1.get()
             res= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
             temp=res.json()['main']['temp']
             canvas.create_text(200,200 ,text=f"{int(temp)}°", font=("Arial", 35, "bold"), fill="white")
             temp1=res.json()['weather'][0]['description']
             lon=res.json()['coord']['lon']
             lat=res.json()['coord']['lat']
             res1= requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}")
             aqi=res1.json()['list'][0]['main']['aqi']
             if aqi == 1 :
                 aqi_value='good'
             elif aqi == 2 :
                 aqi_value='Fair'
             elif aqi == 3 :
                 aqi_value='Moderate '
             elif aqi == 4 :
                aqi_value='Poor' 
             else :
               aqi_value='Very Poor'    
    
             rect1=canvas.create_rectangle(25,265,375,360, fill="#050E55", outline="grey", width=2)
             resda = requests.get ("https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.20&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto")
             mn=resda.json()['daily']['temperature_2m_min'][0]
             mx=resda.json()['daily']['temperature_2m_max'][0]
             da0 = resda.json()['daily']['time'][1]
             d0=da0.split('-')
             mn1=resda.json()['daily']['temperature_2m_min'][1]
             mx1=resda.json()['daily']['temperature_2m_max'][1]
             da1 = resda.json()['daily']['time'][2]
             d1=da1.split('-')
             mn2=resda.json()['daily']['temperature_2m_min'][2]
             mx2=resda.json()['daily']['temperature_2m_max'][2]
             da2 = resda.json()['daily']['time'][3]
             d2=da2.split('-')
             mn3=resda.json()['daily']['temperature_2m_min'][3]
             mx3=resda.json()['daily']['temperature_2m_max'][3]
             da3 = resda.json()['daily']['time'][4]
             d3=da3.split('-')
             mn4=resda.json()['daily']['temperature_2m_min'][4]
             mx4=resda.json()['daily']['temperature_2m_max'][4]
             canvas.create_text(55, 285, text=f"Today", font=("Arial", 10), fill="white")
             canvas.create_text(60, 313, text=f"{int(temp)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(55, 340, text=f"{int(mn)}°/{int(mx)}°", font=("Arial", 8), fill="white")
             canvas.create_text(125, 285, text=f"{d0[1]}/{d0[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(130, 313, text=f"{int((int(mn1)+int(mx1))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(125, 340, text=f"{int(mn1)}°/{int(mx1)}°", font=("Arial", 8), fill="white")
             canvas.create_text(125, 285, text=f"{d0[1]}/{d0[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(130, 313, text=f"{int((int(mn1)+int(mx1))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(125, 340, text=f"{int(mn1)}°/{int(mx1)}°", font=("Arial", 8), fill="white")
             canvas.create_text(195, 285, text=f"{d1[1]}/{d1[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(200, 313, text=f"{int((int(mn2)+int(mx2))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(195, 340, text=f"{int(mn2)}°/{int(mx2)}°", font=("Arial", 8), fill="white")
             canvas.create_text(265, 285, text=f"{d2[1]}/{d2[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(270, 313, text=f"{int((int(mn3)+int(mx3))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(265, 340, text=f"{int(mn3)}°/{int(mx3)}°", font=("Arial", 8), fill="white")
             canvas.create_text(335, 285, text=f"{d3[1]}/{d3[2]}", font=("Arial", 10, "bold"), fill="white")
             canvas.create_text(340, 313, text=f"{int((int(mn4)+int(mx4))/2)}°", font=("Arial", 20, "bold"), fill="white")
             canvas.create_text(335, 340, text=f"{int(mn4)}°/{int(mx4)}°", font=("Arial", 8), fill="white")
             
             canvas.create_text(200, 237, text=f"{temp1} {int(mn)}°/{int(mx)}°  Air quality: {aqi_value} ", font=("Arial", 10, "bold"), fill="white")

             rect2=canvas.create_rectangle(25,380,133,443,fill='#050E55', outline='grey',width=2)
             rect3=canvas.create_rectangle(155,380,252,443, fill="#050E55", outline="grey", width=2)
             rect4=canvas.create_rectangle(275,380,375,443, fill="#050E55", outline="grey", width=2)
             rect5=canvas.create_rectangle(25,460,133,523, fill="#050E55", outline="grey", width=2)
             rect6=canvas.create_rectangle(155,460,252,523, fill="#050E55", outline="grey", width=2)
             rect7=canvas.create_rectangle(275,460,375,523, fill="#050E55", outline="grey", width=2)
             humidity=res.json()['main']['humidity']
             canvas.create_text(65, 400, text=f"Humidity", font=("Arial",12),fill="grey",)
             canvas.create_text(55, 423, text=f"{humidity}%", font=("Arial", 12),fill="white")
       
             like=res.json()['main']['feels_like'] 
             like=res.json()['main']['feels_like'] 
             like=abs(like)  
             canvas.create_text(196, 400, text=f"Feels like", font=("Arial", 12),fill="grey")
             canvas.create_text(180, 423, text=f"{int(like)}°", font=("Arial", 12),fill="white")
       
             pre=res.json()['main']['pressure']  
             canvas.create_text(315, 400, text=f"Pressure", font=("Arial", 12),fill="grey")
             canvas.create_text(315, 423, text=f"{pre}hPa", font=("Arial", 12),fill="white")
     
             vis=res.json()['visibility']
             vis=int(vis /1000) 
             canvas.create_text(195, 480, text=f"Visibility", font=("Arial", 12),fill="grey")
             canvas.create_text(188, 500, text=f"{vis}km", font=("Arial", 12),fill="white")
       

             wind=res.json()['wind']['speed']
             canvas.create_text(75, 480, text=f"Wind speed", font=("Arial", 12),fill="grey")
             canvas.create_text(65, 500, text=f"{wind}m/s", font=("Arial", 12),fill="white")  
       
 
             co2=res1.json()['list'][0]['components']['co'] 
             canvas.create_text(315, 480, text=f"Co2 level", font=("Arial", 12),fill="grey")
             canvas.create_text(310, 500, text=f"{int(co2)}ppm", font=("Arial", 12),fill="white") 
              
             rect7=canvas.create_rectangle(25,543,375,613, fill="#050E55", outline="grey", width=2) 
             t1=res.json()['sys']['sunrise']
             t2=res.json()['sys']['sunset']
             canvas.create_text(70, 563, text= unix_to_ist(t2), font=("Arial", 10), fill="white")
             canvas.create_text(327, 563, text= unix_to_ist(t1), font=("Arial", 10), fill="white")
             canvas.create_line(60, 580, 340, 580, fill="#000020", width=7, capstyle=tk.ROUND)  
             if hour == 20 or hour == 21 or hour==22 or hour==23 :
                  canvas.create_oval(215, 575, 225, 585, fill="grey", outline="grey")
             elif hour == 0 or hour == 1 or hour==2 or hour==3 :  
                  canvas.create_oval(305, 575, 315,585 ,fill="grey", outline="grey") 
             else :
                  canvas.create_oval(335, 575, 345, 585 ,fill="grey", outline="grey")         

             canvas.create_text(70, 595, text=f"Sunset", font=("Arial", 10), fill="white")
             canvas.create_text(327, 595, text=f"Sunrise", font=("Arial", 10), fill="white")
     
             l1.bind('<Button-3>',add)
             l1.bind('<Button-1>',add)
       
e1=tk.Entry(win,width=41,font=("arial", 19),bg='white')
e1.place(x=0,y=20)
e1.bind('<Return>',show)        

win.mainloop()