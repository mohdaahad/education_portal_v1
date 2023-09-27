# Sample Django Application

![alt text](docs/demoscreenshot.png)


Sample app to deploy on AWS Lambda for my talk at PyCon India 2020

It displays data from [Nasa Data API](https://api.nasa.gov/)

## Setup

1. Create a Python 3.6 virtual env
```
python3 -m venv venv
```

2. Activate the virtual env
```
source venv/bin/activate
```

3. Upgrade pip to latest version and install dependencies
```
pip install --upgrade pip && pip install -r requirements.txt
```

4. Run the application!
```
cd src/
python manage.py runserver
```

## Generating NASA DATA API Key

By default the app uses a `DEMO_KEY` to make API calls, it maybe however too restrictive depending on your usage. So you might want to generate your own key.

1. Head over to [NASA DATA API](https://api.nasa.gov)
2. Look for 'Generate API Key' section
3. Fill in the form details
4. You should see something like this, copy this key to the [.sample-env](.sample-env) file

![alt text](docs/nasapikey.png)

### Acknowledgements

- [Nasa Data API](https://api.nasa.gov/)
- [Nasa Insight API Team](https://api.nasa.gov/assets/insight/insight_mars_wind_rose.html)
# education_portal_v1



Project Overview:
This project aims to create a quiz application that allows users to log in, sign up, and take quizzes. The application will also manage user sessions and store user data in the backend.

Features:

1. User Authentication:

Login Page: Users can log in with their username and password.
Signup Page: New users can create an account by providing their name, username, father's name, class, email, and password.
2. Quiz Management:

Once logged in, the system checks if the user has taken a quiz before.
If the user has taken a quiz, a "Logout" button is displayed, and they cannot retake the quiz.
If the user has not taken a quiz, a "Start Quiz" button is displayed.
3. Quiz Information:

Clicking the "Start Quiz" button provides information about the quiz, such as the number of questions, the time allocated per question, and the total quiz duration.
4. Taking the Quiz:

Users are presented with quiz questions, each with four options.
A timer shows the remaining time for each question.
Users must select an answer within the time limit.
If the user doesn't select an option in time, they cannot answer the question, and the next question is presented.
5. Quiz Completion:

After answering all questions or when the time runs out, the quiz ends.
Users are shown their quiz results and score.
6. Data Storage:

User data (including name, username, father's name, class, email) is stored in the backend database.
Quiz results are stored in the backend, indicating which users have taken quizzes and their scores.
7. Session Management:

User sessions are managed to ensure security and track user actions.
If a user is logged in, they cannot access the quiz again until they log out.
8. Logout:

Users can log out of their accounts, which redirects them to the login page.
9. User Statistics:

The application provides statistics on the number of registered users and their quiz results.
10. User-Friendly Interface:

The application features an intuitive and user-friendly design for easy navigation.
11. Error Handling:

Proper error handling mechanisms are in place to handle login failures, invalid data, and other potential issues.
12. Security:

User passwords are securely hashed and stored in the database to ensure data security.
13. Admin Panel (Optional):

An admin panel can be implemented to manage user data, quiz questions, and monitor user activity.
Technologies Used:

Frontend: HTML, CSS, JavaScript
Backend: Server (Node.js, Python, etc.), Database (MySQL, MongoDB, etc.)
User Authentication: JWT (JSON Web Tokens) or OAuth
Timer Functionality: JavaScript or libraries like setInterval
Conclusion:
This project aims to create a feature-rich quiz application with user authentication, quiz management, data storage, and session handling. It provides an engaging and secure environment for users to take quizzes and view their results while ensuring data integrity and user privacy.





