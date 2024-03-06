import asyncio
import aiohttp

# Define your base URL
base_url = 'BASE_URL'
# base_url = 'http://localhost:3000/local'

# Define your endpoint path
endpoint_path = '/auth/update-roles'

# Construct the full endpoint URL
endpoint_url = base_url + endpoint_path

# Define the sample payload
payload = {'JSON_PAYLOAD'}

# Define your bearer token
bearer_token = 'TOKEN'

# Define the number of requests you want to send
num_requests = 100

# Define the time interval between each request (in seconds)
interval = 1  # Adjust this based on your throttling policy

# Define the headers with the bearer token
headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'
}

async def send_request(session):
    async with session.post(endpoint_url, json=payload, headers=headers, ssl=False) as response:
        print(f"Status Code - {response.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session) for _ in range(num_requests)]
        await asyncio.gather(*tasks)

# Run the main function
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
