# build the project
# pip install -r requirements.txt
echo "build the project"
pip -m pip install -r requirements.txt

# Make migration
echo "Make migration"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# Collect static
echo "Collect static"
python3.9 manage.py collectstatic --noinput --clear