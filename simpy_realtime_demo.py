import simpy
from simpy.rt import RealtimeEnvironment
import time
import matplotlib.pyplot as plt


# ============================================================
# SIMPY REAL-TIME ENVIRONMENT DEMO
# Electrical Load Monitoring
# ============================================================

# Each 1 simulation second = 0.5 real seconds
REAL_TIME_FACTOR = 0.5

# Total simulation duration
SIMULATION_TIME = 12


# ------------------------------------------------------------
# Shared system state
# ------------------------------------------------------------
loads = {
    "Motor": 0.0,
    "Heater": 0.0,
    "EV Charger": 0.0
}

# Data storage
sim_time_history = []
real_time_history = []
power_history = []

start_wall_time = None


# ------------------------------------------------------------
# Electrical load process
# ------------------------------------------------------------
def electrical_load(env, name, power_kw, on_time, off_time):

    # Wait until switching ON
    yield env.timeout(on_time)

    loads[name] = power_kw

    real_elapsed = time.perf_counter() - start_wall_time

    print(
        f"[Real={real_elapsed:5.2f}s | Sim={env.now:5.2f}s] "
        f"{name:12s} ON  -> {power_kw:.1f} kW"
    )

    # Remain ON
    yield env.timeout(off_time - on_time)

    loads[name] = 0.0

    real_elapsed = time.perf_counter() - start_wall_time

    print(
        f"[Real={real_elapsed:5.2f}s | Sim={env.now:5.2f}s] "
        f"{name:12s} OFF"
    )


# ------------------------------------------------------------
# Real-time power monitor
# ------------------------------------------------------------
def power_monitor(env):

    while True:

        total_power = sum(loads.values())

        real_elapsed = time.perf_counter() - start_wall_time

        sim_time_history.append(env.now)
        real_time_history.append(real_elapsed)
        power_history.append(total_power)

        print(
            f"       Monitor -> "
            f"Sim Time = {env.now:5.2f} s | "
            f"Real Time = {real_elapsed:5.2f} s | "
            f"Total Power = {total_power:5.1f} kW"
        )

        # Sample every 0.5 simulation seconds
        yield env.timeout(0.5)


# ------------------------------------------------------------
# Create REAL-TIME environment
# ------------------------------------------------------------
env = RealtimeEnvironment(
    factor=REAL_TIME_FACTOR,
    strict=False
)

start_wall_time = time.perf_counter()


# ------------------------------------------------------------
# Add electrical loads
# ------------------------------------------------------------

# Motor:
# ON at t=2 s
# OFF at t=8 s
env.process(
    electrical_load(
        env,
        "Motor",
        power_kw=15,
        on_time=2,
        off_time=8
    )
)

# Heater:
# ON at t=4 s
# OFF at t=10 s
env.process(
    electrical_load(
        env,
        "Heater",
        power_kw=10,
        on_time=4,
        off_time=10
    )
)

# EV Charger:
# ON at t=6 s
# OFF at t=9 s
env.process(
    electrical_load(
        env,
        "EV Charger",
        power_kw=7,
        on_time=6,
        off_time=9
    )
)


# Add monitor
env.process(power_monitor(env))


# ------------------------------------------------------------
# Run simulation
# ------------------------------------------------------------
print("=" * 65)
print("SIMPY REAL-TIME ELECTRICAL LOAD SIMULATION")
print("=" * 65)

print(f"Real-time factor : {REAL_TIME_FACTOR}")
print(f"Simulation time  : {SIMULATION_TIME} s")
print()

env.run(until=SIMULATION_TIME)


# ------------------------------------------------------------
# Finish
# ------------------------------------------------------------
total_real_time = time.perf_counter() - start_wall_time

print()
print("=" * 65)
print("SIMULATION FINISHED")
print("=" * 65)

print(f"Simulation time : {SIMULATION_TIME:.2f} s")
print(f"Actual real time: {total_real_time:.2f} s")
print(
    f"Expected real time: "
    f"{SIMULATION_TIME * REAL_TIME_FACTOR:.2f} s"
)


# ============================================================
# Plot results
# ============================================================

plt.figure(figsize=(10, 5))

plt.step(
    sim_time_history,
    power_history,
    where="post",
    linewidth=2
)

plt.xlabel("Simulation Time (s)")
plt.ylabel("Total Electrical Power (kW)")

plt.title(
    "SimPy Real-Time Environment\n"
    "Electrical Load Simulation"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "SimPy_RealTime_Result.png",
    dpi=300
)

plt.show()