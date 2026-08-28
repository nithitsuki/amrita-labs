# Assignment 01 — WordCount on the Bee Movie script

**Result:** Hadoop pseudo-distributed (1-node cluster on this laptop) counted
**2,923 unique words** in the Bee Movie script (49 KB, 1,363 lines).
Every count matches a ground-truth check (`sort | uniq -c` on the local file) exactly.

```
input (HDFS)  ──▶  YARN job  ──▶  output (HDFS)
/user/nithilan/wordcount/bee-input   /user/nithilan/wordcount/bee-output
```

## Commands (the Hadoop way)

```bash
hdfs dfs -mkdir -p /user/nithilan/wordcount/bee-input
hdfs dfs -put bee-movie-script.txt /user/nithilan/wordcount/bee-input/
hadoop jar wordcount.jar WordCount /user/nithilan/wordcount/bee-input \
                                  /user/nithilan/wordcount/bee-output
hdfs dfs -cat /user/nithilan/wordcount/bee-output/part-r-00000 | sort
```

Job `job_1786676676927_0002` completed successfully (1 map task, 1 reduce task,
~21 seconds). Top words: `a 241, I 235, the 224, to 183, you 148, of 131, is 93`.

## What exactly is going on

1. **HDFS split.** Hadoop reads the input file from HDFS and splits it into
   input splits (one file, one split here). Each split becomes one map task.
2. **Map.** `TokenizerMapper` receives each line as `(key=byte offset, value=line)`.
   It splits the line on whitespace and emits `(word, 1)` for every word.
3. **Combine.** The combiner (same code as the reducer) pre-sums counts on the
   map side: `(the, 1)(the, 1)(the, 1)` becomes `(the, 3)` locally. Less data
   crosses the network.
4. **Shuffle and sort.** Hadoop groups all `(word, 1)` pairs by key. All pairs
   with the same word land in the same reducer, sorted by key.
5. **Reduce.** `IntSumReducer` receives `(word, [1, 1, 1, ...])` and writes
   `(word, total)` once per word to `part-r-00000` on HDFS.
6. **Result.** The output file is one line per word: `word<TAB>count`.
   The partitioner decides which reducer gets which word (hash of the key).

The whole pipeline runs inside YARN containers on this laptop — one
NodeManager hosts the map and reduce containers, scheduled by the
ResourceManager. That is the same architecture a real cluster uses; here the
cluster has exactly one node.

## Files

| File | Purpose |
|---|---|
| `../wordcount/WordCount.java` | Mapper, Combiner, Reducer, job driver |
| `../wordcount/bee-movie-script.txt` | Input data (downloaded gist) |
| `../wordcount/build.sh`, `run.sh` | Build jar; run a demo job |
