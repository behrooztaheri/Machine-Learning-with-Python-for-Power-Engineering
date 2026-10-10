import pandapower as pp
import pandapower.plotting as plot

net = pp.create_empty_network(name="sample_network", sn_mva=1.0, f_hz=50)

bus_hv = pp.create_bus(net, vn_kv=110.0, name="HV Bus")
bus_mv1 = pp.create_bus(net, vn_kv=20.0, name="MV Bus 1")
bus_mv2 = pp.create_bus(net, vn_kv=20.0, name="MV Bus 2")
bus_mv3 = pp.create_bus(net, vn_kv=20.0, name="MV Bus 3")
bus_lv = pp.create_bus(net, vn_kv=0.4, name="LV Bus")

pp.create_ext_grid(net, bus=bus_hv, vm_pu=1.02, va_degree=0.0, name="Grid Source")

pp.create_transformer(net, hv_bus=bus_hv, lv_bus=bus_mv1, std_type="63 MVA 110/20 kV", name="HV/MV Transformer")
pp.create_transformer(net, hv_bus=bus_mv3, lv_bus=bus_lv, std_type="0.4 MVA 20/0.4 kV", name="MV/LV Transformer")

line1 = pp.create_line(net, from_bus=bus_mv1, to_bus=bus_mv2, length_km=2.5, std_type="NA2XS2Y 1x240 RM/25 12/20 kV", name="MV Line 1")
line2 = pp.create_line(net, from_bus=bus_mv2, to_bus=bus_mv3, length_km=1.8, std_type="NA2XS2Y 1x240 RM/25 12/20 kV", name="MV Line 2")
line3 = pp.create_line(net, from_bus=bus_mv1, to_bus=bus_mv2, length_km=2.5, std_type="NA2XS2Y 1x240 RM/25 12/20 kV", name="MV Line 1 Parallel")
pp.create_switch(net, bus=bus_mv1, element=line3, et="l", closed=False, type="LS", name="Parallel Line Switch")

pp.create_load(net, bus=bus_mv2, p_mw=1.2, q_mvar=0.4, name="MV Load 1")
pp.create_load(net, bus=bus_mv3, p_mw=0.8, q_mvar=0.25, name="MV Load 2")
pp.create_load(net, bus=bus_lv, p_mw=0.15, q_mvar=0.05, name="LV Load")

pp.create_sgen(net, bus=bus_mv3, p_mw=0.4, q_mvar=0.0, sn_mva=0.5, type="PV", name="PV Plant")

pp.create_shunt(net, bus=bus_mv2, q_mvar=-0.3, p_mw=0.0, name="Capacitor Bank")

pp.runpp(net, algorithm="nr", init="flat")

print("Bus results:")
print(net.res_bus)

print("\nLine results:")
print(net.res_line)

print("\nTransformer results:")
print(net.res_trafo)

print("\nExternal grid:")
print(net.res_ext_grid)

print(f"\nMinimum voltage: {net.res_bus.vm_pu.min():.4f} pu")
print(f"Maximum line loading: {net.res_line.loading_percent.max():.2f} %")

plot.simple_plot(net)