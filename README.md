# CropCare - Crop Recommendation System

## Overview

CropCare is a web-based crop recommendation system developed using Django and Machine Learning. It helps users identify suitable crops for cultivation based on soil nutrient values and environmental conditions.

The system uses a trained Random Forest model to analyze agricultural parameters and recommend an appropriate crop. It also provides user authentication, prediction history, profile management, and administrative features through a web interface.

## Features

- **Machine Learning-Based Prediction:** Recommends suitable crops using a trained Random Forest model.
- **User Registration and Authentication:** Supports account creation and secure login.
- **Crop Prediction:** Accepts agricultural and environmental parameters to generate crop recommendations.
- **Prediction History:** Allows users to review previous crop predictions.
- **User Profile Management:** Provides profile viewing and updating functionality.
- **Password Management:** Allows authenticated users to change their passwords.
- **Administrative Dashboard:** Provides administrative access to relevant application information.
- **Responsive User Interface:** Uses HTML, CSS, and Bootstrap to provide a user-friendly experience.

## Technology Stack

### Backend
- Python
- Django

### Machine Learning
- Scikit-learn
- NumPy
- Pandas
- Pickle for loading the trained model

### Frontend
- HTML5
- CSS3
- Bootstrap
- JavaScript
- SweetAlert2

### Database
- SQLite

### Development Tools
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
crop_recommendation/
|
|-- crop_recommendation/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   |-- wsgi.py
|
|-- recommender/
|   |-- migrations/
|   |-- ml/
|   |   |-- crop_recommendation_RF.pkl
|   |   |-- loader.py
|   |-- static/
|   |   |-- css/
|   |   |-- images/
|   |-- templates/
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|
|-- manage.py
|-- .gitignore
|-- README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/smriti3114/cropcare-crop-recommendation
cd cropcare-crop-recommendation
```

Replace `YOUR_USERNAME` with your GitHub username and use your actual repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
venv\Scripts\activate
```

### 3. Install Dependencies

Install the packages used by the project:

```bash
pip install django numpy pandas scikit-learn
```

If the project uses additional packages, install those as well. It is recommended to create and maintain a `requirements.txt` file containing the project's actual dependencies, then install them with:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Before deploying the application or publishing it publicly, configure sensitive settings such as Django's secret key and debug mode through environment variables.

Do not commit production credentials, private keys, or other secrets to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the prompts to configure the administrator account.

### 7. Start the Development Server

```bash
python manage.py runserver
```



## How It Works

1. The user registers or logs in to the application.
2. The user enters the required soil and environmental parameters.
3. The backend validates the submitted inputs.
4. The trained Random Forest model processes the input features.
5. The application displays the predicted crop recommendation.
6. The prediction can be stored in the database and viewed later through prediction history.

The model file must be compatible with the installed machine learning library versions and the feature order expected by the application.

## Input Parameters

The application uses agricultural and environmental features for crop prediction, such as:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

The exact parameter names and expected ranges depend on the dataset and trained model used by the application.

## Future Improvements

- Deploy the application to a production hosting platform.
- Add comprehensive input validation and automated tests.
- Improve model evaluation and document its performance metrics.
- Add visualizations for historical predictions.
- Integrate weather or soil data from external services.
- Improve accessibility and mobile responsiveness.

## Security Considerations

- Keep Django's production `SECRET_KEY` private.
- Disable debug mode in production.
- Configure allowed hosts and HTTPS for deployment.
- Use secure password and session settings.
- Avoid committing databases containing personal information.
- Review uploaded model files and dependencies before deployment.

## Disclaimer

CropCare provides machine learning-based crop recommendations for informational purposes. Actual crop suitability depends on additional factors, including soil characteristics, local climate, water availability, farming practices, and regional agricultural guidance.

## Author

