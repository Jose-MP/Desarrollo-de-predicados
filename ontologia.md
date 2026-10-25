```mermaid
graph TD
    Animal["Animal"]
    Mamifero["Mamifero"]
    Ave["Ave"]
    Carnivoro["Carnivoro"]
    Ungulado["Ungulado"]

    Animal -->|es_un| Mamifero
    Animal -->|es_un| Ave
    Mamifero -->|es_un| Carnivoro
    Mamifero -->|es_un| Ungulado

    Guepardo["guepardo"]
    Tigre["tigre"]
    Jirafa["jirafa"]
    Cebra["cebra"]
    Pinguino["pinguino"]
    Albatros["albatros"]
    Buho["buho"]
    Lechuza["lechuza"]
    Vaca["vaca"]
    Toro["toro"]

    Carnivoro -->|Color leonado y manchas oscuras| Guepardo
    Carnivoro -->|Rayas negras| Tigre
    Ungulado -->|Cuello largo y manchas oscuras| Jirafa
    Ungulado -->|Rayas negras| Cebra
    Ave -->|Nada y es blanco con negro| Pinguino
    Ave -->|Vuela muy bien| Albatros
    Ave -->|Nocturno, ojos frontales y penachos| Buho
    Ave -->|Nocturno y cara en forma de corazon| Lechuza
    Mamifero -->|Tiene ubres| Vaca
    Mamifero -->|Cuernos grandes, robusto y sin ubres| Toro