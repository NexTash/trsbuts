import json

import requests

import frappe


class UTSConnection:
    def __init__(self):
        self._s = requests.Session()

    def connect(self, servicepath: str, servicedata: str):
        company = frappe.defaults.get_user_default("Company")
        if frappe.db.get_value("TR UTS Company Settings", company, "usetest") == 0:
            url = frappe.db.get_single_value("TR UTS Integration Settings", "server")
            utstoken = ("TR UTS Company Settings", company, "systemtoken")
        else:
            url = frappe.db.get_single_value("TR UTS Integration Settings", "testserver")
            utstoken = ("TR UTS Company Settings", company, "testsystemtoken")

        url = url + servicepath
        # her web servis çağrısının başlık (header) kısmına utsToken etiketiyle sistem token’ının değerini eklemelidir
        headers = {
            'utsToken': utstoken,
            'Content-Type': frappe.db.get_single_value("TR UTS Integration Settings", "contenttype")
        }

        self._s.headers.update(headers)
        # Web servislerin tamamında HTTP request method olarak “POST” metodu kullanılmaktadır.
        response = self._s.post(url, servicedata)

        # For successful API call, response code will be 200 (OK)
        if response.ok:
            # Loading the response data into a dict variable
            # json.loads takes in only binary or string variables so using content to fetch binary content
            # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
            return json.loads(response.content)
        else:
            # If response code is not ok (200), print the resulting http error code with description
            return response.raise_for_status()
