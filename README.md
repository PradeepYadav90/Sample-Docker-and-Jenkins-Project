# Sample-Docker-and-Jenkins-Project

# Flask To-Do API

A simple Flask-based REST API for managing to-do tasks. This project is containerized with Docker, ready for CI/CD with Jenkins, and deployable on an AWS EC2 instance.

-------------------------
📁 Project Structure:
-------------------------
- app.py                      # Main Flask app logic
- requirements.txt            # Python dependencies
- Dockerfile                  # Docker configuration
- Jenkinsfile                 # Jenkins pipeline automation
- .gitignore                  # Git ignored files
- README.md                   # Project guide (this file)

-------------------------
☁️ Deploy on AWS EC2:
-------------------------
1. Launch an EC2 Instance:
   - Choose Ubuntu 20.04
   - Open ports: 22 (SSH), 5000 (Flask), 8080 (optional for Jenkins)

2. SSH into EC2:
   ssh -i your-key.pem ubuntu@<your-ec2-public-ip>

3. Install required software:
   Jenkins and Docker

4.Run the Jenkins Build

5. Open in your browser:
   http://<your-ec2-public-ip>:5000

-------------------------
🤖 Jenkins Pipeline:
-------------------------
1. Go to Jenkins dashboard > New Item > Pipeline
2. Select “Pipeline script from SCM”
3. Paste your GitHub repo URL
4. Jenkins will detect the Jenkinsfile automatically

-------------------------
📦 requirements.txt:
-------------------------
flask


