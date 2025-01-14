# Changelog

## 0.9.0 – 2024-05-10

- Document file format
- Adjust median calculation to be more robust
- Use masked arrays and default netCDF fill values
- Save array-type attributes as true arrays instead of strings
- Improve azimuth check in sun flag

## 0.8.3 – 2024-03-22

- Fix scan time for BLB files

## 0.8.2 – 2024-02-21

- Add documentation

## 0.8.1 – 2024-02-13

- Add exceptions.py
- Avoid mwr-multi processing if only one measurement

## 0.8.0 – 2024-02-08

- Improve LWP offset correction with humidity dependent threshold
- Adjust method for cloud detection
- Fix rolling mean calculation for plotting

## 0.7.1 – 2024-02-07

- Skip invalid files

## 0.7.0 – 2023-12-13

- Update lev2 quality flags and attributes
- Change lev2 indexing to allow combining products retrieved with different elevation angles
- Update thresholds for spectral retrieval

## 0.6.3 – 2023-12-05

- Use tempfiles

## 0.6.2 – 2023-12-05

- Optimize bit handling in level 2 processing

## 0.6.1 – 2023-12-04

- Fix package exports

## 0.6.0 – 2023-12-02

- Add flags to level 2 products
- Exclude scans in LWP offset correction
- Fix many warnings and typing issues

## 0.5.1 – 2023-09-12

- Fix `ir_zenith_angle` variable metadata

## 0.5.0 – 2023-09-11

- Support files with one measurement
- Merge spectral-product branch

## 0.4.3 – 2023-08-14

- Add `MissingInputData` exception

## 0.4.2 – 2023-08-14

- Skip files with only one measurement

## 0.4.1 – 2023-08-11

- Adjust file name parsing

## 0.4.0 – 2023-08-11

- Read coefficients from input
- Split ascii file reading to its own function
- Implement spectral product

## 0.3.1 – 2023-05-26

- Raise error if missing config files

## 0.3.0 – 2023-05-25

- Use correct key when checking height dimension
- Adjust lwp offset correction
- Fix command line usage

## 0.2.0 – 2023-05-16

- Read coefficients for all sites
- Add tests

## 0.1.8 – 2023-05-12

- Speed up the code

## 0.1.7 – 2023-05-11

- Fix time unit issues

## 0.1.6 – 2023-05-10

- Fix bug in lwp offset calculation

## 0.1.5 – 2023-05-08

- Comment suspicious timezone conversion to make tests pass
- Test with Python 3.11

## 0.1.4 – 2023-05-08

- Update MANIFEST.in

## 0.1.3 – 2023-05-08

- Add py.typed

## 0.1.2 – 2023-05-02

- Add MANIFEST.in

## 0.1.1 – 2023-05-02

- First release

## 0.1.0 – 2023-05-02

Initial version
