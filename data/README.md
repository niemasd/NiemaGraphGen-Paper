# GNU `time` Experiments (runtime + memory)
## Barabasi-Albert (BA)
### Expected Degree ≈ 10 → *m* = 5
```bash
# NiemaGraphGen
for n in 100 1000 10000 100000 1000000 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed10/time.ba.ngg.r$r.txt ~/NiemaGraphGen-Paper/tools/ngg_1.0.0/ngg_barabasi_albert $n 5 > /dev/null ; done ; done

# NetworkX (n = 1000000 took more than 2 GB of RAM)
for n in 100 1000 10000 100000 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed10/time.ba.nx.r$r.txt ~/NiemaGraphGen-Paper/tools/nx_2.5.1/nx_barabasi_albert.py $n 5 > /dev/null ; done ; done

# iGraph
for n in 100 1000 10000 100000 1000000 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed10/time.ba.ig.r$r.txt ~/NiemaGraphGen-Paper/tools/ig_0.9.4/ig_barabasi_albert.py $n 5 > /dev/null ; done ; done
```

### Expected Degree ≈ 20 → *m* = 10
```bash
# NiemaGraphGen
for n in 100 1000 10000 100000 1000000 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed20/time.ba.ngg.r$r.txt ~/NiemaGraphGen-Paper/tools/ngg_1.0.0/ngg_barabasi_albert $n 10 > /dev/null ; done ; done

# NetworkX (n = 1000000 took more than 2 GB of RAM)
for n in 100 1000 10000 100000 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed20/time.ba.nx.r$r.txt ~/NiemaGraphGen-Paper/tools/nx_2.5.1/nx_barabasi_albert.py $n 10 > /dev/null ; done ; done

# iGraph
for n in 100 1000 10000 100000 1000000 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed20/time.ba.ig.r$r.txt ~/NiemaGraphGen-Paper/tools/ig_0.9.4/ig_barabasi_albert.py $n 10 > /dev/null ; done ; done
```

### Expected Degree ≈ 40 → *m* = 20
```bash
# NiemaGraphGen
for n in 100 1000 10000 100000 1000000 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed40/time.ba.ngg.r$r.txt ~/NiemaGraphGen-Paper/tools/ngg_1.0.0/ngg_barabasi_albert $n 20 > /dev/null ; done ; done

# NetworkX (n = 1000000 took more than 2 GB of RAM)
for n in 100 1000 10000 100000 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed40/time.ba.nx.r$r.txt ~/NiemaGraphGen-Paper/tools/nx_2.5.1/nx_barabasi_albert.py $n 20 > /dev/null ; done ; done

# iGraph
for n in 100 1000 10000 100000 1000000 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed40/time.ba.ig.r$r.txt ~/NiemaGraphGen-Paper/tools/ig_0.9.4/ig_barabasi_albert.py $n 20 > /dev/null ; done ; done
```

## Erdos-Renyi (ER)
```bash
# NiemaGraphGen
for n in 100 1000 10000 100000 1000000 ; do for ed in 10 20 40; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed$ed/time.ba.ngg.r$r.txt ~/NiemaGraphGen-Paper/tools/ngg_1.0.0/ngg_erdos_renyi $n $(echo "$ed / $n" | bc -l) > /dev/null ; done ; done ; done
```
