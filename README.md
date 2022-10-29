# photo-app-api
app api source code


## Contents
- `Dockerfile` contains list of instructions for docker to build our docker image. 
    - inherit the container structure from a lightweight docker image running python 3.7
    - set the environment variable, running python in unbuffered mode
    - copy requirements file to docker image and install dependencies from it
    - make a dir within the docker image to store our app src code
    - make it the default working directory, any application using this docker container will run from this location unless specified otherwise
    - copy src code from local machine to the docker image
    - create a user that will run processes from the app (without root access) over the image and switch to that user.

- `docker-compose.yml` contains the docker-compose configurations for the project. It is a tool that helps us to run the docker image easily from our project location, allowing easy management of the different services that make up our project. 
    - `version`:- version of the docker compose we are going to use.
    - `services`:- define services that make up our project.
    - `build: context`:- location for docker build file.
    - `ports`: mapping from host's port to container's port.
    - `volumes`: allows us to get updates that we make into our container in real time. 
            Maps volumes from local machine to container for syncing without container restart.
    - `command`: command that is used to run our application in our docker container.

    run: `docker-compose build`

- `.travis.yml` is the TravisCI config file, which tells travis what to do every time we push a change to the project.
    - spin up a python server
    - make sure the docker service is available
    - use pip to install docker-compose
    - finally run the scripts and if the build fails, send a notification.
