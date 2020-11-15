# Zebra-Zeal



## Setting up application
<br/>

**Note**: application can be run by using `build.sh` script

<br/>

### [FOR DEVELOPMENT] Running develoment Flask server

1. Start pip virtual environment
2. Export environment variables: `export $(cat .env)`
3. Run the dev flask server using bash script `./build -dev`

<br/>

### [FOR STAGING LOCAL] Running as docker container

1. Export environment variables: `export $(cat .env)`
2. Run staging environment `./build.sh -stag`
3. Images are automatically pulled and set up
4. Access application on `localhost/join`

<br/>

### [FOR PRODUCTION REMOTE] 

1. Just don't for now, bad things will happen ;)

