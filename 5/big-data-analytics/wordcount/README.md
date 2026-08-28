# WordCount on Hadoop (pseudo-distributed)

This project runs the classic WordCount MapReduce job the Hadoop way on a single laptop:

1. HDFS stores the input and the output.
2. YARN schedules and runs the job.
3. A Mapper emits `(word, 1)` pairs.
4. A Reducer sums the counts per word.
5. A Combiner pre-aggregates at the mapper side.

## Architecture

| Component | Service | Web UI |
|---|---|---|
| NameNode | `hadoop-namenode.service` | http://localhost:9870 |
| DataNode | `hadoop-datanode.service` (also starts NodeManager) | — |
| ResourceManager | `hadoop-resourcemanager.service` | http://localhost:8088 |
| JobHistory Server | `hadoop-historyserver.service` | http://localhost:19888 |

The services run as the `hadoop` system user. The cluster is a real one-node cluster: HDFS has one DataNode with replication factor 1, YARN has one NodeManager with 6 GB of memory.

## Files

| File | Purpose |
|---|---|
| `WordCount.java` | The MapReduce program |
| `build.sh` | Compiles the Java and builds `wordcount.jar` |
| `run.sh` | Uploads input to HDFS, runs the job, prints the result |
| `input.txt` | Sample input text |

## Quick start

```bash
./build.sh   # compile WordCount.java -> wordcount.jar
./run.sh     # the Hadoop way: HDFS in, YARN job, HDFS out
```

`run.sh` uses these HDFS paths:

* Input: `/user/<you>/wordcount/input`
* Output: `/user/<you>/wordcount/output`

The output directory must not exist before the job runs. `run.sh` removes an old one automatically.

## Manual commands

```bash
# build
javac -cp "$(hadoop classpath)" -d classes WordCount.java
jar cf wordcount.jar -C classes .

# load input into HDFS
hdfs dfs -mkdir -p /user/$USER/wordcount/input
hdfs dfs -put input.txt /user/$USER/wordcount/input/

# run the job through YARN
hadoop jar wordcount.jar WordCount /user/$USER/wordcount/input /user/$USER/wordcount/output

# read the result from HDFS
hdfs dfs -cat /user/$USER/wordcount/output/part-r-00000 | sort
```

## Notes

* Tokenization is case-sensitive. `Big` and `big` are two different words.
* Word order in the output is not sorted. Hadoop emits keys in hash order.
  Sort the output with `sort` for reading.
* `yarn.nodemanager.vmem-check-enabled=false` disables the virtual-memory
  check. Modern JVMs reserve large virtual address spaces and can otherwise
  get their containers killed.
* To stop the cluster: `systemctl stop hadoop-namenode hadoop-datanode hadoop-resourcemanager hadoop-historyserver`
* To wipe the cluster: stop the services, delete `/var/lib/hadoop/dfs`,
  run `sudo -u hadoop hdfs namenode -format`, start the services again,
  and re-apply the HDFS `/tmp` permissions
  (`hdfs dfs -chmod 1777 /tmp /tmp/hadoop-yarn`).
  YARN stages job files under HDFS `/tmp`; without world-writable
  permissions, job submission fails with
  `Permission denied ... access=EXECUTE`.
