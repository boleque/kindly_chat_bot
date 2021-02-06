# Kindly chat bot

Simple chatbot, that able to reply on four types of content: 
1) Greeting - something the bot can say at the beginning of the conversation; 
2) Sample dialog - a reply to a full phrase the user says;
3) Keyword dialogue - a reply to something that is mentioned by the user; 
4) Fallback - a reply for when the bot does not understand what the user is saying.

## REST API

#### Starting conversation
URL: /api/conversation/start
Method: POST

##### Data Parameters in JSON:
```sh
language String (required)
```
##### Success Response
New conversation started
**Code**: 201
**Content**: unique id in response in JSON format

```sh
>>> import requests
>>> reply = requests.post('http://0.0.0.0:8000/api/conversation/start', json={"language":"en"})
>>> r.text
u'{"user_id":1,"message":"Hi there!"}'
```
##### Error Response
Required field is missing or wrong
**Code**: 400
**Content**: {"language":[{"message":"This field is required.","code":"required"}]}'

#### Continue conversation
URL: /api/conversation/message
Method: POST

##### Success Response
Chat bot returns a reply
**Code**: 200
**Content**: reply in JSON format

```sh
>>> import requests
>>> reply = requests.post('http://0.0.0.0:8000/api/conversation/message/', json={"user_id":1,"message":"Do you know any robot jokes?"})
>>> reply.text
u'{"message":"Do you know why robots take summer holidays? To charge the batteries!"}'

```
##### Error Response
User id doesn't exist
**Code**: 404
**Content**: wrong user id

Required field is missing or wrong
**Code**: 400
**Content**: {"message":[{"message":"This field is required.","code":"required"}]}'

####  Build&Run REST API service
##### Build app
```sh
docker-compose build
```
##### Run app
```sh
docker-compose up
```
##### Development tools

###### Run unit tests
```sh
docker-compose run app sh -c "python manage.py test"
```
##### REST API service configuration
By default service bind to 0.0.0.0 interface by 8000 port.



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
