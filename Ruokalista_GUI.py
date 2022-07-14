# TIE-01200 Johdatus ohjelmointiin
# Salla Ponkala, opiskelijanro 99226, sähköposti ponkala.salla.k@student.uta.fi
# Ratkaisu tehtävään 13.10 Graafinen käyttöliittymä
# Status: READY

# Tämä ohjelma auttaa käyttäjää valitsemaan, mitä ruokaa minäkin päivänä
# syödään. Valinnan jälkeen voit tulostaa listan aineksista, joita kaupasta
# täytyy tuoda. Ohjelma lukee ruokien tiedot ja reseptit valmiista testitiedos-
# toista. TAVOITE: haastavampi, skaalautuva käyttöliittymä.

# KÄYTTÖOHJE:
# Ohjelman pääikkunaan aukeaa erilaisia vaihtoehtoja, joista käyttäjä voi
# valita haluamansa toiminnon.
#
# Toiminto "Valitse päivän ruoka" avaa uuden ikkunan,
# jossa käyttäjä voi antaa aikaisempana kahtena päivänä syömänsä ruoat,
# minkä perusteella ohjelma valitsee satunnaisen ruokalajin, kunhan se ei ole
# samaa tyyppiä kuin käyttäjän kahtena aikaisempana päivänä syömät ruoat.
# Käyttäjän ei ole pakko syöttää aikaisempia ruokia, sillä ne voivat helposti
# unohtua, tai käyttäjä ei välitä, vaikka söisi samaa/saman tyyppistä ruokaa
# useampana päivänä. Myös siinä tapauksessa, vaikka käyttäjä syöttäisi tyypin,
# jota ei löydy listasta, valinta voidaan suorittaa, sillä kaikkia mahdollisia
# tyyppejä ei löydy tästä listasta. Valinnan suorittamisen jälkeen käyttäjä voi
# halutessaan tulostaa näytölle ruokaan tarvittavat ainekset. Jos valintaa ei
# ole tehty, tulostetaan virheilmoitus.
#
# Toiminto "Tulosta kaikki tyypit" näyttää käyttäjälle, minkä tyyppisiä ruokia
# listalla on, jotta hän voi syöttää valintaan jonkin niistä tyypeistä.
#
# Toiminto "Tulosta kaikki lajit" puolestaan tulostaa ruokalajit, jotta käyttä-
# jä voi halutessaan itse valita lajeista mieluisensa.
#
# Toiminnon "Lisää ruokia listalle" avulla käyttäjä voi lisätä listalle ruokia,
# joita siellä ei vielä ole. Ohjelma pyytää käyttäjältä tyypin ja ruokalajin ni-
# men ja lisää sen ruokalista-tiedostoon. Tyhjä syöte ei kelpaa, ja siitä
# ilmoitetaan virheellä.
#
# Toiminto "Hae resepti" johtaa valikkoon, jossa käyttää voi valita pudotus-
# valikosta mieluisensa ruokalajin. Ruokalajin valittuaan käyttäjä saa ruoan
# valmistamiseen tarvittavat ainekset, ja voi kirjoittaa niistä kauppalistan.
# Jos ruokalaji on uusi, eikä sillä ole vielä aineslistaa, ohjelma ilmoittaa
# siitä ja ehdottaa reseptin lisäämistä. Reseptin voi sitten lisätä.
# Virheellisestä syötteestä on tässäkin tapauksessa tarkoitus ilmoittaa
# virheellä.


import random

from tkinter import *


