#!/bin/bash

if [[ $# -eq 0 ]] ; then
    echo 'please define a build format (-dev | -prod)'
    exit 0
fi

while [ ! $# -eq 0 ]
do 
    case "$1" in
        --help | -h)
            helpmenu
            exit
            ;;

        --development | -dev)

            export BUILD='dev'

            echo "-------------------------"
            echo "Building '$BUILD' environment."
            echo "-------------------------"
            echo "Starting Flask application on port $APP_PORT..."

            flask run --port=$APP_PORT

            exit
            ;;
        
        --staging | -stag)

            export BUILD='stag'

            echo "-------------------------"
            echo "Building '$BUILD' environment."
            echo "-------------------------"
            echo "Shutting down current containers..."

            # shutdown and remove all containers
            docker stop $(docker ps -aq) && docker rm $(docker ps -aq)           

            echo "Successful shut down of current and running containers!"
            echo "-------------------------"
            echo "Reading 'docker-compose.yml' file in detached mode (-d)."
            
            docker-compose up --build -d

            echo "Succesfully built $BUILD environment!"
            echo "Running STAGING environment..."

            exit
            ;;

        
        --production | -prod)
            
            export BUILD='prod'

            echo "-------------------------"
            echo "Building '$BUILD' environment."
            echo "-------------------------"
            echo "Shutting down current containers..."

            # shutdown and remove all containers
            docker stop $(docker ps -aq) && docker rm $(docker ps -aq)     

            echo "Successful shut down of current and running containers!"
            echo "-------------------------"
            echo -e "Reading 'docker-compose.prod.yml' file in detached mode (-d)."

            docker-compose -f docker-compose.prod.yml up --build -d

            echo "Succesfully built $BUILD environment!"
            echo "Running PRODUCTION environment..."

            exit
            ;;

    esac
    shift
done




