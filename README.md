# Elektro Inženjer PRO ⚡

Elektro Inženjer PRO je moćna web aplikacija bazirana na Flask framework-u, dizajnirana da olakša svakodnevne inženjerske proračune. Namenjena je profesionalcima, studentima i hobistima u oblastima elektrotehnike, automatike i robotike.

🚀 Karakteristike

Aplikacija je podeljena na specijalizovane module za preciznu analizu:

⚡ Elektro: Brzi proračun struje, otpora trošila i pada napona u kablovima (monofazni i trofazni sistemi).

⚙️ Motori: Detaljna analiza motornog pogona, preporuka adekvatnih kontaktora, podešavanje bimetalne zaštite i proračun momenta na vratilu.

🤖 Automatika: Skaliranje industrijskih signala (4-20mA), analiza PT100 temperaturnih senzora i preporuke za PID tuning (Ziegler-Nichols).

🔋 Kompenzacija: Proračun potrebne jalove snage (kVAr) za popravku faktora snage (cos φ) i dimenzionisanje opreme.

☀️ Solar: Projektovanje solarnih sistema – određivanje broja panela, snage invertora i kapaciteta baterija za off-grid sisteme.

🦾 Robotika: Proračun statičkog i dinamičkog momenta robotske ruke na osnovu mase tereta i kraka.

🛠️ Instalacija i Pokretanje

Pratite ove korake kako biste podesili lokalno razvojno okruženje:

1. Kloniranje projekta

Prvo, preuzmite kod sa GitHub-a:

git clone https://github.com/grujo85/elektro-inzenjer-pro.git
cd elektro-inzenjer-pro


2. Podešavanje virtuelnog okruženja

Preporučuje se korišćenje venv kako biste izolovali biblioteke:

# Kreiranje okruženja
python3 -m venv venv

# Aktivacija (Linux/macOS)
source venv/bin/activate

# Aktivacija (Windows)
# venv\Scripts\activate


3. Instalacija zavisnosti

Instalirajte sve potrebne pakete jednim klikom:

pip install -r requirements.txt


4. Pokretanje aplikacije

Pokrenite Flask server:

python3 app.py


Nakon pokretanja, aplikaciji možete pristupiti putem pretraživača na adresi:
👉 http://localhost:8501

Napomena: Aplikacija je optimizovana za rad na portu 8501. Ukoliko želite da je koristite u lokalnoj mreži, konfiguracija je već podešena na 0.0.0.0.
