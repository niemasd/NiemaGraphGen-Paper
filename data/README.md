# GNU `time` Experiments (runtime + memory)
## Barabasi-Albert (BA)
### Expected Degree ≈ 10 → *m* = 5
```bash
# NiemaGraphGen
for n in 100 1000 10000 100000 1000000 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed10/time.ba.r$r.txt ~/NiemaGraphGen-Paper/tools/ngg_1.0.0/ngg_barabasi_albert $n 5 > /dev/null ; done ; done
```
