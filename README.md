# community-hacktoberfest-tracker

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

A simple hacktoberfest tracker for your community. Generates a image with the github avatars of the community people as collage and puts the hacktoberfest stats on the image, you can customize by adding logos too.

![pic](./images/pic.jpg)

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

2. Use the command for help about the parameters that can be inputed.
```
python3 scripts/script.py -h
```
3. Running the script:
+ Get the stats on an individual user.
```
python3 scripts/script.py -u <username>
```
+ Get the stats of the group from the text file.
```
python3 scripts/script.py -t <textfile.txt>
```


## Contributing Help
If you are really interested in contributing to this repository please refer to the [CONTRIBUTING.md](CONTRIBUTING.md).

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
