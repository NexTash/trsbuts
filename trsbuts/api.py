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
    if len(d) == 1:
        return d[0].get('KRN')
    if len(d) == 0:
        frappe.throw(
            title='Hata',
            msg='Vergi No ÜTS\'de kayıtlı değildir.'
        )
    if len(d) > 1:
        branches: list = list()
        for branch in d:
            if branch.get('DRM') == 'AKTIF':
                branchlist: list = list()
                branchlist.append(branch.get('KRN'))
                branchlist.append(branch.get('GAD'))
                branches.append(branchlist)
        frappe.msgprint(
            msg=branches,
            title='Aktif şubeler',
            as_table=True,
            as_list=False
        )
