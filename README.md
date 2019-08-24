# Item Catalog

* Description of project

## Installation and Setup
Prerequisites:  
Ensure the following applications are accessible from your PATH variable  
1. First you'll need VirtualBox installed on your machine. Find your operating system and install [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
2. Next you'll need to install [Vagrant](https://www.vagrantup.com/downloads.html)

Next, run these commands in your terminal:  

```sh
 $ git clone https://github.com/udacity/fullstack-nanodegree-vm.git
 $ cd fullstack-nanodegree-vm/vagrant
 $ vagrant up
```

`vagrant up` may take awhile to download. Wait until it is done before continuing  
this project is made for python 2.7 -- the vagrant instance will have python 2.7 preinstalled  
for development on your local machine you can install python 2.7.16 [here](https://www.python.org/downloads/release/python-2716/)  
  
Continue running the following commands:  
  
```sh
 $ vagrant ssh
 $ git clone https://github.com/lumodon/item-catalog.git /vagrant/lumodon-catalog
 $ cd $_
 $ ./init.sh
```

*Setup Static Assets*  
1. Follow directions provided in email / project submission notes for static assets  

Finally run the application:  
  
```sh
 $ python app.py
```

Don't forget to try the JSON route which doesn't have any hyperlinks for standard users  
For example:  
`http://localhost:5001/categories/4/listing/JSON`  

## Architecture

`app.py` is the starting point for the app  

## References Useds

* Safe filter for passing JSON in render templates: https://www.pythonanywhere.com/forums/topic/1627/
* Google Signout: https://developers.google.com/identity/sign-in/web/sign-in#before_you_begin
* Alternative Signin to get around `googleUser.getBasicProfile()` not working: https://stackoverflow.com/questions/31331428/how-to-call-getbasicprofile-of-google-to-google-signin-on-only-button-click
* Isoformat method for datetime serialization: https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable

## Notes:
* `# noqa` added to comments with urls that go over 79 character limit for ease of access
* Also, for ease of testing - here is a quick reference to one of the links for the JSON routes:
http://localhost:5001/categories/2/listing/JSON

## License

This is free and unencumbered software released into the public domain.  
  
Anyone is free to copy, modify, publish, use, compile, sell, or  
distribute this software, either in source code form or as a compiled  
binary, for any purpose, commercial or non-commercial, and by any  
means.  
  
In jurisdictions that recognize copyright laws, the author or authors  
of this software dedicate any and all copyright interest in the  
software to the public domain. We make this dedication for the benefit  
of the public at large and to the detriment of our heirs and  
successors. We intend this dedication to be an overt act of  
relinquishment in perpetuity of all present and future rights to this  
software under copyright law.  
  
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,  
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF  
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR  
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,  
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR  
OTHER DEALINGS IN THE SOFTWARE.  
  
For more information, please refer to <http://unlicense.org/>  
