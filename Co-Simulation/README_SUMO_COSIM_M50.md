# CARLA + SUMO Co-Simulation for M50 Motorway Map

This guide explains how to set up **co-simulation between CARLA and SUMO** using a custom HD map of the M50 motorway. The SUMO network is generated directly from the `.xodr` OpenDRIVE file exported from RoadRunner and imported into CARLA. This pipeline is underdevelopement, and does not yet produce working Co-Simulation on the M50.

---

## Requirements

- CARLA (v0.9.15 or later)
- SUMO (v1.10 or later)
- Python 3.7+
- `carla` Python API
- `traci` (SUMO Python interface)
- `netconvert` (comes with SUMO)
- `carla-sumo` bridge scripts

---

## Files Overview

- `M50Map.xodr` — OpenDRIVE file for the M50 motorway
- `M50Map.net.xml` — SUMO network file generated from the XODR
- `sumo_config/` — SUMO route, additional vehicle, and network configuration
- `carla_config.py` — defines sync behavior and spawn settings for co-sim

---

## Step-by-Step Instructions

### 1. Start CARLA

Launch the CARLA server and load the M50 map:

```bash
./CarlaUE4.sh
```

Ensure the `M50Map` is listed among available maps. Use a Python client to confirm:

```bash
python3 config.py --map \<Desired Map Name\>
```

---

### 2. Generate SUMO Network from `.xodr`

If not already done, use `netconvert`:

```bash
netconvert --opendrive-files \<Desired Map Name\>.xodr -o \<Desired Map Name\>.net.xml
```

The xodr file and the net file for the m50 map can be found in this directory

---

### 3. Configure SUMO Simulation

This is the current stage of debugging believe to have some issue generating the route file
please see [Link](https://carla.readthedocs.io/en/latest/adv_sumo/#run-a-custom-co-simulation) for carla documentation on this step.
The current struggle is with the route file and how to set this up using the NETFILE 

Set up your SUMO configuration:

- **net file**: `M50Map.net.xml`
- **route file**: `sumo_config/routes.rou.xml`
- **additional files**: `sumo_config/additional.add.xml`
- **view settings** (optional): `sumo_config/view_settings.xml`

Example `sumo_config.sumocfg`:
```xml
<configuration>
    <input>
        <net-file value="M50Map.net.xml"/>
        <route-files value="sumo_config/routes.rou.xml"/>
        <additional-files value="sumo_config/additional.add.xml"/>
    </input>
</configuration>
```

---

### 4. Run CARLA-SUMO Co-Simulation

Run the synchronization script from your co-simulation bridge setup:

```bash
python3 run_synchronization.py --sumo-config-file sumo_config/sumo_config.sumocfg --sync-mode --sumo-gui
```

Add additional arguments as needed:
- `--map M50Map`
- `--host localhost`
- `--sumo-port 8813`

---

## Configuration Tips

- Use `carla_config.py` to manage spawn points and sync rate.
- Adjust `route.rou.xml` for custom vehicle flows or timed spawns.
- Visualize SUMO network in `sumo-gui` to debug routing or geometry issues.

---

## Validation and Debugging

- Use `sumo-gui` to step through the simulation and ensure routing is valid.
- Visual debug tools in CARLA can confirm agent sync status.
- Use `--debug` flags on both sides if vehicles fail to sync.

---

## Reference

- [CARLA SUMO Integration Docs](https://carla.readthedocs.io/en/latest/carla_sumo/)
- [SUMO Docs](https://sumo.dlr.de/docs/)
- Original map created in RoadRunner, exported as `.xodr`, and imported into CARLA.

---

## 📜 License

This guide and integration workflow are open-source. Refer to upstream licenses for CARLA and SUMO.
