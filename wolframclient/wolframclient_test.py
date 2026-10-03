from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr


# ============================================================
# PYTHON <-> WOLFRAM 15 USING wolframclient
# ============================================================

print("=" * 70)
print("Python <-> Wolfram 15 Test using wolframclient")
print("=" * 70)


# ------------------------------------------------------------
# 1. Wolfram Kernel path
# ------------------------------------------------------------

KERNEL_PATH = (
    r"C:\Program Files\Wolfram Research\Wolfram\15.0"
    r"\WolframKernel.exe"
)

print("\nWolfram Kernel:")
print(KERNEL_PATH)


# ------------------------------------------------------------
# 2. Mathematica/Wolfram model file
# ------------------------------------------------------------

MODEL_FILE = Path(__file__).with_name(
    "wolfram_model.wl"
).resolve()

model_path_wolfram = MODEL_FILE.as_posix()

print("\nWolfram model file:")
print(MODEL_FILE)


# ------------------------------------------------------------
# 3. Create Wolfram session
# ------------------------------------------------------------

session = WolframLanguageSession(
    KERNEL_PATH
)


try:

    # --------------------------------------------------------
    # 4. Start Wolfram Kernel
    # --------------------------------------------------------

    print("\nStarting Wolfram Kernel...")

    session.start()

    print("Connection established successfully.")


    # --------------------------------------------------------
    # 5. Get Wolfram version
    # --------------------------------------------------------

    version = session.evaluate(
        wlexpr("$Version")
    )

    print("\nDetected Wolfram version:")
    print(version)


    # --------------------------------------------------------
    # 6. Get installation directory
    # --------------------------------------------------------

    install_directory = session.evaluate(
        wlexpr("$InstallationDirectory")
    )

    print("\nInstallation directory:")
    print(install_directory)


    # --------------------------------------------------------
    # 7. Simple calculation test
    # --------------------------------------------------------

    print("\nTesting Wolfram calculation...")

    integral_result = session.evaluate(
        wlexpr(
            "N[Integrate[Sin[x]^2, {x, 0, Pi}]]"
        )
    )

    print(
        "Integral of Sin[x]^2 from 0 to Pi =",
        integral_result
    )


    # --------------------------------------------------------
    # 8. Load Wolfram model file
    # --------------------------------------------------------

    print("\nLoading Wolfram model...")

    load_command = (
        f'Get["{model_path_wolfram}"]'
    )

    session.evaluate(
        wlexpr(load_command)
    )

    print("Wolfram model loaded successfully.")


    # --------------------------------------------------------
    # 9. Solve differential equation in Wolfram
    # --------------------------------------------------------

    print("\nSolving differential equation in Wolfram...")

    data = session.evaluate(
        wlexpr(
            "solveSystem[10, 0.01]"
        )
    )

    print("Calculation completed successfully.")


    # --------------------------------------------------------
    # 10. Convert Wolfram result to NumPy
    # --------------------------------------------------------

    data = np.array(
        data,
        dtype=float
    )

    time = data[:, 0]
    response = data[:, 1]


    # --------------------------------------------------------
    # 11. Print received data
    # --------------------------------------------------------

    print("\nData received from Wolfram:")

    print(
        "Number of samples =",
        len(time)
    )

    print("\nFirst 10 samples:")
    print(data[:10])


    # --------------------------------------------------------
    # 12. Result information
    # --------------------------------------------------------

    print("\nResult information:")

    print(
        f"Maximum x(t) = {np.max(response):.6f}"
    )

    print(
        f"Minimum x(t) = {np.min(response):.6f}"
    )

    print(
        f"Final x(t)   = {response[-1]:.6f}"
    )


    # --------------------------------------------------------
    # 13. Plot result
    # --------------------------------------------------------

    plt.figure(
        figsize=(10, 5)
    )

    plt.plot(
        time,
        response,
        linewidth=2,
        label="Wolfram NDSolve"
    )

    plt.axhline(
        y=0,
        linewidth=0.8
    )

    plt.xlabel(
        "Time (s)",
        fontsize=12
    )

    plt.ylabel(
        "x(t)",
        fontsize=12
    )

    plt.title(
        "Dynamic System Solved by Wolfram 15 "
        "and Visualized in Python",
        fontsize=13
    )

    plt.grid(
        True,
        alpha=0.3
    )

    plt.legend(
        fontsize=10
    )

    plt.tight_layout()


    # --------------------------------------------------------
    # 14. Save figure
    # --------------------------------------------------------

    output_file = Path(__file__).with_name(
        "wolframclient_result.png"
    )

    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )

    print("\nFigure saved as:")
    print(output_file)


    # --------------------------------------------------------
    # 15. Show figure
    # --------------------------------------------------------

    plt.show()


except Exception as error:

    print("\n" + "=" * 70)
    print("ERROR")
    print("=" * 70)

    print(error)


finally:

    # --------------------------------------------------------
    # 16. Close Wolfram Kernel
    # --------------------------------------------------------

    try:
        session.terminate()

        print("\nWolfram Kernel terminated successfully.")

    except Exception:
        pass

    print("=" * 70)