if [ $# -eq 0 ]
    then
        echo "Applying default argument - 8080"
        PORT=8080
else
    echo "Applying argument - " $1
    PORT=$1
fi
python manage.py runserver 0.0.0.0:$PORT
