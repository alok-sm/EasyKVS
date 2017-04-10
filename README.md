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


## Using the API

The API endpoint `/kvs` is all you need. You can send the following functions
The API throws an error if the `key` is `null` or if the request body is `null` for the `POST` and `PUT` requests

#### `GET` to get the value of a key
```
GET /kvs/<key>
```

Returns the value of the key with response code 200 if the key exists
Sends a `500` error if the key does not exist
  
#### `POST` to set the value of a key
```
POST /kvs/<key>
```

Sets the value for the key to the text sent in the request body and will return a `204` empty response
Sends a `500` error if you try to set the value for a key that exists

#### `PUT` to modify the value of a key
```
PUT /kvs/<key>
```

Modifies the value for the key to the text sent in the request body and will return a `204` empty response

If the `strict_modify` key is set to `true` in `config.json`, this will return a `500` error if you try to 
modify the value of a key that does not exist. 

If the `strict_modify` key is set to `false`, this will behave similar to the `POST` request when the key 
does not exist, i.e: It will create a new key and set the value to the string in the request body.

#### `DELETE` to drop a key
```
DELETE /kvs/<key>
```

Deletes the key value pair for the key sent and will return a `204` empty reponse


If the `strict_delete` key is set to `true` in `config.json`, this will return a `500` error if you try to 
delete a key that does not exist. 

If the `strict_delete` key is set to `false`, this will not throw an error and will simply
send a `204` empty response even if the key to be deleted never existed
