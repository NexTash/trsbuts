import trsbuts.UTSConnection as UTSConnection


class ActionNotificationService:
    def __init__(self):
        self._utsconnection = UTSConnection()
        self._servicepath = self._servicepath + ""

    # Üretim Bildirimi
    # Üretici, ürettiği tekil ürünlerin her biri için bir Üretim Bildirimi yapar.
    def uretimbildir(self, uno, lno, sno, urt, skt, adt, udi, sip, kus, gtk):
        servicepath = self._servicepath + "/uretim/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"" \
                      + ",\"LNO\":\"" + lno + "\"" \
                      + ",\"SNO\":\"" + sno + "\"" \
                      + ",\"URT\":\"" + urt + "\"" \
                      + ",\"SKT\":\"" + skt + "\"" \
                      + ",\"ADT\":" + adt + "," \
                      + ",\"UDI\":\"" + udi + "\"" \
                      + ",\"SIP\":\"" + sip + "\"" \
                      + ",\"KUS\":\"" + kus + "\"" \
                      + ",\"GTK\":\"" + gtk + "\"" \
                      + "}"

    # İthalat Bildirimi
    # İthalatçı, ithal ettiği tekil ürünler için İthalat Bildirimi yapar.
    def ithalatbildir(self, uno, lno, sno, urt, skt, itt, adt, udi, ieu, meu, gbn, sip, kus, gtk):
        servicepath = self._servicepath + "/ithalat/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"URT\":\"" + urt + "\"," \
                      + "\"SKT\":\"" + skt + "\"," \
                      + "\"ITT\":\"" + itt + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"IEU\":" + ieu + "," \
                      + "\"MEU\":" + meu + "," \
                      + "\"GBN\":\"" + gbn + "\"," \
                      + "\"SIP\":\"" + sip + "\"," \
                      + "\"KUS\":\"" + kus + "\"," \
                      + "\"GTK\":\"" + gtk + "\"" \
                      + "}"

    # Yetkili Bayi İle İthalat Bildirimi
    # İthalatçı tarafından yetki verilen bayi ithalat bildirimi yapabilmektedir. Bunun için bayinin ithalat yapmak istediği
    # ürüne ait ithalatçı tarafından girilmiş olan yetkili distribütörlük belgesi olmalıdır.
    def yetkilibayiileithalatbildir(self, uik, uno, lno, sno, urt, skt, itt, adt, udi, ieu, meu, gbn, sip, kus, gtk):
        servicepath = self._servicepath + "/ithalat/yetkiliBayiIle/ekle"
        servicedata = "{" \
                      + "\"UIK\":" + uik + "," \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"URT\":\"" + urt + "\"," \
                      + "\"SKT\":\"" + skt + "\"," \
                      + "\"ITT\":\"" + itt + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"IEU\":" + ieu + "," \
                      + "\"MEU\":" + meu + "," \
                      + "\"GBN\":\"" + gbn + "\"," \
                      + "\"SIP\":\"" + sip + "\"," \
                      + "\"KUS\":\"" + kus + "\"," \
                      + "\"GTK\":\"" + gtk + "\"" \
                      + "}"

    # Verme Bildirimi
    # Kurum/firma kullanıcısı sahip olduğu tekil ürünlerini başka bir kurum/firmaya verdiğinde Verme Bildirimi yapar.
    # Satış, hibe, iade vb. yöntemler için Verme Bildirimi yapılır.
    def vermebildir(self, uno, lno, sno, adt, kun, ben, bno, git):
        servicepath = self._servicepath + "/verme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"KUN\":" + kun + "," \
                      + "\"BEN\":\"" + ben + "\"," \
                      + "\"BNO\":\"" + bno + "\"," \
                      + "\"GIT\":\"" + git + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Verme Bildirimi
    def essizkimlikbilgisiilevermebildir(self, udi, adt, kun, bno):
        sservicepath = self._servicepath + "/verme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"KUN\":" + kun + "," \
                      + "\"BNO\":\"" + bno + "\"" \
                      + "}"

    # Alma Bildirimi
    # Kurum/firma kendisine verilen tekil ürünleri kabul etmek için Alma Bildirimi yapar. Bu bildirimle beraber tekil ürünün
    # sahipliği alıcı tarafa geçmiş olur.
    def almabildir(self, vbi, adt, gkk, udi, uno, lno, sno):
        servicepath = self._servicepath + "/alma/ekle"
        servicedata = "{" \
                      + "\"VBI\":" + vbi + "," \
                      + "\"ADT\":" + adt + "," \
                      + "\"GKK\":" + gkk + "," \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Alma Bildirimi
    def essizkimlikbilgisiilealmabildir(self, udi, adt, gkk):
        servicepath = self._servicepath + "/alma/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"GKK\":" + gkk \
                      + "}"

    # ÜTS’de Tanımsız Yere Verme Bildirimi
    # Kurum/firma ÜTS'de tanımlı olmayan bir firmaya tekil ürün verdiğinde ÜTS’de Tanımsız Yere Verme Bildirimi yapar.
    def utsdetanimsizyerevermebildir(self, uno, lno, sno, adt, ben, vkn, bno):
        servicepath = self._servicepath + "/utsdeTanimsizYereVerme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"BEN\":\"" + ben + "\"," \
                      + "\"VKN\":" + vkn + "," \
                      + "\"BNO\":\"" + bno + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle ÜTS’de Tanımsız Yere Verme Bildirimi
    def essizkimlikbilgisiileutsdetanimsizyerevermebildir(self, udi, adt, ben, vkn, men, tkn, mek, odk, bno):
        servicepath = self._servicepath + "/utsdeTanimsizYereVerme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"BEN\":\"" + ben + "\"," \
                      + "\"VKN\":" + vkn + "," \
                      + "\"MEN\":" + men + "," \
                      + "\"TKN\":" + tkn + ", " \
                      + "\"MEK\":" + mek + "," \
                      + "\"ODK\":" + odk + "," \
                      + "\"BNO\":\"" + bno + "\"" \
                      + "}"

    # ÜTS’de Tanımsız Yerden İade Alma Bildirimi
    # Kurum/firma ÜTS'de tanımlı olmayan bir firmaya verdiği tekil ürünlerini iade aldığında ÜTS’de Tanımsız Yerden
    # İade Alma Bildirimi yapar.
    def utsdetanimsizyerdeniadealmabildir(self, uti, adt, udi, uno, lno, sno):
        servicepath = self._servicepath + "/utsdeTanimsizYerdenIadeAlma/ekle"
        servicedata = "{" \
                      + "\"UTI\":" + uti + "," \
                      + "\"ADT\":" + adt + "," \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi ile ÜTS’de Tanımsız Yerden İade Alma Bildirimi
    def essizkimlikbilgisiileutsdetanimsizyerdeniadealmabildir(self, udi, adt):
        servicepath = self._servicepath + "/utsdeTanimsizYerdenIadeAlma/ekle"
        servicedata = "{" \
                      + "\"UDI\":" + udi + "," \
                      + "\"ADT\":" + adt \
                      + "}"

    # Kullanım Bildirimi
    # Sağlık kuruluşu/uygulama tesisi tekil ürünü hasta/tüketiciye kullandığında Kullanım Bildirimi yapar.
    def kullanimbildir(self, uno, lno, sno, adt, haa, has, tkn, ykn, pan, git, ktn, tur, dta):
        servicepath = self._servicepath + "/kullanim/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"HAA\":\"" + haa + "\"," \
                      + "\"HAS\":\"" + has + "\"," \
                      + "\"TKN\":" + tkn + "," \
                      + "\"YKN\":" + ykn + "," \
                      + "\"PAN\":\"" + pan + "\"," \
                      + "\"GIT\":\"" + git + "\"," \
                      + "\"KTN\":" + ktn + "," \
                      + "\"TUR\":\"" + tur + "\"," \
                      + "\"DTA\":\"" + dta + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Kullanım Bildirimi
    def essizkimlikbilgisiilekullanimbildir(self, udi, adt, haa, has, tkn, ykn, pan, git, ktn, tur, dta):
        servicepath = self._servicepath + "/kullanim/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"HAA\":\"" + haa + "\"," \
                      + "\"HAS\":\"" + has + "\"," \
                      + "\"TKN\":" + tkn + ", " \
                      + "\"YKN\":" + ykn + "," \
                      + "\"PAN\":\"" + pan + "\"," \
                      + "\"GIT\":\"" + git + "\"," \
                      + "\"KTN\":" + ktn + "," \
                      + "\"TUR\":\"" + tur + "\"," \
                      + "\"DTA\":\"" + dta + "\"" \
                      + "}"

    # Tüketiciye Verme Bildirimi
    # Satış yeri, tüketiciye verdiği tekil ürünler için tüketiciye verme bildirimi yapar. Satış, hibe vb. yöntemler için
    # Tüketiciye Verme Bildirimi yapılır.
    def tuketiciyevermebildir(self, uno, lno, sno, adt, ben, tua, tus, tkn, ykn, pan, git, ktn, tur, dta):
        servicepath = self._servicepath + "/tuketiciyeVerme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"BEN\":\"" + ben + "\"," \
                      + "\"TUA\":\"" + tua + "\"," \
                      + "\"TUS\":\"" + tus + "\"," \
                      + "\"TKN\":" + tkn + ", " \
                      + "\"YKN\":" + ykn + "," \
                      + "\"PAN\":\"" + pan + "\"," \
                      + "\"GIT\":\"" + git + "\"," \
                      + "\"KTN\":" + ktn + "," \
                      + "\"TUR\":\"" + tur + "\"," \
                      + "\"DTA\":\"" + dta + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Tüketiciye Verme Bildirimi
    def essizkimlikbilgisiiletuketiciyevermebildir(self, udi, adt, ben, tua, tus, tkn, ykn, pan, git, ktn, tur, dta):
        servicepath = self._servicepath + "/tuketiciyeVerme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"BEN\":\"" + ben + "\"," \
                      + "\"TUA\":\"" + tua + "\"," \
                      + "\"TUS\":\"" + tus + "\"," \
                      + "\"TKN\":" + tkn + ", " \
                      + "\"YKN\":" + ykn + "," \
                      + "\"PAN\":\"" + pan + "\"," \
                      + "\"GIT\":\"" + git + "\"," \
                      + "\"KTN\":" + ktn + "," \
                      + "\"TUR\":\"" + tur + "\"," \
                      + "\"DTA\":\"" + dta + "\"" \
                      + "}"

    # Tüketiciden İade Alma Bildirimi
    # Kurum/firma, daha önce tüketiciye verdiği tekil ürünü geri alması durumunda Tüketiciden İade Alma Bildirimi yapar.
    def tuketicideniadealmabildir(self, tid, adt, vkn, udi, uno, lno, sno):
        servicepath = self._servicepath + "/tuketicidenIadeAlma/ekle"
        servicedata = "{" \
                      + "\"TID\":" + tid + "," \
                      + "\"ADT\":" + adt + "," \
                      + "\"VKN\":" + vkn + "," \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi ile Tüketiciden İade Alma Bildirimi
    def essizkimlikbilgisiiletuketicideniadealmabildir(self, udi, vkn, adt):
        servicepath = self._servicepath + "/tuketicidenIadeAlma/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"VKN\":" + vkn + "," \
                      + "\"ADT\":" + adt \
                      + "}"

    # Geçici Kullanıma Verme Bildirimi
    # Kurum/firma, geçici süreliğine bir kişinin kullanımına verdiği tekil ürünler için Geçici Kullanıma Verme Bildirimi
    # yapar.
    def gecicikullanimavermebildir(self, uno, lno, sno, adt, tua, tus, tkn, ykn, pan, git, ktn, tur, dta):
        servicepath = self._servicepath + "/geciciKullanimaVerme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"TUA\":\"" + tua + "\"," \
                      + "\"TUS\":\"" + tus + "\"," \
                      + "\"TKN\":" + tkn + ", " \
                      + "\"YKN\":" + ykn + "," \
                      + "\"PAN\":\"" + pan + "\"," \
                      + "\"GIT\":\"" + git + "\"," \
                      + "\"KTN\":" + ktn + "," \
                      + "\"TUR\":\"" + tur + "\"," \
                      + "\"DTA\":\"" + dta + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Geçici Kullanıma Verme Bildirimi
    def essizkimlikbilgisiilegecicikullanimavermebildir(self, udi, adt, tua, tus, tkn, ykn, pan, git, ktn, tur, dta):
        servicepath = self._servicepath + "/tuketiciyeVerme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"TUA\":\"" + tua + "\"," \
                      + "\"TUS\":\"" + tus + "\"," \
                      + "\"TKN\":" + tkn + ", " \
                      + "\"YKN\":" + ykn + "," \
                      + "\"PAN\":\"" + pan + "\"," \
                      + "\"GIT\":\"" + git + "\"," \
                      + "\"KTN\":" + ktn + "," \
                      + "\"TUR\":\"" + tur + "\"," \
                      + "\"DTA\":\"" + dta + "\"" \
                      + "}"

    # Kullanımdan Alma Bildirimi
    # Kurum/firma, geçici süreliğine hasta/tüketicinin kullanımına verdiği tekil ürünleri geri aldığında Kullanımdan Alma
    # Bildirimi yapar.
    def kullanimdanalmabildir(self, gki, adt, udi, uno, lno, sno):
        servicepath = self._servicepath + "/kullanimdanAlma/ekle"
        servicedata = "{" \
                      + "\"GKI\":" + gki + "," \
                      + "\"ADT\":" + adt + "," \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi ile Kullanımdan Alma Bildirimi
    def essizkimlikbilgisiilekullanimdanalmabildir(self, udi, adt):
        servicepath = self._servicepath + "/kullanimdanAlma/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt \
                      + "}"

    # Yeniden İşleme Bildirimi
    # Kurum/firma ÜTS’de tanımlı tekil ürünü başka bir tekil ürünün üretiminde hammadde olarak kullanması durumunda
    # yeniden işleme bildirimi yapar.
    def yenidenislemebildir(self, uno, lno, sno, adt):
        servicepath = self._servicepath + "/yenidenIsleme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Yeniden İşleme Bildirimi
    def essizkimlikbilgisiileyenidenislemebildir(self, udi, adt):
        servicepath = self._servicepath + "/yenidenIsleme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt \
                      + "}"

    # İhracat Bildirimi
    # İhracatçı, ihraç ettiği tekil ürünler için İhracat Bildirimi yapar.
    def ihracatbildir(self, uno, lno, sno, adt, ben, gbn):
        servicepath = self._servicepath + "/ihracat/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"BEN\":\"" + ben + "\"," \
                      + "\"GBN\":\"" + gbn + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle İhracat Bildirimi
    def essizkimlikbilgisiileyihracatbildir(self, udi, adt, ben, gbn):
        servicepath = self._servicepath + "/ihracat/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"BEN\":\"" + ben + "\"," \
                      + "\"GBN\":\"" + gbn + "\"" \
                      + "}"

    # Mahrecine İade Etme Bildirimi
    # İthalatçı, ithal ettiği tekil ürünü iade ettiğinde Mahrecine İade Bildirimi yapar.
    def mahrecineiadeetmebildir(self, uno, lno, sno, adt, gbn):
        servicepath = self._servicepath + "/mahrecineIadeEtme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"GBN\":\"" + gbn + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Mahrecine İade Etme Bildirimi
    def essizkimlikbilgisiilemahrecineiadeetmebildir(self, udi, adt, gbn):
        servicepath = self._servicepath + "/mahrecineIadeEtme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"GBN\":\"" + gbn + "\"" \
                      + "}"

    # HEK / Zayiat Bildirimi
    # Kurum/firma, ekonomik ömrünü tamamlayan veya zayi olan tekil ürünleri için HEK / Zayiat bildirimi yapar. HEK
    # ifadesi Hurda / Enkaz / Köhne kelimelerinin kısaltmasıdır.
    def hekzayiatbildir(self, uno, lno, sno, adt, tur, dta):
        servicepath = self._servicepath + "/hekZayiat/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"TUR\":\"" + tur + "\"," \
                      + "\"DTA\":\"" + dta + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle HEK / Zayiat Bildirimi
    def essizkimlikbilgisiilehekzayiatbildir(self, udi, adt, tur, dta):
        servicepath = self._servicepath + "/hekZayiat/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"TUR\":\"" + tur + "\"," \
                      + "\"DTA\":\"" + dta + "\"" \
                      + "}"

    # Geri Çekme Verme Bildirimi
    # Kurum/firma, geri çekme kapsamındaki tekil ürünleri başka bir kurum/firmaya verdiğinde Geri Çekme Verme
    # Bildirimi yapar.
    def gericekmevermebildir(self, uno, lno, sno, adt, kun, bno):
        servicepath = self._servicepath + "/geriCekmeVerme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"KUN\":" + kun + "," \
                      + "\"BNO\":\"" + bno + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Geri Çekme Verme Bildirimi
    def essizkimlikbilgisiilegericekmevermebildir(self, udi, adt, kun, bno):
        servicepath = self._servicepath + "/geriCekmeVerme/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"KUN\":" + kun + "," \
                      + "\"BNO\":\"" + bno + "\"" \
                      + "}"

    # Geri Çekme Alma Bildirimi
    # Kurum/firma, geri çekme kapsamında kendisine verilen tekil ürünleri kabul etmek için Geri Çekme Alma Bildirimi
    # yapar.
    def gericekmealmabildir(self, gvi, adt, gkk, udi, uno, lno, sno):
        servicepath = self._servicepath + "/geriCekmeAlma/ekle"
        servicedata = "{" \
                      + "\"GVI\":\"" + gvi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"GKK\":" + gkk + "," \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi ile Geri Çekme Alma Bildirimi
    def essizkimlikbilgisiilegericekmealmabildir(self, udi, adt, gkk):
        servicepath = self._servicepath + "/geriCekmeAlma/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"GKK\":" + gkk \
                      + "}"

    # Islah / Düzeltici Faaliyet Bildirimi
    # Kurum/firma, uygunsuz veya teknik düzenlemeye aykırı olduğu için geri çekilen tekil ürünlerdeki gerekli
    # düzenlemeyi yaptığında Islah Bildirimi yapar.
    def islahduzelticifaaliyetbildir(self, uno, lno, sno, adt, kun):
        servicepath = self._servicepath + "/islahDuzelticiFaaliyet/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"KUN\":" + kun \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Islah / Düzeltici Faaliyet Bildirimi
    def essizkimlikbilgisiileislahduzelticifaaliyetbildir(self, udi, adt, kun):
        servicepath = self._servicepath + "/islahDuzelticiFaaliyet/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"KUN\":" + kun \
                      + "}"

    # İmha / Bertaraf Bildirimi
    # Kurum/firma, tekil ürünleri herhangi bir gerekçeyle imha ettiğinde İmha / Bertaraf Bildirimi yapar.
    def imhabertarafbildir(self, uno, lno, sno, adt, grk, dga, bno):
        servicepath = self._servicepath + "/geriCekmeVerme/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"GRK\":" + grk + "," \
                      + "\"DGA\":" + dga + "," \
                      + "\"BNO\":\"" + bno + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle İmha / Bertaraf Bildirimi
    def essizkimlikbilgisiileimhabertarafbildir(self, udi, adt, grk, dga, bno):
        servicepath = self._servicepath + "/imhaBertaraf/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"GRK\":" + grk + "," \
                      + "\"DGA\":" + dga + "," \
                      + "\"BNO\":\"" + bno + "\"" \
                      + "}"

    # Hastanın Vücudundan Çıkarma Bildirimi
    # Hakkında geri çekme kararı olan, miadı dolmuş veya görevini tamamlamış tıbbi cihazların tüketiciden geri alınması
    # durumunda Hastadan Geri Toplatma Bildirimi yapılır.
    def hastaninvucudundancikarmabildir(self, uno, lno, sno, haa, has, tkn, ykn, pan, grk, dga, git, ktn, tur, dta):
        servicepath = self._servicepath + "/hastaninVucudundanCikarma/ekle"
        servicedata = "{" \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"HAA\":\"" + haa + "\"," \
                      + "\"HAS\":\"" + has + "\"," \
                      + "\"TKN\":" + tkn + ", " \
                      + "\"YKN\":" + ykn + "," \
                      + "\"PAN\":\"" + pan + "\"," \
                      + "\"GRK\":" + grk + "," \
                      + "\"DGA\":" + dga + "," \
                      + "\"GIT\":\"" + git + "\"," \
                      + "\"KTN\":" + ktn + "," \
                      + "\"TUR\":\"" + tur + "\"," \
                      + "\"DTA\":\"" + dta + "\"" \
                      + "}"

    # Eşsiz Kimlik Bilgisi İle Hastanın Vücudundan Çıkarma Bildirimi
    def essizkimlikbilgisiilehastaninvucudundancikarmabildir(self, udi, haa, has, tkn, ykn, pan, grk, dga, git, ktn,
                                                             tur, dta):
        servicepath = self._servicepath + "/hastaninVucudundanCikarma/ekle/essizKimlik"
        servicedata = "{" \
                      + "\"UDI\":\"" + udi + "\"," \
                      + "\"HAA\":\"" + haa + "\"," \
                      + "\"HAS\":\"" + has + "\"," \
                      + "\"TKN\":" + tkn + ", " \
                      + "\"YKN\":" + ykn + "," \
                      + "\"PAN\":\"" + pan + "\"," \
                      + "\"GRK\":" + grk + "," \
                      + "\"DGA\":" + dga + "," \
                      + "\"GIT\":\"" + git + "\"," \
                      + "\"KTN\":" + ktn + "," \
                      + "\"TUR\":\"" + tur + "\"," \
                      + "\"DTA\":\"" + dta + "\"" \
                      + "}"

    # Envanter Bildirimi
    # Sağlık hizmet sunucuları, envantere almak istediği ürünler için bir Envanter Bildirimi yapar.
    def envanterbildir(self, uik, uno, lno, sno, ent, skt, sbt):
        servicepath = self._servicepath + "/envanter/ekle"
        servicedata = "{" \
                      + "\"UIK\":" + uik + "," \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ENT\":\"" + ent + "\"," \
                      + "\"SKT\":\"" + skt + "\"," \
                      + "\"SBT\":\"" + sbt + "\"" \
                      + "}"

    # Stok Bildirimi
    # Sağlık hizmet sunucuları dışındaki kurumlar, stok yapmak istediği ürünler için Stok Bildirimi yapar.
    def stokbildir(self, uik, uno, lno, sno, adt, urt, skt):
        servicepath = self._servicepath + "/stok/ekle"
        servicedata = "{" \
                      + "\"UIK\":" + uik + "," \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt + "," \
                      + "\"URT\":\"" + urt + "\"," \
                      + "\"SKT\":\"" + skt + "\"" \
                      + "}"

    # Eczane Stok Bildirimi
    # Eczaneler, stok bildirmek istediği tekil ürünler için Eczane Stok Bildirimi yapar. Eczane sadece İnsülin Kalem İğne
    # Ucu ve Şeker Ölçüm Çubuğu branş türündeki ürünler için stok bildirimi yapabilir.
    def eczanestokbildir(self, uik, uno, lno, sno, adt):
        servicepath = self._servicepath + "/eczane/stok/ekle"
        servicedata = "{" \
                      + "\"UIK\":" + uik + "," \
                      + "\"UNO\":\"" + uno + "\"," \
                      + "\"LNO\":\"" + lno + "\"," \
                      + "\"SNO\":\"" + sno + "\"," \
                      + "\"ADT\":" + adt \
                      + "}"
