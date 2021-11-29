import requests
from .error import *
import re

class cb0t:
    def create(self, url:str):
        """
        This can create shorten url.
        """
        r = requests.post("https://cb0t.cc/api/create", data = {"url": url})
        if r.status_code == 400:
            raise Invalidurl("Invalid url specified.")
        elif r.status_code == 406:
            raise Invalidurl("Sorry but the specified domain is on our blacklist.")
        else:
            return r.json()["url"]
            
    def view(self, url:str):
        url = re.compile(r"https?://cb0t.cc/(\d+)")
        if re.match(url) is not None:
            code = re.match(url)[0]
            query = {
                "code": code
            }
            r = request.get("https://cb0t.cc/api/view", params = query)
            if r.status_code == 404:
                raise Invalidurl("I can't found that url")
            else:
                return r.json()["url"]
        else:
            raise Invaildurl("This url is not vaild")
