Ed's Godaddy DNS Updater
========================

This program is intended to replace third party dynamic dns for people
who have a Godaddy domain. It updates one host in your Godaddy DNS
to point to your outside IPv4 address if it differs.

Usage
-----

To use this, just copy conf.py.example to conf.py then edit conf.py following
the simple directions. You will need to go to https://developer.godaddy.com to
make an API production key/secret that you then fill in to the conf.py file.

You'll probably want to symlink update_godaddy_dns.py in your /etc/cron.hourly/
folder to have this check and update hourly. *NOTE: Symlinks in cron.hourly
won't run if they have a '.' in them, so make sure the link doesn't have '.py'
on the end.*

Enjoy!

License
-------

This software was written by Edward Flick (directrix1 -=at=- gmail -=dot=- com)
in 2016, and is released under the GPLv2 license.
