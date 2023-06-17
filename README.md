# Arch Gate
At the core, it's a flask application along with dockerization and CI/CD enabled through Git Actions.
It allows users to register using unername and password. Registered users can login to create, update or delete their posts.

**Hosting on _http://krprince.pythonanywhere.com/_ for limited period.**

## Running Docker Image
Make sure docker is installed. Install it if not already done.

### Guide for Linux (Ubuntu like systems)
- Check if docker is installed:  
`docker version`  
This should show Client and Server Details if docker is installed.
- Install docker, if not installed, using the following command:  
`sudo apt install docker.io`  
- Confirm it once installation finishes:  
`docker version`  
- Pull docker image from Docker Hub registry:  
`docker pull livedockyard/arch-gate:latest`  
- Run docker image:  
`docker run --rm -it livedockyard/arch-gate:latest`  

    This step would launch docker's terminal where the url of served application can be found. Open the url in a browser to use the application.

- To stop serving the application and remove the container close the terminal lauched in the previous step (Ctrl+C).

## Local Development Environment Setup
- Open terminal and go to the directory where you want to create 'arch-gate' directory and clone the repository.  
- Run  
`git clone https://github.com/krprince98/arch-gate.git`  
or  
`git clone git@github.com:krprince98/arch-gate.git`  
to clone the repository.
- Go to arch-gate directory  
`cd arch-gate`
- Create a virtual environment to isolate development from system environment  
`python3 -m venv .venv`
- Activate virtual environment  
`source .venv/bin/activate`
- Set env variable to tell flask where to find app 
`export FLASK_APP=src/archg`  
- Setup database  
`flask create-db`
- Run application  
`flask run`  

  This will start serving the application. Find the url from console and open it in browser to start uning the app.  

- To stop serving the app simply stop the process started in last step (Ctrl+C)  
- To deactivate the virtual environment:  
`deactivate`  
- Activate the virtual environment and run `flask run` from `arch-gate` directory to start the application again. Running `flask create-db` before the `flask run` step will erase previous database and setup a fresh one. Skip it to contunue on historical data.