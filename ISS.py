import requests
import time
import matplotlib.pyplot as plt
import json
from datetime import datetime  

latitude = []
longitude = []
time_stamp = []

url = "http://api.open-notify.org/iss-now.json"

start_time = time.time()  

for i in range(100):
    response = requests.get(url)
    result = response.json()

    if result["message"] == "success":
        coordinate = result["iss_position"]
        lat_pos = float(coordinate["latitude"])
        long_pos = float(coordinate["longitude"])
        time_sta = result["timestamp"]

        latitude.append(lat_pos)
        longitude.append(long_pos)
        time_stamp.append(time_sta)

        
        print(f"Latitude = {lat_pos}, Longitude = {long_pos}")

    time.sleep(1)

end_time = time.time()  

if latitude and longitude:
    plt.plot(longitude, latitude, marker='o', linestyle='-', color='b')
    plt.title('ISS Position: Longitude vs Latitude')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()
else:
    print("No graph available")

print(f"Start time: {datetime.fromtimestamp(start_time)}")
print(f"End time: {datetime.fromtimestamp(end_time)}")