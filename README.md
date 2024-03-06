**Load Testing Script for API Endpoint**  
This Python script is designed to help you load test or test throttling settings on an API endpoint. It utilizes asynchronous programming with asyncio and aiohttp libraries to send multiple HTTP requests concurrently.  

**Prerequisites**   
Python 3 installed on your system  
The following Python libraries installed:  
* asyncio  
* aiohttp  
You can install these libraries using pip:    

**Copy code**   
pip install asyncio aiohttp  

Usage  
Open the Python script **throttle.py** in your preferred text editor.  
Update the script with your endpoint URL, payload, bearer token, and other parameters as needed.  
Save the changes to the script.  
Open a terminal or command prompt.  
Navigate to the directory containing the script.  
Run the script using the following command:  
**Copy code**  
**python3 throttle.py**   
The script will start sending requests to the specified endpoint. You can adjust the number of requests and the time interval between requests in the script according to your testing requirements.  

Script Parameters  
base_url: The base URL of your API endpoint.  
endpoint_path: The endpoint path to test.  
payload: The sample payload to send in the request.  
bearer_token: The bearer token for authentication.  
num_requests: The number of requests to send.  
interval: The time interval between each request (in seconds).  
headers: Additional headers to include in the request.  

