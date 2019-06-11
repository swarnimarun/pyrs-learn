# pyrs-learn
This is a simple lib for showcasing some results of Rust Module performance.

## Code Comparison

**Rust**

```rust
fn unique_count(val: &str) -> PyResult<usize> {
    let letters : HashSet<u8> = val.bytes().collect();
    Ok(letters.len())
}
```
**Python**
```python
def unique_count(val):
    ls = set(list(val))
    return len(ls)
```

This code assumes the system/core is the most optimized way of writing code(which in most cases is True) :P

## Performance

| Name (time in ms)  | Min      | Max      |  Mean    |  
|--------------------|----------|----------|----------|
| test_mod_rust      | 15.6655  | 18.4673  | 15.9664  |   
| test_pure_python   | 18.8871  | 21.4613  | 19.2286  |   


Now to put that in perspective, 

We see a 21% jump in Min Perf,
and then 16% jump in Max Perf,
and also 20% jump in Mean Performance.


This all might not mean much much on a small scale but on a scale where performance critical workload needs to be processed it means a lot.
And the best part is the code is almost the same and this took very little effort to actually get it ready.


#### PS: The Performance Noted from Rust is not the limit of it's performance, cause it's easy to vectorise and/or parallelise it can become multiple times faster and surely with control of a low level language we could always optimize the code a bit more.
