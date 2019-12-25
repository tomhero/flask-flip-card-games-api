# flask-flip-card-games-api
An API server which is use to sync high score with flip card games app 

## Quick Start

### Development

Uses the default Flask development server.

1. Rename __*.env.dev-sample*__ to __*.env.dev*__.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:5000](http://localhost:5000). The "api" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. Rename __*.env.prod-sample*__ to __*.env.prod*__. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:9000](http://localhost:9000). No mounted folders. To apply changes, the image must be re-built.
