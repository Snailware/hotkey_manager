# <center> Hotkey Manager </center>
<center> an easy to use hotkey generator written in python </center>

## Quick Start Guide
1. using git, clone this repo to your machine by running this command in your terminal:
```sh
git clone https://github.com/Snailware/hotkey_manager.git
```

2. create a virtual environment to be used by running this command in your terminal:
```sh
python -m venv .env
```

3. navigate to the `hotkey_manager` directory and activate the virtual environment by running this command in your terminal:
```sh
cd hotkey_manager
source .env/bin/activate
```

4. download and install the required modules by running this command in your terminal:
```sh
pip install -r requirements.txt
```

5. edit the `hotkeys.json` file to contain your desired hotkeys. the file provided currently only has basic media controls, but it should be enough to explain what goes where.

6. now run the `main.py` script (or automate its execution if desired). **you may need to modify this scripts permissions to allow execution.**

## Resources
* a list of valid keys can be found [here](https://github.com/boppreh/keyboard/blob/master/keyboard/_canonical_names.py).