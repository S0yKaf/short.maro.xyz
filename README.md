# short.maro.xyz
Url Shortner for maro.xyz

## Requirements
* Python3
* Virtualenv (optional)
* Pip3
* Bower

## How to run

### setup a virtualenv (optional)
* `$ virtualenv env`
* `$ . env/bin/activate`

### install requirements
* `$ pip3 install -r requirements.txt`
* `$ bower install`

### Run
`$ python3 app.py`

---

## Usage

### exemple
####request
```
curl -H "Content-Type: application/json" -X POST -d '{"url":"http://facebook.com"}' http://localhost:5000/`
```
####response
```
{
  "short_url": "localhost:5000/VSoVV3M",
  "url": "http://facebook.com"
}
```
