source .env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
API_URL=https://randia-production.up.railway.app reflex export --frontend-only
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate