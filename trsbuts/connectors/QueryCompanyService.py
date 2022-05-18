from trsbuts.connectors.UTSConnection import UTSConnection


class QueryCompanyService:
    _servicepath = "/UTS/rest/kurum"

    # FİRMA SORGULAMA SERVİSİ
    # Firmaların MERSİS numarası, vergi numarası, ÇKYS numarası ve/ya firma unvanı ile firma tanımlayıcı numarası
    # içeren firma bilgilerini sorgulamasını sağlayan servistir.
    def firmasorgula(self, mrs="", vrg="", unv="", krn="", cky=""):
        servicepath = self._servicepath + "/firmaSorgula"
        parametercheck = False
        servicedata = dict()
        if mrs != "":
            #     servicedata = servicedata + "\"MRS\":\"" + mrs + "\""
            servicedata['MRS'] = mrs
            parametercheck = True
        if vrg != "":
            #     servicedata = servicedata + ",\"VRG\":\"" + vrg + "\""
            servicedata['VRG'] = vrg
            parametercheck = True
        if unv != "":
            #     servicedata = servicedata + ",\"UNV\":\"" + unv + "\","
            servicedata['UNV'] = unv
            parametercheck = True
        if krn != "":
            #     servicedata = servicedata + ",\"KRN\":" + krn
            servicedata['KRN'] = krn
            parametercheck = True
        if cky != "":
            #     servicedata = servicedata + ",\"CKY\":\"" + cky + "\""
            servicedata['CKY'] = cky
            parametercheck = True
        #
        # servicedata = servicedata + "}"

        if parametercheck:
            return UTSConnection().connect(servicepath, servicedata)
        else:
            return ""
