# Steps

pip install virtualenv

virtualenv venv --python=python3.10

source venv/bin/activate

pip freeze > requirements.txt

pip install -r requirements.txt

python3 -m pip install <package>

python3 -m unittest discover -s src/tests -p "*_test.py" -v
