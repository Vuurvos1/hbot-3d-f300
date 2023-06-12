# HBOT 3D F300

This repository contains Simplify 3D profiles and manuals in both English and Polish for the HBOT 3D F300 printer. Additionally, and it documents some of the troubleshooting steps I had to take to fix the 3D printer.

If the print head runs into the build plate while leveling. This issue could very well be related to one or more of the strain gauges beeing broken or disconnected.

## Importing profiles

### Prusa Slicer

Goto `File > Import > Import Config Bundle...` and select one of the profiles inside the PrusaSlicer folder.

## Known Issues

### Prusa Slicer

When exporting gcode with Prusa slicer all line endings will always be of type `lf` something which this printer does not support, this can be fixed by setting a postprocessor under output options like the following

**Windows**

```
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -File "<path to file>\PrusaSlicer\line_ending_postprocessor.ps1"
```

_Note:_
I tried using gcode substitutions but this sadly doesn't seem to puck up on the `cr` character and inserts `lf` line endings instead

### Bed leveling Issue

One I faced while repairing this printer was that the print head rams into the build plate while leveling. This issue is most likely related to one or more of the strain gauges inside the print head being broken or disconnected.

Note: A diagram showing how the strain gauges are wired will be added soon.

### Material Mismatch

The material type may not match due to the g-code being generated on different systems. For instance, Linux-based systems have line endings defined by `lf` by default, whereas Windows uses `crlf` as the standard. This results in the printer giving a `Material type does not match. Gcode: None` error.

## Future

- [ ] Add a wiring diagram for strain gauges.
- [ ] Improve PrusaSlicer profiles for better printing results.
