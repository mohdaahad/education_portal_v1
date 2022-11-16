# Sample Django Application

![alt text](docs/demoscreenshot.png)


Sample app to deploy on AWS Lambda for my talk at PyCon India 2020

It displays data from [Nasa Data API](https://api.nasa.gov/)

## Setup

1. Create a Python 3.6 virtual env
```
python3 -m venv venv
```

2. Activate the virtual env
```
source venv/bin/activate
```

3. Upgrade pip to latest version and install dependencies
```
pip install --upgrade pip && pip install -r requirements.txt
```

4. Run the application!
```
cd src/
python manage.py runserver
```

## Generating NASA DATA API Key

By default the app uses a `DEMO_KEY` to make API calls, it maybe however too restrictive depending on your usage. So you might want to generate your own key.

1. Head over to [NASA DATA API](https://api.nasa.gov)
2. Look for 'Generate API Key' section
3. Fill in the form details
4. You should see something like this, copy this key to the [.sample-env](.sample-env) file

![alt text](docs/nasapikey.png)

### Acknowledgements

- [Nasa Data API](https://api.nasa.gov/)
- [Nasa Insight API Team](https://api.nasa.gov/assets/insight/insight_mars_wind_rose.html)
