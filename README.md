# API Test Automation Framework
Python-based test automation framework for RESTful APIs built with **pytest** and **requests**. This framework features global authentication, environment switching, contract validation, and automated reporting.

















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
   