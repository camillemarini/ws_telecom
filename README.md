Website of the Telecom workshop about scientific computing with python and software engineering best practices.

#### How to run it locally?

##### 1. Install the application

Clone the project: `git clone https://github.com/camillemarini/ws_telecom.git`
Install dependencies (might be useful to create a virtual environment before, eg using [virtualenv and virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)):
`pip install -r requirements.txt`.

##### 2. Define environment variables

- `EMAIL_HOST_PASSWORD`: password of the email account workshop.python.telecom

##### 3. Apply migrations

Run: `python manage.py migrate`

##### 4. Run the server (localhost)

Run: `python manage.py runserver`

