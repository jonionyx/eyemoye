# This is a Utility class to provide acentralised place for data generation
import random
import string
from faker import Faker
import logging
import os
from datetime import datetime

fake = Faker()

class DataGenerator:

 @staticmethod
 def generate_random_string(length=10):
    """Generate a random alphanumeic string for IDs or passwords."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))   


 @staticmethod
 def generate_restfulbooker_user_payload():
        """Generate a realistic user object for POST requests"""
        return {
           "firstName": fake.first_name(),
           "lastName": fake.last_name(),
           "username": fake.user_name(),
            "email": fake.email(),
            "password": DataGenerator.generate_random_string(12),
        #     "createdAt": fake.past_date(),
        # "modifiedAt": fake.date_time_ad(),
        "icon": fake.image_url(),

        }
def generate_placeholder_user():
         return {
               "name": "Anthony Joshua",
               "username": fake.user_name(),
               "email": fake.email(),
               "address": {
                    "street": fake.street_address(),
                    "suite": "Suite 323",
                    "city": fake.city(),
                    "zipcode": fake.zipcode(),
                    "geo": {
                         "lat": 40.741895,
                         "lng": 40.741895,
                         }
                         },
                         "phone": "234 5678901",
                         "website": fake.url(),
                         "company": {
                              "name": "Company Testa",
                              "catchPhrase": f"We Build Dream",
                              "bs": "harness real-time e-markets"
                              }
                              },
         
    
@staticmethod
def setup_logger():
    """Configures a global logger for the framework."""
    log_dir = "logs"
    if not os.path.exists(log_dir):
            os.makedirs(log_dir)
    
    
    log_file = os.path.join(log_dir, f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logger()
# 
     

@staticmethod
def generate_random_string(length=10):
    """Generate a random alphanumeic string for IDs or passwords."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

@staticmethod
def get_invalid_email():
    """ Returns email that shoul dfail email validation"""
    return random.choice(["plainaddress", "#@%^%#$@#$@#.com", "@example.com" ])


