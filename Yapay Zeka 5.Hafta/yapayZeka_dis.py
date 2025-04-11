# Python 3.10+ uyumluluğu için collections patch
import collections
import collections.abc
collections.Mapping = collections.abc.Mapping

from experta import KnowledgeEngine, Fact, Rule


# Diş ile ilgili belirtileri temsil eden Fact sınıfı
class DisProblemi(Fact):
    """Diş problemi için belirti"""
    pass


# Uzman sistemi sınıfı
class DisUzmanSistemi(KnowledgeEngine):

    @Rule(DisProblemi(dis_eti_kanamasi=True, uzun_sureli=False))
    def dis_hastaligi_var(self):
        print("→ Diş hastalığı vardır. Diş hekimine başvur.")

    @Rule(DisProblemi(dis_eti_kanamasi=True, uzun_sureli=True))
    def diseti_cekilmesi_var(self):
        print("→ Dişeti çekilmesi vardır. Diş hekimine başvur.")

    @Rule(DisProblemi(diseti_cekilmesi=True, dis_koku_gorunuyor=True))
    def dis_koku_gorunuyor(self):
        print("→ Diş kökü görünüyorsa, dolgu yaptır.")

    @Rule(DisProblemi(renk_degisim=True))
    def dis_temizligi(self):
        print("→ Dişte renk değişimi var. Dişleri temizle.")

    @Rule(DisProblemi(morarma_var=True, yeni_dis_cikiyor=True))
    def yeni_dis_morarma(self):
        print("→ Yeni diş çıkarken morarma var. Diş hekimine başvur.")

    @Rule(DisProblemi(curuk_var=True, agri_yapmiyor=True))
    def curuk_agrisiz(self):
        print("→ Dişte ağrı yapmayan çürük var. Dolgu yaptır.")

    @Rule(DisProblemi(curuk_ileri=True))
    def ileri_curuk(self):
        print("→ Dişteki çürük ileri derecede. Kanal tedavisi ve dolgu yaptır.")


# Uzman sistemin çalıştırılması
if __name__ == "__main__":
    engine = DisUzmanSistemi()
    engine.reset()

    # Test verileri
    engine.declare(DisProblemi(dis_eti_kanamasi=True, uzun_sureli=True))
    engine.declare(DisProblemi(diseti_cekilmesi=True, dis_koku_gorunuyor=True))
    engine.declare(DisProblemi(renk_degisim=True))
    engine.declare(DisProblemi(morarma_var=True, yeni_dis_cikiyor=True))
    engine.declare(DisProblemi(curuk_var=True, agri_yapmiyor=True))
    engine.declare(DisProblemi(curuk_ileri=True))

    engine.run()
