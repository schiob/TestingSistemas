sig_usuario_test_cases = [
    {
        'name': 'case 1 ok',
        'input': 'Tom 4\nSusana 2\nAndres 10\nPepe 3\nLuis 2',
        'expected_output': [
            ['Susana', '2'],
            ['Pepe', '3'],
            ['Tom', '4'],
            ['Andres', '10'],
        ],
        'expected_raise': False,
    },
    {
        'name': 'case 1 error',
        'input': 'Tom 4\nSusana 2\nAndres 10\nPepe 3\nLuis 2',
        'expected_output': [
            'Susana', '2',
            ['Pepe', '3'],
            ['Tom', '4'],
            ['Andres', '10'],
        ],
        'expected_raise': True,
    },
]

viajes_disponibles_test_cases = [
    {
        'name': 'case 1 ok',
        'input': 'Juan 3\nJesus 2\nMaria 3\nToño 1',
        'expected_output': [[1, 50], [2, 40], [3, 50], [4, 30]],
        'expected_raise': False,
    },
]

extraer_conductores_test_cases = [
    {
        'name': 'case 1 ok',
        'input': 'Juan 3\nJesus 2\nMaria 3\nToño 1',
        'expected_output': [['Juan', '3'], ['Jesus', '2'], ['Maria', '3'], ['Toño', '1']],
        'expected_raise': False,
    },
]

calcular_tarifa_test_cases = [
    {
        'name': 'case 1 ok',
        'input': 20,
        'expected_output': 220,
        'expected_raise': False,
    },
    {
        'name': 'case 2 error',
        'input': 'abc',
        'expected_output': 0,
        'expected_raise': True,
    },
]

funcion_principal_test_cases = [
    {
        'name': 'case 1 ok',
        'input': 'Tom 4\nSusana 2\nAndres 10\nPepe 3\nLuis 2',
        'input2': 'Juan 3\nJesus 2\nMaria 3\nToño 1',
        'expected_output': ['Susana - viaje 30', 'Pepe - viaje 40', 'Tom - viaje 50', 'Andres - viaje 50'],
        'expected_raise': False,
    },
    {
        'name': 'case 2 error',
        'input': 'Juan 3\nJesus 2\nMaria 3\nToño 1',
        'input2': 'Juan 3\nJesus 2\nMaria 3\nToño 1',
        'expected_output': None,
        'expected_raise': True,
    },
]