============================= test session starts =============================
platform win32 -- Python 3.7.0, pytest-4.6.2, py-1.8.0, pluggy-0.12.0
benchmark: 3.2.2 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: E:\Github\rspython\.test-env
plugins: benchmark-3.2.2
collected 2 items

Src\lookup.py ..                                                         [100%]


Computing stats ...Computing stats ... group 1/1Computing stats ... group 1/1: minComputing stats ... group 1/1: min (1/2)Computing stats ... group 1/1: min (2/2)Computing stats ... group 1/1: min (1/2)Computing stats ... group 1/1: min (2/2)Computing stats ... group 1/1: maxComputing stats ... group 1/1: max (1/2)Computing stats ... group 1/1: max (2/2)Computing stats ... group 1/1: max (1/2)Computing stats ... group 1/1: max (2/2)Computing stats ... group 1/1: meanComputing stats ... group 1/1: mean (1/2)Computing stats ... group 1/1: mean (2/2)Computing stats ... group 1/1: mean (1/2)Computing stats ... group 1/1: mean (2/2)Computing stats ... group 1/1: medianComputing stats ... group 1/1: median (1/2)Computing stats ... group 1/1: median (2/2)Computing stats ... group 1/1: median (1/2)Computing stats ... group 1/1: median (2/2)Computing stats ... group 1/1: iqrComputing stats ... group 1/1: iqr (1/2)Computing stats ... group 1/1: iqr (2/2)Computing stats ... group 1/1: iqr (1/2)Computing stats ... group 1/1: iqr (2/2)Computing stats ... group 1/1: stddevComputing stats ... group 1/1: stddev (1/2)Computing stats ... group 1/1: stddev (2/2)Computing stats ... group 1/1: stddev (1/2)Computing stats ... group 1/1: stddev (2/2)Computing stats ... group 1/1: opsComputing stats ... group 1/1: ops (1/2)Computing stats ... group 1/1: ops (2/2)Computing stats ... group 1/1: ops (1/2)Computing stats ... group 1/1: ops (2/2)Computing stats ... group 1/1: ops: outliersComputing stats ... group 1/1: ops: outliers (1/2)Computing stats ... group 1/1: ops: outliers (2/2)Computing stats ... group 1/1: ops: roundsComputing stats ... group 1/1: ops: rounds (1/2)Computing stats ... group 1/1: ops: rounds (2/2)Computing stats ... group 1/1: ops: iterationsComputing stats ... group 1/1: ops: iterations (1/2)Computing stats ... group 1/1: ops: iterations (2/2)--------------------------------------------------------------------------------- benchmark: 2 tests --------------------------------------------------------------------------------
Name (time in ms)         Min                Max               Mean            StdDev             Median               IQR            Outliers      OPS            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_mod_rust         15.6655 (1.0)      18.4673 (1.0)      15.9664 (1.0)      0.4342 (1.01)     15.8359 (1.0)      0.1872 (1.0)           7;9  62.6314 (1.0)          64           1
test_pure_python      18.8871 (1.21)     21.4613 (1.16)     19.2286 (1.20)     0.4307 (1.0)      19.0714 (1.20)     0.2374 (1.27)          8;8  52.0060 (0.83)         55           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
========================== 2 passed in 3.96 seconds ===========================
