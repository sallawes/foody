Foody

Status: TOIMII, mutta vaatii kehittämistä.

Tämä ohjelma auttaa käyttäjää valitsemaan, mitä ruokaa minäkin päivänä
syödään. Valinnan jälkeen voit tulostaa listan aineksista, joita kaupasta
täytyy tuoda. Ohjelma lukee ruokien tiedot ja reseptit valmiista tekstitiedos-
toista. TAVOITE: haastavampi, skaalautuva käyttöliittymä.

KÄYTTÖOHJE:
Ohjelman pääikkunaan aukeaa erilaisia vaihtoehtoja, joista käyttäjä voi
valita haluamansa toiminnon.

Toiminto "Valitse päivän ruoka" avaa uuden ikkunan,
jossa käyttäjä voi antaa aikaisempana kahtena päivänä syömänsä ruoat,
minkä perusteella ohjelma valitsee satunnaisen ruokalajin, kunhan se ei ole
samaa tyyppiä kuin käyttäjän kahtena aikaisempana päivänä syömät ruoat.
Käyttäjän ei ole pakko syöttää aikaisempia ruokia, sillä ne voivat helposti
unohtua, tai käyttäjä ei välitä, vaikka söisi samaa/saman tyyppistä ruokaa
useampana päivänä. Myös siinä tapauksessa, vaikka käyttäjä syöttäisi tyypin,
jota ei löydy listasta, valinta voidaan suorittaa, sillä kaikkia mahdollisia
tyyppejä ei löydy tästä listasta. Valinnan suorittamisen jälkeen käyttäjä voi
halutessaan tulostaa näytölle ruokaan tarvittavat ainekset. Jos valintaa ei
ole tehty, tulostetaan virheilmoitus.
HUOM: Nykyisessä versiossa edellisten ruokatyyppien huomiotta jättämistoiminto ei vielä toimi toivotusti!

Toiminto "Tulosta kaikki tyypit" näyttää käyttäjälle, minkä tyyppisiä ruokia
listalla on, jotta hän voi syöttää valintaan jonkin niistä tyypeistä.

Toiminto "Tulosta kaikki lajit" puolestaan tulostaa ruokalajit, jotta käyttä-
jä voi halutessaan itse valita lajeista mieluisensa.

Toiminnon "Lisää ruokia listalle" avulla käyttäjä voi lisätä listalle ruokia,
joita siellä ei vielä ole. Ohjelma pyytää käyttäjältä tyypin ja ruokalajin ni-
men ja lisää sen ruokalista-tiedostoon. Tyhjä syöte ei kelpaa, ja siitä
ilmoitetaan virheellä.

Toiminto "Hae resepti" johtaa valikkoon, jossa käyttää voi valita pudotus-
valikosta mieluisensa ruokalajin. Ruokalajin valittuaan käyttäjä saa ruoan
valmistamiseen tarvittavat ainekset ja voi kirjoittaa niistä kauppalistan.
Jos ruokalaji on uusi, eikä sillä ole vielä aineslistaa, ohjelma ilmoittaa
siitä ja ehdottaa reseptin lisäämistä. Reseptin voi sitten lisätä.
Virheellisestä syötteestä on tässäkin tapauksessa tarkoitus ilmoittaa
virheellä.
