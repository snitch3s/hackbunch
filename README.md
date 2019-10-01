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


## Contributing Help
If you are really interested in contributing to the please follow the below steps and rules.
1. Fork the project :fork_and_knife: (Star :star: the repo before that :stuck_out_tongue:)
2. Clone it.
```
git clone https://github.com/<username>/instahack-flask/
```
3. Build the project according to the [Installation Steps](installation-steps).
4. Look for any issues clicking the issues tab. Go through it and assign take one. Make sure you get assigned or atleast say that you are gonna work on it.
5. Always create a new branch and work on the feature or bug. Check this if you are not that familiar with branching, [Git Branching](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).
6. If you are using any other module for implementing any new features, please install the modules in the virtual environment and update it in the `requirements.txt` by using the below command.
```
pip freeze > requirements.txt
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
