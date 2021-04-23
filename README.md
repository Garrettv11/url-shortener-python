# url-shortener-python
URL Shortener that allows users to register and manage shortened urls

## Installation and Start

1. Open a terminal at the root directory of the project
2. Create a virtual environment with the following command:
```bash
python3 -m venv venv
```
2. Activate the virtual environment with the following command:
```bash
source venv/bin/activate
```
3. Install the required python packages by executing the following command:
```bash
pip3 install -r requirements.txt
```
4. Execute the sql migrations by executing the following command:
```bash
python3 manage.py migrate 
```
5. To start the server, run the following command:
```bash
python3 manage.py runserver
```

### Route Organization

There are two main route branches:

*/urls/manager*

and 

*/urls/r*


The *manager* route path is used for performing CRUD operations on shortened URLs.  
The *r* route path is used for resolving short urls into original long urls.


## Curl Commands

GET ALL Managed URLs
```
curl http://localhost:8000/urls/manager/
```
GET ONE Managed URL
```
curl http://localhost:8000/urls/manager/1
```
### Creating a ShortURL:

```
curl --location --request POST 'http://localhost:8000/urls/manager/' --header 'Content-Type: application/json' --data-raw '{"full_url": "http://chart.apis.google.com/chart?chs=500x500&chma=0,0,100,100&cht=p&chco=FF0000%2CFFFF00%7CFF8000%2C00FF00%7C00FF00%2C0000FF&chd=t%3A122%2C42%2C17%2C10%2C8%2C7%2C7%2C7%2C7%2C6%2C6%2C6%2C6%2C5%2C5&chl=122%7C42%7C17%7C10%7C8%7C7%7C7%7C7%7C7%7C6%7C6%7C6%7C6%7C5%7C5&chdl=android%7Cjava%7Cstack-trace%7Cbroadcastreceiver%7Candroid-ndk%7Cuser-agent%7Candroid-webview%7Cwebview%7Cbackground%7Cmultithreading%7Candroid-source%7Csms%7Cadb%7Csollections%7Cactivity|Chart"}'

```
The shorturl create endpoint returns the created shorturl object. An example looks like this:
```
{
    "id":212,
    "full_url":"http://chart.apis.google.com/chart?chs=500x500&chma=0,0,100,100&cht=p&chco=FF0000%2CFFFF00%7CFF8000%2C00FF00%7C00FF00%2C0000FF&chd=t%3A122%2C42%2C17%2C10%2C8%2C7%2C7%2C7%2C7%2C6%2C6%2C6%2C6%2C5%2C5&chl=122%7C42%7C17%7C10%7C8%7C7%7C7%7C7%7C7%7C6%7C6%7C6%7C6%7C5%7C5&chdl=android%7Cjava%7Cstack-trace%7Cbroadcastreceiver%7Candroid-ndk%7Cuser-agent%7Candroid-webview%7Cwebview%7Cbackground%7Cmultithreading%7Candroid-source%7Csms%7Cadb%7Csollections%7Cactivity|Chart",
    "short_path_component":"3q",
    "short_url":"/urls/r/3q"
}
```
The *short_url* relative url can then be used to resolve the original url by appending it to the host.  
EX: http://localhost:8000/urls/r/3q

### Resolving a ShortURL:

```
curl http://localhost:8000/urls/r/{short_path_component}
```
EX: http://localhost:8000/urls/r/3q