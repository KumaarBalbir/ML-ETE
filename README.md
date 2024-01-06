# Overview 
This repository contains code for an end-to-end machine learning web application developed in Python. The application is about prediction of math score of a student based on certain attributes like Gender, Race/Ethnicity, Writing score, Reading score, etc. The application does not focus on the quality of model and dataset rather a good focus on making a generic template for end to end application.

- **Github Actions**: Platform and set of tools provided by Github, that allows you to automate various tasks such as CI/CD pipelines, in response to events that occur in your repository.
- **Github Workflow**: A GitHub Workflow is an automated procedure defined using GitHub Actions. It consists of one or more jobs, each containing a series of steps. Workflows are written in `YAML` and describe how GitHub Actions will be used to perform a specific task or series of tasks in response to a specific event.
- **Github Runner**: It is execution environment where github workflows run. When you create a workflow using GitHub Actions, these workflows require a runtime environment to execute the defined steps and tasks. The GitHub-provided infrastructure might not cover all scenarios or might not be available in all regions. This is where GitHub Runners come into play.
- **Continuos Integration (CI)**: This involves tasks such as building your code, running tests, and performing static code analysis whenever new code is pushed to the repository.
- **Continuous Deployment (CD)**: This part involves deploying your application to your hosting platform (Azure, AWS, etc.) after the CI checks have passed. This might include steps like building a Docker image, pushing it to a container registry, and deploying it to your hosting service.
- **CI/CD pipeline**: Setting up a CI/CD pipeline using GitHub Actions involves creating a workflow file (typically named `main.yml` or similar) in your repository's `.github/workflows` directory. This workflow file defines the sequence of steps that GitHub Actions will execute when triggered by an event, such as a new commit being pushed to the repository.

## Got confused among github actions, github workflows and github runner?
Here is how they are connected:
- When a specific event (such as a push, pull request, etc.) occurs in your GitHub repository, GitHub Actions looks for the workflows defined in `.github/workflows`.
- Once triggered, GitHub Actions selects an available runner (either a GitHub-hosted runner or a self-hosted runner) to execute the workflow.
- The runner then downloads the necessary code and executes the jobs and steps defined in the workflow.
- Within each job, the runner runs the actions specified in the workflow file, executing the tasks required for the CI/CD pipeline or other automation tasks.
- As actions within the workflow are completed, the runner reports the status and results back to GitHub.
# Features 
- Machine Learning algorithms: `Random Forest`, `Decision tree`, `Gradient Boosting`, `Linear Regression`, `XGBRegressor`, `CatBoosting Regressor`,`AdaBoost Regressor`
- Deployment Platforms:
    - **Azure**
        - Container Registry
        - Azure web app
    - **AWS**
      - Elastic Container Registry
      - Elastic Cloud Compute (EC2)
- Customization:
    - To check data congestion: `python src/components/data_ingestion.py`
    - To check data transformation: `src/components/data_transformation.py`
    - To check model trainer: `src/components/model_trainer.py`
    - To check utils functions: `src/utils.py`
    - To check custom exception: `src/exception.py`
    - To check logging: `src/logger.py`
    - To check pipeline: `src/pipeline/` (Best practise is to define ingestion, transformation, training, prediction all in `pipeline` directory).
    - To check setup file: `./setup.py`
    - To check main file: `./app.py`
    - To check dockerfile: `./Dockerfile`
    - To check aws workflow: `./.github/workflows/main.yml`
    - To check azure workflow: `./.github/workflows/main_mathscoreprediction.yml`

# How to reproduce code and environment locally?
1. Clone the repository:
   ```bash
   git clone https://github.com/kumaarbalbir/ML-ETE.git
   cd ML-ETE
2. Create and activate conda virtual environment:
   ```bash
   conda create --name venv python=3.8
   conda activate venv
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python app.py
### Additional Notes: 
- Ensure you have Python 3.8 installed.
- Modify the virtual environment name (`venv`) according to your preferences.

# Dockerizing the Application
1. Install the docker on your system and Open `Docker Desktop`.
2. Run the following command from your terminal or command prompt:
   ```bash
   $ docker images
   NOTE: If it produces output something like, congrats, you are good to go :
   REPOSITORY      TAG       IMAGE ID       CREATED      SIZE
   mathscore-app   latest    1f07bbe6c0e8   2 days ago   3.01GB

3. Build the docker image:
   ```bash
   docker build -t <your-image-name>
4. Run the docker container:
   ```bash
   $ docker run -p 5000:5000 <your-image-name>
   Adjust the port mapping (-p host_port:container_port) if you want your application (app.py) to run on different port.
5. Access the application:
   Once the container is running, access the application in your browser or through an HTTP request at `http://localhost:5000` (or the specified port).
6. Do inference:
   Move to `http://localhost:5000/predictdata` to check if your model predicts for the given data.
7. Stop the container:
   ```bash
   docker stop <your-image-name>

