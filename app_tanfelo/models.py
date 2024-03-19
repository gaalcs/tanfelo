from django.db import models
from django.contrib.auth.models import User
# Create your models here.

   
class Tanfelo_Tantargy(models.Model):
    """Model definition for Tantargy."""

    # TODO: Define fields here

    nev = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    tantargygondozoi = models.ManyToManyField(User)

    class Meta:
        """Meta definition for Tantargy."""

        verbose_name = 'Tantárgy'
        verbose_name_plural = 'Tantárgyak'

    def __str__(self):
        return f'{self.nev} ({ ", ".join([f"{user.last_name} {user.first_name}" for user in self.tantargygondozoi.all()]) })'

    
class Tanfelo_Tanar(models.Model):
    """Model definition for Tanar."""

    # TODO: Define fields here

    nev = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # betöltetlen álláshely esetén nincs user!
    tantargyai = models.ManyToManyField(Tanfelo_Tantargy)


    class Meta:
        verbose_name = 'Tanár'
        verbose_name_plural = 'Tanárok'

    def __str__(self):
        return f'{self.nev} ({", ".join([ " 🎓 " + str(t) for t in self.tantargyai.all()])})'

    def ok_tantargylista_alapjan(tantargyak):
        tanarok = []
        for tantargy in tantargyak:
            tanarok += [ tanar for tanar in Tanfelo_Tanar.objects.all() if tantargy in tanar.tantargyai.all()]
        return sorted(tanarok, key=lambda t: t.nev)


class Tanfelo_Tanulocsoport(models.Model):

    nev = models.CharField(max_length=100)
    kreta = models.CharField(max_length=255)
    lehetseges_tantargyai = models.ManyToManyField(Tanfelo_Tantargy)

    class Meta:
        verbose_name = "Tanulócsoport"
        verbose_name_plural = "Tanulócsoportok"

    def __str__(self):
        return self.nev + ", ".join([ "  🎓 " + t.nev for t in self.lehetseges_tantargyai.all()])

    def ok_tantargylista_alapjan(tantargyak):
        csoportok = []
        for tantargy in tantargyak:
            csoportok += [ tanulocsoport for tanulocsoport in Tanfelo_Tanulocsoport.objects.all() if tantargy in tanulocsoport.lehetseges_tantargyai.all()]
        return sorted(csoportok, key=lambda cs: cs.nev)


class Tanfelo_Kmk(models.Model):

    tanar = models.ForeignKey(Tanfelo_Tanar, on_delete=models.CASCADE)
    tantargy = models.ForeignKey(Tanfelo_Tantargy, on_delete=models.CASCADE)
    tanulocsoport = models.ForeignKey(Tanfelo_Tanulocsoport, on_delete=models.CASCADE)
    oraszam = models.IntegerField()
    
    class Meta:
        verbose_name = "Ki tanít, mit, kinek?"
        verbose_name_plural = "Ki tanít, mit, kinek?"

    def __str__(self):
        return f'{self.tanar} -> {self.tantargy} -> {self.tanulocsoport} ({self.oraszam} db)'
    
    def felulet(tantargygondozo_tantargyai, kiosztando_csoportok, felhasznalhato_tanarok):
        result = []
        for a_tantargy in tantargygondozo_tantargyai:
            for a_tanulocsoport in kiosztando_csoportok:
                a_kivalasztott_tanar, a_kivalasztott_oraszam = Tanfelo_Kmk.get_tanar_oraszam(a_tantargy, a_tanulocsoport)
                result.append({
                    'csoport': a_tanulocsoport,
                    'tantargy': a_tantargy,
                    'valaszthato_tanarok': felhasznalhato_tanarok,
                    'a_kivalasztott_tanar': a_kivalasztott_tanar,
                    'a_kivalasztott_oraszam': a_kivalasztott_oraszam,
                })
        return result
    
    def get_tanar_oraszam(a_tantargy, a_tanulocsoport):
        a_kmk = Tanfelo_Kmk.objects.filter(tantargy=a_tantargy, tanulocsoport=a_tanulocsoport).first()
        van = a_kmk == None
        a_kivalasztott_tanar = a_kmk.tanar if van else 0
        a_kivalasztott_oraszam = a_kmk.oraszam if van else 0
        return (a_kivalasztott_tanar, a_kivalasztott_oraszam)

class Tanfelo_Csoportbontasi_szempont(models.Model):

    nev = models.CharField(max_length=255)
    magyarazat = models.TextField()
    

    class Meta:
        verbose_name = "Csoportbontási szempont"
        verbose_name_plural = "Csoportbontási szempontok"

    def csoportjai(a_csoportositasi_szempont):
        return [ csoportbontas.resz for csoportbontas in Tanfelo_Csoportbontas.objects.filter(szempont=a_csoportositasi_szempont)]
    
    def univerzuma(a_csoportositasi_szempont):
        return Tanfelo_Csoportbontas.objects.filter(szempont=a_csoportositasi_szempont).first().univerzum


    def __str__(self):
        return self.nev
    
    


class Tanfelo_Csoportbontas(models.Model):

    szempont = models.ForeignKey(Tanfelo_Csoportbontasi_szempont, on_delete=models.CASCADE, null=True, blank=True)
    resz = models.ForeignKey(Tanfelo_Tanulocsoport, related_name='resz', on_delete=models.CASCADE)
    univerzum = models.ForeignKey(Tanfelo_Tanulocsoport, related_name='univerzum', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Csoportbontás"
        verbose_name_plural = "Csoportbontások"

    def __str__(self):
        return f'{"-" if self.szempont == None else self.szempont.nev} ( {self.resz} ⊆ {self.univerzum})'