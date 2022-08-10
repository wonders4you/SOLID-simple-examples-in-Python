# SOLID part 2 S%O%LID
# 
# O Open/closed principle

# Elementy oprogramowania, takie jak klasy, moduły i funkcje, 
# powinny być otwarte na rozszerzenia, ale zamknięte na modyfikacje

# Poniższa klasa musi być modyfikowwana za każdym razem gdy dodamy
# do niej nowy rodzaj dokumentu, czy też zmienimy metodeę walidacji.
# Za każdą taką modyfikacją wiąże się sprawdzanie całego kodu i inne 
# problemy.


# class Printer():
#     def print_pdf():
#         pass 

#     def print_odt():
#         pass

#     def verify_data():
#         pass

# Zgodnie z zasadą Open/closed principle, powyższa klasę można
# zreafaktoryzować w poniższy sposób:


from abc import ABC, abstractmethod


# Tworzymy klase wzorzec dla wszystkich "printów dokumentów".
class Printer(ABC):
   
    @abstractmethod
    def hardware_print():
        pass

# Tworzymy klasę weryfikującą dane
class VerifyData():
    
     def veryfied():
        pass

# Tworzymy klasy drukujące poszczególe dokumenty implementujące
# interfejs Printer, możemy dzięki temu dowolnie rozszerzać kod, 
# o nowe urządzenia.

class PrintPDF (Printer):

    def hardware_print():
        pass

class PrintDOC (Printer):

    def hardware_print():
        pass    

class PrintODT (Printer):

    def hardware_print():
        pass  

class PrintJSON (Printer):

    def hardware_print():
        pass  
