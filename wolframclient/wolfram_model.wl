(* ::Package:: *)

ClearAll[solveSystem, x, t];

solveSystem[tmax_: 10, dt_: 0.01] := Module[
    {sol},

    sol = NDSolveValue[
        {
            x''[t] + 1.2*x'[t] + 25*x[t] == 0,
            x[0] == 1,
            x'[0] == 0
        },
        x,
        {t, 0, tmax}
    ];

    N[
        Table[
            {tt, sol[tt]},
            {tt, 0, tmax, dt}
        ]
    ]
];
