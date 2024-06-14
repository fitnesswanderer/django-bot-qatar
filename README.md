# Qatar Baggage Chatbot
Qatar Baggage Chatbot is a machine learning based intelligent chatbot designed to provide human-like conversation. 
Chatbot is created with intention to shorten the gap between business and customer and get queries answered regarding baggage.  

# Technologies Used:
- Python3
- Django Framework
- Tensorflow
- NLTK
- Numpy
- HTML, CSS
- JavaScript

### Prerequisites
You must have django,nltk,numpy,tensorflow installed

### Project Structure
This project consists of:
1. When a Django project is created,files are created automatically.
   
2.jsonfile.json- This is a json file contaning input which may be given to chatbot by user and the response given by bot. It is a data given to chatbot.We can also use LLMs like openAI to chat with relevant data for the business.

3. templates - This folder contains the HTML template (index.html) to allow user to enter question and displays the response.
4. 
5. static - This folder contains the stylesheets folder with staticStyle.css file which has the styling required for out index.html file.It containes images as well used for UI.

# How to run ChatBot on your computer 🤔
- Clone the repository:
```
git clone https://github.com/fitnesswanderer/django-bot-qatar.git
cd djangobotqatardemo
```

- Install the required packages.
```
pip install -r requirements.txt
```
- First create `secret key` for project
- Requirements for creating new key:
	- Be a minimum of 50 characters in length
	- Contain a minimum of 5 unique characters
	- Not be prefixed with "django-insecure-"

- Now open project directory `/django-bot-qatar/project/` where `settings.py` is located.
- Create new `.env` file and add the newly generated `secret key`
- .env file should look like this:
```
SECRET_KEY = "dlm*zt#1-3g!xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
- Save the .env file
- Do the migrations 
```
python manage.py migrate
```
Run the Django server
```
python manage.py runserver
```

- A link http://127.0.0.1:8000/ is created and click on it to open the chatbot. 

