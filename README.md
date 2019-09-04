# Item Catalog
Readme broken into two parts.  
[Part 1](#production-server) includes production server information.  
[Part 2](#project) includes information specifically pertaining to this Item Catalog project itself.  

# Production Server
## Connection Information
### For Udacity Grader
#### Information

*URL* http://dev.leafsoj.com

Using tmux to run detatched `uwsgi --ini /home/ubuntu/projects/Item-Catalog/flaskproject.ini`  
Use `tmux -S /tmp/shareds attach -t shared -r` to view shared multiplexer session. Learn more at https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/  
Shared session learend from: https://www.howtoforge.com/sharing-terminal-sessions-with-tmux-and-screen  
  
DNS: dev.leafsoj.com  
IP Address: 34.214.24.34  
SSH Port: 2200  
Username Provided: "grader"  

#### Instructions To Connect
1. Follow special instructions provided in "Extra Notes" section of project submission
2. Connect with following command:
```sh
ssh -i "grader_rsa" -p 2200 grader@dev.leafsoj.com
```

### For all others
Contact me at directly via my email and I can create a user for you

## Server Configurations
* Added `dev.leafsoj.com` to validated domains in google console with TXT record
* Generated Static IP and associated with AWS Route 53 DNS A record
* Added nginx list: `sudo add-apt-repository ppa:nginx/stable`
* Installed nginx: `sudo apt-get install nginx`
* Installed dependencies: `sudo apt-get install libpq-dev python-dev`
* Install uWSGI for nginx: `pip install uwsgi`
* Followed nginx wsgi tutorial: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04#step-6-%E2%80%94-configuring-nginx-to-proxy-requests
* Fixed errors from previous tutorial being outdated - [see here](#uwsgi-and-nginx-configurations)
* Created uWSGI & nginx configurations (See `/var/www/flaskapp/` and `/home/ubuntu/projects/Item-Catalog/flaskproject.ini`)
* Start nginx: `sudo /etc/init.d/nginx start`
* Root user disabled via nologin shell in `/etc/passwd`
* UFW ubuntu firewall enabled
* UFW allows all outgoing and denies all incoming with following exceptions:
    * UFW allows 2200/tcp incoming (v4 & v6)
    * UFW allows 123/udp incoming (v4 & v6)
    * UFW allows 80/tcp incoming (v4 & v6)
* /etc/ssh/sshd_config modified as follows:
    * SSH port set to 2200 (instead of 22)
* Lightsail dashboard firewall settings changed as follows:
    * AWS firewall allows custom ports 2200 TCP and 123 UDP
    * Default settings already allowed port 80 - left alone
* User "grader" added
    * `.ssh` folder added to grader's home directory
    * RSA public key added to grader's `authorized_keys` file
    * grader added to "sudo" group
    * grader settings file added to `sudoers.d`
* `/etc/nologin.txt` added to give explicit message for failed login
* Package lists and packages themselves updated
* `Finger` and `chef-local` installed

See `/home/ubuntu/.bash_history` for more details

# Project
## Project Installation and Setup
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
 $ source ./init.sh
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

## References Used

* Safe filter for passing JSON in render templates: https://www.pythonanywhere.com/forums/topic/1627/
* Google Signout: https://developers.google.com/identity/sign-in/web/sign-in#before_you_begin
* Alternative Signin to get around `googleUser.getBasicProfile()` not working: https://stackoverflow.com/questions/31331428/how-to-call-getbasicprofile-of-google-to-google-signin-on-only-button-click
* Isoformat method for datetime serialization: https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
* APIRoutes uses `make_response` instead of abort with arguments due to error listed in this link with solution: https://stackoverflow.com/questions/41319058/typeerror-response-36-bytes-200-ok-is-not-json-serializable
* Fixing signout not fully disconnecting (in navbar.html): https://stackoverflow.com/questions/34515499/google-api-auth2-signout-not-working
* Disable root user: https://www.tecmint.com/disable-root-login-in-linux/
* psycop error fixed by installing dependencies: `sudo apt-get install libpq-dev python-dev` from: https://stackoverflow.com/questions/11618898/pg-config-executable-not-found

#### uWSGI and nginx configurations

* Tutorial 1 - almost worked but was for Ubuntu 13.04: https://vladikk.com/2013/09/12/serving-flask-with-nginx-on-ubuntu/
* Docs for uWSGI to debug (no useful information): https://uwsgi-docs.readthedocs.io/en/latest/PythonModule.html
* Tutorial 1 configuration fix which failed: https://serverfault.com/questions/775965/wiring-uwsgi-to-work-with-django-and-nginx-on-ubuntu-16-04
* Tutorial 2 which failed: https://www.gab.lc/articles/flask-nginx-uwsgi/
* Not loading error which lead to modification of app.py to not wrap everything inside name = main check: https://stackoverflow.com/questions/12030809/flask-and-uwsgi-unable-to-load-app-0-mountpoint-callable-not-found-or-im
* Permissions error which lead to .sock file chmod 660 to 666 fix: https://stackoverflow.com/questions/23948527/13-permission-denied-while-connecting-to-upstreamnginx
* Tutorial 3: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04#step-6-%E2%80%94-configuring-nginx-to-proxy-requests

And many MANY other stackoverflows etc.

## Notes:
* `# noqa` added to comments with urls that go over 79 character limit for ease of access
* Also, for ease of testing - here is a quick reference to one of the links for the JSON routes:
http://localhost:5001/categories/2/listing/JSON

## Todo:
1. Refactor navbar - seperate the *actual* navbar portion from common modules such as signout.
1. When signing out from within a safe page, don't push toaster notification of not being allowed on that page.

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
