echo "Do you want to make a new virtual environment? :y,n"

read dist

if [ $dist = y ]

    then

    echo "A new environment is now being made!"

    sudo apt-get install python-pip

    sudo pip install virtualenv

    virtualenv venv

    source venv/bin/activate

    echo "Note: console spam will take place when install wikiapi you should not get a error however if you do contact me at Github.com"

    pip install flask

    pip install simplejson

    pip install flask-restful

    pip install wikiapi

    pip install wordnik

    echo "The Disce API server setup has now completed and will now run"

    python server.py

elif [ $dist = n ]

    then

    echo "Place a env in the current directory. Note: rename your virtualenv venv"

    source venv/bin/activate

    echo "Note: console spam will take place when install wikiapi you should not get a error however if you do contact me at Github.com"

    pip install flask

    pip install simplejson

    pip install flask-restful

    pip install wikiapi

    pip install wordnik

    echo "The Disce API server setup has now completed and will now run"

    python server.py

fi