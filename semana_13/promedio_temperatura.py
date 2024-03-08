TEMPERATURA = [
    [  # QUITO
        [  # SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 23},
            {"DIA": "MIERCOLES", "TEMPERATURA": 18},
            {"DIA": "JUEVES", "TEMPERATURA": 13},
            {"DIA": "VIERNES", "TEMPERATURA": 31},
            {"DIA": "SABADO", "TEMPERATURA": 20},
            {"DIA": "DOMINGO", "TEMPERATURA": 24}
        ],
        [  # SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 21},
            {"DIA": "MARTES", "TEMPERATURA": 32},
            {"DIA": "MIERCOLES", "TEMPERATURA": 30},
            {"DIA": "JUEVES", "TEMPERATURA": 25},
            {"DIA": "VIERNES", "TEMPERATURA": 31},
            {"DIA": "SABADO", "TEMPERATURA": 16},
            {"DIA": "DOMINGO", "TEMPERATURA": 12}
        ],
        [  # SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 28},
            {"DIA": "MARTES", "TEMPERATURA": 22},
            {"DIA": "MIERCOLES", "TEMPERATURA": 30},
            {"DIA": "JUEVES", "TEMPERATURA": 21},
            {"DIA": "VIERNES", "TEMPERATURA": 30},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 32}
        ],
        [  # SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 32},
            {"DIA": "MIERCOLES", "TEMPERATURA": 35},
            {"DIA": "JUEVES", "TEMPERATURA": 36},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 34},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
    ],
    [  # LATACUNGA
        [  # SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 26},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 21},
            {"DIA": "VIERNES", "TEMPERATURA": 31},
            {"DIA": "SABADO", "TEMPERATURA": 28},
            {"DIA": "DOMINGO", "TEMPERATURA": 32}
        ],
        [  # SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 29},
            {"DIA": "MARTES", "TEMPERATURA": 31},
            {"DIA": "MIERCOLES", "TEMPERATURA": 32},
            {"DIA": "JUEVES", "TEMPERATURA": 35},
            {"DIA": "VIERNES", "TEMPERATURA": 31},
            {"DIA": "SABADO", "TEMPERATURA": 37},
            {"DIA": "DOMINGO", "TEMPERATURA": 28}
        ],
        [  # SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 29},
            {"DIA": "MARTES", "TEMPERATURA": 25},
            {"DIA": "MIERCOLES", "TEMPERATURA": 32},
            {"DIA": "JUEVES", "TEMPERATURA": 20},
            {"DIA": "VIERNES", "TEMPERATURA": 31},
            {"DIA": "SABADO", "TEMPERATURA": 28},
            {"DIA": "DOMINGO", "TEMPERATURA": 29}
        ],
        [  # SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 29},
            {"DIA": "MARTES", "TEMPERATURA": 31},
            {"DIA": "MIERCOLES", "TEMPERATURA": 26},
            {"DIA": "JUEVES", "TEMPERATURA": 32},
            {"DIA": "VIERNES", "TEMPERATURA": 28},
            {"DIA": "SABADO", "TEMPERATURA": 33},
            {"DIA": "DOMINGO", "TEMPERATURA": 28}
        ],
    ],
    [  # AMBATO
        [  # SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 29},
            {"DIA": "MARTES", "TEMPERATURA": 26},
            {"DIA": "MIERCOLES", "TEMPERATURA": 32},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 28},
            {"DIA": "SABADO", "TEMPERATURA": 29},
            {"DIA": "DOMINGO", "TEMPERATURA": 31}
        ],
        [  # SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 28},
            {"DIA": "MARTES", "TEMPERATURA": 31},
            {"DIA": "MIERCOLES", "TEMPERATURA": 29},
            {"DIA": "JUEVES", "TEMPERATURA": 35},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 35},
            {"DIA": "DOMINGO", "TEMPERATURA": 29}
        ],
        [  # SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 29},
            {"DIA": "MARTES", "TEMPERATURA": 26},
            {"DIA": "MIERCOLES", "TEMPERATURA": 32},
            {"DIA": "JUEVES", "TEMPERATURA": 30},
            {"DIA": "VIERNES", "TEMPERATURA": 29},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 32}
        ],
        [  # SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 29},
            {"DIA": "MARTES", "TEMPERATURA": 32},
            {"DIA": "MIERCOLES", "TEMPERATURA": 31},
            {"DIA": "JUEVES", "TEMPERATURA": 33},
            {"DIA": "VIERNES", "TEMPERATURA": 31},
            {"DIA": "SABADO", "TEMPERATURA": 35},
            {"DIA": "DOMINGO", "TEMPERATURA": 30}
        ],
    ],
]

suma_temperatura = float()
peomedio_semanal = float()
c = int()
x = int()
for ciudad in TEMPERATURA:
    x += 1
    if x == 1:
        print("PRONOSTICO SEMANAL DE LAS TEMPERATURAS EN LA CIUDAD DE QUITO")

    if x == 2:
        print("PRONOSTICO SEMANAL DE LAS TEMPERATURAS EN LA CIUDAD LATACUNGA")

    if x == 3:
        print("PRONOSTICO SEMANAL DE LAS TEMPERATURAS EN LA CIUDAD AMBATO")

    for semana in ciudad:
        c += 1
        for dia in semana:
            suma_temperatura += dia["TEMPERATURA"]
        promedio_semanal = suma_temperatura / 7
        print(f"La semana {c},  un promedio de temperatura {promedio_semanal}")
        print()
