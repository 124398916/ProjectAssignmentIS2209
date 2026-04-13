Introduction:
We developed a small flask-based web service application about cat facts, which integrates an external API with a web interface. Our application retrieves cat facts from a public API, displaying them to the user through simple web interface. The Flask backend sends requests using Python requests library and displays the returned fact on the /catfacts page. In our project we demonstrated DevOps practices, including version control with GitHub, containerization using Docker and collaborative development through pull requests and feature branches. Docker was used to containerize the application, ensuring consistent execution across development environments. GitHub hosts the project repository and manages collaboration through pull requests, branching and issue tracking.
The application contains 2 main pages: a home page and a cat facts page, which displays a randomly generated cat fact when refreshed.
We agreed to use a lightweight feature branch workflow. All development occurred in short-lived feature branches created from the master branch. Each feature is implemented in a separate branch, as in feature/docker file, feature/ui. When the feature is complete, a pull request is opened and reviewed by another team member before merging into master. The project uses GitHub actions to automate continuous integration and deployment. Whenever a pull request is opened or code is pushed to the master branch, the pipeline runs automatically.

Context:
We illustrated the relationship between the user, the application and external services.
The primary interaction occurs between the user's web browser and the Flask application. The Flask application processes requests and retrieves data from an external cat facts API, before returning the results to the user interface. Development and deployment processes interact with additional systems such as GitHub, Docker and the CI/CD pipeline.
User (Browser)  Flask Web App  Cat facts external API
Developer  GitHub Repository  GitHub Actions  Docker Image Build  Deployment Environment
The user only interacts with the web interface, while the backend manages communication with external services.

Integration Points:
Our application integrates with several services and tools that support its functionality and development workflow.
External API integration:
Our application integrates with a public cat facts API that provides random cat facts yeah HTTP requests. The Flask backend sends a request to the API using the Python requests library. When the user navigates to the cat facts page, the backend retrieves a random fact from the API and passes the result to the HTML template for rendering. This demonstrates the aggregation of data from an external service and the ability of the application to present dynamic content
Flask Web Framework:
Flask is used as the core web framework for handling HTTP requests and routing. The framework enables the creation of endpoints such as the home page and the /catfacts page. Flask also manages templates rendering using Jinja templates, allowing dynamic content to be inserted into HTML pages. 
Docker containerization:
Docker is used to containerize the application. This ensures that the application runs consistently across different development environments by packaging the application code, dependencies and runtime configuration into a single image. 
GitHub repository:
The repository stores the application code, configuration files and documentation. We collaborate through pull requests, issue tracking and commit history.

Branching Model: 
The main branch (master) contains the stable version of the application. All new work is developed in separate feature branches that are created from the master.
We have used some feature branches during the development and these include: feature/dockerfile, feature/requirements, feature/ui-improvements.
Each of us created a branch for their task and committed their changes locally. When the feature is complete, a pull request is open on GitHub to merge the branch into the master branch.

CI/CD pipeline:
Our project implements as CI pipeline using GitHub actions. The pipeline automatically runs when new code is pushed to the repository or when a pull request is created. The pipeline performs several automated steps such as:
-	When one of us pushes code to GitHub or open the pull request GitHub actions automatically triggers the CI workflow;
-	The workflow installs the required dependencies specified in the requirements.txt file, ensuring that the environment matches the application runtime configuration;
-	The docker file is used to build a container image containing the application and its dependencies, ensuring the application can run consistently in any environment that supports docker;
-	the build container image can then be used for deployment or testing environments.

Conclusion:
Our application about Cat Facts is simple but demonstrates an effective software architecture that integrates external APIs with a web interface, while incorporating DevOps development practices. The architecture emphasises collaborative development through Git branching strategies and automated validation through CI pipelines. By combining all these tools, our project provides an environment that supports efficient team collaboration.
