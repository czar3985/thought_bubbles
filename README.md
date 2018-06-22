# Thought Bubbles

A simple journal website server that serves up the Thought Bubbles site. 

The browser sends GET requests to the server that responds with the web page containing
a form for inputting thoughts and all previous inputs sorted from the most recent entry.

Upon receiving the POST request for a new input, the server fixes the current date and
time that corresponds to the entry before saving it to memory. The client is then
redirected to the upgraded page.

![Thought Bubbles website](./screenshot.jpg?raw=true "Title")

## Prerequisites

1. Install **python 3.6.3**.
2. Clone the github repository [thought_bubbles](https://github.com/czar3985/thought_bubbles).
```
$ git clone https://github.com/czar3985/thought_bubbles
```
3. The necessary files needed to the run the program are:
```
base_page.html
main.css
thoughts_server.py_
```

## Usage

**Server side:**
Run the python script _thoughts_server.py_. The following resource 
gives more information on how to run python scripts: 
[How to Run a Python Script via a File or the Shell](https://www.pythoncentral.io/execute-python-script-file-shell/).

**Client side:**
The website is currently hardcoded to run in http://localhost:8000/

No databases used. The data lasts only until the server is closed.

## License

Thought Bubbles is released under the [MIT License](https://opensource.org/licenses/MIT).