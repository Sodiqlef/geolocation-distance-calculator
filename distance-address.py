import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

# Define the IPinfo API endpoint
IPINFO_API_URL = "http://ipinfo.io/json"

# Make a request to get device location based on IP address
response = requests.get(IPINFO_API_URL)
data = response.json()

# Extract latitude and longitude from the response
device_latitude, device_longitude = data.get("loc", "").split(",")

# Define the coordinates of the other point
other_latitude = float(input("Input the latitude: "))
other_longitude = float(input("Input the longitude: "))

# Calculate the distance between device and other point
device_location = (float(device_latitude), float(device_longitude))
other_location = (other_latitude, other_longitude)
distance = geodesic(device_location, other_location).kilometers

# Perform reverse geocoding to get the full address of the other location
geolocator = Nominatim(user_agent="distance-calculator")
location = geolocator.reverse(other_location, exactly_one=True)

address = location.raw.get("display_name", "Unknown")

print(
    f"Device Location: Latitude {device_latitude}, Longitude {device_longitude}")
print(
    f"Other Location: Latitude {other_latitude}, Longitude {other_longitude}")
print(f"Full Address of Other Location: {address}")
print(f"Distance: {distance:.2f} kilometers")