class Kayttoliittyma:
    """ Graafinen käyttöliittymä, jonka rajoissa ohjelma toimii."""

    def __init__(self):
        """Rakentaja: pääikkunan elementit"""
        self.__paaikkuna = Tk()
        self.__paaikkuna.minsize(width=500, height=500)
        self.__paaikkuna.title("Ruokalista-sovellus")
        self.__background_image = PhotoImage(file="Webp.net-gifmaker.gif")
        self.__background_label = Label(self.__paaikkuna,
                                        image=self.__background_image)

        self.__file = read_file("Ruokalista")

        self.__tervetuloteksti = Label(self.__paaikkuna,
                                       text="Tervetuloa "
                                            "Ruokalista-sovellukseen!",
                                       font=("Bodoni 72", 20, "normal"))

        self.__ohjeteksti = Label(self.__paaikkuna,
                                  text="Tämän ohjelman ansiosta "
                                        "et joudu koskaan enää päättämään,\n"
                                        "mitä haluat tänään syödä!\n")

        self.__valintateksti = Label(self.__paaikkuna, text="Valitse toiminto:")
        self.__valintateksti.configure(background="pink")

        self.__valintanappi = Button(self.__paaikkuna, text="Valitse päivän ruoka",
                                     command=self.choose_dish)

        self.__tyypit = Button(self.__paaikkuna, text="Tulosta kaikki tyypit",
                               command=self.print_types_list)

        self.__ruokalajit = Button(self.__paaikkuna, text="Tulosta kaikki lajit",
                                   command=self.print_dishes_list)

        self.__lisaysnappi = Button(self.__paaikkuna, text="Lisää ruokia listalle",
                                    command=self.lisaa_ruokia)

        self.__reseptit = Button(self.__paaikkuna, text="Hae resepti",
                                 command=self.hae_resepti)

        self.__tyhja = Label(self.__paaikkuna)

        self.__lopeta = Button(self.__paaikkuna, text="Lopeta",
                               command=self.quit)

        self.__valinta = ""
        self.__paaikkunan_toiminnot = [self.__valintanappi, self.__tyypit,
                                      self.__ruokalajit, self.__lisaysnappi,
                                       self.__reseptit, self.__tyhja,
                                       self.__lopeta]

        self.__background_label.pack()
        self.__tervetuloteksti.pack()
        self.__ohjeteksti.pack()
        self.__valintateksti.pack()

        for toiminto in self.__paaikkunan_toiminnot:
            toiminto.pack()

    def quit(self):
        """Ohjelman lopettava metodi."""
        self.__paaikkuna.destroy()

    def start(self):
        """Ohjelman käynnistävä metodi."""
        self.__paaikkuna.mainloop()

    def print_types_list(self):
        """Tulostaa listan ruokien tyypeistä."""

        window = Toplevel(self.__paaikkuna)
        window.focus_set()
        window.grab_set()
        lista = tyyppilista("Ruokalista")

        for sana in lista:
            label = Label(window, text=sana)
            label.pack()

        paluu = Button(window, text="Paluu", command=window.destroy)
        paluu.pack()

    def print_dishes_list(self):
        """Tulostaa listan tuokalajeista"""

        window = Toplevel(self.__paaikkuna)
        window.focus_set()
        window.grab_set()

        lista = lajilista()

        for sana in lista:
            label = Label(window, text=sana)
            label.pack()

        paluu = Button(window, text="Paluu", command=window.destroy)
        paluu.pack()

    def choose_dish(self):
        """
        Valitsee satunnaisen ruokalajin, joka ei ole samaa tyyppiä kuin kahtena
        aikaisempana päivänä syöty ruoka.
        """

        self.__dish_window = Toplevel(self.__paaikkuna)
        self.__dish_window.focus_set()
        self.__dish_window.grab_set()
        self.__infolabel = Label(self.__dish_window,
                                 text="Ettet joutuisi syömään saman tyyppistä\n"
                                    "ruokaa liian usein, kerro, mitä söit eilen\n"
                                    "ja toissapäivänä:", font=(None, 15))

        self.__label_eilen = Label(self.__dish_window,
                                   text="Minkä tyyppisen ruoan söit eilen?")

        self.__syote_eilen = Entry(self.__dish_window)
        self.__eilen = str(self.__syote_eilen.get())

        self.__label_toissapaivana = Label(self.__dish_window,
                                           text="Minkä tyyppisen ruoan"
                                                " söit toissapäivänä?")

        self.__syote_toissapaivana = Entry(self.__dish_window)
        self.__toissapaivana = str(self.__syote_toissapaivana.get())

        self.__execute_button = Button(self.__dish_window,
                                        text="Suorita valinta",
                                        command=self.execute_choosing)

        self.__valinta_lable = Label(self.__dish_window)
        self.__valinta_lable2 = Label(self.__dish_window)
        self.__exit = Button(self.__dish_window, text="Paluu",
                             command=self.__dish_window.destroy)

        self.__huomioteksti_pun = Label(self.__dish_window,
                                    text="Huom! Jos jätät kentät tyhjiksi,\n"
                                        "ohjelma valitsee täysin satunnaisen "
                                         "ruoan.\n"
                                        "Voit tulostaa listalla olevat tyypit\n" 
                                        "pääsivun painikkeesta 'tulosta kaikki "
                                         "tyypit'.",
                                            foreground="red", font=(None, 10))

        self.__valintakuva = PhotoImage(file="kuva2.gif")
        self.__valintakuva_label = Label(self.__dish_window,
                                         image=self.__valintakuva)

        self.__valintakuva_label.pack()

        self.__ingredientsButton = Button(self.__dish_window,
                                          text="Näytä ainekset",
                                          command=self.give_ingredients_execute)

        pakattavat = [self.__infolabel, self.__label_eilen, self.__syote_eilen,
                      self.__label_toissapaivana, self.__syote_toissapaivana,
                      self.__huomioteksti_pun, self.__execute_button,
                      self.__valinta_lable, self.__valinta_lable2]

        for toiminto in pakattavat:
            toiminto.pack()

        self.__ingredientsButton.pack(side=LEFT)
        self.__exit.pack(side=RIGHT)

    def execute_choosing(self):
        """
        Metodi, joka toteuttaa satunnaisen valinnan. Valitsee ensin satunnai-
        sen tyypin, joka ei ole sama kuin eilinen tai toissapäiväinen ruoka.
        Sen jälkeen se valitsee tyypin sisältä satunnaisen ruokalajin.
        """

        ruokalista = read_file("Ruokalista")

        tyypit_1 = []
        tyypit_2 = []
        for avain in tyyppilista("Ruokalista"):
            if str(avain).strip() != str(self.__eilen).strip():
                tyypit_1.append(avain)
                for tyyppi in tyypit_1:
                    if str(tyyppi).strip() != str(
                            self.__toissapaivana).strip():
                        tyypit_2.append(tyyppi)

        luku = len(tyypit_2) - 1
        if luku < 0:
            luku = 0
        indeksi = int(random.randint(0, luku))

        laji = tyypit_2[indeksi]  # Valitaan satunnainen tyyppi
        luku = len(ruokalista[laji]) - 1
        indeksi = int(random.randint(0, luku))  # Valitaan satunnainen

        self.__valinta = ruokalista[laji][indeksi]

        self.__valinta_lable["text"] = "Paivan ruoka on: "
        self.__valinta_lable2.configure(text=self.__valinta,
                                        font=("Bodoni 72", 20, "normal"),
                                        background="pink")

        # Käyttäjä voi halutessaan tulostaa valinnasta aineslistan:
        self.__ingredientsButton = Button(self.__dish_window,
                                          text="Näytä ainekset",
                                          command=self.give_ingredients_execute)
        self.__syote_eilen.delete(0, END)
        self.__syote_toissapaivana.delete(0, END)

    def lisaa_ruokia(self):
        """Toiminnolla voi lisätä ruokia Ruokalistatiedostoon."""

        self.__lisays_window = Toplevel(self.__paaikkuna)
        self.__lisays_window.focus_set()
        self.__lisays_window.grab_set()

        self.__muokattava_ruokalista = open("Ruokalista", "a")

        self.__tyyppi_label = Label(self.__lisays_window,
                                    text="Lisättävän ruoan tyyppi\n"
                                         "(yksi tyyppi/ruokalaji):")

        self.__tyyppi_entry = Entry(self.__lisays_window)

        self.__ruokalaji_label = Label(self.__lisays_window,
                                       text="Lisättävän ruokalajin nimi:")

        self.__ruokalaji_entry = Entry(self.__lisays_window)

        self.__execute_lisaa = Button(self.__lisays_window, text="Lisää",
                                      command=self.execute_lisaa_ruokia)

        self.__virheilmoitustila = Label(self.__lisays_window)

        poistutaan = Button(self.__lisays_window, text="Paluu",
                            command=self.__lisays_window.destroy)

        self.__tyyppi_label.pack()
        self.__tyyppi_entry.pack()
        self.__ruokalaji_label.pack()
        self.__ruokalaji_entry.pack()
        self.__virheilmoitustila.pack()
        self.__execute_lisaa.pack(side=RIGHT)
        poistutaan.pack(side=LEFT)

    def execute_lisaa_ruokia(self):
        """
        Toteuttaa ruoan lisäyksen listalle, kun käyttäjä painaa lisäysnappia
        """

        self.__lisattava_tyyppi = self.__tyyppi_entry.get()
        self.__lisattava_laji = self.__ruokalaji_entry.get()

        if ruokalista_tarkista_syote(self.__lisattava_tyyppi) and \
                ruokalista_tarkista_syote(self.__lisattava_laji):

            if self.__lisattava_laji not in lajilista():
                # Jos syötetty laji ei ole vielä listalla, se lisätään sinne,
                # kunhan syöte ei ole tyhjä.

                if self.__lisattava_laji != "" or self.__lisattava_tyyppi != "":
                    self.__muokattava_ruokalista.write("\n")
                    self.__muokattava_ruokalista.write(self.__lisattava_laji)
                    self.__muokattava_ruokalista.write(", ")
                    self.__muokattava_ruokalista.write(self.__lisattava_tyyppi)
                    self.__infoikkuna = Toplevel(self.__lisays_window)
                    self.__infoikkuna.focus_set()
                    self.__infoikkuna.grab_set()
                    ilmoitus = Label(self.__infoikkuna,
                                     text="Ruokalaji lisätty listalle.\n"
                                        "Haluatko lisätä toisen ruokalajin?")
                    poistumisnappi1 = Button(self.__infoikkuna, text="Kyllä",
                                             command=self.__infoikkuna.destroy)

                    poistumisnappi2 = Button(self.__infoikkuna, text="Ei kiitos",
                                        command=lambda:
                                    [f() for f in[self.__lisays_window.destroy,
                                             self.sulje_tiedosto]])

                    ilmoitus.pack()
                    poistumisnappi1.pack(side=RIGHT)
                    poistumisnappi2.pack(side=LEFT)

                    self.__ruokalaji_entry.delete(0, END)
                    self.__tyyppi_entry.delete(0, END)

                else:
                    # Tyhjä syöte ei keplpaa, vaan aiheuttaa virheen.

                    infoikkuna = Toplevel(self.__lisays_window)
                    infoikkuna.focus_set()
                    infoikkuna.grab_set()
                    ilmoitus = Label(infoikkuna,
                                     text="Virhe: Tyhjä syöte.\n"
                                            "Haluatko yrittää uudelleen?")

                    poistumisnappi1 = Button(infoikkuna, text="Kyllä",
                                             command=infoikkuna.destroy)

                    poistumisnappi2 = Button(infoikkuna, text="Ei kiitos",
                                             command=lambda:
                                             [f() for f in
                                            [self.__lisays_window.destroy,
                                             self.sulje_tiedosto]])

                    ilmoitus.pack()
                    poistumisnappi1.pack(side=RIGHT)
                    poistumisnappi2.pack(side=LEFT)

            elif self.__lisattava_laji in lajilista():
                # Jos ruokalaji on jo listalla, tulostetaan myös virhe.

                infoikkuna = Toplevel(self.__lisays_window)
                infoikkuna.focus_set()
                infoikkuna.grab_set()
                ilmoitus = Label(infoikkuna, text="Ruokalaji on jo listalla.\n"
                                                  "Syötä jokin toinen ruoka.")

                poistumisnappi = Button(infoikkuna, text="Ok",
                                        command=infoikkuna.destroy)

                ilmoitus.pack()
                poistumisnappi.pack()
                self.__tyyppi_entry.delete(0, END)
                self.__ruokalaji_entry.delete(0, END)
        else:
            # Jos syöte sisältää vääriä merkkejä, tulostetaan virhe:

            self.__virheilmoitustila.configure(text="Tyyppi ja laji eivät saa\n"
                                                    "sisältää merkkejä.",
                                               foreground="red")
            self.__tyyppi_entry.delete(0, END)
            self.__ruokalaji_entry.delete(0, END)

    def sulje_tiedosto(self):
        """Metodi, jolla muokattavaksi avatun ruokalistan saa suljettua. """
        self.__muokattava_ruokalista.close()

    def hae_resepti(self):
        """
        Hae resepti -toiminnon toteutus. Käyttäjä voi valita ruokalajin, jo-
        hon haluaa reseptin vetovalikosta, minkä jälkeen ohjelma tulostaa re-
        septin.
        """

        self.__resepti_window = Toplevel(self.__paaikkuna)
        self.__resepti_window.focus_set()
        self.__resepti_window.grab_set()

        labelimage = PhotoImage(file="bag.gif")
        self.__imagelabel = Label(self.__resepti_window, image=labelimage)
        self.__imagelabel.photo = labelimage

        self.__resepti_window.minsize(width=250, height=200)

        paluu = Button(self.__resepti_window, text="Paluu", command=
                      self.__resepti_window.destroy)

        label = Label(self.__resepti_window, text="Valitse ruokalaji:",
                      font=("Bodoni 72", 20, "normal"))

        self.__valikko = StringVar(self.__resepti_window)
        self.__valikko.set(lajilista()[0])

        self.__menu = OptionMenu(self.__resepti_window, self.__valikko,
                                 *lajilista())

        self.__tulostus = Label(self.__resepti_window, text="")

        self.__select = Button(self.__resepti_window, text="Valitse",
                               command=self.get_selection)

        self.__imagelabel.pack()
        label.pack()
        self.__menu.pack()
        self.__select.pack()
        self.__tulostus.pack()
        paluu.pack(side=BOTTOM)

    def give_ingredients_execute(self):
        """Tulostaa listan käyttäjälle valitusta ruokalajista."""

        self.__ingredient_window = Toplevel(self.__dish_window)
        self.__ingredient_window.focus_set()
        self.__ingredient_window.grab_set()
        self.__ingredient_window.minsize(width=200, height=150)

        ingredients_dict = reseptidicti()
        sad_image = PhotoImage(file="sad_face.gif")

        if self.__valinta == "":
            # Jos valintaa ei ole suoritettu, ei aineksia voida tulostaa, vaan
            # Ilmoitetaan virheestä.

            label_1 = Label(self.__ingredient_window, image=sad_image)
            label_1.photo = sad_image
            label_2 = Label(self.__ingredient_window,
                            text="Et suorittanut vielä valintaa.",
                            foreground="red")

            label_1.pack()
            label_2.pack()
            exit = Button(self.__ingredient_window, text="Paluu",
                          command=self.__ingredient_window.destroy)
            exit.pack(side=BOTTOM)

        else:
            if self.__valinta in ingredients_dict:
                ingredients_list = ingredients_dict[self.__valinta]

                for ingredient in ingredients_list:
                    label = Label(self.__ingredient_window, text=ingredient)
                    label.pack()

                exit = Button(self.__ingredient_window, text="Paluu",
                              command=self.__ingredient_window.destroy)
                exit.pack()

            elif self.__valinta not in ingredients_dict:
                # Jos ruokalajille ei ole vielä aineslistaa, siitä ilmoitetaan
                # Ja ehdotetaan käyttäjälle reseptin lisäämistä.

                ilmoitusteksti = Label(self.__ingredient_window,
                                       text="Ruokalajille ei ole vielä\n"
                                            "aineslistaa.\n"
                                            "\n"
                                            "Lisätäänkö ainekset?")

                nappi1 = Button(self.__ingredient_window, text="Lisää",
                                command=lambda: self.lisaa_resepti(self.__ingredient_window,
                                                                   self.__valinta))

                nappi2 = Button(self.__ingredient_window, text="Ei kiitos",
                                command=self.__ingredient_window.destroy)

                ilmoitusteksti.pack()
                nappi1.pack(side=RIGHT)
                nappi2.pack(side=LEFT)

    def get_selection(self):
        """
        Tulostaa käyttäjän valitseman ruokalajin ainesosat.
        Tätä metodia hyödynnetään Hae resepti -toiminnossa.
        """

        self.__resepti_valinta = self.__valikko.get()
        reseptit = reseptidicti()
        if self.__resepti_valinta in reseptit:
            self.__resepti = reseptit[self.__resepti_valinta]
            self.__tulostus.configure(text="\n".join(self.__resepti))
        else:
            self.__ilmoitus = Toplevel(self.__resepti_window)
            self.__ilmoitus.focus_set()
            self.__ilmoitus.grab_set()
            ilmoitusteksti = Label(self.__ilmoitus, text="Ruokalajille ei ole vielä\n"
                                                  "aineslistaa.\n"
                                                  "\n"
                                                  "Lisätäänkö ainekset?")
            nappi1 = Button(self.__ilmoitus, text="Lisää",
                            command=lambda: self.lisaa_resepti(self.__ilmoitus,
                                                    self.__resepti_valinta))
            nappi2 = Button(self.__ilmoitus, text="Ei kiitos",
                            command=self.__ilmoitus.destroy)

            ilmoitusteksti.pack()
            nappi1.pack(side=RIGHT)
            nappi2.pack(side=LEFT)

    def lisaa_resepti(self, window, resepti):
        """
        Käyttäjä voi lisätä listalle reseptin syöttämällä tyypin ja ruoka-
        lajin.
        """

        self.__reseptin_lisays_ikkuna = Toplevel(window)
        self.__reseptin_lisays_ikkuna.focus_set()
        self.__reseptin_lisays_ikkuna.grab_set()

        label1 = Label(self.__reseptin_lisays_ikkuna,
                      text="Lisää ainekset ruokalajille:")

        label2 = Label(self.__reseptin_lisays_ikkuna,
                       text=resepti, font=("Bodoni 72", 20, "normal"),
                       background="pink")

        label3 = Label(self.__reseptin_lisays_ikkuna,
                       text="Lisää ainekset erotettuna pilkulla,\n "
                            "ilman välilyöntiä:")

        self.__ainekset_entry = Entry(self.__reseptin_lisays_ikkuna)

        self.__execute_button = Button(self.__reseptin_lisays_ikkuna,
                                text="Lisää", command=lambda:
                                self.execute_lisaa_resepti(resepti))

        poistutaan = Button(self.__reseptin_lisays_ikkuna, text="Paluu",
                            command=lambda:
                            [f() for f in [self.__reseptin_lisays_ikkuna.destroy,
                            window.destroy]])

        self.__loppuinfo = Label(self.__reseptin_lisays_ikkuna)

        label1.pack()
        label2.pack()
        label3.pack()
        self.__ainekset_entry.pack()
        self.__execute_button.pack()
        self.__loppuinfo.pack()
        poistutaan.pack(side=BOTTOM)

    def execute_lisaa_resepti(self, resepti):
        """
        Toteuttaa reseptin lisäyksen aineslistaan, kun komento annetaan.
        :param resepti: tiedostoon lisättävä reseptisyöte (str).
        """

        tiedosto = open("Ainekset", "a")

        self.__ainekset = self.__ainekset_entry.get()

        if ainekset_tarkista_syote(self.__ainekset):
            if self.__ainekset != "":
                tiedosto.write("\n")
                tiedosto.write(resepti)
                tiedosto.write(":")
                tiedosto.write(self.__ainekset)
                self.__loppuinfo.configure(text="Aineslista lisätty!",
                                           foreground="black")
                self.__ainekset_entry.delete(0, END)
                self.__ainekset_entry.configure(state=DISABLED)
                self.__execute_button.configure(state=DISABLED)
            else:
                self.__loppuinfo.configure(text="Tyhjä syöte ei kelpaa.\n"
                                            "Yritä uudelleen.",
                                            foreground="red")

                self.__ainekset_entry.delete(0, END)

            tiedosto.close()

        else:
            if self.__ainekset == "":
                self.__loppuinfo.configure(text="Tyhjä syöte ei kelpaa.\n"
                                                "Yritä uudelleen.",
                                           foreground="red")
                self.__ainekset_entry.delete(0, END)
            else:
                self.__loppuinfo.configure(text="Syötteessä voi olla vain\n"
                                            "aakkosia ja pilkkuja.",
                                            foreground="red")


