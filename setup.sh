wget https://github.com/designmodo/Flat-UI/archive/master.zip

unzip master.zip

rm -r master.zip

mv  Flat-UI-master flatstrap

sudo mv flatstrap/ static/

rm -r flatstrap

sudo apt-get install python-pip

sudo pip install virtualenv

echo "Do you want to make a new virtual environment? :y,n"

read dist

if [ $dist = y ]

    then

    echo "A new environment is now being made!"

    virtualenv venv

    virtualenv venv

    source venv/bin/activate

    pip install flask

    pip install simplejson

    echo "The Disce frontend etup has now completed and will now run"

    python main.py

elif [ $dist = n ]

    then

    echo "Place a env in the current directory. Note: rename your virtualenv venv"

    source venv/bin/activate

    pip install flask

    pip install simplejson

    echo "The Disce frontend etup has now completed and will now run"

    python main.py

fi
