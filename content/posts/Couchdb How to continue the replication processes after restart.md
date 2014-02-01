Title: Couchdb: How to continue the replication processes after restart
Date: 2012-08-30 12:58:45
Category: English
Tags: couchdb
Author: frommelmak

As you probably know, the replication in couchdb is triggered by sending a JSON doc to the `_replicate` URL using a POST request. Something like that:

    :::console
    curl -X POST http://localhost:5984/_replicate -d '{source:http://src_ip:5984/src_db, target:dst_db, continuous:true}' -H 'Content-Type: application/json'

The problem using this approach is that the replication process does not continue after a CouchDB restart. Since CouchDB 1.1.0, you can use the `_replicator` database to ensure that the replication processes are triggered again after a service restart. Just fill up the `_replicator` database with a documment defining the replication process in the same way that you did using the `_replicate` API.

    :::console
    curl -X POST -d '{source:http://src_ip:5984/source_db, target:dst_db, continuous:true}' -H 'Content-Type: application/json' http://localhost:5984/_replicator

Now you don't need to worry about the replication processes after a service restart.

more info: [http://wiki.apache.org/couchdb/Replication](http://wiki.apache.org/couchdb/Replication)
