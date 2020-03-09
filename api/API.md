# Documentation on the REST API for the Impact website


The Impact website uses a RESTful API as its backend. This is designed as an API reference for those familer with the project and REST. 


### Format
This documentation follows the format of 
`Title`

`Description`

`URL`

`JSON/CODES`


#### Authenticate user
Authenticates a user and verfies whether they are logged in

##### With username and password
Authenticate with username and password (i.e from login form)

URL: `/api/auth/logmein`

SENT: JSON:
``` json
{
    "username": 'user username',
    "password": 'user password',
}
```
RESPONSE: CODE: 

`200`: Success, user is logged in a valid

`403`: Failure, user credentials invalid

##### With token
Authenticate with token (i.e from remember me cookie)

URL: `/api/auth/whoami/<TOKEN>`

SENT: `N/A`

RESPONSE: JSON:
``` json
{
    "username": 'user username to display',
    "uuid": 'user uuid to use for searches',
}
```


#### Get post(s)
Get a post or posts from the database

SENT: JSON:
```json
{
"id": "post id, or 'all' for all posts (up to 20)"
}
```


