# Focal interview project



## Getting started

To run the tests, you first need to install Python's virtualenv. Here are the steps:
```
pip install virtualenv
```
Go into project directory:
```
cd focal_interview
virtualenv venv
```
Activate virtualenv. If you are using macOS or Unix distribution:
```
source venv/bin/activate
```
For Windows:
```
.\venv\Scripts\activate
```
Next, install project dependencies:
```
pip install -r requirements.txt
```

To run all tests, type the following command:
```
pytest
```
To run a specific test, use this command:
```
pytest tests/test_login.py
```
To get html report run the tests with additional option:
```
pytest --html=report.html
```
You can specify browser on which tests will be running (chrome, firefox, edge or safari).
By default tests are running on chrome.
```
pytest --browser=chrome
```

## Docs

In docs you can find some [issues](./docs/issues.md) found during creation of automation tests.
