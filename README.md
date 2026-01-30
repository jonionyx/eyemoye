# API Test Automation Framework

Python-based test automation framework for RESTful APIs built with **pytest** and **requests**. This framework features global authentication, environment switching, contract validation and automated reporting.
## Features
- **Environment switching:** Run tests against different api resources for testing purposes, this set up  mimicks tunning tests against different environments such as Dev or Staging or Prod using CLI flags
- **Global Auth:** Centralised session management with automatic Bearer token injection
- **Contract Testing:**JSON Schema validation using jsonschema
- **Dynamic Data**: Synthetic data generation using Faker
- **CI/CD Ready:**Configured GitHub Action workflows 
- **Reporting:** 
  - Rich HTML reports with request / response logs on failure
  - Allure reporting with Json Data attachment for drilling down capabilities
- **Performance SLAs:** 

## Prerequisites
- Python: 3.10 or higher

## Installation & Setup

















## REPORTING
#### Generating the Report
Generating an Allure report is a two-step process:
1. **Run tests** to generate raw JSON data files:
 ``` 
 pytest tests/ --env staging --alluredir=allure-results
 ```
1. **Serve the report** to convert those files into a visual dashboard:
```
allure serve allure-results
```
2. ;
   


### Mock Data with FAKER 
1. [readthedocs](https://faker.readthedocs.io/en/master/)
2. [geeksforgeeks](https://www.geeksforgeeks.org/python-faker-library/#)
3. [zetcode](https://zetcode.com/python/faker/)
   

### Free API Resources
1. NASA Open APIs: https://api.nasa.gov/
 Nasa API that return a list of asteroids: Asteroids - NeoWs : https://api.nasa.gov/neo/rest/v1/feed
2. Bill Pay: https://gauravkhurana.in/practise-api/index.html