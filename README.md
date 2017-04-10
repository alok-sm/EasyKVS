# EasyKVS
EasyKVS - an easy key value store server written in Python for small web apps

## Starting the server

### Install the Requirements

Install all the required packages using pip:

```
pip install requirements.txt
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

- `debug`: If this is set to `true`, the server auto restarts if the source code of the server changes

- `threaded`: If this is set to `true`, the server runs on multiple threads for better performance but debugging might be harder.

- `strict_modify`: refer to the [`PUT` requestion section](https://github.com/alok-sm/EasyKVS/blob/master/README.md#put-to-modify-the-value-of-a-key) of this readme

- `strict_delete`: refer to the [`DELETE` requestion section](https://github.com/alok-sm/EasyKVS/blob/master/README.md#delete-to-drop-a-key) of this readme


## Using the API

The API endpoint `/kvs` is all you need. You can send the following functions
The API throws an error if the `key` is `null` or if the request body is `null` for the `POST` and `PUT` requests

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
