Title: Utilizar certificados SSL en Amazon ELB 
Date: 2015-02-26 19:03:23
Category: English
Tags: amazon, aws, elb, ssl 
Author: frommelmak

En esta entrada voy a tratar de explicar cómo utilizar el servicio de balanceo de carga de Amazon (ELB) como terminador de conexiones SSL.

El escenario de partida sería este:

![ELB HTTP](/images/ELB_HTTP_server.png)

Como se observa en este diagrama, todo el tráfico va en plano. Desde el cliente HTTP del usuario/aplicación hasta las instancias que ofrecen el servicio HTTP.

El objetivo es cifrar todo el tráfico entre la aplicación y nuestros servidores. Para ello, lo más sencillo es configurar nuestro balanceador de carga como terminador de las conexiones SSL. Así, conseguimos de forma transparente el acceso cifrado a los servicios HTTP, ya que evitamos tener que añadir el certificado a cada uno de los servicios a securizar.

Otra ventaja es que el tráfico seguirá llegando en plano a las instancias, facilitando así el debug de posibles problemas que requieran analizar el tráfico. 

![ELB](/images/ELB_SSL_HTTPS_server.png)

El cifrado SSL/TLS utilizado por el protocolo HTTPS, utiliza criptografía de clave pública (o asimétrica) para autenticar la identidad del servidor con el que estamos comunicando. Esta, también se utiliza para intercambiar la clave simétrica que se utilizará para cifrar el tráfico.

A grandes rasgos los pasos a seguir para añadir un certificado al balaceador de carga son estos:

1. Obtener el certificado SSL
    * Generar una clave privada.
    * Generar la solicitud del certificado ([CSR](http://en.wikipedia.org/wiki/Certificate_signing_request)) a partir de la clave privada.
    * Solicitar un certificado SSL a nuestra autoridad certificadora ([CA](http://en.wikipedia.org/wiki/Certificate_authority)): [Goodady](https://www.godaddy.com) en este ejemplo.
2. Convertir el certificado al formato soportado por Amazon.
3. Subir el certificado a Amazon. 
4. Añadir listener HTTPS al balanceador y configurarlo con el nuevo certificado.


## 1 Obtener el certificado SSL

Creamos una clave privada que utilizaremos para crear la solicitud de certificado. 

    ::::bash
    openssl genrsa -out my-private-key-file.pem 2048

Creamos la solicitud de firma del certificado: Certificate Signing Request (CSR). La solicitud no es más que un fichero creado a partir de la clave privada que utilizaremos para solicitar un certificado [X.509](http://en.wikipedia.org/wiki/X.509) a la autoridad certificadora.

    ::::bash
    openssl req -sha256 -new -key my-private-key-file.pem -out csr.pem

Este proceso nos realizará un una serie de preguntas. Hemos de prestar especial atención al valor que introducimos para:

  + Common Name

Nos aseguraremos de que corresponda con el [FQDN](http://en.wikipedia.org/wiki/Fully_qualified_domain_name) que vamos a utilizar para nuestro dominio.

Verificamos que la información que hemos introducido es correcta:

    ::::bash
    openssl req -in csr.pem -noout -text

Con el fichero `csr.pem`  generado, solicitamos el certificado a nuestra CA. GoDaddy en este caso.


## 2 Convertir el certificado al formato soportado por Amazon

La CA nos retorna el certificado en dos ficheros con nombres similares a estos:

Goodady files: `a0cde33bcde324cd.crt` + `gd_bundle-g2-g1.crt`

El primer fichero es nuestro certificado. El segundo la certificate chain: una lista de certificados y el certificado raiz de Godaddy.

Amazon requiere que estos fichero estén en un formato soportado por el servicio AWS IAM. Así que deberemos convertir el certificado al formato soportado: PEM X.509 en este caso.

    ::::bash
    openssl x509 -inform PEM -in a0cde33bcde324cd.crt > my-public-key-file.pem
    openssl x509 -inform PEM -in gd_bundle-g2-g1.crt > my-certificate-chain-file.pem 


## 3 Subir el certificado a Amazon
Ahora, con estos tres ficheros: La clave privada, nuestro certificado y los certificados de Goodady, podemos dar de alta el certificado en Amazon.

    ::::bash
    iMac: frommelmak$ aws iam upload-server-certificate --server-certificate-name my-server-certificate --certificate-body file://my-public-key-file.pem --private-key file://my-private-key-file.pem --certificate-chain file://my-certificate-chain-file.pem
    {
        "ServerCertificateMetadata": {
            "ServerCertificateId": "ASC...............JJJ",
            "ServerCertificateName": "my-server-certificate",
            "Expiration": "2016-02-25T15:27:49Z",
            "Path": "/",
            "Arn": "arn:aws:iam::765165175371:server-certificate/my-server-certificate",
            "UploadDate": "2015-02-26T12:27:59.876Z"
        }
    }

Mediante el siguiente comando, verificamos que se ha subido correctamente:

    ::::bash
    iMac: frommelmak$ aws iam get-server-certificate --server-certificate-name my-server-certificate
    {
            "ServerCertificate": {
            "CertificateChain": "-----BEGIN CERTIFICATE-----\nMI ... JCa\n-----END CERTIFICATE-----",
            "CertificateBody": "-----BEGIN CERTIFICATE-----\nMI ... kkd\n-----END CERTIFICATE-----",
            "ServerCertificateMetadata": {
                "ServerCertificateId": "ASC...............JJJ",
                "ServerCertificateName": "my-server-certificate",
                "Expiration": "2016-02-25T15:27:49Z",
                "Path": "/",
                "Arn": "arn:aws:iam::76........71:server-certificate/my-server-certificate",
                "UploadDate": "2015-02-26T12:27:59Z"
            }
        }
    }


## 4 Añadir listener HTTPS al balanceador y configurarlo con el nuevo certificado.

Ahora ya sólo tenemos que añadir un nuevo Listener mediante la consola de Amazon.

En "Listener Configuration" del load balancer seleccionamos:

  + Load Balancer Protocol: HTTPS(Secure HTTP)
  + Load Balancer Port: 443
  + Instance Protocol: 80
  + Instance Port: 80

En el momento de seleccionar el certificado utilizaremos la opción: "Choose an existing SSL Certificate". Veremos que ya aparece el que acabamos de publicar.

  + info: [Elastic Load Balancing: SSL Server Cert](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/ssl-server-cert.html)
