# HBOT 3D F300

This repository contains Simplify 3D profiles and manuals in both English and Polish for the HBOT 3D F300 printer. Additionally, and it documents some of the troubleshooting steps I had to take to fix the 3D printer.

If the print head runs into the build plate while leveling. This issue could very well be related to one or more of the strain gauges beeing broken or disconnected.

## Known Issues

### Bed leveling Issue

One I faced while repairing this printer was that the print head rams into the build plate while leveling. This issue is most likely related to one or more of the strain gauges inside the print head being broken or disconnected.

Note: A diagram showing how the strain gauges are wired will be added soon.

### Material Mismatch

The material type may not match due to the g-code being generated on different systems. For instance, Linux-based systems have line endings defined by `lf` by default, whereas Windows uses `crlf` as the standard. This results in the printer giving a `Material type does not match. Gcode: None` error.

## Future

- [ ] Add a wiring diagram for strain gauges.
- [ ] Add Cooling duct STL.
- [ ] Add PrusaSlicer profiles for enhanced printing experience.
