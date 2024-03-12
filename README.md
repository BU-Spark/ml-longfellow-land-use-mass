# TEMPLATE-base-repo

All Pull Requests must follow the Pull Request Template, with a title formatted like such `[Project Name]: <Descriptive Title>`

# DRAINS: Deed Restriction Artificial Intelligence Notification System
(descriptions of drains)

## Requirements
Install essential libraries:
```
pip -r install requirements.txt
```

## Set up OpenAI_API_KEY
In folder `modules`: 

1. Duplicate the file `env.template`

2. Add your `api key` and `organization id` to `OPENAI_API_KEY` and `OPENAI_ORG_ID`

3. Rename this file to `.env`

   
## Quick Start
In file `main.py`, change the folder path to your path(line 24).

Then in command line, run:
```
python main.py
```
