# community-hacktoberfest-tracker
A simple hacktoberfest tracker for your community. 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
You need to have `python3` with a virtual environment and Flask framework.

### Installation Steps
1. First of all you need to setup your virtual environment. (setup and activate)
```
pyvenv-3.6 chtenv
```
Install the python virtual environment setup using this command `sudo apt install python3.6-venv`
```
source chtenv/bin/activate
```
2. Install all the dependencies, python modules 
```
pip3 install -r requirements
```
3. Run the python app
```
python3 app.py
```
Now, the app should be running on the localhost, browse to to the link where your app is running. (most probably, http://127.0.0.1:5000/)

## Working with the scripts
1. You need to save the usernames in a textfile, which is stored in the scripts file.

> Make sure that the usernames are accurate, without any unwanted spaces anywhere.

2. Use the command for help about the parameters that can be inputted
```
python3 scripts/script.py -h
```
3. Running the script:
+ Get the stats on an individual user
```
python3 scripts/script.py -u <username>
```
+ Get the stats of the group from the text file
```
python3 scripts/script.py -t <textfile.txt>
```


## Contributing Help
If you are really interested in contributing to the please follow refer to the [CONTRIBUTING.md](CONTRIBUTING.md).

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
