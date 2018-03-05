# Fysikklab

For å sette opp:

1. `cd` til mappen du vil bruke
2. `git clone https://github.com/finnss/fysikklab.git`
3. `python3 -m venv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`

Og da skal dere være good. Nå kan dere kjøre `python experimental_data.py` i samme mappe for å generere grafene fra den eksperimentelle delen, eller `python numeric_solution.py` for å kjøre den numeriske tilnærmingen.

Det ligger grafer i `plots`-mappen. `12_e` er for eksempel energi-grafen til tracker scan nr 12, og `12_fit` er den tilnærmete funksjonsgrafen. `_v` og `_x` er nok ikke helt pålitelige.

I den eksperimentelle delen klarte jeg ikke å få til regresjon via log-space, så nå bruker jeg et sjetteordens polynom.

Jeg er ikke ferdig med den numeriske delen, det er vel det som skal gjøres på labben jeg er borte. Burde være et greit utgangspunkt der ihvertfall.

Lykke til!
