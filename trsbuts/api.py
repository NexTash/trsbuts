import requests
from trsbuts.QueryCompanyService import QueryCompanyService

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
    headers = dict(utsToken=testtoken)
    headers['Content-Type'] = frappe.db.get_single_value("TR UTS Integration Settings", "contenttype")

    # servicedata = "{"
    # servicedata = servicedata + "\"VRG\":\"" + frappe.db.get_value("Company", company, "tax_id") + "\""
    # servicedata = servicedata + "}"
    servicedata = dict(VRG=frappe.db.get_value("Company", company, "tax_id"))

    _requesturl = url + servicepath

    s = requests.Session()
    s.headers.update(headers)
    # Web servislerin tamamında HTTP request method olarak “POST” metodu kullanılmaktadır.
    response = s.post(_requesturl, servicedata)

    return response.text


@frappe.whitelist()
def get_utsid_by_taxid(vrg):
    q = QueryCompanyService()
    d: list = q.firmasorgula(vrg=vrg)
    return d[0].get('KRN')
