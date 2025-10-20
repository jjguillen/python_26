from datetime import datetime, date, time

now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second

timestamp = now.timestamp()
print(day, month, year, hour, minute, second)
print('timestamp', timestamp)

print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

print( now.strftime("%H:%M:%S") )
print( now.strftime("%m/%d/%y, %H:%M:%S") )

fecha = date(2026, 10, 10) #Crea un objeto fecha (date)
print( fecha.strftime("%m/%d/%y") )

date(2025,12,31)

hora = time(21, 47)
print( hora.strftime("%H:%M:%S") )


fecha_hoy = datetime.now()
fecha_nac = datetime(year = 2000, month = 10, day = 10)

diferencia = fecha_hoy - fecha_nac
print(diferencia.days)