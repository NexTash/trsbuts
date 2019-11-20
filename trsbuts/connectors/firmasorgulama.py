import trsbuts.connectors.UTSConnection as UTSConnection


# FİRMA SORGULAMA SERVİSİ
# Firmaların MERSİS numarası, vergi numarası, ÇKYS numarası ve/ya firma unvanı ile firma tanımlayıcı numarası
# içeren firma bilgilerini sorgulamasını sağlayan servistir.
def firmasorgula(mrs, vrg, unv, krn, cky):
    servicepath = "/UTS/rest/kurum/firmaSorgula"
    servicedata = "{"
    if mrs != "":
        servicedata = servicedata + "\"MRS\":\"" + mrs + "\","
    if vrg != "":
        servicedata = servicedata + "\"VRG\":\"" + vrg + "\""
    if unv != "":
        servicedata = servicedata + "\"UNV\":\"" + unv + "\","
    if krn != "":
        servicedata = servicedata + "\"KRN\":" + krn + ","
    if cky != "":
        servicedata = servicedata + "\"CKY\":\"" + cky + "\""

    servicedata = servicedata + "}"

    utsconnection = UTSConnection()

    return utsconnection.connect(servicepath, servicedata)
