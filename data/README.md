# GNU `time` Experiments (runtime + memory)
## Barabasi-Albert (BA)
Expected Degree = *m*/2

```bash
# NiemaGraphGen
for n in 100 1000 10000 100000 1000000 ; do for ed in 10 20 40 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed$ed/time.ba.ngg.r$r.txt ~/NiemaGraphGen-Paper/tools/ngg_1.0.0/ngg_barabasi_albert $n $(echo "$ed / 2" | bc -l) > /dev/null ; done ; done ; done

# NetworkX (n = 1000000 took more than 2 GB of RAM)
for n in 100 1000 10000 100000 ; do for ed in 10 20 40 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed$ed/time.ba.nx.r$r.txt ~/NiemaGraphGen-Paper/tools/nx_2.5.1/nx_barabasi_albert.py $n $(echo "$ed / 2" | bc -l) > /dev/null ; done ; done ; done

# iGraph
for n in 100 1000 10000 100000 1000000 ; do for ed in 10 20 40 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed$ed/time.ba.ig.r$r.txt ~/NiemaGraphGen-Paper/tools/ig_0.9.4/ig_barabasi_albert.py $n $(echo "$ed / 2" | bc -l) > /dev/null ; done ; done ; done
```

## Erdos-Renyi (ER)
Expected Degree = *np*
```bash
# NiemaGraphGen
for n in 100 1000 10000 100000 1000000 ; do for ed in 10 20 40 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed$ed/time.er.ngg.r$r.txt ~/NiemaGraphGen-Paper/tools/ngg_1.0.0/ngg_erdos_renyi $n $(echo "$ed / $n" | bc -l) > /dev/null ; done ; done ; done

# NetworkX
for n in 100 1000 10000 100000 1000000 ; do for ed in 10 20 40 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed$ed/time.er.nx.r$r.txt ~/NiemaGraphGen-Paper/tools/nx_2.5.1/nx_erdos_renyi.py $n $(echo "$ed / $n" | bc -l) > /dev/null ; done ; done ; done

# iGraph
for n in 100 1000 10000 100000 1000000 ; do for ed in 10 20 40 ; do for r in $(seq -w 1 10); do /usr/bin/time -v -o n$n/ed$ed/time.er.ig.r$r.txt ~/NiemaGraphGen-Paper/tools/ig_0.9.4/ig_erdos_renyi.py $n $(echo "$ed / $n" | bc -l) > /dev/null ; done ; done ; done
```

## Newman-Watts-Strogatz (NWS)
Expected Degree = (*n*(Lattice Degree)/2 + (*n* choose 2)*p*) / *n*

Lattice Degree = (20(Expected Degree) - *n* + 1)/10
