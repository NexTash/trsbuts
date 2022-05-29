from trsbuts.UTSConnection import UTSConnection


class InquiringService:
    # SORGULAMA SERVİSLERİ
    def __init__(self):
        self._servicepath = "/UTS/uh/rest"

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

    # Üretici/İthalatçı Sistemin Dışına Çıkmış Tekil Ürün Sorgula
    # Kurum/firma sistem dışına çıkan tekil ürünleri ve bu tekil ürünlere yapılan bildirimleri sorgular.
    def tekilurunsistemdisinacikansorgula(self, uno: str, lno="", sno="", san=1):
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
        if san > 0:
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"SAN\":" + str(san)
            parametercheck = True

        if parametercheck:
            c: UTSConnection = UTSConnection()
            return c.connect(
                self._servicepath + "/bildirim/ureticiIthalatci/tekilUrun/sistemDisinaCikan/sorgula",
                servicedata + "}"
            )
        else:
            return ""

    # Askıdaki Tekil Ürün Sorgula
    # Kurum/firmanın verme bildirimi yapıp, karşı kurum/firmanın alma bildirimi yapmadığı tekil ürünleri sorgular.
    def vermebildirimaskidakilersorgula(self, uno: str, kun="", lno="", sno="", san=1):
        parametercheck = False
        servicedata = "{"
        if str(kun) != "":
            servicedata = servicedata + "\"KUN\":" + str(kun)
            parametercheck = True
        if uno != "":
            if parametercheck:
                servicedata = servicedata + ","
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
        if san != 1:
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"SAN\":" + str(san)
            parametercheck = True

        if parametercheck:
            c: UTSConnection = UTSConnection()
            return c.connect(
                self._servicepath + "/bildirim/verme/askidakiler",
                servicedata + "}"
            )
        else:
            return ""

    # Kabul Edilecek Tekil Ürün Sorgula
    # Kurum/firma kendisine yapılan verme bildirimlerini sorgular/alma yapabileceği bildirimleri listeler.
    def bildirimalmabekleyenlersorgula(self, gkk="", bno="", uno="", bid="", san=0):
        parametercheck = False
        servicedata = "{"
        if str(gkk) != "":
            servicedata = servicedata + "\"GKK\":" + str(gkk)
            parametercheck = True
        if bno != "":
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"BNO\":\"" + bno + "\""
            parametercheck = True
        if uno != "":
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"UNO\":\"" + uno + "\""
            parametercheck = True
        if bid != "":
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"BID\":\"" + bid + "\""
            parametercheck = True
        if san != 0:
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"SAN\":" + str(san)
            parametercheck = True

        c: UTSConnection = UTSConnection()
        return c.connect(
            self._servicepath + "/bildirim/alma/bekleyenler/sorgula",
            servicedata + "}"
        )

    # Alınmak İstenmeyen Verme Bildirimlerimi Sorgula
    # Bir kuruma gelen verme bildirimleri, alma yapması beklenen
    # firma tarafından kabul edilmeyecekse; bu bildirimin artık kuruma gelen verme bildirimleri arasında
    # görüntülenmemesi için firma tarafından Almak İstemiyorum olarak işaretlenir. Verme bildirimini yapan firma ise
    # ilgili bildirimindeki tekil ürününün alınmak istenmiyor olarak işaretlenip işaretlenmediğini sorgulayabilir.
    def alinmakistenmeyenvermebildirimlerimsorgula(self, adt=0, off=""):
        parametercheck = False
        servicedata = "{"
        if adt != 0:
            servicedata = servicedata + "\"ADT\":" + str(adt)
            parametercheck = True
        if off != "":
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"OFF\":\"" + off + "\""

        c: UTSConnection = UTSConnection()
        return c.connect(
            self._servicepath + "/almakIstemiyorum/sorgula/alinmakIstenmeyenVermeBildirimlerim",
            servicedata + "}"
        )

    # Almak İstemediğim Verme Bildirimlerini Sorgula
    # Firma almak istemiyorum olarak işaretlediği verme bildirimlerini sorgular. Dilerse Almak İstiyorum Olarak İşaretle
    # servisini kullanarak bildirimi bu listeden çıkarabilir.
    def almakistemedigimvermebildirimlerisorgula(self, adt=0, off=""):
        parametercheck = False
        servicedata = "{"
        if adt != 0:
            servicedata = servicedata + "\"ADT\":" + str(adt)
            parametercheck = True
        if off != "":
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"OFF\":\"" + off + "\""

        c: UTSConnection = UTSConnection()
        return c.connect(
            self._servicepath + "/almakIstemiyorum/sorgula/almakIstemedigimVermeBildirimlerim",
            servicedata + "}"
        )

    # Bildirim Sorgula
    # Kurum/firmanın yapmış olduğu bildirimleri sorgular.
    def bildirimsorgula(self, uno="", lno="", sno="", san=1):
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
        if san != 1:
            if parametercheck:
                servicedata = servicedata + ","
            servicedata = servicedata + "\"SAN\":" + str(san)
            parametercheck = True

        if parametercheck:
            c: UTSConnection = UTSConnection()
            return c.connect(
                self._servicepath + "/bildirim/sorgula",
                servicedata + "}"
            )
        else:
            return ""
