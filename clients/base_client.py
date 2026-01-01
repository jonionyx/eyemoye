import requests
import logging
import json
from utils.helpers import logger

class BaseClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        
        # Default headers
        self.session.headers.update({"Content-Type": "application/json"})


    def authenticate(self, username, password):
         """
        Authenticates against the endpoint and extracts the JWT.
        """
         if "herokuapp" in self.base_url:
              login_url = f"{self.base_url}/auth"
              payload = {"username": username, "password": password}
              response = self.session.post(login_url, json=payload)
              token = response.json().get("token")
         elif "reqres" in self.base_url:
              login_url = f"{self.base_url}/auth"
              payload = {"username": username, "password": password}
              response = self.session.post(login_url, json=payload)
              token = response.json().get("token") 
         elif "ethixdevelopment" in self.base_url:             
              login_url = f"{self.base_url.rstrip('/')}/api/authenticate/eb360" # for my original auth url
              payload = {"username": username, "password": password}
              response = self.session.post(login_url, json=payload)
              if response.status_code != 200:
                   raise ValueError(f"Auth failed with status {response.status_code}: {response.text}")
              token = response.json().get("authToken")             
         else:
              login_url = f"{self.base_url}" # for my original auth url
              payload = {"username": username, "password": password}
              response = self.session.post(login_url, json=payload)
              token = response.json().get("authToken")


         if not token:
              raise ValueError("Login failed: No token received")
         

         # Restful-booker uses a custom 'Cookie' header instead of 'Bearer'
         if "herokuapp" in self.base_url:
              self.session.headers.update({"Cookie": f"token={token}"})
         else:
              self.session.headers.update({"Authorization": f"Bearer {token}"})
              


          

     #     login_url = f"{self.base_url}/auth"

     #     payload = {
     #          "username": username,
     #          "password": password
     #     }
     #     try:
     #          response = self.session.post(login_url, json=payload, timeout=self.timeout)
     #          response.raise_for_status()

     #          data = response.json()
     #          token = data.get("token")

     #          if not token:
     #               raise ValueError(f"Login successful but 'authToken' missing from response: {data}")
              
     #        # Persist token for all future requests in this session
     #          self.session.headers.update({"Authorization": f"Bearer {token}"})
     #          return data
     #     except requests.exceptions.RequestException as e:
     #          logging.error(f"Authentication Request Failed: {e}")
     #          raise


    def _request(self, method, endpoint, **kwargs):
           # Centralised loggins goes here
           path = endpoint if endpoint.startswith('/') else f"/{endpoint}"
           url = f"{self.base_url}{path}"
           kwargs.setdefault('timeout', self.timeout)

          #  Log the Request
           logger.info(f"REQUEST: {method} {url}")
           if "json" in kwargs:
                logger.info(f"Payload: {json.dumps(kwargs['json'])}")


           response = self.session.request(method, url, **kwargs)

          #  Log the Response
           logger.info(f"RESPONSE: {response.status_code} ({response.elapsed.total_seconds()}s)")

           try:
               #  Use try/except in case the response is not JSON, for example, an HTML error page
               logger.info(f"Body: {json.dumps(response.json(), indent=2)}")
           except Exception:
                logger.info(f"Body: {response.text}")
          
           return response             
                


    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)
    
    def post(self, endpoint, data=None, json=None, **kwargs):
        return self._request("POST", endpoint, data=data, json=json, **kwargs)
        