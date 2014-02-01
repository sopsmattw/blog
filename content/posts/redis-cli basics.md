Title: redis-cli basics
Date: 2011-07-22 13:49:08
Category: Spanish
Tags: redis, nosql
Author: frommelmak

Redis es un servidor de datos Nosql (clave-valor) en memoria similar  a memcached. Redis puede almacenar -además de cadenas de texto-  estructuras ms complejas como: hashes, lists, sets u sorted sets. Es capaz de realizar diferentes tipos de operaciones atómicas sobre estas estructuras de datos, disponer de persistencia (pese a trabajar en memoria), replicación, y otras características que están haciendo que redis se utilice cada vez en mas [proyectos](http://redis.io/topics/whos-using-redis).

En esta entrada, vamos a ver los 4 conceptos básicos que hay que  tener en cuenta a la hora de trabajar con la lnea de comandos de redis  para la administracin de este servicio.

**Keys**: Redis utiliza cadenas para las keys. éstas no pueden contener espacios en blanco ni saltos de carro.

##Tipos de datos

  * **strings**: Cadena de texto.
  * **listas**: lista de elementos (*values*) ordenados.
  * **sets**: como una lista sólo que los elementos (*members*) no están ordenados. A diferencia de las listas, no se puede contener elementos duplicados.
  * **sorted sets**: igual que un set normal pero cada elemento dispone de un indice que se utiliza para ordenar los elementos.

Redis dispone de una útil lnea de comandos que nos ayudará a debugar nuestra aplicación y/o entender qué esta pasando en el servidor redis. Desde la lnea de comandos podremos ejecutar todos los comandos que soporta redis. Estos comandos puden agruparse por el tipo de datos sobre el que trabajan. A continuación muestro algunos ejemplos de comandos.

##Comandos sobre keys

`KEYS pattern`

  * Mostrar todas las keys almacenadas: `keys *`
  * Mostrar todas las keys con un patron determinado: `keys pattern`

`EXPIRE key seconds`
    
  * Expirar una clave en 5 segundos: `EXPIRE articulo_234 5`
    

##Comandos sobre stirngs

`SET key value`

  * Establecer una calve y su correspondiente valor: `SET articulo_234 Samsung`

`APPEND key value`

  * Añadir algo al valor de la key anterior: `APPEND articulo_234  Galaxy S I`
    

`GET key`

  * Obtener el valor de una clave determinada: `GET articulo_234`

##Comandos sobre listas

`RPUSH key value`

  * Añade un elemento al final de la lista: `RPUSH mi_lista elemento1`

`LPUSH key value` 

  * Añade un elemento al prinpicio de la lista: `LPUSH mi_lista elemento5`

`LRANGE key start stop`

  * Mostrar todos los 3 primeros items de una lista: `LRANGE mi_lista 0 2`
  * Mostrar todos los items de una lista: `LRANGE mi_lista 0 -1`

`LLEN key`

  * Mostrar el nmero de elementos de una lista: `LLEN mi_lista`

##Comandos sobre sets:

`SADD key member`

 * Añadir un elemento a un set: `SADD mi_set leche desnatada`

`SMEMBERS key`

 * Mostrar los elementos de un set: `SMEMBERS mi_set`

`SCARD key`

 * Mostrar el número de elementos de un set: `SCARD mi_set`

##Comandos sobre sorted sets

`ZADD key score member`

  * Añadir elemento (*member*) a un sorted set: `ZADD mi_stored_set 3 natillas danone`

`ZRANGE key start stop`

  * Mostrar todos los members de un sorted set: `ZRANGE 628srv_log 0 -1`

##Otros comandos

  * `SELECT db`: Cambia la base de datos de la sesion actual
  * `DBSIZE`: restorna en numero de keys de la bbdd actual
  * `MONITOR`: Muestra en timpo real todas las peticions que entran a la base de datos.
  * `IINFO`: Muestra estadsticas sobre el servidor redis.

+info:

[http://redis.io/commands]()

[http://redis.io/topics/data-types-intro]()

[http://try.redis-db.com/]()
