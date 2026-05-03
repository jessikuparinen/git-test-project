from kotitehtävä6 import Klapi, Tulipesa

#1

klapi1 = Klapi("Koivu", 2.5)
klapi2 = Klapi("Mänty", 1.8)

print(klapi1)
print(klapi2)

klapi1.sytyta()
print("Sytytettiin klapi1.")

klapi1.pala(0.5)
print(klapi1)

klapi1.pala(1.0)
print(klapi1)

klapi1.sammuta()
print("Sammutettiin klapi1.")

klapi1.pala(0.2)
print(klapi1)

#2

k1 = Klapi("Koivu", 2.0)
k2 = Klapi("Mänty", 1.5)
k3 = Klapi("Kuusi", 1.0)

tulipesa = Tulipesa()

tulipesa.lisaa_klapi(k1)
tulipesa.lisaa_klapi(k2)
tulipesa.lisaa_klapi(k3)

print(tulipesa)

tulipesa.sytyta_kaikki()
print("Sytytetään kaikki klapit.")

tulipesa.polta(0.3)
print(tulipesa)

tulipesa.polta(0.5)
print(tulipesa)


