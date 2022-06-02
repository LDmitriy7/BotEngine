# Template for telegram bots

## Run

### Requirements:

- `python3.10`
- `pipenv`
- `mongo`

### Prepare:

1) Create file `.env` from `sample.env`
2) Command `pipenv install`
3) Command `pipenv shell`

### Start:

Command `python app.py`

## Deploy

### Requirements:

- `docker`
- `docker-compose-plugin`
- `bash`

### Prepare:

1) Create file `.env` from `sample.env`
2) Open `bash`

### Start:

Command `. scripts/deploy.sh`

### Stop:

Command `. scripts/stop.sh`

### Logs:

Command `. scripts/logs.sh`
