# CatPhish

## Project Description
A Flask based web app to help people verify authenticity of urls sent to them. 

## Project Objective
   Built on Flask, The concept is to take a input URL from the user, run it through who.is, then to find out if the 
registration matches who the sender claims it to be by asking the user who they think the email or text message with the 
potential phish is from.  
</br>
   Initially I intended for this project to be based on Django, however after some experimentation realised that Flask would
be far more suitable for what will eventually be a single page website, allowing the user to input just a url and type 
in whom they think sent them the URL.  
</br>
   The idea for this project was born from friends and relatives forwarding me emails or text messages in a panic
thinking that their details had been compromised, in some cases they had already filled in their details and had their 
login details phished before realising it was a scam, me and Atib wanted a way to quickly and easily verify potential
phishing scams. For someone technical, it's easy to spot a phishing scam, or at least it used to be, however these scammers
are becoming ever more resourceful and for non technical people it isn't always easy to spot a scam.  
</br>
   The way I have approached this problem is to check who the url is registered to, in our small sample size of scam URLs
we found a few common occurrences:
1. for headers and title pages most scams use images. My theory is this is to avoid google being able to accurately crawl them.
2. the who.is registration is almost always privatised. For Obvious reasons. My reason for checking the who.is registration is that I see no legitimate reason for a legitimate company to privatise their domain registration
3. they use a subdomain or many subdomains to pose as the company they are impersonating, this usually hides the actual domain they are using in the address bar
</br>
I acknowledge this is probably not the most ideal solution, and my intention is to build in many more factors to authenticate against in the future.

## Contributors
[Anayat Chowdhury](https://github.com/Anayatc) - Backend  
[Atib Chowdhury](https://github.com/atib) - Frontend

## Stack Elements:
1. Python 3.6
2. Imports: python-whois; requests, urllib.parse
3. Flask
4. Bootstrap - frontend
5. Javascript
6. CSS

## Testing
py.test - to test the script in it's ability to follow short urls to their destination, to test stripping the url of subdomains and other infromation to return just the domain name, to test the what the who.is look up returns

## How to Run
1. install Python 3.6
2. pip install, python-whois, requests, flask,  `pip install python-whois`, `pip install requests`, `pip install flask`
3. clone repository
4. cd to location of clone
5. run main.py in python shell
6. application should run on local host port 5000

## Bugs
As this is still a work in progress in it's early stages I will update this section as the project nears a more complete stage. 