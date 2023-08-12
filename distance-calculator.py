import requests
from geopy.distance import geodesic

# Define the IPinfo API endpoint
IPINFO_API_URL = "http://ipinfo.io/json"

# Make a request to get device location based on IP address
response = requests.get(IPINFO_API_URL)
print()
data = response.json()

# Extract latitude and longitude from the response
device_latitude, device_longitude = data.get("loc", "").split(",")

# Define the coordinates of the other point
other_latitude = 40.712776
other_longitude = -74.005974

# Calculate the distance between device and other point
device_location = (float(device_latitude), float(device_longitude))
other_location = (other_latitude, other_longitude)
distance = geodesic(device_location, other_location).kilometers

print(
    f"Device Location: Latitude {device_latitude}, Longitude {device_longitude}")
print(
    f"Other Location: Latitude {other_latitude}, Longitude {other_longitude}")
print(f"Distance: {distance:.2f} kilometers")
