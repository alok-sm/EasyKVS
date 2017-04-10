# EasyKVS
EasyKVS - an easy key value store server written in Python for small web apps

## Starting the server

### Install Python 2.7

Python 2.7 can be installed from [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Install pip

Pip can be installed from [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/)

### Download the source

Run the git clone command to clone this repo to your machine

```
git clone https://github.com/alok-sm/EasyKVS.git
```

### Install the Requirements

`cd` into the EasyKVS directory

```
cd EasyKVS
```

Install all the required packages using pip:

```
pip install --upgrade -r requirements.txt
```


### Running server

Run the routes.py file:

```
python routes.py
```


### Configuring the server (optional)

You can configure the server by modifying the `config.json` to suit you needs. Here's what each key does:
- `host`: This sets the host of the server. `0.0.0.0` allows you to access the server from a remote location whereas `localhost` only lets you access the API from a local site. You can also set this value to the IP address of the machine that you are using to run the server.

- `port`: By default, the server runs on port `8000` but you can change this if it conflicts with your webserver.

- `storage_file`: This key sets the file name of the file where the data is stored. If the file name does not exist, an empty file is created with the given name.

- `debug`: If this is set to `true`, the server auto restarts if the source code of the server changes

- `threaded`: If this is set to `true`, the server runs on multiple threads for better performance but debugging might be harder.

- `strict_modify`: refer to the [`PUT` requestion section](https://github.com/alok-sm/EasyKVS/blob/master/README.md#put-to-modify-the-value-of-a-key) of this readme

- `strict_delete`: refer to the [`DELETE` requestion section](https://github.com/alok-sm/EasyKVS/blob/master/README.md#delete-to-drop-a-key) of this readme

- `allow_empty_values`: refer to the [Using the API](https://github.com/alok-sm/EasyKVS/blob/master/README.md#using-the-api) section of this readme.


## Using the API

The API endpoint `/kvs` is all you need. You can send the following HTTP methods to perform actions on the API

The API throws an error if the `key` is `null` or empty

if the `allow_empty_values` key is set to `false` in `config.json`, the API will throw and error if the request body is 
`null` for the `POST` and `PUT` requests, i.e: The API will not let you set empty values. If it is set to `true`, the 
API will allow you to store empty values.

#### `GET` to get the value of a key
```
GET localhost:8000/kvs/<key>
```

Returns the value of the key with response code 200 if the key exists
Sends a `500` error if the key does not exist
  
#### `POST` to set the value of a key
```
POST localhost:8000/kvs/<key>
```

Sets the value for the key to the text sent in the request body and will return a `204` empty response
Sends a `500` error if you try to set the value for a key that exists

#### `PUT` to modify the value of a key
```
PUT localhost:8000/kvs/<key>
```

Modifies the value for the key to the text sent in the request body and will return a `204` empty response

If the `strict_modify` key is set to `true` in `config.json`, this will return a `500` error if you try to 
modify the value of a key that does not exist. 

If the `strict_modify` key is set to `false`, this will behave similar to the `POST` request when the key 
does not exist, i.e: It will create a new key and set the value to the string in the request body.

#### `DELETE` to drop a key
```
DELETE localhost:8000/kvs/<key>
```

Deletes the key value pair for the key sent and will return a `204` empty reponse


If the `strict_delete` key is set to `true` in `config.json`, this will return a `500` error if you try to 
delete a key that does not exist. 

If the `strict_delete` key is set to `false`, this will not throw an error and will simply
send a `204` empty response even if the key to be deleted never existed

## Troubleshooting

In some machines, you might need to use `python2` instead of `python` and `pip2` instead of `pip`

## Checking stored values

You can run
```
python print_db.py <storage file name>
```
to print out the contents of the data stored in the specified file name in `JSON` format.

If no file name is specified, the script defaults to the file specified in `config.json`
