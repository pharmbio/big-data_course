# Data storage (5 points)

*Big Data in Life Science — re-exam 2026-08-17*

**(a) [1 p]** You have already transferred a 10 GB dataset to a remote server. You now edit a handful of lines in a couple of files and want to synchronize the changes to the server as efficiently as possible. Which tool is best suited for this?

- ☐ A. `scp`
- ☐ B. `sftp`
- ☐ C. `rsync`
- ☐ D. `wget`

**(b) [1 p]** Which of the following archive formats allows you to extract a single file from the archive *without* first decompressing everything else in it?

- ☐ A. `.gz` (gzip)
- ☐ B. `.tar.gz`
- ☐ C. `.zip`
- ☐ D. None of the above

**(c) [1 p]** On a shared HPC cluster you have access both to a network-mounted project directory and to a local scratch disk on the compute node. When running an analysis that reads a large dataset many times, why is it often recommended to first copy the data to the local scratch disk?

- ☐ A. The local scratch disk has more storage capacity than the network directory.
- ☐ B. Reading from a local disk is typically much faster than reading over the network.
- ☐ C. Files on the local scratch disk are automatically backed up.
- ☐ D. The local scratch disk supports more file formats than network storage.

**(d) [2 p]** In the Linux world, collections of files are commonly distributed as a single `.tar.gz` (or `.tgz`) archive. Explain in your own words what `tar` contributes, what `gzip` contributes, and *why* it is useful to combine them rather than using either one alone.

---

## Marking key

- **(a)** **C** — `rsync` transfers only the *differences* between source and destination.
- **(b)** **C** — `.zip` stores each file separately with an index, so entries can be listed and extracted individually. `.gz` compresses a single stream, and `.tar.gz` requires decompressing the whole tar stream to reach any file.
- **(c)** **B** — local-disk I/O is much faster than network I/O and avoids saturating shared bandwidth.
- **(d) [2 p]** Full credit for identifying that:
  1. `tar` **bundles** many files and directories into one archive file but does not compress;
  2. `gzip` **compresses** a single file/stream but cannot bundle;
  3. combining them gives you both — a single, compressed archive of many files.

  Half credit for correctly describing one of the two roles but not the trade-off / why-both.

**Point gradient:** three quick recognition/reasoning MCs across the three sub-topics (transfer, compression, storage), then a slightly meatier free-text that rewards students who can articulate the *why*.
