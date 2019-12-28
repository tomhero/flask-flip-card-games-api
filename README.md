# flask-flip-card-games-api
An API server which is use to sync high score with flip card games app 

## Quick Start

### Database

I would recommend you to use mongo altas cluster to manage your database
1. [Create an Atlas Account.](https://docs.atlas.mongodb.com/tutorial/create-atlas-account/)
2. [Deploy a Free Tier Cluster.](https://docs.atlas.mongodb.com/tutorial/deploy-free-tier-cluster/)
3. [Whitelist Your Connection IP Address.](https://docs.atlas.mongodb.com/tutorial/whitelist-connection-ip-address/)
4. [Create a MongoDB User for Your Cluster.](https://docs.atlas.mongodb.com/tutorial/create-mongodb-user-for-cluster/)
5. [Connect to Your Cluster.](https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/#id2)

> From `Connect to Your Cluster section`, you will get a **database connection url**
### Next

> ### Allow firewall on your host server with https 443 first
> ### Before Start please don't forget to add your host server ip address to mongo altas cluster whitelist!!!
> ### Generate **API key** for flask server at https://www.uuidgenerator.net/

### Deployment 🏗

Uses gunicorn + nginx.

1. Rename __*.env.prod-sample*__ to __*.env.prod*__. Update the environment variables.

   `DATABASE_URL` : is a **database connection url** from mongo db

   `DATABASE_NAME` : you can specifig your database name here

   `API_KEY` : please place your **generated API key** here and remenber this will also use in frontend

2. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```
    NOTE : No mounted folders. To apply changes, the image must be re-built.

### Development 👨‍💻

Uses the default Flask development server.

1. Rename __*.env.dev-sample*__ to __*.env.dev*__.
2. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
3. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:5000](http://localhost:5000). The "api" folder is mounted into the container and your code changes apply automatically.

### Clear Data

You can also clear score in database.
* After you have been spin docker container up:

    ```sh
    $ docker-compose -f docker-compose.prod.yml exec api python manage.py clear_data

    # if development mode
    $ docker-compose exec api python manage.py clear_data
    ```