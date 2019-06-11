use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use std::collections::HashSet;

#[pyfunction]
/// Gets the count of the unique elements in a string
fn unique_count(val: &str) -> PyResult<usize> {
    let letters : HashSet<u8> = val.bytes().collect();
    Ok(letters.len())
}

/// This module is a python module implemented in Rust.
#[pymodule]
fn string_sum(_: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(unique_count))?;
    Ok(())
}