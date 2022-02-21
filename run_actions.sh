docker run -ti --user 1000 -v $(pwd):/app/ -w /app/actions -p 5005:5005 -l my_rasa=testing rasa/rasa:2.8.25-full run actions
