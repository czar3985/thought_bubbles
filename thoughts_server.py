#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import datetime

# Thoughts are stored as a list of tuples
# [(date1, thought1), (date2, thought2),...]
memory = []


class ThoughtHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # How long was the thought?
        length = int(self.headers.get('Content-length', 0))

        # Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()
        # Extract the "thought" field from the request data.
        thought = parse_qs(data)["thoughtInput"][0]

        # Escape HTML tags in the thought so users can't break world+dog.
        thought = thought.replace("<", "&lt;")

        # Get date and time
        current_date_time = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

        # Store it in memory.
        memory.append((current_date_time, thought))

        # 1.  Send a 303 redirect back to the root page.
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        # Handle css file getting
        if self.path == "/main.css":
            css_file = open("main.css")
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            self.wfile.write(css_file.read().encode())
            css_file.close()
            return

        elif self.path == "/favicon.ico":
            return

        # Load html file into a string
        html_file = open('base_page.html', encoding='utf-8-sig')
        form_string = html_file.read()
        html_file.close()

        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # 2. Put the response together out of the form and the stored thoughts.
        # Display thoughts inputted in reverse order
        previous_thoughts = ''
        for item in memory[::-1]:
            one_line = '''<p class="thought__date">{}</p>
                        <p class="thought__text">{}</p>
                        '''.format(item[0], item[1])
            previous_thoughts += one_line
        response = form_string.format(previous_thoughts)

        # 3. Send the response.
        self.wfile.write(response.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, ThoughtHandler)
    httpd.serve_forever()
