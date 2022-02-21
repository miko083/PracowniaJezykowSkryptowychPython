docker exec -it -w /app $(docker ps -a | grep "Up" | grep "rasa run actions" | awk '{print $1}') rasa run --enable-api --credentials credentials.yml --cors "*"
