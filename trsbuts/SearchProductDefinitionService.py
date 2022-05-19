import trsbuts.connectors.UTSConnection as UTSConnection


class SearchProductDefinitionService:
    def __index__(self):
        self._servicepath = "/UTS/rest/tibbiCihaz"

    # ÜRÜN SORGULAMA SERVİSİ
    # Birincil ürün numarası ve üretici ÜTS firma numarası ile ürün bilgilerini sorgulamasını sağlayan servistir.
    def urunsorgula(self, uno: str):
        servicedata = "{"
        if uno != "":
            servicedata = servicedata + "\"UNO\":\"" + uno + "\""
            c: UTSConnection = UTSConnection()
            return c.connect(
                self._servicepath + "/urunSorgula",
                servicedata + "}"
            )
        else:
            return ""

    # BÜTÜN ÜRÜNLERİ SORGULAMA SERVİSİ
    # Firmaların kendi ürünlerini çoklu olarak sorgulamalarını sağlayan servistir.
    def butunurunlerisorgula(self, sayfaBuyuklugu, sayfaIndeksi, baslangicTarihi, bitisTarihi):
        servicepath = self._servicepath + "/tibbiCihazSorgula"
        servicedata = "{"
        servicedata = servicedata + "\"sayfaBuyuklugu\":" + sayfaBuyuklugu
        servicedata = servicedata + ",\"sayfaIndeksi\":" + sayfaIndeksi
        servicedata = servicedata + ",\"baslangicTarihi\":\"" + baslangicTarihi + "\""
        servicedata = servicedata + ",\"bitisTarihi\":\"" + bitisTarihi + "\""
        servicedata = servicedata + "}"
