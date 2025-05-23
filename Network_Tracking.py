import requests

def get_location_from_ip(ip_address):
    # Replace with your actual API key
    api_key = 'AIzaSyBb2Tohg2Vv1CVNFGS5Yw1X3Z273Fv2Wbg'

    # Geocoding API URL
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={ip_address}&key={api_key}"

    # Make the request
    response = requests.get(geocode_url)
    data = response.json()

    # Check if the response contains a valid location
    if data['status'] == 'OK':
        # Get the formatted address from the API response
        location = data['results'][0]['formatted_address']
        return location
    else:
        return None

# Take IP address input from user
ip_address = input("Please enter an IP address: ")

# Get the location for the entered IP address
location = get_location_from_ip(ip_address)

# Print the result
if location:
    print(f"Location for IP {ip_address}: {location}")
else:
    print(f"Could not find location for IP {ip_address}.")
