## Reddit's /r/Entrepreneur top 10 of the week

### How to get started

Create and fill mail.conf

    cp template_mail.conf mail.conf

Create a virtualenv and install dependencies

    virtualenv .
    source bin/activate
    pip install -r requirements.txt


Launch the script

    python main.py

If it doesn't work, try changing the "Access for less secure apps" to Enabled (it was enabled, change it to disabled and than back to enabled) : https://myaccount.google.com/security