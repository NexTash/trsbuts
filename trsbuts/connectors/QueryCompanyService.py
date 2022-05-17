class QueryCompanyService:
    def __index__(self):
        self._utsconnection = UTSConnection()
        self._servicepath = "/UTS/rest/kurum"

    # FİRMA SORGULAMA SERVİSİ
    # Firmaların MERSİS numarası, vergi numarası, ÇKYS numarası ve/ya firma unvanı ile firma tanımlayıcı numarası
    # içeren firma bilgilerini sorgulamasını sağlayan servistir.
    def firmasorgula(self, mrs, vrg, unv, krn, cky):
        servicepath = self._servicepath + "/firmaSorgula"
        parametercheck = False
        servicedata = "{"
        if mrs != "":
            servicedata = servicedata + "\"MRS\":\"" + mrs + "\""
            parametercheck = True
        if vrg != "":
            servicedata = servicedata + ",\"VRG\":\"" + vrg + "\""
            parametercheck = True
        if unv != "":
            servicedata = servicedata + ",\"UNV\":\"" + unv + "\","
            parametercheck = True
        if krn != "":
            servicedata = servicedata + ",\"KRN\":" + krn
            parametercheck = True
        if cky != "":
            servicedata = servicedata + ",\"CKY\":\"" + cky + "\""
            parametercheck = True

        servicedata = servicedata + "}"

        if parametercheck:
            return self._utsconnection.connect(servicepath, servicedata)
        else:
            return ""
