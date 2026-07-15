# PYTHON_3_12_13::library/debug.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/debug.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Debugging and Profiling
***********************

These libraries help you with Python development: the debugger enables
you to step through code, analyze stack frames and set breakpoints
etc., and the profilers run code and give you a detailed breakdown of
execution times, allowing you to identify bottlenecks in your
programs. Auditing events provide visibility into runtime behaviors
that would otherwise require intrusive debugging or patching.

* Audit events table

* "bdb" --- Debugger framework

* "faulthandler" --- Dump the Python traceback

  * Dumping the traceback

  * Fault handler state

  * Dumping the tracebacks after a timeout

  * Dumping the traceback on a user signal

  * Issue with file descriptors

  * Example

* "pdb" --- The Python Debugger

  * Debugger Commands

* The Python Profilers

  * Introduction to the profilers

  * Instant User's Manual

  * "profile" and "cProfile" Module Reference

  * The "Stats" Class

  * What Is Deterministic Profiling?

  * Limitations

  * Calibration

  * Using a custom timer

* "timeit" --- Measure execution time of small code snippets

  * Basic Examples

  * Python Interface

  * Command-Line Interface

  * Examples

* "trace" --- Trace or track Python statement execution

  * Command-Line Usage

    * Main options

    * Modifiers

    * Filters

  * Programmatic Interface

* "tracemalloc" --- Trace memory allocations

  * Examples

    * Display the top 10

    * Compute differences

    * Get the traceback of a memory block

    * Pretty top

      * Record the current and peak size of all traced memory blocks

  * API

    * Functions

    * DomainFilter

    * Filter

    * Frame

    * Snapshot

    * Statistic

    * StatisticDiff

    * Trace

    * Traceback
