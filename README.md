# TinkerHub Link Generator
To generate custom links for tinkerhub events and resources!
## How it Works ?
We map the actual link to custom link and store in database. When the custom link is requested the flask web app redirect it to the original URL.
## Libraries used
- Flask
- sqlite3

## How to configure and run

Create a ```env.dev.sh``` in ops directory and add the following 

```
APP_SETTINGS=donationpage.config.TestingConfig
```

then run 

```
docker compose build
```
for building and

```
docker compose up -d
```

for running

## How to Test 
The current env.dev.sh configuration is set for testing mode. For production edit the APP_SETTINGS in env.dev.sh as

```
APP_SETTINGS=donationpage.config.ProductionConfig
```

## Contributors

1. [Gopikrishnan Sasikumar](https://github.com/GopikrishnanSasikumar)
2. [Niyas Ashraf](https://github.com/niyamax)