import json

import requests

import frappe


class UTSConnection:
    _s = requests.Session()
    _integration_settings_doctype = "TR UTS Integration Settings"
    _company_settings_doctype = "TR UTS Company Settings"

    def connect(self, servicepath, servicedata):
        company = frappe.defaults.get_user_default("Company")
        server_url = frappe.db.get_single_value(self._integration_settings_doctype, "server")
        utstoken = frappe.db.get_value(self._company_settings_doctype, company, "systemtoken")
        if frappe.db.get_value(self._company_settings_doctype, company, "usetest") == 1:
            server_url = frappe.db.get_single_value(self._integration_settings_doctype, "testserver")
            utstoken = frappe.db.get_value(self._company_settings_doctype, company, "testsystemtoken")
        service_url = server_url + servicepath
        # her web servis çağrısının başlık (header) kısmına utsToken etiketiyle sistem token’ının değerini eklemelidir
        headers = dict(utsToken=utstoken)
        headers['Content-Type'] = frappe.db.get_single_value(self._integration_settings_doctype, "contenttype")

        self._s = requests.Session()
        self._s.headers.update(headers)
        # Web servislerin tamamında HTTP request method olarak “POST” metodu kullanılmaktadır.
        response = self._s.post(service_url, servicedata)

        # For successful API call, response code will be 200 (OK)
        if response.ok:
            # Loading the response data into a dict variable json.loads takes in only binary or string variables so
            # using content to fetch binary content Loads (Load String) takes a Json file and converts into python
            # data structure (dict or list, depending on JSON)
            return json.loads(response.content)
        else:
            # If response code is not ok (200), print the resulting http error code with description
            return response.raise_for_status()
