from flask import Flask, render_template_string, request
import math

app = Flask(__name__)

HTML_SABLON = """
<!DOCTYPE html>
<html>
<head>
    <title>Elektro Inženjer PRO</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; margin: 0; padding: 20px; color: #333; }
        .main-container { max-width: 1000px; margin: auto; background: white; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); overflow: hidden; }
        
        /* Navigacija sa tabovima */
        .tabs { display: flex; background: #2c3e50; padding: 10px 10px 0 10px; gap: 5px; flex-wrap: wrap; }
        .tab-btn { padding: 12px 18px; border: none; background: #34495e; color: #bdc3c7; cursor: pointer; border-radius: 8px 8px 0 0; font-weight: bold; transition: 0.3s; text-decoration: none; font-size: 0.9em; }
        .tab-btn.active { background: #f0f2f5; color: #2c3e50; }
        .tab-btn:hover { background: #485e74; color: white; }

        .content { padding: 30px; }
        h2 { margin-top: 0; color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        label { font-weight: bold; display: block; margin-top: 15px; font-size: 0.85em; }
        input, select { width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; }
        
        button { width: 100%; padding: 14px; margin-top: 25px; border: none; border-radius: 6px; color: white; font-weight: bold; cursor: pointer; font-size: 1em; transition: 0.2s; }
        .btn-blue { background: #2980b9; }
        .btn-red { background: #e74c3c; }
        .btn-purple { background: #9b59b6; }
        .btn-green { background: #27ae60; }
        .btn-orange { background: #f39c12; }
        .btn-teal { background: #16a085; }

        /* Novi stil za rezultate - Bela pozadina */
        .res-box { 
            background: #ffffff; 
            color: #2c3e50; 
            border: 1px solid #dcdde1;
            border-left: 10px solid #2980b9; /* Plava linija za naglasak */
            padding: 20px; 
            margin-top: 25px; 
            border-radius: 8px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }

        .res-line { 
            border-bottom: 1px solid #f1f2f6; 
            padding: 10px 0; 
            display: flex; 
            justify-content: space-between; 
            align-items: center;
        }

        .res-val { 
            font-weight: 800; 
            color: #9b59b6;; 
            font-family: 'Consolas', monospace; /* Vrednosti ostaju u 'kod' stilu radi preglednosti */
            font-size: 1.1em;
        }

        .res-box h3 {
            margin-top: 0;
            color: #2980b9;
            font-size: 1.2em;
            border-bottom: 2px solid #f1f2f6;
            padding-bottom: 10px;
        }
        .res-val.warning {color: #f39c12;text-decoration: underline; }
        .res-box { background: #1e1e1e; color: #00ff00; border-left: 10px solid #9b59b6; padding: 20px; font-family: 'Consolas', monospace; box-shadow: inset 0 0 10px #000;}
        .error { color: #c0392b; font-weight: bold; }
    </style>
</head>
<body>
<div class="main-container">
    <div class="tabs">
        <a href="/?tab=elektro" class="tab-btn {{ 'active' if tab == 'elektro' else '' }}">⚡ Elektro</a>
        <a href="/?tab=motor" class="tab-btn {{ 'active' if tab == 'motor' else '' }}">⚙️ Motori</a>
        <a href="/?tab=auto" class="tab-btn {{ 'active' if tab == 'auto' else '' }}">🤖 Automatika</a>
        <a href="/?tab=komp" class="tab-btn {{ 'active' if tab == 'komp' else '' }}">🔋 Baterije</a>
        <a href="/?tab=solar" class="tab-btn {{ 'active' if tab == 'solar' else '' }}">☀️ Solar</a>
        <a href="/?tab=robot" class="tab-btn {{ 'active' if tab == 'robot' else '' }}">🦾 Robotika</a>
    </div>

    <div class="content">
        {% if tab == 'elektro' %}
        <h2>⚡ Elektro: Snaga, Otpor i Vod</h2>
        <form method="POST"><input type="hidden" name="tab" value="elektro">
            <div class="grid">
                <div>
                    <label>Napon U (V):</label>
                    <select name="u">
                        <option value="400">400V (Trofazni)</option>
                        <option value="230">230V (Monofazni)</option>
                    </select>
                    <label>Snaga P (W):</label>
                    <input type="number" name="p" placeholder="Unesi snagu trošila">
                </div>
                <div>
                    <label>Dužina kabla L (m):</label>
                    <input type="number" name="l" step="0.1" value="10">
                    <label>Presek kabla S (mm²):</label>
                    <input type="number" name="s" step="0.1" value="2.5">
                </div>
            </div>
            <button type="submit" class="btn-blue">Izračunaj parametre</button>
        </form>

        {% elif tab == 'motor' %}
        <h2>⚙️ Detaljan Proračun Motornog Pogona</h2>
        <form method="POST"><input type="hidden" name="tab" value="motor">
            <div class="grid">
                <div>
                    <label>Snaga P (kW):</label><input type="number" name="m_kw" step="0.01" value="7.5">
                    <label>Napon U (V):</label>
                    <select name="m_u"><option value="400">400V (3~)</option><option value="230">230V (1~)</option></select>
                    <label>Obrtaji (RPM):</label><input type="number" name="m_rpm" value="1450">
                </div>
                <div>
                    <label>cos φ:</label><input type="number" name="m_cos" step="0.01" value="0.85">
                    <label>Efikasnost (η):</label><input type="number" name="m_eff" step="0.01" value="0.88">
                    <label>Start:</label>
                    <select name="m_start"><option value="dol">Direktno</option><option value="yd">Y-Δ</option><option value="vfd">VFD</option></select>
                </div>
            </div>
            <button type="submit" class="btn-red">Analiziraj Pogon</button>
        </form>

        {% elif tab == 'auto' %}
        <h2>🤖 Automatika (4-20mA & PT100)</h2>
        <form method="POST"><input type="hidden" name="tab" value="auto">
            <label>Tip signala:</label>
            <select name="a_tip"><option value="ma">Skaliranje 4-20mA</option><option value="pt100">PT100 Senzor</option></select>
            <label>Ulaz (mA ili Ω):</label><input type="number" name="a_val" step="0.001">
            <label>Opseg merenja (Min / Max):</label>
            <div class="grid">
                <input type="number" name="a_min" placeholder="npr. 0 bar">
                <input type="number" name="a_max" placeholder="npr. 16 bar">
            </div>
            <button type="submit" class="btn-purple">Izvrši Skaliranje</button>
        </form>

        {% elif tab == 'komp' %}
        <h2>🔋 Kapacitivne Baterije (kVAr)</h2>
        <form method="POST"><input type="hidden" name="tab" value="komp">
            <label>Snaga P (kW):</label><input type="number" name="k_p" step="0.1">
            <div class="grid">
                <div><label>Trenutni cos φ:</label><input type="number" name="k_c1" step="0.01" value="0.75"></div>
                <div><label>Ciljani cos φ:</label><input type="number" name="k_c2" step="0.01" value="0.95"></div>
            </div>
            <button type="submit" class="btn-teal">Proračunaj Kompenzaciju</button>
        </form>

        {% elif tab == 'solar' %}
        <h2>☀️ Solarni Sistemi</h2>
        <form method="POST"><input type="hidden" name="tab" value="solar">
            <label>Dnevna energija (kWh):</label><input type="number" name="s_kwh" step="0.1">
            <label>Snaga jednog panela (W):</label><input type="number" name="s_w" value="450">
            <button type="submit" class="btn-orange">Proračunaj Sistem</button>
        </form>

        {% elif tab == 'robot' %}
        <h2>🦾 Robotika i Mehanika</h2>
        <form method="POST"><input type="hidden" name="tab" value="robot">
            <label>Masa tereta (kg):</label><input type="number" name="r_kg">
            <label>Dužina kraka ruke (m):</label><input type="number" name="r_m" step="0.01">
            <button type="submit" class="btn-green">Izračunaj Moment</button>
        </form>
        {% endif %}

        {% if res %}
        <div class="res-box">
            <h3>📊 Rezultati:</h3>
            {% for k, v in res.items() %}
            <div class="res-line"><span>{{ k }}</span> <span class="res-val">{{ v }}</span></div>
            {% endfor %}
        </div>
        {% endif %}
    </div>
</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    tab = request.args.get('tab', 'elektro')
    res = None
    if request.method == 'POST':
        tab = request.form.get('tab')
        try:
            if tab == 'elektro':
                # Dobijanje podataka iz forme
                u_str = request.form.get('u') or "400"
                u = float(u_str)
                p = float(request.form.get('p') or 0)
                l = float(request.form.get('l') or 1)
                s = float(request.form.get('s') or 2.5)
                
                rho = 0.0175 # Bakar
                cos_phi = 0.9
                
                # 1. Proračun struje (I)
                if u > 300: # Trofazni
                    i = p / (u * 1.732 * cos_phi) if p > 0 else 0
                    du_v = (1.732 * l * i * cos_phi * rho) / s
                else: # Monofazni
                    i = p / (u * cos_phi) if p > 0 else 0
                    du_v = (2 * l * i * cos_phi * rho) / s
                
                # 2. DODATO: Proračun OTPORA (R)
                # Otpor trošila (npr. grejača) na radnoj temperaturi
                r_trosila = (u**2 / p) if p > 0 else 0
                
                # Otpor same linije (kabla)
                r_kabla = (rho * l * 2 / s) if u < 300 else (rho * l / s)
                
                du_procent = (du_v / u) * 100

                res = {
                    "Struja (I)": f"{round(i, 2)} A",
                    "OTPOR TROŠILA (R)": f"{round(r_trosila, 2)} Ω",
                    "Otpor voda (R_line)": f"{round(r_kabla, 4)} Ω",
                    "Pad napona": f"{round(du_v, 2)} V ({round(du_procent, 2)} %)",
                    "Status": "✅ OK" if du_procent < 3 else "⚠️ PAD > 3%" if du_procent < 5 else "❌ KRITIČNO"
                }
                
                # Pronađi deo koda gde se računa 'motor' i zameni ga ovim:

            elif tab == 'motor':
                p_kw = float(request.form.get('m_kw') or 0)
                u = float(request.form.get('m_u'))
                rpm = float(request.form.get('m_rpm') or 1)
                cos = float(request.form.get('m_cos') or 0.85)
                eff = float(request.form.get('m_eff') or 0.85)
                start = request.form.get('m_start')

                # Proračun nazivne struje
                i_n = (p_kw*1000)/(1.732*u*cos*eff) if u == 400 else (p_kw*1000)/(u*cos*eff)
                i_st = i_n * (6.0 if start == 'dol' else (2.0 if start == 'yd' else 1.2))
                
                # Izbor kontaktora (AC-3 standard)
                # Uzimamo sigurnosni faktor 1.25x za dugovečnost kontakata
                kontaktor_struja = i_n * 1.25
                if kontaktor_struja <= 9: k_tip = "9A (npr. LC1D09)"
                elif kontaktor_struja <= 12: k_tip = "12A (npr. LC1D12)"
                elif kontaktor_struja <= 18: k_tip = "18A (npr. LC1D18)"
                elif kontaktor_struja <= 25: k_tip = "25A (npr. LC1D25)"
                elif kontaktor_struja <= 32: k_tip = "32A (npr. LC1D32)"
                elif kontaktor_struja <= 40: k_tip = "40A (npr. LC1D40)"
                elif kontaktor_struja <= 65: k_tip = "65A (npr. LC1D65)"
                else: k_tip = f"{math.ceil(kontaktor_struja)}A Industrijska serija"

                res = {
                    "Nazivna struja (In)": f"{round(i_n,2)} A",
                    "Polazna struja (Istart)": f"{round(i_st,2)} A",
                    "Podešavanje bimetala": f"{round(i_n * 1.05, 2)} - {round(i_n * 1.15, 2)} A",
                    "PREPORUČEN KONTAKTOR": f"AC-3 min. {k_tip}",
                    "Glavni osigurač": f"{math.ceil(i_n * 2) if start=='dol' else math.ceil(i_n * 1.5)} A (Tromi)",
                    "Moment na vratilu": f"{round(9550*(p_kw/rpm),2)} Nm"
                }
            elif tab == 'auto':
                # Dobijanje podataka iz forme
                tip = request.form.get('a_tip')
                val = float(request.form.get('a_val') or 0)
                mn = float(request.form.get('a_min') or 0)
                mx = float(request.form.get('a_max') or 100)
                
                # 1. Skaliranje i Analiza Signala
                if tip == 'ma':
                    # Procenat signala (4mA=0%, 20mA=100%)
                    procentualno = ((val - 4) / 16) * 100
                    skalirano = ((val - 4) / 16) * (mx - mn) + mn
                    
                    # Provera integriteta (NAMUR NE43 standard)
                    status = "OK"
                    if val < 3.6: status = "Senzor: PREKID / KRATAK SPOJ"
                    elif val > 21.0: status = "Senzor: ZASIĆENJE / GREŠKA"
                    
                    res = {
                        "Fizička vrednost": f"{round(skalirano, 3)} units",
                        "Procenat signala": f"{round(procentualno, 2)} %",
                        "NAMUR NE43 Status": status,
                        "Rezolucija (12-bit PLC)": f"{round((mx-mn)/4095, 4)} units/bit"
                    }
                
                # 2. Temperaturni proračun (PT100) sa tolerancijom
                elif tip == 'pt100':
                    # Formula: Rt = R0 * (1 + A*t + B*t^2) -> Aproksimacija: (R-100)/0.385
                    temp = (val - 100) / 0.3851
                    # Klasa tačnosti A (standardna za industriju)
                    tolerancija = 0.15 + 0.002 * abs(temp)
                    
                    res = {
                        "Izmerena temperatura": f"{round(temp, 2)} °C",
                        "Otpor provodnika (procena)": "Uključiti 3-žičnu vezu!",
                        "Klasa A Tolerancija": f"± {round(tolerancija, 3)} °C",
                        "Max. dozvoljena struja": "1 mA (da se izbegne grejanje sonde)"
                    }

                # 3. PID Tuning (Ziegler-Nichols metoda)
                # Pretpostavimo da korisnik unese kritično pojačanje (Ku) i period (Tu) u polja min/max
                ku = mn if mn > 0 else 1.0
                tu = mx if mx > 0 else 1.0
                
                res.update({
                        "--- PID TUNING (Z-N) ---": "Preporuka za regulaciju:",
                        "Kp (Pojačanje)": round(0.6 * mn, 2),
                        "Ti (Integralno)": round(mx / 2, 2),
                        "Td (Derivativno)": round(mx / 8, 2)
                    })

            elif tab == 'komp':
                pk = float(request.form.get('k_p') or 0)  # Aktivna snaga u kW
                c1 = float(request.form.get('k_c1') or 0.75)
                c2 = float(request.form.get('k_c2') or 0.95)
                u = 400  # Standardni napon
                
                # 1. Proračun potrebne jalove snage (Q)
                phi1 = math.acos(c1)
                phi2 = math.acos(c2)
                q_ukupno = pk * (math.tan(phi1) - math.tan(phi2))
                
                # 2. Nazivna struja baterije (In_cap)
                # I = Q / (sqrt(3) * U)
                i_n_cap = (q_ukupno * 1000) / (1.732 * u)
                
                # 3. Dimenzionisanje opreme (Standard IEC 60831)
                # Oprema mora izdržati 1.3x do 1.5x In zbog harmonika i napona
                struja_zastite = i_n_cap * 1.43
                presek_kabla = "6 mm²" if struja_zastite < 32 else "10 mm²" if struja_zastite < 45 else "16 mm²+"
                
                # 4. Predlog stepenovanja (npr. za automatski regulator sa 6 stepeni)
                osnovni_korak = q_ukupno / 6
                
                res = {
                    "UKUPNA SNAGA (Qc)": f"{round(q_ukupno, 2)} kVAr",
                    "Nazivna struja baterije": f"{round(i_n_cap, 2)} A",
                    "OSIGURAČI (min. vrednost)": f"{math.ceil(struja_zastite)} A (gG tip)",
                    "KONTAKTORI": f"Specijalni za kondenzatore (sa prigušnicama)",
                    "Presek napojnog kabla": presek_kabla,
                    "Predlog koraka (1:1:2:2)": f"{round(osnovni_korak, 1)} kVAr po koraku",
                    "--- VAŽNO ---": "Ako je Qc > 20% snage trafoa, proveri harmonike (THD)!"
                }

            elif tab == 'solar':
                kwh_dan = float(request.form.get('s_kwh') or 0)
                p_panel = float(request.form.get('s_w') or 450)
                u_sistema = 48  # Standard za ozbiljnije sisteme (24V ili 48V)
                dani_autonomije = 2
                
                # 1. Potrebna snaga panela uzimajući u obzir insolaciju (prosek za Srbiju ~3.5h)
                # Gubici sistema (gubici u invertoru, kablovima, prljanje panela) ~ 25% (0.75)
                insolacija = 3.5
                ukupno_w_panela = (kwh_dan * 1000) / (insolacija * 0.75)
                br_panela = math.ceil(ukupno_w_panela / p_panel)
                
                # 2. Dimenzionisanje Invertora
                # Invertor treba da bude bar 20% jači od ukupne snage panela za on-grid
                snaga_invertora = (br_panela * p_panel) / 1000
                
                # 3. Proračun Baterija (za Off-Grid sisteme)
                # Kapacitet (Ah) = (Potrošnja * Dani) / (Napon * DoD)
                # DoD (Depth of Discharge) za LiFePO4 je 0.8, za AGM 0.5
                dod = 0.8 
                kapacitet_ah = (kwh_dan * 1000 * dani_autonomije) / (u_sistema * dod)
                
                # 4. Struja punjenja (Bitno za izbor regulatora - MPPT)
                i_punjenja = (br_panela * p_panel) / u_sistema
                
                res = {
                    "Broj panela (za 3.5h sunca)": f"{br_panela} kom",
                    "Ukupna instalirana snaga": f"{round((br_panela * p_panel)/1000, 2)} kWp",
                    "Potreban Invertor (min)": f"{round(snaga_invertora * 1.2, 2)} kW",
                    "--- OFF-GRID DODATAK ---": "Za rad bez mreže:",
                    "Baterije (48V sistem)": f"{round(kapacitet_ah, 2)} Ah",
                    "Broj LiFePO4 (100Ah/48V)": f"{math.ceil(kapacitet_ah / 100)} kom",
                    "MPPT Regulator (struja)": f"min. {math.ceil(i_punjenja * 1.2)} A",
                    "Površina na krovu": f"{round(br_panela * 2.2, 1)} m²"
                }

            elif tab == 'robot':
                kg = float(request.form.get('r_kg') or 0) # Masa tereta
                m = float(request.form.get('r_m') or 0)   # Dužina ruke (krak)
                v = 1.5 # Ciljana linearna brzina m/s
                acc = 2.0 # Standardno ubrzanje m/s^2
                g = 9.81
                
                # 1. Statički moment (samo držanje tereta)
                m_stat = kg * g * m
                
                # 2. Dinamički moment (ubrzanje + gravitacija)
                # F = m * (g + a) -> Moment = F * krak
                m_dyn = kg * (g + acc) * m
                
                # 3. Potrebna snaga pri brzini v
                # P = F * v
                p_rob = (kg * (g + acc)) * v
                
                # 4. Rezolucija (pretpostavka: 20-bitni enkoder i reduktor 1:50)
                # Jedan krug motora = 1,048,576 impulsa. Sa reduktorom 1:50 to je ogromna preciznost.
                rezolucija = 360 / (1024 * 50) # Za standardni 10-bitni enkoder i reduktor
                
                res = {
                    "Statički moment (držanje)": f"{round(m_stat, 2)} Nm",
                    "Dinamički moment (ubrzanje)": f"{round(m_dyn, 2)} Nm",
                    "Preporučeni moment motora": f"{round(m_dyn * 1.5, 2)} Nm (sa S.F. 1.5)",
                    "Potrebna snaga (W)": f"{round(p_rob, 2)} W",
                    "Preciznost (sa reduktom 1:50)": f"{round(rezolucija, 5)} °/pulsu",
                    "Max. radijus delovanja": f"{m} m"
                }
        except: res = {"Greška": "Proverite unos (sva polja moraju biti brojevi)"}
    return render_template_string(HTML_SABLON, tab=tab, res=res)

if __name__ == '__main__':
    app.run(port=8501, debug=True)
