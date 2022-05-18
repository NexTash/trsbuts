import json

import requests
from connectors.QueryCompanyService import QueryCompanyService
import frappe


@frappe.whitelist()
def test_integration(test, testtoken):
    company = frappe.defaults.get_user_default("Company")
    servicepath = "/UTS/rest/kurum/firmaSorgula"
    # Replace with the correct URL
    url = ""
    if test == "real":
        url = frappe.db.get_single_value("TR UTS Integration Settings", "server")
    if test == "test":
        url = frappe.db.get_single_value("TR UTS Integration Settings", "testserver")

    # her web servis çağrısının başlık (header) kısmına utsToken etiketiyle sistem token’ının değerini eklemelidir
    __headers = dict(utsToken=testtoken)
    __headers['Content-Type'] = frappe.db.get_single_value("TR UTS Integration Settings", "contenttype")

    # servicedata = "{"
    # servicedata = servicedata + "\"VRG\":\"" + frappe.db.get_value("Company", company, "tax_id") + "\""
    # servicedata = servicedata + "}"
    servicedata = dict(VRG=frappe.db.get_value("Company", company, "tax_id"))

    _requesturl = url + servicepath

    s = requests.Session()
    s.headers.update(__headers)
    # Web servislerin tamamında HTTP request method olarak “POST” metodu kullanılmaktadır.
    response = s.post(_requesturl, servicedata)

    return response.text


@frappe.whitelist()
def get_utsid_by_taxid(vrg):
    d: dict = QueryCompanyService().firmasorgula(vrg=vrg)
    return d.get('KRN')


def connect(self, servicepath: str, servicedata: dict):
    company = frappe.defaults.get_user_default("Company")
    server_url: str = frappe.db.get_single_value("TR UTS Integration Settings", "server")
    utstoken: str = frappe.db.get_value("TR UTS Company Settings", company, "systemtoken")
    if frappe.db.get_value("TR UTS Company Settings", company, "usetest") == 0:
        server_url = frappe.db.get_single_value("TR UTS Integration Settings", "testserver")
        utstoken = frappe.db.get_value("TR UTS Company Settings", company, "testsystemtoken")
    service_url = server_url + servicepath
    # her web servis çağrısının başlık (header) kısmına utsToken etiketiyle sistem token’ının değerini eklemelidir
    __headers = dict(utsToken=utstoken)
    __headers['Content-Type'] = frappe.db.get_single_value("TR UTS Integration Settings", "contenttype")

    s = requests.Session()
    s.headers.update(__headers)
    # Web servislerin tamamında HTTP request method olarak “POST” metodu kullanılmaktadır.
    response = s.post(service_url, servicedata)

    # For successful API call, response code will be 200 (OK)
    if response.ok:
        # Loading the response data into a dict variable json.loads takes in only binary or string variables so
        # using content to fetch binary content Loads (Load String) takes a Json file and converts into python
        # data structure (dict or list, depending on JSON)
        return json.loads(response.content)
    else:
        # If response code is not ok (200), print the resulting http error code with description
        return response.raise_for_status()
