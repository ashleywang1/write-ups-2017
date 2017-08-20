# picoCTF 2017 : lazy-dev-50

**Category:** Master
**Points:** 50
**Solves:** 
**Description:**

> I really need to login to this website, but the developer hasn't implemented login yet. Can you help?
> 
> 
>  HINTS
> 
> Where does the password check actually occur?
> 
> Can you interact with the javascript directly?


## Write-up

One of the first things you do during almost all Web Exploid problems is go to the console and look at the html.

```
<body>
    <h1>Enter the password</h1>
    <input id="password">
    <button type="button" onclick="process_password()">Submit</button>
    <p id="res"></p>
<script type="text/javascript" src="/static/client.js"></script>
</body>
```

The **process_password** function looks interesting, so it'd be nice to know more about it. Sometimes, (especially for low-effort websites like this), developers make their functions globally readable. This means you can access it in the console. So, typing ```process_password``` in the console results in:


```
ƒ process_password(){
  var pword = document.getElementById("password").value;
  var res = validate(pword);
  var server_res = make_ajax_req(res);
}
```

Typing ```validate``` in the console results in:

```
ƒ validate(pword){
  //TODO: Implement me
  return false;
}
```

One thing I forgot to mention - if these functions are globally readable, then they are *also globally writable*. We can rewrite the ```validate``` function with

```
validate = function(pword){
  return true;
}
```

With this, we can just press **submit**, and we'll get the flag.

FLAG: ```client_side_is_the_dark_side6295c70148b5939179f1d1b6b70fb0c7```

## Other write-ups and resources

* none yet
