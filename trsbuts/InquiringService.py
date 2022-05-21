from trsbuts.UTSConnection import UTSConnection


class InquiringService:
    def __init__(self):
        self._servicepath = "/UTS/uh/rest"

    # SORGULAMA SERVİSLERİ
    # Tekil Ürün Sorgula
    # Kurum/firma üzerindeki tekil ürünleri sorgular.
    def tekilurunsorgula(self, uno: str, lno="", sno=""):
        parametercheck = False
        servicedata = "{"
        if uno != "":
            servicedata = servicedata + "\"UNO\":\"" + uno + "\""
            parametercheck = True
        if lno != "":
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"LNO\":\"" + lno + "\""
            parametercheck = True
        if sno != "":
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"SNO\":\"" + sno + "\","
            parametercheck = True

        if parametercheck:
            c: UTSConnection = UTSConnection()
            return c.connect(
                self._servicepath + "/tekilUrun/sorgula",
                servicedata + "}"
            )
        else:
            return ""
