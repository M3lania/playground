# Playground


&nbsp;
### Introduction
---
Playground is a suite of Selenium and RoboBrowser automated tests for [Geocode.xyz](https://geocode.xyz/).

&nbsp;
### Running the tests locally
---

* System requirements:
  * python 3
  * pip
  * Google Chrome
  * [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

* Clone this repo

* Create and activate a virtual environment:

       virtualenv ve-playground -p python3.6
       source ve-playground/bin/activate

* Install packages and project dependencies:

      pip install pip-tools
      cd playground
      pip-compile --output-file requirements.txt requirements.in
      pip install -r requirements.txt

* Run a certain test, on a certain browser (Chrome by default):

       pytest -v -s -k test_sign_up_with_valid_data --browser=firefox

* Run only the tests which are not marked as "regression"

        pytest -v -s -m "not regression"


&nbsp;
### Remarks
---

* Before you make the first commit, install [pre-commit](https://pre-commit.com/#install) by following their instructions.

        pre-commit install
        pre-commit run

* [Black](https://github.com/ambv/black) can be used to format the code:

        pip install black
        black . --py36 -S --diff
        black . --py36 -S

(from root project)



