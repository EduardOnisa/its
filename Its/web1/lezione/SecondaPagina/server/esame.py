#Classe Student:
#Attributi:

    #student_id: str - identificatore univoco per lo studente.
    #courses: list[str] - la lista dei corsi ai quali lo studente è iscritto.

#Metodi:

    #enroll(course: str) - aggiunge il corso specificato alla lista dei corsi dello studente oppure stampa il messaggio "Lo studente è già iscritto al corso {course}."
    #get_courses(): restituisce la lista dei corsi ai quali lo studente è iscritto.

#Classe School:
#Attributi:

    #students: dict[str, Student] - un dizionario per memorizzare gli studenti, in cui la chiave è una stringa ID mentre il valore è un oggetto di tipo Studente.

#Metodi:

    #create_student(student_id: str): crea un nuovo studente con l'ID specificato e una lista di corsi vuota oppure stampa il messaggio "Lo studente con ID {student_id} esiste già."
    #enroll_student(student_id: str, course: str): se lo studente esiste viene iscritto al corso specificato, altrimenti  stampa il messaggio "Studente non trovato."
    #get_student_courses(student_id: str): se lo studente esiste restituisce la lista dei corsi dello studente con l'ID specificato, altrimenti ritorna il messaggio "Studente non trovato."
    #get_stundent_list(): Ritorna una lista di tutte le chiavi all'interno del dizionario students.
    #search_by_course(self, course: str): Trova e restituisce tutti gli ID degli studenti iscritti ad un determinato corso. Restituisce una lista di tutte le chiavi all'interno del dizionario students che hanno il corso specificato tra i valori oppure il messaggio di errore "Nessuno studente è iscritto al corso {course}." se non ci sono studenti che frequentano il corso specificato.

class Student:
    def __init__(self, student_id: str, courses):
        self.student_id = student_id
        self.courses = []

    def enroll(self, course: str):
        self.course = course

        if self.course in self.courses:
            print (f"Lo studente è già iscritto al corso {course}.")
        else:
            self.course.append(course)

    def get_courses(self):
        return self.courses
    
class School:
    def __init__(self):
        self.students = []

    def create_student(self, student_id: str):
        self.student_id = student_id

        if self.student_id not in self.students:
            student: Student = Student(student_id)
            self.courses = []
        else: 
            print (f"Lo studente con ID {student_id} esiste già.")

    def enroll_student(self, student_id: str, course: str):
        self.student_id = student_id
        self.course = course

        if student_id in self.students:
            self.course.append(self.student_id)
        else:
            print (f"Studente non trovato.")

    def get_student_courses(self, student_id: str):
        self.student_id = student_id

        if student_id in self.students:
            return self.courses 
        else:
            print (f"Studente non trovato.")

    def get_stundent_list(self):
        keylist = []

        for key in self.students.keys:
            keylist.append(key)          

    def search_by_course(self, course: str):
        self.course = course

        if self.student_id in self.course:  
            return 
        else:
            print (f"Nessuno studente è iscritto al corso {course}.")

    
    












#In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di elettrodomestici.

#Classe Base: Elettrodomestico
#Crea una classe base chiamata Elettrodomestico con i seguenti attributi e metodi:
#Attributi: marca: str, modello: str, potenza: int
#Metodi:
#__init__(self, marca: str, modello: str, potenza: int): metodo costruttore che inizializza gli attributi marca, modello e potenza.
#descrivi_elettrodomestico(self): metodo che stampa una descrizione dell'elettrodomestico nel formato "Marca: {marca}, Modello: {modello}, Potenza: {potenza}W"

#2. Classe Derivata: Frigorifero
#Crea una classe derivata chiamata Frigorifero che eredita dalla classe Elettrodomestico e aggiunge i seguenti attributi e metodi:
#Attributi: capacità: int
#Metodi:
#__init__(self, marca: str, modello: str, potenza: int, capacità: int): metodo costruttore che inizializza gli attributi della classe base e capacità.
#descrivi_elettrodomestico(self): metodo che sovrascrive quello della classe base per includere anche la capacità nella descrizione, nel formato "Marca: {marca}, Modello: {modello}, Potenza: {potenza}W, Capacità: {capacità}L"

#Classe Derivata: Lavatrice
#Crea una classe derivata chiamata Lavatrice che eredita dalla classe Elettrodomestico e aggiunge i seguenti attributi e metodi:
#Attributi: - carico_max: int
#Metodi:
#- __init__(self, marca: str, modello: str, potenza: int, carico_max: int): metodo costruttore che inizializza gli attributi della classe base e carico_max.
#- descrivi_elettrodomestico(self): metodo che sovrascrive quello della classe base per includere anche il carico massimo nella descrizione, nel formato "Marca: {self.marca}, Modello: {modello}, Potenza: {potenza}W, Carico massimo: {carico_max}kg".

        class Elettrodomestico:
            def __init__(self, marca: str, modello: str, potenza: int):
                self.marca = marca
                self.modello = modello
                self.potenza = potenza

        def descrivi_elettrodomestico(self):
            print (f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W")

    class Frigorifero(Elettrodomestico):
        def __init__(self, marca: str, modello: str, potenza: int, capacità: int):
            super().__init__(marca, modello, potenza)
            self.capacità = capacità
            
        def descrivi_elettrodomestico(self):
            print (f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Capacità: {self.capacità}L")

    class Lavatrice(Elettrodomestico):
        def __init__(self, marca: str, modello: str, potenza: int, carico_max: int):
            super().__init__(marca, modello, potenza)
            self.carico_max = carico_max

        def descrivi_elettrodomestico(self):
            print (f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Carico massimo: {self.carico_max}kg")


#Scrivere un frammento di codice che modifichi il valore intero memorizzato nella variabile n nel seguente modo:
    #se n è pari, deve essere incrementato di 10;
    #se n è dispari, deve essere decrementato di 5.

def modifica_valore(n: int) -> int:
    if n % 2 == 0:
        n+= 10
    if n % 2 != 0:
        n-= 5
        
    return n


#Scrivi una funzione che accetti tre parametri: user, passw e stato dell'account (attivo/non attivo). 
# L'accesso è consentito solo se il nome utente è "manager", la password corrisponde a "67890" e l'account è attivo (True). 
# La funzione ritorna "Ingresso consentito" oppure "Ingresso negato".

def verifica_accesso(user: str, passw: str, stato: bool):
    if user == "manager" and passw == "67890" and stato == True:
        return "Ingresso consentito"

    else:
        return "Ingresso negato"
    



#Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi 
# e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, 
# ma con i prezzi aumentati del 10% e arrotondati a due cifre decimali.

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
        for prezzo, prodotti in dict.items():
            if prezzo > 50:
