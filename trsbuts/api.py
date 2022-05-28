import requests
from trsbuts.ActionNotificationService import ActionNotificationService
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
def create_importnotification_via_purchasereceipt(name):
    main_doctype = "Purchase Receipt"
    purchasereceipt = frappe.get_doc(main_doctype, name)
    for item in frappe.get_all(
            purchasereceipt.get_table_field_doctype("items"),
            filters={
                'parent': name,
                'parentfield': 'items',
                'parenttype': main_doctype
            }):
        if item.barcode is not None:
            product_number = item.barcode
        else:
            product_number = get_barcode_of_item(item.item_code)
        if get_urun_by_uno(product_number):
            imported_country = frappe.get_doc("TR UTS Country Reference Code",
                                              purchasereceipt.supplier_address.get("country")
                                              ).get("EDI XML Reference Code")
            origin_country = frappe.get_doc("TR UTS Country Reference Code",
                                            item.country_of_origin
                                            ).get("EDI XML Reference Code")
            ans = ActionNotificationService()
            if item.serial_no is not None or item.serial_no != "":
                item_serial = frappe.get_doc("Serial No", item.serial_no)
                batch = frappe.get_doc("Batch", item_serial.batch_no)
                d: dict = ans.ithalat_ekle(
                    uno=product_number,
                    lno=str.strip(batch.get("vendor_batch")),
                    sno=item_serial.serial_no,
                    urt=batch.get("manufacturing_date"),
                    skt=batch.get("expiry_date"),
                    itt=purchasereceipt.posting_date,
                    udi="",
                    ieu=imported_country,
                    meu=origin_country,
                    gbn=purchasereceipt.supplier_delivery_note,
                    sip="",
                    kus="",
                    gtk="")

            else:
                batch = frappe.get_doc("Batch", item.batch_no)
                d: dict = ans.ithalat_ekle(
                    uno=product_number,
                    lno=str.strip(batch.get("vendor_batch")),
                    urt=batch.get("manufacturing_date"),
                    skt=batch.get("expiry_date"),
                    itt=purchasereceipt.posting_date,
                    adt=item.received_qty,
                    udi="",
                    ieu=imported_country,
                    meu=origin_country,
                    gbn=purchasereceipt.supplier_delivery_note,
                    sip="",
                    kus="",
                    gtk="")
    return ""


@frappe.whitelist()
def get_utsid_by_taxid(vrg):
    object_name = "Vergi No"
    q = QueryCompanyService()
    firma: list = q.firmasorgula(vrg=vrg)
    if len(firma) == 1:
        return firma[0].get('KRN')
    if len(firma) == 0:
        frappe.throw(
            title='Hata',
            msg=object_name + ' ÜTS\'de kayıtlı değildir.'
        )
    if len(firma) > 1:
        branches: list = list()
        for branch in firma:
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
def get_urun_by_uno(urun_numarasi):
    q = SearchProductDefinitionService()
    urun: dict = q.urunsorgula(uno=urun_numarasi)
    if urun.get("sonuc") == 1:
        return False
    return True


