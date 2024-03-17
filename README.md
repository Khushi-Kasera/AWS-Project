## AWS Cloud Deployment for Iris Data Analysis with Flask

### Overview:
- This project utilizes AWS (Amazon Web Services) to deploy a machine learning model trained on the Iris dataset. The model is deployed using Flask, allowing users to make predictions on new Iris flower samples. The model is serialized using pickle and deployed on an AWS EC2 instance, providing a scalable and accessible solution for real-time predictions.

### Features:
1. Utilizes the famous Iris dataset for classification tasks.
2. Trains a machine learning model to classify Iris flower species based on sepal and petal measurements.
3. Deploys the trained model on an AWS EC2 instance using Flask.

### Deployment Steps:
1. Clone Repository: Clone the project repository to your local machine.
2. Set Up AWS Account: Create an AWS account if you don't have one already.
3. Launch EC2 Instance: Launch an EC2 instance on AWS and configure security groups to allow inbound traffic on port 5000.
4. Install Dependencies: SSH into the EC2 instance and install necessary dependencies using pip install -r requirements.txt.
5. Run Flask App: Start the Flask application using python app.py.

### Repository Structure:
1. app.py: Flask application script containing routes for model prediction.
2. model.pkl: Serialized machine learning model trained on the Iris dataset.
3. requirements.txt: List of Python dependencies required for the project.
4. templates/: Directory containing HTML templates for the user interface.

### Usage:
1. Navigate to the deployed Flask application URL.
2. Enter the sepal and petal measurements for an Iris flower sample.
3. Click the "Submit" button to receive the predicted Iris species.

Link - "file:///Users/khushi/Documents/All_Projects/IRIS_Cloud_Project/Templates/main.html"