def read_file(tiedosto):
    """
    Lukee Ruokalistan sisältävän tiedoston ja muuttaa ruokalistan dictiksi.
    :return: ruokalista dict-muodossa, jolloin avaimena on tyyppi ja arvona
    lista tyyppiä olevista ruokalajeista.
    """

    tiedosto = open(tiedosto, "r")
    ruokalista = {}
    for rivi in tiedosto:
        rivi = rivi.split(",")
        tyyppi = rivi[1].strip()
        ateria = rivi[0].strip()
        ruokalista[tyyppi] = []
        ruokalista[tyyppi].append(ateria)

    tiedosto.close()
    return ruokalista


def lajilista():
    """
    Tuottaa ruokalistan sisältävästä tiedostosta aakkosittain järjestetyn
    listan ruokalajeista.
    :return: list. ruokalajit aakkosittain listassa.
    """

    lukutiedosto = open("Ruokalista", "r")
    lajilista = []
    for rivi in lukutiedosto:
        rivi = rivi.split(",")
        ateria = rivi[0].strip()
        lajilista.append(ateria)

    lukutiedosto.close()
    return sorted(lajilista)

def tyyppilista(tiedosto):
    """
    Tuottaa tiedostosta listan eri tyypeistä.
    :return: lista tyypeistä aakkosjärjestyksessä.
    """

    lukutiedosto = open(tiedosto, "r")
    tyyppilista = []
    for rivi in lukutiedosto:
        rivi = rivi.split(",")
        tyyppi = rivi[1].strip()
        if tyyppi not in tyyppilista:
            tyyppilista.append(tyyppi)
    lukutiedosto.close()
    return sorted(tyyppilista)