@frappe.whitelist()
def get_tekilurun_by_batch(batch, vendor_batch):
    object_name = "Tekil Ürün"
    b = frappe.get_doc("Batch", batch)
    q = InquiringService()
    if b.vendor_batch == "":
        b.vendor_batch = vendor_batch
    d: dict = q.tekilurunsorgula(uno=get_barcode_of_item(b.item), lno=str.strip(b.vendor_batch))
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
    for child in frappe.get_all(
            b.get_table_field_doctype("individual_product"),
            filters={
                'parent': b.name,
                'parentfield': 'individual_product',
                'parenttype': 'Batch'
            }):
        frappe.delete_doc(
            b.get_table_field_doctype("individual_product"),
            child.name,
            delete_permanently=True)
    b.save()
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
    q = InquiringService()
    if b.vendor_batch == "":
        b.vendor_batch = vendor_batch
    d: dict = q.tekilurunsistemdisinacikansorgula(uno=get_barcode_of_item(b.item), lno=str.strip(b.vendor_batch))
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
    for child in frappe.get_all(
            b.get_table_field_doctype("individual_product_out_of_the_system"),
            filters={
                'parent': b.name,
                'parentfield': 'individual_product_out_of_the_system',
                'parenttype': 'Batch'
            }):
        frappe.delete_doc(
            b.get_table_field_doctype("individual_product_out_of_the_system"),
            child.name,
            delete_permanently=True)
    b.save()
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
    q = InquiringService()
    if b.vendor_batch == "":
        b.vendor_batch = vendor_batch
    d: dict = q.vermebildirimaskidakilersorgula(uno=get_barcode_of_item(b.item), lno=str.strip(b.vendor_batch))
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
    for child in frappe.get_all(
            b.get_table_field_doctype("pending_individual_product"),
            filters={
                'parent': b.name,
                'parentfield': 'pending_individual_product',
                'parenttype': 'Batch'
            }):
        frappe.delete_doc(
            b.get_table_field_doctype("pending_individual_product"),
            child.name,
            delete_permanently=True)
    b.save()
    lowerdict: dict = dict()
    for individual in individuals:
        for key in individual.keys():
            lowerdict[key.lower()] = individual.get(key)

        b.append("pending_individual_product", lowerdict)
    b.save()
    return ""


@frappe.whitelist()
def get_bildirim_by_batch(batch, vendor_batch):
    object_name = "Bildirim"
    b = frappe.get_doc("Batch", batch)
    q = InquiringService()
    if b.vendor_batch == "":
        b.vendor_batch = vendor_batch
    d: dict = q.bildirimsorgula(uno=get_barcode_of_item(b.item), lno=str.strip(b.vendor_batch))
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
    for child in frappe.get_all(
            b.get_table_field_doctype("notification"),
            filters={
                'parent': b.name,
                'parentfield': 'notification',
                'parenttype': 'Batch'
            }):
        frappe.delete_doc(
            b.get_table_field_doctype("notification"),
            child.name,
            delete_permanently=True)
    b.save()
    lowerdict: dict = dict()
    for individual in individuals:
        for key in individual.keys():
            lowerdict[key.lower()] = individual.get(key)

        b.append("notification", lowerdict)
    b.save()
    return ""


@frappe.whitelist()
def get_all_declinedoutgoingdeliverynotifications():
    object_name = "Alınmak İstenmeyen Verme Bildirimlerim"
    q = InquiringService()
    d: dict = q.alinmakistenmeyenvermebildirimlerimsorgula()

    notifications = d.get("SNC").get("LST")
    if len(notifications) == 0:
        frappe.throw(
            title='Hata',
            msg=object_name + ' ÜTS\'de kayıtlı değildir.'
        )
    _doctype = "TR UTS Declined Outgoing Delivery Notification"
    refill_doctype_table(_doctype, notifications)
    return ""


@frappe.whitelist()
def get_all_incomingnotificationsdeclined():
    object_name = "Almak İstemediğim Verme Bildirimleri"
    q = InquiringService()
    d: dict = q.almakistemedigimvermebildirimlerisorgula()

    notifications = d.get("SNC").get("LST")
    if len(notifications) == 0:
        frappe.throw(
            title='Hata',
            msg=object_name + ' ÜTS\'de kayıtlı değildir.'
        )
    _doctype = "TR UTS Incoming Notifications Declined"
    refill_doctype_table(_doctype, notifications)
    return ""


def refill_doctype_table(doctype: str, entries: dict):
    for n in frappe.get_list(doctype):
        frappe.delete_doc_if_exists(doctype=doctype, name=n.get('name'))
    for entry in entries:
        lowerdict: dict = dict(doctype=doctype)
        for key in entry.keys():
            lowerdict[key.lower()] = entry.get(key)
        # create a new document
        doc = frappe.get_doc(lowerdict)
        doc.insert()


def get_barcode_of_item(name):
    i = frappe.get_doc("Item", name)
    l: list = frappe.get_all(
        i.get_table_field_doctype("barcodes"),
        filters={
            'parent': name,
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
    else:
        return l[0].get('barcode')
