import trsbuts.connectors.UTSConnection as UTSConnection


class ActionNotificationService:
    def __index__(self):
        self._utsconnection = UTSConnection()
        self._servicepath = self._servicepath + ""

    # Üretim Bildirimi
    # Üretici, ürettiği tekil ürünlerin her biri için bir Üretim Bildirimi yapar.
    def uretimbildir(self, UNO, LNO, SNO, URT, SKT, ADT, UDI, SIP, KUS, GTK):
        servicepath = self._servicepath + "/uretim/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"" \
                      + ",\"LNO\":\"" + LNO + "\"" \
                      + ",\"SNO\":\"" + SNO + "\"" \
                      + ",\"URT\":\"" + URT + "\"" \
                      + ",\"SKT\":\"" + SKT + "\"" \
                      + ",\"ADT\":" + ADT + "," \
                      + ",\"UDI\":\"" + UDI + "\"" \
                      + ",\"SIP\":\"" + SIP + "\"" \
                      + ",\"KUS\":\"" + KUS + "\"" \
                      + ",\"GTK\":\"" + GTK + "\"" \
                      + "}"

    # İthalat Bildirimi
    # İthalatçı, ithal ettiği tekil ürünler için İthalat Bildirimi yapar.
    def ithalatbildir(self, UNO, LNO, SNO, URT, SKT, ITT, ADT, UDI, IEU, MEU, GBN, SIP, KUS, GTK):
        servicepath = self._servicepath + "/ithalat/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"URT\":\"" + URT + "\"," \
                      + "\"SKT\":\"" + SKT + "\"," \
                      + "\"ITT\":\"" + ITT + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"IEU\":" + IEU + "," \
                      + "\"MEU\":" + MEU + "," \
                      + "\"GBN\":\"" + GBN + "\"," \
                      + "\"SIP\":\"" + SIP + "\"," \
                      + "\"KUS\":\"" + KUS + "\"," \
                      + "\"GTK\":\"" + GTK + "\"" \
                      + "}"

    # Yetkili Bayi İle İthalat Bildirimi
    # İthalatçı tarafından yetki verilen bayi ithalat bildirimi yapabilmektedir. Bunun için bayinin ithalat yapmak istediği
    # ürüne ait ithalatçı tarafından girilmiş olan yetkili distribütörlük belgesi olmalıdır.
    def yetkilibayiileithalatbildir(self, UIK, UNO, LNO, SNO, URT, SKT, ITT, ADT, UDI, IEU, MEU, GBN, SIP, KUS, GTK):
        servicepath = self._servicepath + "/ithalat/yetkiliBayiIle/ekle"
        servicedata = "{" \
                      + "\"UIK\":" + UIK + "," \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"URT\":\"" + URT + "\"," \
                      + "\"SKT\":\"" + SKT + "\"," \
                      + "\"ITT\":\"" + ITT + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"IEU\":" + IEU + "," \
                      + "\"MEU\":" + MEU + "," \
                      + "\"GBN\":\"" + GBN + "\"," \
                      + "\"SIP\":\"" + SIP + "\"," \
                      + "\"KUS\":\"" + KUS + "\"," \
                      + "\"GTK\":\"" + GTK + "\"" \
                      + "}"

    # Verme Bildirimi
    # Kurum/firma kullanıcısı sahip olduğu tekil ürünlerini başka bir kurum/firmaya verdiğinde Verme Bildirimi yapar.
    # Satış, hibe, iade vb. yöntemler için Verme Bildirimi yapılır.
    def vermebildir(self, UNO, LNO, SNO, ADT, KUN, BEN, BNO, GIT):
        servicepath = self._servicepath + "/verme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"KUN\":" + KUN + "," \
                      + "\"BEN\":\"" + BEN + "\"," \
                      + "\"BNO\":\"" + BNO + "\"," \
                      + "\"GIT\":\"" + GIT + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Verme Bildirimi
    def essizkimlikbilgisiilevermebildir(self, UDI, ADT, KUN, BNO):
        sservicepath = self._servicepath + "/verme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"KUN\":" + KUN + "," \
                      + "\"BNO\":\"" + BNO + "\"" \
                      + "}"

    # Alma Bildirimi
    # Kurum/firma kendisine verilen tekil ürünleri kabul etmek için Alma Bildirimi yapar. Bu bildirimle beraber tekil ürünün
    # sahipliği alıcı tarafa geçmiş olur.
    def almabildir(self, VBI, ADT, GKK, UDI, UNO, LNO, SNO):
        servicepath = self._servicepath + "/alma/ekle"
        servicedata = "{" \
                      + "\"VBI\":" + VBI + "," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"GKK\":" + GKK + "," \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Alma Bildirimi
    def essizkimlikbilgisiilealmabildir(self, UDI, ADT, GKK):
        servicepath = self._servicepath + "/alma/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"GKK\":" + GKK \
                      + "}"

    # ÜTS’de Tanımsız Yere Verme Bildirimi
    # Kurum/firma ÜTS'de tanımlı olmayan bir firmaya tekil ürün verdiğinde ÜTS’de Tanımsız Yere Verme Bildirimi yapar.
    def utsdetanimsizyerevermebildir(self, UNO, LNO, SNO, ADT, BEN, VKN, BNO):
        servicepath = self._servicepath + "/utsdeTanimsizYereVerme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"BEN\":\"" + BEN + "\"," \
                      + "\"VKN\":" + VKN + "," \
                      + "\"BNO\":\"" + BNO + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle ÜTS’de Tanımsız Yere Verme Bildirimi
    def essizkimlikbilgisiileutsdetanimsizyerevermebildir(self, UDI, ADT, BEN, VKN, MEN, TKN, MEK, ODK, BNO):
        servicepath = self._servicepath + "/utsdeTanimsizYereVerme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"BEN\":\"" + BEN + "\"," \
                      + "\"VKN\":" + VKN + "," \
                      + "\"MEN\":" + MEN + "," \
                      + "\"TKN\":" + TKN + "," \
                      + "\"MEK\":" + MEK + "," \
                      + "\"ODK\":" + ODK + "," \
                      + "\"BNO\":\"" + BNO + "\"" \
                      + "}"

    # ÜTS’de Tanımsız Yerden İade Alma Bildirimi
    # Kurum/firma ÜTS'de tanımlı olmayan bir firmaya verdiği tekil ürünlerini iade aldığında ÜTS’de Tanımsız Yerden
    # İade Alma Bildirimi yapar.
    def utsdetanimsizyerdeniadealmabildir(self, UTI, ADT, UDI, UNO, LNO, SNO):
        servicepath = self._servicepath + "/utsdeTanimsizYerdenIadeAlma/ekle"
        servicedata = "{" \
                      + "\"UTI\":" + UTI + "," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi ile ÜTS’de Tanımsız Yerden İade Alma Bildirimi
    def essizkimlikbilgisiileutsdetanimsizyerdeniadealmabildir(self, UDI, ADT):
        servicepath = self._servicepath + "/utsdeTanimsizYerdenIadeAlma/ekle"
        servicedata = "{" \
                      + "\"UDI\":" + UDI + "," \
                      + "\"ADT\":" + ADT \
                      + "}"

    # Kullanım Bildirimi
    # Sağlık kuruluşu/uygulama tesisi tekil ürünü hasta/tüketiciye kullandığında Kullanım Bildirimi yapar.
    def kullanimbildir(self, UNO, LNO, SNO, ADT, HAA, HAS, TKN, YKN, PAN, GIT, KTN, TUR, DTA):
        servicepath = self._servicepath + "/kullanim/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"HAA\":\"" + HAA + "\"," \
                      + "\"HAS\":\"" + HAS + "\"," \
                      + "\"TKN\":" + TKN + "," \
                      + "\"YKN\":" + YKN + "," \
                      + "\"PAN\":\"" + PAN + "\"," \
                      + "\"GIT\":\"" + GIT + "\"," \
                      + "\"KTN\":" + KTN + "," \
                      + "\"TUR\":\"" + TUR + "\"," \
                      + "\"DTA\":\"" + DTA + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Kullanım Bildirimi
    def essizkimlikbilgisiilekullanimbildir(self, UDI, ADT, HAA, HAS, TKN, YKN, PAN, GIT, KTN, TUR, DTA):
        servicepath = self._servicepath + "/kullanim/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"HAA\":\"" + HAA + "\"," \
                      + "\"HAS\":\"" + HAS + "\"," \
                      + "\"TKN\":" + TKN + "," \
                      + "\"YKN\":" + YKN + "," \
                      + "\"PAN\":\"" + PAN + "\"," \
                      + "\"GIT\":\"" + GIT + "\"," \
                      + "\"KTN\":" + KTN + "," \
                      + "\"TUR\":\"" + TUR + "\"," \
                      + "\"DTA\":\"" + DTA + "\"" \
                      + "}"

    # Tüketiciye Verme Bildirimi
    # Satış yeri, tüketiciye verdiği tekil ürünler için tüketiciye verme bildirimi yapar. Satış, hibe vb. yöntemler için
    # Tüketiciye Verme Bildirimi yapılır.
    def tuketiciyevermebildir(self, UNO, LNO, SNO, ADT, BEN, TUA, TUS, TKN, YKN, PAN, GIT, KTN, TUR, DTA):
        servicepath = self._servicepath + "/tuketiciyeVerme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"BEN\":\"" + BEN + "\"," \
                      + "\"TUA\":\"" + TUA + "\"," \
                      + "\"TUS\":\"" + TUS + "\"," \
                      + "\"TKN\":" + TKN + "," \
                      + "\"YKN\":" + YKN + "," \
                      + "\"PAN\":\"" + PAN + "\"," \
                      + "\"GIT\":\"" + GIT + "\"," \
                      + "\"KTN\":" + KTN + "," \
                      + "\"TUR\":\"" + TUR + "\"," \
                      + "\"DTA\":\"" + DTA + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Tüketiciye Verme Bildirimi
    def essizkimlikbilgisiiletuketiciyevermebildir(self, UDI, ADT, BEN, TUA, TUS, TKN, YKN, PAN, GIT, KTN, TUR, DTA):
        servicepath = self._servicepath + "/tuketiciyeVerme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"BEN\":\"" + BEN + "\"," \
                      + "\"TUA\":\"" + TUA + "\"," \
                      + "\"TUS\":\"" + TUS + "\"," \
                      + "\"TKN\":" + TKN + "," \
                      + "\"YKN\":" + YKN + "," \
                      + "\"PAN\":\"" + PAN + "\"," \
                      + "\"GIT\":\"" + GIT + "\"," \
                      + "\"KTN\":" + KTN + "," \
                      + "\"TUR\":\"" + TUR + "\"," \
                      + "\"DTA\":\"" + DTA + "\"" \
                      + "}"

    # Tüketiciden İade Alma Bildirimi
    # Kurum/firma, daha önce tüketiciye verdiği tekil ürünü geri alması durumunda Tüketiciden İade Alma Bildirimi yapar.
    def tuketicideniadealmabildir(self, TID, ADT, VKN, UDI, UNO, LNO, SNO):
        servicepath = self._servicepath + "/tuketicidenIadeAlma/ekle"
        servicedata = "{" \
                      + "\"TID\":" + TID + "," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"VKN\":" + VKN + "," \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi ile Tüketiciden İade Alma Bildirimi
    def essizkimlikbilgisiiletuketicideniadealmabildir(self, UDI, VKN, ADT):
        servicepath = self._servicepath + "/tuketicidenIadeAlma/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"VKN\":" + VKN + "," \
                      + "\"ADT\":" + ADT \
                      + "}"

    # Geçici Kullanıma Verme Bildirimi
    # Kurum/firma, geçici süreliğine bir kişinin kullanımına verdiği tekil ürünler için Geçici Kullanıma Verme Bildirimi
    # yapar.
    def gecicikullanimavermebildir(self, UNO, LNO, SNO, ADT, TUA, TUS, TKN, YKN, PAN, GIT, KTN, TUR, DTA):
        servicepath = self._servicepath + "/geciciKullanimaVerme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"TUA\":\"" + TUA + "\"," \
                      + "\"TUS\":\"" + TUS + "\"," \
                      + "\"TKN\":" + TKN + "," \
                      + "\"YKN\":" + YKN + "," \
                      + "\"PAN\":\"" + PAN + "\"," \
                      + "\"GIT\":\"" + GIT + "\"," \
                      + "\"KTN\":" + KTN + "," \
                      + "\"TUR\":\"" + TUR + "\"," \
                      + "\"DTA\":\"" + DTA + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Geçici Kullanıma Verme Bildirimi
    def essizkimlikbilgisiilegecicikullanimavermebildir(self, UDI, ADT, TUA, TUS, TKN, YKN, PAN, GIT, KTN, TUR, DTA):
        servicepath = self._servicepath + "/tuketiciyeVerme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"TUA\":\"" + TUA + "\"," \
                      + "\"TUS\":\"" + TUS + "\"," \
                      + "\"TKN\":" + TKN + "," \
                      + "\"YKN\":" + YKN + "," \
                      + "\"PAN\":\"" + PAN + "\"," \
                      + "\"GIT\":\"" + GIT + "\"," \
                      + "\"KTN\":" + KTN + "," \
                      + "\"TUR\":\"" + TUR + "\"," \
                      + "\"DTA\":\"" + DTA + "\"" \
                      + "}"

    # Kullanımdan Alma Bildirimi
    # Kurum/firma, geçici süreliğine hasta/tüketicinin kullanımına verdiği tekil ürünleri geri aldığında Kullanımdan Alma
    # Bildirimi yapar.
    def kullanimdanalmabildir(self, GKI, ADT, UDI, UNO, LNO, SNO):
        servicepath = self._servicepath + "/kullanimdanAlma/ekle"
        servicedata = "{" \
                      + "\"GKI\":" + GKI + "," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi ile Kullanımdan Alma Bildirimi
    def essizkimlikbilgisiilekullanimdanalmabildir(self, UDI, ADT):
        servicepath = self._servicepath + "/kullanimdanAlma/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT \
                      + "}"

    # Yeniden İşleme Bildirimi
    # Kurum/firma ÜTS’de tanımlı tekil ürünü başka bir tekil ürünün üretiminde hammadde olarak kullanması durumunda
    # yeniden işleme bildirimi yapar.
    def yenidenislemebildir(self, UNO, LNO, SNO, ADT):
        servicepath = self._servicepath + "/yenidenIsleme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Yeniden İşleme Bildirimi
    def essizkimlikbilgisiileyenidenislemebildir(self, UDI, ADT):
        servicepath = self._servicepath + "/yenidenIsleme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT \
                      + "}"

    # İhracat Bildirimi
    # İhracatçı, ihraç ettiği tekil ürünler için İhracat Bildirimi yapar.
    def ihracatbildir(self, UNO, LNO, SNO, ADT, BEN, GBN):
        servicepath = self._servicepath + "/ihracat/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"BEN\":\"" + BEN + "\"," \
                      + "\"GBN\":\"" + GBN + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle İhracat Bildirimi
    def essizkimlikbilgisiileyihracatbildir(self, UDI, ADT, BEN, GBN):
        servicepath = self._servicepath + "/ihracat/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"BEN\":\"" + BEN + "\"," \
                      + "\"GBN\":\"" + GBN + "\"" \
                      + "}"

    # Mahrecine İade Etme Bildirimi
    # İthalatçı, ithal ettiği tekil ürünü iade ettiğinde Mahrecine İade Bildirimi yapar.
    def mahrecineiadeetmebildir(self, UNO, LNO, SNO, ADT, GBN):
        servicepath = self._servicepath + "/mahrecineIadeEtme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"GBN\":\"" + GBN + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Mahrecine İade Etme Bildirimi
    def essizkimlikbilgisiilemahrecineiadeetmebildir(self, UDI, ADT, GBN):
        servicepath = self._servicepath + "/mahrecineIadeEtme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"GBN\":\"" + GBN + "\"" \
                      + "}"

    # HEK / Zayiat Bildirimi
    # Kurum/firma, ekonomik ömrünü tamamlayan veya zayi olan tekil ürünleri için HEK / Zayiat bildirimi yapar. HEK
    # ifadesi Hurda / Enkaz / Köhne kelimelerinin kısaltmasıdır.
    def hekzayiatbildir(self, UNO, LNO, SNO, ADT, TUR, DTA):
        servicepath = self._servicepath + "/hekZayiat/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"TUR\":\"" + TUR + "\"," \
                      + "\"DTA\":\"" + DTA + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle HEK / Zayiat Bildirimi
    def essizkimlikbilgisiilehekzayiatbildir(self, UDI, ADT, TUR, DTA):
        servicepath = self._servicepath + "/hekZayiat/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"TUR\":\"" + TUR + "\"," \
                      + "\"DTA\":\"" + DTA + "\"" \
                      + "}"

    # Geri Çekme Verme Bildirimi
    # Kurum/firma, geri çekme kapsamındaki tekil ürünleri başka bir kurum/firmaya verdiğinde Geri Çekme Verme
    # Bildirimi yapar.
    def gericekmevermebildir(self, UNO, LNO, SNO, ADT, KUN, BNO):
        servicepath = self._servicepath + "/geriCekmeVerme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"KUN\":" + KUN + "," \
                      + "\"BNO\":\"" + BNO + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Geri Çekme Verme Bildirimi
    def essizkimlikbilgisiilegericekmevermebildir(self, UDI, ADT, KUN, BNO):
        servicepath = self._servicepath + "/geriCekmeVerme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"KUN\":" + KUN + "," \
                      + "\"BNO\":\"" + BNO + "\"" \
                      + "}"

    # Geri Çekme Alma Bildirimi
    # Kurum/firma, geri çekme kapsamında kendisine verilen tekil ürünleri kabul etmek için Geri Çekme Alma Bildirimi
    # yapar.
    def gericekmealmabildir(self, GVI, ADT, GKK, UDI, UNO, LNO, SNO):
        servicepath = self._servicepath + "/geriCekmeAlma/ekle"
        servicedata = "{" \
                      + "\"GVI\":\"" + GVI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"GKK\":" + GKK + "," \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi ile Geri Çekme Alma Bildirimi
    def essizkimlikbilgisiilegericekmealmabildir(self, UDI, ADT, GKK):
        servicepath = self._servicepath + "/geriCekmeAlma/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"GKK\":" + GKK \
                      + "}"

    # Islah / Düzeltici Faaliyet Bildirimi
    # Kurum/firma, uygunsuz veya teknik düzenlemeye aykırı olduğu için geri çekilen tekil ürünlerdeki gerekli
    # düzenlemeyi yaptığında Islah Bildirimi yapar.
    def islahduzelticifaaliyetbildir(self, UNO, LNO, SNO, ADT, KUN):
        servicepath = self._servicepath + "/islahDuzelticiFaaliyet/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"KUN\":" + KUN \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Islah / Düzeltici Faaliyet Bildirimi
    def essizkimlikbilgisiileislahduzelticifaaliyetbildir(self, UDI, ADT, KUN):
        servicepath = self._servicepath + "/islahDuzelticiFaaliyet/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"KUN\":" + KUN \
                      + "}"

    # İmha / Bertaraf Bildirimi
    # Kurum/firma, tekil ürünleri herhangi bir gerekçeyle imha ettiğinde İmha / Bertaraf Bildirimi yapar.
    def imhabertarafbildir(self, UNO, LNO, SNO, ADT, GRK, DGA, BNO):
        servicepath = self._servicepath + "/geriCekmeVerme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"GRK\":" + GRK + "," \
                      + "\"DGA\":" + DGA + "," \
                      + "\"BNO\":\"" + BNO + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle İmha / Bertaraf Bildirimi
    def essizkimlikbilgisiileimhabertarafbildir(self, UDI, ADT, GRK, DGA, BNO):
        servicepath = self._servicepath + "/imhaBertaraf/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"GRK\":" + GRK + "," \
                      + "\"DGA\":" + DGA + "," \
                      + "\"BNO\":\"" + BNO + "\"" \
                      + "}"

    # Hastanın Vücudundan Çıkarma Bildirimi
    # Hakkında geri çekme kararı olan, miadı dolmuş veya görevini tamamlamış tıbbi cihazların tüketiciden geri alınması
    # durumunda Hastadan Geri Toplatma Bildirimi yapılır.
    def hastaninvucudundancikarmabildir(self, UNO, LNO, SNO, HAA, HAS, TKN, YKN, PAN, GRK, DGA, GIT, KTN, TUR, DTA):
        servicepath = self._servicepath + "/hastaninVucudundanCikarma/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"HAA\":\"" + HAA + "\"," \
                      + "\"HAS\":\"" + HAS + "\"," \
                      + "\"TKN\":" + TKN + "," \
                      + "\"YKN\":" + YKN + "," \
                      + "\"PAN\":\"" + PAN + "\"," \
                      + "\"GRK\":" + GRK + "," \
                      + "\"DGA\":" + DGA + "," \
                      + "\"GIT\":\"" + GIT + "\"," \
                      + "\"KTN\":" + KTN + "," \
                      + "\"TUR\":\"" + TUR + "\"," \
                      + "\"DTA\":\"" + DTA + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Hastanın Vücudundan Çıkarma Bildirimi
    def essizkimlikbilgisiilehastaninvucudundancikarmabildir(self, UDI, HAA, HAS, TKN, YKN, PAN, GRK, DGA, GIT, KTN,
                                                             TUR, DTA):
        servicepath = self._servicepath + "/hastaninVucudundanCikarma/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + UDI + "\"," \
                      + "\"HAA\":\"" + HAA + "\"," \
                      + "\"HAS\":\"" + HAS + "\"," \
                      + "\"TKN\":" + TKN + "," \
                      + "\"YKN\":" + YKN + "," \
                      + "\"PAN\":\"" + PAN + "\"," \
                      + "\"GRK\":" + GRK + "," \
                      + "\"DGA\":" + DGA + "," \
                      + "\"GIT\":\"" + GIT + "\"," \
                      + "\"KTN\":" + KTN + "," \
                      + "\"TUR\":\"" + TUR + "\"," \
                      + "\"DTA\":\"" + DTA + "\"" \
                      + "}"

    # Envanter Bildirimi
    # Sağlık hizmet sunucuları, envantere almak istediği ürünler için bir Envanter Bildirimi yapar.
    def envanterbildir(self, UIK, UNO, LNO, SNO, ENT, SKT, SBT):
        servicepath = self._servicepath + "/envanter/ekle"
        servicedata = "{" \
                      + "\"UIK\":" + UIK + "," \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ENT\":\"" + ENT + "\"," \
                      + "\"SKT\":\"" + SKT + "\"," \
                      + "\"SBT\":\"" + SBT + "\"" \
                      + "}"

    # Stok Bildirimi
    # Sağlık hizmet sunucuları dışındaki kurumlar, stok yapmak istediği ürünler için Stok Bildirimi yapar.
    def stokbildir(self, UIK, UNO, LNO, SNO, ADT, URT, SKT):
        servicepath = self._servicepath + "/stok/ekle"
        servicedata = "{" \
                      + "\"UIK\":" + UIK + "," \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT + "," \
                      + "\"URT\":\"" + URT + "\"," \
                      + "\"SKT\":\"" + SKT + "\"" \
                      + "}"

    # Eczane Stok Bildirimi
    # Eczaneler, stok bildirmek istediği tekil ürünler için Eczane Stok Bildirimi yapar. Eczane sadece İnsülin Kalem İğne
    # Ucu ve Şeker Ölçüm Çubuğu branş türündeki ürünler için stok bildirimi yapabilir.
    def eczanestokbildir(self, UIK, UNO, LNO, SNO, ADT):
        servicepath = self._servicepath + "/eczane/stok/ekle"
        servicedata = "{" \
                      + "\"UIK\":" + UIK + "," \
                      + "\"UNO\":\"" + UNO + "\"," \
                      + "\"LNO\":\"" + LNO + "\"," \
                      + "\"SNO\":\"" + SNO + "\"," \
                      + "\"ADT\":" + ADT \
                      + "}"
