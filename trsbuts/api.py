import requests
from trsbuts.InquiringService import InquiringService
from trsbuts.QueryCompanyService import QueryCompanyService
from trsbuts.SearchProductDefinitionService import SearchProductDefinitionService

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
    object_name = "Vergi No"
    q = QueryCompanyService()
    d: list = q.firmasorgula(vrg=vrg)
    if len(d) == 1:
        return d[0].get('KRN')
    if len(d) == 0:
        frappe.throw(
            title='Hata',
            msg=object_name + ' ÜTS\'de kayıtlı değildir.'
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


@frappe.whitelist()
def get_urun_by_uno(uno):
    object_name = "Parti"
    q = SearchProductDefinitionService()
    d: list = q.urunsorgula(uno=uno)
    if len(d) == 1:
        return d[0].get('KRN')
    if len(d) == 0:
        frappe.throw(
            title='Hata',
            msg=object_name + ' ÜTS\'de kayıtlı değildir.'
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


@frappe.whitelist()
def get_tekilurun_by_batch(batch, vendor_batch):
    object_name = "Tekil Ürün"
    b = frappe.get_doc("Batch", batch)
    i = frappe.get_doc("Item", b.item)
    l: list = frappe.get_all(
        i.get_table_field_doctype("barcodes"),
        filters={
            'parent': b.item,
            'parentfield': 'barcodes',
            'parenttype': 'Item',
            'barcode_type': 'EAN'
        },
        fields={
            "barcode"
        })
    if len(l) == 0:
        frappe.throw(
            title='Hata',
            msg='Sisteminizde Birincil Ürün Numarası kayıtlı değildir.'
        )
    q = InquiringService()
    if b.vendor_batch == "":
        b.vendor_batch = vendor_batch
    d: dict = q.tekilurunsorgula(uno=l[0].get('barcode'), lno=str.strip(b.vendor_batch))
    individual: dict = dict()
    try:
        individual = d.get("SNC")[0]
    except IndexError:
        frappe.throw(
            title='Hata',
            msg=object_name + ' ÜTS\'de kayıtlı değildir.'
        )
    if len(individual) == 0:
        return ""
    for children in frappe.get_all(
            b.get_table_field_doctype("individual_product"),
            filters={
                'parent': b.name,
                'parentfield': 'individual_product',
                'parenttype': 'Batch'
            }):
        frappe.delete_doc(
            b.get_table_field_doctype("individual_product"),
            children.name,
            delete_permanently=True)
    lowerdict: dict = dict()
    for key in individual.keys():
        lowerdict[key.lower()] = individual.get(key)

    b.append("individual_product", lowerdict)
    b.save()
    return ""


@frappe.whitelist()
def get_sistemdisitekilurun_by_batch(batch, vendor_batch):
    object_name = "Sistem Dışına Çıkan Tekil Ürün"
    b = frappe.get_doc("Batch", batch)
    i = frappe.get_doc("Item", b.item)
    l: list = frappe.get_all(
        i.get_table_field_doctype("barcodes"),
        filters={
            'parent': b.item,
            'parentfield': 'barcodes',
            'parenttype': 'Item',
            'barcode_type': 'EAN'
        },
        fields={
            "barcode"
        })
    if len(l) == 0:
        frappe.throw(
            title='Hata',
            msg='Sisteminizde Birincil Ürün Numarası kayıtlı değildir.'
        )
    q = InquiringService()
    if b.vendor_batch == "":
        b.vendor_batch = vendor_batch
    d: dict = q.tekilurunsistemdisinacikansorgula(uno=l[0].get('barcode'), lno=str.strip(b.vendor_batch))
    individuals: dict = dict()
    try:
        individuals = d.get("SNC")
    except IndexError:
        frappe.throw(
            title='Hata',
            msg=object_name + ' ÜTS\'de kayıtlı değildir.'
        )
    if len(individuals) == 0:
        return ""
    for children in frappe.get_all(
            b.get_table_field_doctype("individual_product_out_of_the_system"),
            filters={
                'parent': b.name,
                'parentfield': 'individual_product_out_of_the_system',
                'parenttype': 'Batch'
            }):
        frappe.delete_doc(
            b.get_table_field_doctype("individual_product_out_of_the_system"),
            children.name,
            delete_permanently=True)
    lowerdict: dict = dict()
    for individual in individuals:
        for key in individual.keys():
            lowerdict[key.lower()] = individual.get(key)

        b.append("individual_product_out_of_the_system", lowerdict)
    b.save()
    return ""


@frappe.whitelist()
def get_askidakitekilurun_by_batch(batch, vendor_batch):
    object_name = "Askıdaki Tekil Ürün"
    b = frappe.get_doc("Batch", batch)
    i = frappe.get_doc("Item", b.item)
    l: list = frappe.get_all(
        i.get_table_field_doctype("barcodes"),
        filters={
            'parent': b.item,
            'parentfield': 'barcodes',
            'parenttype': 'Item',
            'barcode_type': 'EAN'
        },
        fields={
            "barcode"
        })
    if len(l) == 0:
        frappe.throw(
            title='Hata',
            msg='Sisteminizde Birincil Ürün Numarası kayıtlı değildir.'
        )
    q = InquiringService()
    if b.vendor_batch == "":
        b.vendor_batch = vendor_batch
    d: dict = q.vermebildirimaskidakilersorgula(uno=l[0].get('barcode'), lno=str.strip(b.vendor_batch))
    individuals: dict = dict()
    try:
        individuals = d.get("SNC")
    except IndexError:
        frappe.throw(
            title='Hata',
            msg=object_name + ' ÜTS\'de kayıtlı değildir.'
        )
    if len(individuals) == 0:
        return ""
    for children in frappe.get_all(
            b.get_table_field_doctype("pending_individual_product"),
            filters={
                'parent': b.name,
                'parentfield': 'pending_individual_product',
                'parenttype': 'Batch'
            }):
        frappe.delete_doc(
            b.get_table_field_doctype("pending_individual_product"),
            children.name,
            delete_permanently=True)
    lowerdict: dict = dict()
    for individual in individuals:
        for key in individual.keys():
            lowerdict[key.lower()] = individual.get(key)

        b.append("pending_individual_product", lowerdict)
    b.save()
    return ""
