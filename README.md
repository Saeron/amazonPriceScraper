# amzonPriceScraper
Automation for check the price of a Amazon item.

#Requirements
This program is using b24, html5lib and 
request as a external packages, 
that means that you'll have to 
install those:

<code>pip3 install request bs4 html5lib</code>

If you don't have pip installed you'll
have to search the way of install
on your system.

Also this script is running on 
python 3, more exactly was made
whit python 3.6.3, you can find
it here : https://www.python.org/

**Notes:** Some times is need it
to add the path of the external
packages. In other to do that:

<ol>
    <li>Open python in cmd (type <code>python</code> python> and press enter)</li>
    <li>Import the module in cmd (type <code>import modulename</code>)</li>
    <li>Type <code>modulename.__file__</code></li>
    <li>You will get the path where the module is stored</li>
    <li>Copy the corresponding folder</li>
    <li>In IDLE, <code>import sys</code> and typing <code>sys.path.append("/home/dm/.local/lib/python3.6/site-packages")</code> to add the paths where it looks for modules to import</li>
</ol>

# How this works

First you'll need to set up your's
preferences:

URL: Just copy here the URLS from
object to check, you don't have
to copy the <code>qid</code> part.

my_email: The email you are goin to
use for notifications.

password: The password of your email,
but in this case i suggest you use
an additional on, i order to do that
( gmail case ), first you need to
activate the 2 steps verification.
Then you can go to https://myaccount.google.com/apppasswords
and create a new password application.

my_price: The offer you want to
check for.


Finally you only have run the
script: <code>python3 amazonScraper.py</code>

**Notes:** The time to re-check
is set to 24h so it does not make
problems, but some time amazon can
block you. Yo can change the user-agent 
on <code>headers</code>, find somes
on google: user agent.
