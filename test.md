============================= test session starts =============================
platform win32 -- Python 3.7.0, pytest-4.6.2, py-1.8.0, pluggy-0.12.0
benchmark: 3.2.2 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: E:\Github\rspython\.test-env
plugins: benchmark-3.2.2
collected 2 items

Src\lookup.py ..                                                         [100%]



Name (time in ms)          Min                 Max                Mean            StdDev              Median               IQR            Outliers      OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_mod_rust          15.6393 (1.0)       17.5906 (1.0)       15.9078 (1.0)      0.2887 (1.0)       15.8205 (1.0)      0.1419 (1.0)           6;6  62.8621 (1.0)          64           1
test_pure_python      656.5403 (41.98)    658.1508 (37.41)    657.2557 (41.32)    0.5784 (2.00)     657.2002 (41.54)    0.5302 (3.74)          2;0   1.5215 (0.02)          5           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
========================== 2 passed in 7.47 seconds ===========================