def reseptidicti():
    """
    Tuottaa ainekset sisältävästä tiedostosta dictin, jossa avain on ruokalajin
    nimi ja arvo lista siihen tarvittavista aineksista.
    :return: dict. ruokalajit ja siihen tarvittavat ainekset.
    """

    lukutiedosto = open("Ainekset", "r")
    reseptit = {}
    for rivi in lukutiedosto:
        rivi=rivi.split(":")
        ruoka = rivi[0]
        rivi[1] = rivi[1].split(",")
        ainekset = []
        for aines in rivi[1]:
            ainekset.append(aines)
        reseptit[ruoka] = ainekset

    lukutiedosto.close()
    return reseptit

def ruokalista_tarkista_syote(sana):
    """
    Tarkistaa, että syöte koostuu kirjaimista ja mahdollisista
    välilyönneistä. Tarkastaa syötteen, kun ruokia lisätään ruokalistalle.
    :param sana: syöte, joka tarkastetaan (str).
    """
    if all(i.isalpha() or i.isspace() for i in sana):
        return True
    else:
        return False

def ainekset_tarkista_syote(syote):
    """
    Tarkistaa, että syöte sisältää vain aakkosia ja pilkkuja. Tarkistaa
    syötteen lisättäessä uutta reseptiä ainelistaan.
    :param syote: syöte, joka tarkastetaan (str).
    """

    try:
        if any(merkki.isspace() for merkki in syote):
            raise ValueError
        elif any(merkki.isdigit() for merkki in syote):
            raise ValueError
        elif all(merkki.isalpha() for merkki in syote):
            return True
        else:
            for merkki in syote:
                if not merkki.isalpha():
                    if merkki != ",":
                        raise ValueError
            return True

    except ValueError:
        return False


def main():
    """Pääohjelma, joka käynnistää graafisen käyttöliittymän."""
    ui = Kayttoliittyma()
    ui.start()

main()

