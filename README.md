# Python Flask Starter

A simple boilerplate for a Python Flask Web App.

## Getting Started

Get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python installed on your system. You can download Python from [here](https://www.python.org/downloads/). Additionally, you will need to install the project's dependencies which are listed in the `requirements.txt` file. 

### Installing

Clone the repository to your local machine:

```bash
git clone https://github.com/username/project.git
```

Navigate to the project directory:

```bash
cd project
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### File Structure

The project has the following structure:

```
.
├── run.py
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── forms.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   │   └── main.css
│   │   └── js/
│   │       └── main.js
│   └── templates/
│       ├── base.html
│       └── index.html
├── config.py
└── requirements.txt
```

### Usage

To start the application, you can run the following command in the project root directory:

```bash
python run.py
```

This will start the application, and you can access it by navigating to `http://localhost:5000` in your browser.

## Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
