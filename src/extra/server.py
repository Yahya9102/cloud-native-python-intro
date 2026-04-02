from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from src.service.user_service import add_user, list_users, user_exists, delete_user, update_user


class UserRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/users":
            users = list_users()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response_body = json.dumps(users)
            self.wfile.write(response_body.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode("utf-8"))



    def do_POST(self):
        if self.path =="/users":
           content_length = int(self.headers.get("Content-Length", 0))
           body = self.rfile.read(content_length)
           data =  json.loads(body.decode("utf-8"))

           name = data.get("name", "")
           success = add_user(name)

           if success:
               self.send_response(201)
               self.send_header("Content-type", "application/json")
               self.end_headers()
               self.wfile.write(json.dumps({"message": "User created"}).encode("utf-8"))
           else:
               self.send_response(400)
               self.send_header("Content-type", "application/json")
               self.end_headers()
               self.wfile.write(json.dumps({"error": "invalid or duplicate user"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode("utf-8"))


    def do_PUT(self):
        if self.path == "/users":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            data =  json.loads(body.decode("utf-8"))

            old_name = data.get("old_name", "")
            new_name = data.get("new_name", "")

            success, message = update_user(old_name, new_name)

            if success:
               self.send_response(200)
               self.send_header("Content-type", "application/json")
               self.end_headers()
               self.wfile.write(json.dumps({"message": "User Updated"}).encode("utf-8"))
            else:
               self.send_response(400)
               self.send_header("Content-type", "application/json")
               self.end_headers()
               self.wfile.write(json.dumps({"error": message}).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode("utf-8"))



    def do_DELETE(self):
        if self.path =="/users":
           content_length = int(self.headers.get("Content-Length", 0))
           body = self.rfile.read(content_length)
           data =  json.loads(body.decode("utf-8"))

           name = data.get("name", "")
           success = delete_user(name)

           if success:
               self.send_response(200)
               self.send_header("Content-type", "application/json")
               self.end_headers()
               self.wfile.write(json.dumps({"message": "User Deleted"}).encode("utf-8"))
           else:
               self.send_response(404)
               self.send_header("Content-type", "application/json")
               self.end_headers()
               self.wfile.write(json.dumps({"error": "User not found"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode("utf-8"))


def run_server():
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, UserRequestHandler)
    print("Server running on http://localhost:8080")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()

