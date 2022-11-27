WORDLE

Programul "...." reprezinta o clona a jocului Wordle

Programul "....." reprezinta algoritmul de rezolvare a jocului.

Algoritmul calculeaza frecventa fiecarei litere pe fiecare pozitie si o stocheaza intr-un dictionar. Calculeaza probabilitatea ca fiind frecventa literei pe pozitia corespunzatoare/ numarul total de cuvinte. Entropia este apoi calculata cu formula E= Σ (p(x)*log2(1/p(x))), unde p(x) este probabilitatea.

Cuvantul cu cea mai mare entropie este urmatorul guess, iar din lista initiala de cuvinte scoatem cuvintele care au litere pentru care am primit feedback 'n' ( adică litera respectiva nu este in cuvântul cheie), dar si cuvintele care au litere pe poziția unde feedback-ul este 'g' ( litera respectiva este in cuvânt, dar nu este pe poziția respectiva)

exemplu : cheie : BUNIC cuvânt introdus : BANCA feedback : vnvgn

Deci, scoatem cuvintele care conțin 'A', dar și pe cele care au 'C' pe poziția 4.
