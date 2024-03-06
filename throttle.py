import asyncio
import aiohttp

# Define your base URL
base_url = 'https://s4079dmhe4.execute-api.ap-southeast-1.amazonaws.com/dev'
# base_url = 'http://localhost:3000/local'

# Define your endpoint path
endpoint_path = '/auth/update-roles'

# Construct the full endpoint URL
endpoint_url = base_url + endpoint_path

# Define the sample payload
payload = {
    "data": {
        "uid": "GGnRso2eqoaRQF3mlZHEPqH4qB22",
        "customClaims": {
            "role": {
                "isAdmin": True,
                "isCS": False,
                "isWHOps": False,
                "isMarketing": False
            },
            "warehouse": [
                "JP"
            ],
            "module": {
                "BFM": {
                    "access": [
                        "View",
                        "Update"
                    ]
                }
            }
        }
    }
}

# Define your bearer token
bearer_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjNiYjg3ZGNhM2JjYjY5ZDcyYjZjYmExYjU5YjMzY2M1MjI5N2NhOGQiLCJ0eXAiOiJKV1QifQ.eyJyb2xlIjp7ImlzQWRtaW4iOnRydWUsImlzQ1MiOmZhbHNlLCJpc1dIT3BzIjpmYWxzZSwiaXNNYXJrZXRpbmciOmZhbHNlfSwid2FyZWhvdXNlIjpbIkpQIl0sIm1vZHVsZSI6eyJCRk0iOnsiYWNjZXNzIjpbIlZpZXciLCJVcGRhdGUiXX19LCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vc2hpcHBpbmdjYXJ0ZGV2IiwiYXVkIjoic2hpcHBpbmdjYXJ0ZGV2IiwiYXV0aF90aW1lIjoxNzA5NzAwNTcyLCJ1c2VyX2lkIjoiR0duUnNvMmVxb2FSUUYzbWxaSEVQcUg0cUIyMiIsInN1YiI6IkdHblJzbzJlcW9hUlFGM21sWkhFUHFINHFCMjIiLCJpYXQiOjE3MDk3MDA1NzIsImV4cCI6MTcwOTcwNDE3MiwiZW1haWwiOiJtbG9tYm95QHF1YWR4Lnh5eiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1sb21ib3lAcXVhZHgueHl6Il19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.QVSzUj8cqAQAEFZPwnObl8z3ZAjvojdHmnSp0IE8zzBgtKFpeKCMywr4peGetX1iHzVs7RW_eRppf7erTqroBxZIFRCDl-AquA-o1JlTnt4eSlBs5ZWgPIE_hEZM3-gFNJiZKTjyczexg4yUlPeacbdu5NT_nmza-rTD1TMEmNhAO4UDScOqeb3gLsgcVZ_34_jrv1J5EvnqEPBSX4DFKdWfbzYZ2qV21icn51dY_tyZTsElwFNaGwn6efx0e4I710xAAFwftNf5a7xgEhUB2-aHdxiS-S113Vs-rfXFzriEvlUI3IgNF273_hXfRt8sJbDYoJEL0vGU0tP6uldJtg'

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
