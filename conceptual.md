### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Javascript is used more often for front end programming while Python is more for backend programming.  Python has slightly different formatting that javascript, but is often simpler to use

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

one way is to use if, ie: 
if c in myDict
val = myDict[c]
 
 or you can use get with a default value if a values does not exist such as 

 val= myDict.get('c', defaultVal)

- What is a unit test?

A unit tests small parts of code such as a function unlike a integration test that tests how functions work together

- What is an integration test?

An integration tests how functions work together

- What is the role of web application framework, like Flask?

It makes the complicated process of rendering websites possible and does a lot of the behind the scene processes that we dont
even think about for us

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  passing in a parameter is more user friendly, and its easier to identify for both programming and end user.  

- How do you collect data from a URL placeholder parameter using Flask?

Route parameters are enclosed in < > so it would look like
@app.route('/webpage/<user_selection>')
def getSelection(user_selection):
  return('{user_selection}') or whatever you want to do with {user_selection} 


- How do you collect data from the query string using Flask?

you first have to import request from flask
then you use request.args.get('whatWeAreTryingToGet') so
UserInput = request.args.get('userSelection')

if we are using POST we use information = request.form.get('information')

- How do you collect data from the body of the request using Flask?

- What is a cookie and what kinds of things are they commonly used for?

a cookie stores small amounts of information about the user.  They are sent back to the server with every request.  It can store preferences and identify the user

- What is the session object in Flask?

session is encrypted cookie like data, but its stored on the server side.  It uses a secret_Key to keep information encrypted.  It stores informatin in a dictionary. you need to 
import session from flask for it to work

- What does Flask's `jsonify()` do?

it turns a python dictionary into JSON, which is used alot for web API's
