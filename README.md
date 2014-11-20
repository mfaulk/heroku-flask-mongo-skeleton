# Heroku Python Skeleton

## Usage

### Initial

```bash
$ git clone https://github.com/yuvadm/heroku-python-skeleton.git
$ cd heroku-python-skeleton
$ heroku create
$ heroku config:set APP_SETTINGS=config.ProductionConfig
$ heroku config:set HEROKUHQ_URL = 'mongodb://<user>:<password>@dogen.mongohq.com:10059/<your-database>'
$ git push heroku master
```

### Database