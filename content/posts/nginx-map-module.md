Title: Nginx's map module to deal with real life problems
Date: 2019-09-25 19:38:00
Category: English 
Tags: nginx, logs
Author: frommelmak

I'll try to show you how to use nginx's log and map modules to put different header values from the http requests into the same place in the log files.

Imagine you have two kind of http request. One provides some info in an optional http header (like referer), since the other put the same info in a custom header (like client).

curl --referer client-xxx http://someserver/some_resource
curl --header "client: client-xxx" http://someserver/someresource

Nginx sets incoming headers to variables so you can use $http_referer and $http_client in the log_format definition

```
log_format my_format '$msec|$bytes_sent|$http_referer|$remote_addr|$uri';
```

or

```
log_format my_format '$msec|$bytes_sent|$http_client|$remote_addr|$uri';
```

But, what if you want to use the referer header for requests whose include it and client one for the rest ?

I mean: What if If you want to put the "client" value in the logs always in the same position regardless where the request came from ? 

Since the info comes from different varialbes: $http_referer and $http_client, you can't use it in the same position in the log_format definition. But no worries, this is where the Nginx's "map" module comes to the rescue.

The map module allows you to asign conditional values to a new custom variable. Something like this:

```
map $http_referer $new_var {
  string_pattern1 value1;
  string_pattern2 value2;
  regexp1 value3;
  regexp2 value4;
  default value5;
}
```

Values can be setted using an existing var, so you can do something like this:

```
  map $http_referer $client {
    ~^client-* $http_referer;
    default $http_client;
  }
```

log_format my_format '$msec|$bytes_sent|$client|$remote_addr|$uri';

If the referer exists and starts with the pattern "client-", then the value is assigned to a new var called $client if not, the client header will be used as the value of the new $client var.

The new $client var will be used in our log_format definition.

Beatifull and powerfull right ?
