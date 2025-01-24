# Blockchain Elections

## Deployment Link
https://blockchain-1-44f6.onrender.com/

## Introduction
This is an open source module which allows for polling using surveys using Algorand
<img src="https://github.com/user-attachments/assets/6173708e-750f-47ff-94d9-15c0000130d3" alt="image" width="00"/>

## Functionalities
* Survey Creation
* Survey Deployment
* Survey Results

## To run the project
=> python app.py

## To install the dependencies,
=> pip install -r requirements.txt

## Objective
Create an Open Source module to help developers in integrating Pollings and Surveys (based on blockchain, Algorand in our case) on their projects

## Main Functions

/ CREATE SURVEY : Allows creation of surveys with
the desired questions and options
/ RESPONSE SUBMISSION : Allows submission of
responses, internally using Private Key (to
maintain uniqueness) and App ID
/ SURVEY RESULTS: Displays the current status of
the polling (may or may not be made visible to
all)

## Key Features

/ Trustable Pollings:
This can be integrated to individual projects and
allows for easy creation of polls. These polls
would carry a lot of trust factor, through the
private address.
/Why this?
Removes the need to create surveys from
scratch for your applications
/ Empowering Opinions:
With this we aim to revolutionalize the way pollings
are done, now it’s with full privacy and authenticity

## License :
[LICENSE](./LICENSE)

## Video Demo :
https://youtu.be/wzr7Rxd0yG0?si=WTLr5Pz27GiMaEFZ

## PLEASE NOTE:
Put your private key and other details in .env file

For the frontend demo:
Apart from app.py (containing the backend) and the static folder (containing the frontend html files), all other files are not required explicitly

Apart from the survey creation, deployement and interaction files, there are several files which were developed in the initial stages of development and are partly based on web2. They are completely nonfunctional, and just have been kept to know the development history.
