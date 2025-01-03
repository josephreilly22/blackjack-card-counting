def deviated_decision(game,deck, count):

    decks_remaining = len(deck) // 52
    if decks_remaining:
        count = count // decks_remaining
    else:
        count = count // 0.5

    # print(count)

    if count < -2:
        count = -2
    elif count > 6:
        count = 6
    

    pairSplitting = {
        -2: {
            1:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            10: [False, False, False, False, False, False, False, False, False, False],
            9:  [False, True,  True,  True,  True,  True,  False, True,  True,  False],
            8:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            7:  [False, True,  True,  True,  True,  True,  True,  False, False, False],
            6:  [False, False, True,  True,  True,  True,  False, False, False, False],
            5:  [False, False, False, False, False, False, False, False, False, False],
            4:  [False, False, False, False, False, False, False, False, False, False],
            3:  [False, False, False, True,  True,  True,  True,  False, False, False],
            2:  [False, False, False, True,  True,  True,  True,  False, False, False]
        },
        -1: {
            1:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            10: [False, False, False, False, False, False, False, False, False, False],
            9:  [False, True,  True,  True,  True,  True,  False, True,  True,  False],
            8:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            7:  [False, True,  True,  True,  True,  True,  True,  False, False, False],
            6:  [False, False, True,  True,  True,  True,  False, False, False, False],
            5:  [False, False, False, False, False, False, False, False, False, False],
            4:  [False, False, False, False, False, False, False, False, False, False],
            3:  [False, False, False, True,  True,  True,  True,  False, False, False],
            2:  [False, False, False, True,  True,  True,  True,  False, False, False]
        },
        0: {
            1:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            10: [False, False, False, False, False, False, False, False, False, False],
            9:  [False, True,  True,  True,  True,  True,  False, True,  True,  False],
            8:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            7:  [False, True,  True,  True,  True,  True,  True,  False, False, False],
            6:  [False, False, True,  True,  True,  True,  False, False, False, False],
            5:  [False, False, False, False, False, False, False, False, False, False],
            4:  [False, False, False, False, False, False, False, False, False, False],
            3:  [False, False, False, True,  True,  True,  True,  False, False, False],
            2:  [False, False, False, True,  True,  True,  True,  False, False, False]
        },
        1: {
            1:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            10: [False, False, False, False, False, False, False, False, False, False],
            9:  [False, True,  True,  True,  True,  True,  False, True,  True,  False],
            8:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            7:  [False, True,  True,  True,  True,  True,  True,  False, False, False],
            6:  [False, False, True,  True,  True,  True,  False, False, False, False],
            5:  [False, False, False, False, False, False, False, False, False, False],
            4:  [False, False, False, False, False, False, False, False, False, False],
            3:  [False, False, False, True,  True,  True,  True,  False, False, False],
            2:  [False, False, False, True,  True,  True,  True,  False, False, False]
        },
        2: {
            1:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            10: [False, False, False, False, False, False, False, False, False, False],
            9:  [False, True,  True,  True,  True,  True,  False, True,  True,  False],
            8:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            7:  [False, True,  True,  True,  True,  True,  True,  False, False, False],
            6:  [False, False, True,  True,  True,  True,  False, False, False, False],
            5:  [False, False, False, False, False, False, False, False, False, False],
            4:  [False, False, False, False, False, False, False, False, False, False],
            3:  [False, False, False, True,  True,  True,  True,  False, False, False],
            2:  [False, False, False, True,  True,  True,  True,  False, False, False]
        },
        3: {
            1:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            10: [False, False, False, False, False, False, False, False, False, False],
            9:  [False, True,  True,  True,  True,  True,  False, True,  True,  False],
            8:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            7:  [False, True,  True,  True,  True,  True,  True,  False, False, False],
            6:  [False, False, True,  True,  True,  True,  False, False, False, False],
            5:  [False, False, False, False, False, False, False, False, False, False],
            4:  [False, False, False, False, False, False, False, False, False, False],
            3:  [False, False, False, True,  True,  True,  True,  False, False, False],
            2:  [False, False, False, True,  True,  True,  True,  False, False, False]
        },
        4: {
            1:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            10: [False, False, False, False, False, True, False, False, False, False],
            9:  [False, True,  True,  True,  True,  True,  False, True,  True,  False],
            8:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            7:  [False, True,  True,  True,  True,  True,  True,  False, False, False],
            6:  [False, False, True,  True,  True,  True,  False, False, False, False],
            5:  [False, False, False, False, False, False, False, False, False, False],
            4:  [False, False, False, False, False, False, False, False, False, False],
            3:  [False, False, False, True,  True,  True,  True,  False, False, False],
            2:  [False, False, False, True,  True,  True,  True,  False, False, False]
        },
        5: {
            1:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            10: [False, False, False, False, True, True, False, False, False, False],
            9:  [False, True,  True,  True,  True,  True,  False, True,  True,  False],
            8:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            7:  [False, True,  True,  True,  True,  True,  True,  False, False, False],
            6:  [False, False, True,  True,  True,  True,  False, False, False, False],
            5:  [False, False, False, False, False, False, False, False, False, False],
            4:  [False, False, False, False, False, False, False, False, False, False],
            3:  [False, False, False, True,  True,  True,  True,  False, False, False],
            2:  [False, False, False, True,  True,  True,  True,  False, False, False]
        },
        6: {
            1:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            10: [False, False, False, True, True, True, False, False, False, False],
            9:  [False, True,  True,  True,  True,  True,  False, True,  True,  False],
            8:  [True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
            7:  [False, True,  True,  True,  True,  True,  True,  False, False, False],
            6:  [False, False, True,  True,  True,  True,  False, False, False, False],
            5:  [False, False, False, False, False, False, False, False, False, False],
            4:  [False, False, False, False, False, False, False, False, False, False],
            3:  [False, False, False, True,  True,  True,  True,  False, False, False],
            2:  [False, False, False, True,  True,  True,  True,  False, False, False]
        }
    }

        #     A       2      3      4      5      6      7      8      9      10  
 


        #    A    2    3    4    5    6    7    8    9    10
    
    softTotals = {
        -2: {
            21: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            20:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            19:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            18:  ["H", "D", "D", "D", "D", "D", "S", "S", "H", "H"],
            17:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            16:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            15:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            14:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"],
            13:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"]
        }, 
        -1: {
            21: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            20:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            19:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            18:  ["H", "D", "D", "D", "D", "D", "S", "S", "H", "H"],
            17:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            16:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            15:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            14:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"],
            13:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"]
        }, 
        0: {
            21: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            20:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            19:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            18:  ["H", "D", "D", "D", "D", "D", "S", "S", "H", "H"],
            17:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            16:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            15:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            14:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"],
            13:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"]
        },
        1: {
            21: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            20:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            19:  ["S", "S", "S", "S", "D", "D", "S", "S", "S", "S"],
            18:  ["D", "D", "D", "D", "D", "D", "S", "S", "H", "H"],
            17:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            16:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            15:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            14:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"],
            13:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"]
        },
        2: {
            21: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            20:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            19:  ["S", "S", "S", "S", "D", "D", "S", "S", "S", "S"],
            18:  ["D", "D", "D", "D", "D", "D", "S", "S", "H", "H"],
            17:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            16:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            15:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            14:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"],
            13:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"]
        },
        3: {
            21: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            20:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            19:  ["S", "S", "S", "D", "D", "D", "S", "S", "S", "S"],
            18:  ["D", "D", "D", "D", "D", "D", "S", "S", "H", "H"],
            17:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            16:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            15:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            14:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"],
            13:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"]
        },
        4: {
            21: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            20:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            19:  ["S", "S", "S", "D", "D", "D", "S", "S", "S", "S"],
            18:  ["D", "D", "D", "D", "D", "D", "S", "S", "H", "H"],
            17:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            16:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            15:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            14:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"],
            13:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"]
        },
        5: {
            21: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            20:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            19:  ["S", "S", "S", "D", "D", "D", "S", "S", "S", "S"],
            18:  ["D", "D", "D", "D", "D", "D", "S", "S", "H", "H"],
            17:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            16:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            15:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            14:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"],
            13:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"]
        },
        6: {
            21: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            20:  ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            19:  ["S", "S", "S", "D", "D", "D", "S", "S", "S", "S"],
            18:  ["D", "D", "D", "D", "D", "D", "S", "S", "H", "H"],
            17:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            16:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            15:  ["H", "H", "H", "D", "D", "D", "H", "H", "H", "H"],
            14:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"],
            13:  ["H", "H", "H", "H", "D", "D", "H", "H", "H", "H"]
        }
    }
    

        #     A    2    3    4    5    6    7    8    9    10
    
    hardTotals = {
        -2: {
            17: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            16: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            15: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            14: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            13: ["H", "H", "S", "S", "S", "S", "H", "H", "H", "H"],
            12: ["H", "H", "H", "H", "S", "S", "H", "H", "H", "H"],
            11: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            10: ["H", "D", "D", "D", "D", "D", "D", "D", "D", "H"],
            9:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            8:  ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
        }, 
        -1: {
            17: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            16: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            15: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            14: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            13: ["H", "H", "S", "S", "S", "S", "H", "H", "H", "H"],
            12: ["H", "H", "H", "H", "S", "S", "H", "H", "H", "H"],
            11: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            10: ["H", "D", "D", "D", "D", "D", "D", "D", "D", "H"],
            9:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            8:  ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
        },
        0: {
            17: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            16: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            15: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            14: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            13: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            12: ["H", "H", "H", "S", "S", "S", "H", "H", "H", "H"],
            11: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            10: ["H", "D", "D", "D", "D", "D", "D", "D", "D", "H"],
            9:  ["H", "H", "D", "D", "D", "D", "H", "H", "H", "H"],
            8:  ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
        }, 
        1: {
            17: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            16: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "S"],
            15: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            14: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            13: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            12: ["H", "H", "H", "S", "S", "S", "H", "H", "H", "H"],
            11: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            10: ["H", "D", "D", "D", "D", "D", "D", "D", "D", "H"],
            9:  ["H", "D", "D", "D", "D", "D", "H", "H", "H", "H"],
            8:  ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
        },
        2: {
            17: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            16: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "S"],
            15: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            14: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            13: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            12: ["H", "H", "S", "S", "S", "S", "H", "H", "H", "H"],
            11: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            10: ["H", "D", "D", "D", "D", "D", "D", "D", "D", "H"],
            9:  ["H", "D", "D", "D", "D", "D", "H", "H", "H", "H"],
            8:  ["H", "H", "H", "H", "H", "D", "H", "H", "H", "H"],
        },
        3: {
            17: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            16: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "S"],
            15: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            14: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            13: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            12: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            11: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            10: ["H", "D", "D", "D", "D", "D", "D", "D", "D", "H"],
            9:  ["H", "D", "D", "D", "D", "D", "D", "H", "H", "H"],
            8:  ["H", "H", "H", "H", "H", "D", "H", "H", "H", "H"],
        },
        4: {
            17: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            16: ["H", "S", "S", "S", "S", "S", "H", "H", "S", "S"],
            15: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "S"],
            14: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            13: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            12: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            11: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            10: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            9:  ["H", "D", "D", "D", "D", "D", "D", "H", "H", "H"],
            8:  ["H", "H", "H", "H", "H", "D", "H", "H", "H", "H"],
        },
        5: {
            17: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            16: ["H", "S", "S", "S", "S", "S", "H", "H", "S", "S"],
            15: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "S"],
            14: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            13: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            12: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            11: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            10: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            9:  ["H", "D", "D", "D", "D", "D", "D", "H", "H", "H"],
            8:  ["H", "H", "H", "H", "H", "D", "H", "H", "H", "H"],
        },
        6: {
            17: ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],
            16: ["H", "S", "S", "S", "S", "S", "H", "H", "S", "S"],
            15: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "S"],
            14: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            13: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            12: ["H", "S", "S", "S", "S", "S", "H", "H", "H", "H"],
            11: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            10: ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
            9:  ["H", "D", "D", "D", "D", "D", "D", "H", "H", "H"],
            8:  ["H", "H", "H", "H", "H", "D", "H", "H", "H", "H"],
        }
    }

    # Check for pair of current hand
    if game.player.cards[game.current_index][0] == game.player.cards[game.current_index][1]:
        if game.player.cards[game.current_index][0] == 1 and len(game.player.cards) < 3:
            if pairSplitting[count][game.player.cards[game.current_index][0]][game.dealer[0] - 1]:
                return 'P'
        else:
            if pairSplitting[count][game.player.cards[game.current_index][0]][game.dealer[0] - 1]:
                return 'P'
            
    # No hitting after splitting aces
    if len(game.player.cards) > 1 and game.player.cards[0][0] == 1:
        return 'S'

    # See if it is soft total
    if game.check_soft():
        temp = softTotals[count][game.check_player()][game.dealer[0] - 1]
        if temp == 'D' and len(game.player.cards[game.current_index]) > 2:
            return 'H'
        return temp
    else:
        total = game.check_player()
        if total < 8:
            return "H"
        elif total > 17:
            return "S"
        temp = hardTotals[count][total][game.dealer[0] - 1] 
        if temp == 'D' and len(game.player.cards[game.current_index]) > 2:
            return 'H'
        return temp
