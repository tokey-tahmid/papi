* 2025-08-28 tokey-tahmid — adding release script
* 2025-08-15 Treece Burgess — rocp_sdk: Update component tests to enumerate through available events and add them if none of the desired events can be added.
* 2025-08-15 Treece Burgess — Add if defined's around current_socket_power sections to avoid compilation errors in ROCm < 6.0.
* 2025-08-04 Treece Burgess — Updates for event descriptions, comments, and conditional checks for access_rsmi_dev_energy_count and access_rsmi_dev_current_socket_power.
* 2025-06-13 Adam McDaniel — Removed unused `offset` field used to store the initial timestep once the profiling began for energy collection
* 2025-06-13 Adam McDaniel — Added forward declarations for access
* 2025-06-13 Adam McDaniel — Exposed the energy count and current socket power metrics to the profiler
* 2025-08-02 Treece Burgess — cuda: Add newline for SUBDBG message in cuda_stop
* 2025-07-25 Heike Jagode — Update README.md
* 2025-07-25 Heike Jagode — Update LICENSE.txt
* 2025-08-01 Adrien M. BERNEDE — genpapifdef: Get perl from env instead of hard-coded path
* 2025-07-24 Anthony Danalis — ROCP_SDK: Allow different ROCprofiler-SDK installation paths.
* 2025-07-27 Treece Burgess — Cuda: For the CTC metrics, add a note to each metrics description that they are unable to be profiled with the Perfworks API that the cuda component uses.
* 2025-07-25 Treece Burgess — net: Update the test net_values_by_name.c to successfully run and not use hard coded events.
* 2025-07-17 Heike Jagode — Added preferred citation to README.md
* 2025-07-15 Treece Burgess — configure.in: Remove flag --with-libpfm4 from cross compile sample comment
* 2025-07-14 Treece Burgess — rocm_smi: Update tests/Makefile to properly link with existing LDFLAGS e.g. -lrt
* 2025-07-11 Treece Burgess — papi_avail.c: Move print statement for final format line to output even if a component that supports presets is not given.
* 2025-07-10 Anthony Danalis — SDE: update test Makefile to properly use LDFLAGS.
* 2025-07-03 Daniel Barry — framework: correct PAPI_PRESET_ENUM_AVAIL behavior
* 2025-07-03 Treece Burgess — Remove bitbucket-pipelines.yml as PAPI CI is ran through GitHub now with Actions.
* 2025-06-26 Treece Burgess — PAPI_num_events: Remove ifdef that is triggered if debug mode is set.
* 2025-06-26 Treece Burgess — ChangeLogs: Move the ChangeLogs to a new directory in root named ChangeLogs.
* 2025-06-27 Treece Burgess — Bump version number from 7.2.0 to 7.2.1 after the release.
* 2025-06-25 Treece Burgess — Updated ChangeLog and RELEASENOTES for PAPI release 7.2.0.
* 2025-06-25 Treece Burgess — The version numbers for doc/Doxyfile-common, papi.spec, src/Makefile.in, src/configure.in, and src/papi.h have been updated.
* 2025-06-13 Heike Jagode — Prepared Release Notes for PAPI 7.2.0 release.
* 2025-06-17 Treece Burgess — rocm: Skip the test sample_overflow_monitoring.cpp.
* 2025-06-20 Anthony Danalis — ROCP_SDK: Ensure env variables are always respected.
* 2025-06-20 Anthony Danalis — ROCP_SDK: Improve the file/dir check to skip "." and "."
* 2025-06-20 Anthony Danalis — ROCP_SDK: use path instead of hsa to test for devices.
* 2025-06-16 Daniel Barry — rocm: fix segmentation fault in component test
* 2025-06-12 Gerald Ragghianti — rocm/rocm_smi: Allow users to optionally set HIPCC.
* 2025-06-10 Treece Burgess — cuda/rocm components: Restructure update_native_events to not call realloc on a size of 0.
* 2025-06-11 Treece Burgess — configure: Add a warning message if rocm and rocp_sdk are configured together.
* 2025-06-04 Treece Burgess — RAPL Component: Add support in RAPL for Intel Emerald Rapids. Note at this time the PAPI team does not have access to a machine with an Intel Emerald Rapids CPU to verify this addition.
* 2025-06-12 Treece Burgess — rocp_sdk: In the tests Makefile account for CPU agents on amd64.
* 2025-06-12 Daniel Barry — intel_gpu: update environment variable name
* 2025-06-10 Daniel Barry — framework: force init per existing policy
* 2025-06-07 Treece Burgess — intel_gpu: Remove -DDEBUG from Rules.intel_gpu.
* 2025-06-06 Treece Burgess — rocm: Update the component README.md to account for new limitations.
* 2025-06-09 Treece Burgess — sysdetect: Add newline characters to the SUBDBG messages.
* 2025-06-06 Anthony — ROCM: PAPI_strerror() cannot be used at shutdown.
* 2025-06-05 Treece Burgess — PAPI_list_events: Update functions documentation to match the function protoype.
* 2025-06-04 Anthony Danalis — ROCP_SDK: Handle case where all events are removed.
* 2025-06-03 Treece Burgess — rocp_sdk: Remove assignment of info->event_code and info->component_index in rocp_sdk as it is already done in papi_internal.c.
* 2025-06-02 Treece Burgess — PAPI Presets: Update AMD Family 17h to account for PMCx080 and PMCx081 reporting incorrect IC accesses and misses respectively. PMCx060 unit mask 0x10 replaces PMCx081, but there is no suitable replacement for PMCx080 therefore those instances are removed.
* 2025-05-29 Treece Burgess — Various Components: Use only PAPI memory allocation or C memory allocation to avoid possible segmentation faults.
* 2025-06-02 Treece Burgess — rocm_smi/rocp_sdk: Restructure init_private functions to avoid setting initialized equal to 1 even when initialization fails.
* 2025-05-29 Treece Burgess — Sysdetect/Topdown/Infiniband/NVML Components: Properly set .size in a components vector to avoid possible Error! PAPI_library_init.
* 2025-05-27 Treece Burgess — lmsensors component: Remove restriction on the events chosen to be added to an eventset for the test lmsensors_read.c.
* 2025-05-27 Treece-Burgess — Update libpfm4 Current with commit 0727e5f5561101d8c635a36e139dd7512616d49e Author: Vince Weaver <vincent.weaver@maine.edu> Date:   Fri May 23 17:32:23 2025 -0700
* 2025-05-23 Treece Burgess — lmsensors component: Replace fprintf with SUBDBG.
* 2025-05-19 Treece Burgess — Cuda component: Initialize count variable in function cuda_init_private.
* 2025-05-23 Anthony Danalis — ROCP_SDK: More verbose debug messages.
* 2025-05-23 Anthony Danalis — ROCP_SDK: Do not overwrite library in PAPI_ROCP_SDK_LIB.
* 2025-05-23 Anthony Danalis — ROCP_SDK: Cleanup dlopen() error handling.
* 2025-05-21 Daniel Barry — framework: proper memory management functions
* 2025-05-20 Anthony — ROCM_SMI: Added -pthread flag in tests/Makefile.
* 2025-05-20 Treece Burgess — utils/print_header.c: Move for loop counter declaration out of for loop header.
* 2025-05-18 G-Ragghianti — Adding multiple search path functionality for libhsa
* 2025-05-16 Treece Burgess — Remove perfctr and perfctr_ppc documentation from src/components README.
* 2025-05-13 Daniel Barry — utils: fix compiler warnings for papi_avail.c
* 2025-05-13 Daniel Barry — utils: convert tabs in papi_avail.c to spaces
* 2025-05-14 Anthony Danalis — HEADERS: __FILE__ is "const char *", not "char *"
* 2025-05-14 Anthony Danalis — ROCP_SDK: protect the included papi headers from C++
* 2025-05-13 Treece Burgess — Cuda component: Update tests to more gracefully handle multiple pass events.
* 2025-05-13 Anthony Danalis — ROCP_SDK: Update README with linking limitations.
* 2025-05-12 Treece Burgess — Appio Component: Add a component description, as it is missing from papi_component_avail
* 2025-05-12 Treece Burgess — ROCm component: Bug fix for typo in rocm_verify_no_repeated_qualifiers.
* 2025-05-10 Treece Burgess — Update configure.in to have a default value for --with-debug if not provided by a user.
* 2025-05-06 Treece Burgess — Configure: Correctly output the tests chosen by a user with --with-tests.
* 2025-05-08 Treece Burgess — Cuda component: Properly set return value in cuptid_init.
* 2024-11-07 Daniel Barry — utils: papi_avail extension for component presets
* 2024-11-07 Daniel Barry — utils: new modifiers for strictly CPU presets
* 2024-10-31 Daniel Barry — utils: convert tabs to spaces in papi_avail.c
* 2024-10-31 Daniel Barry — framework: support for component presets
* 2024-10-31 Daniel Barry — config: updates for component presets
* 2024-10-28 Daniel Barry — presets: support for NVIDIA Hopper and Ampere
* 2024-10-28 Daniel Barry — cuda: updates for presets
* 2024-10-31 Daniel Barry — framework: fields for component presets
* 2024-12-20 Dandan Zhang — Add loongarch64 support
* 2025-05-06 Treece Burgess — ROCm component: Add stricter qualifiers checks.
* 2025-05-06 Treece Burgess — Cuda component: Add stricter qualifiers checks.
* 2025-05-05 Treece Burgess — Coretemp: Enable support for multiplexing.
* 2025-05-06 Anthony Danalis — ROCP_SDK: Improved handling of pathological paths.
* 2025-05-03 Treece Burgess — Cuda component: Replace int typing with long long to avoid overflow with measured values.
* 2025-05-06 Anthony Danalis — ROCP_SDK: Force fail if PAPI_ROCP_SDK_LIB is bogus.
* 2025-05-05 Anthony Danalis — ROCP_SDK: Suppress ROCprofiler-SDK warnings.
* 2025-05-05 Anthony Danalis — ROCP_SDK: Enable default dlopen() paths, and cleaner error handling.
* 2025-05-05 Anthony Danalis — ROCP_SDK: Move dlclose() to component finalization.
* 2025-04-29 Anthony Danalis — ROCP_SDK: call configure_device_counting_service as early as possible.
* 2025-04-24 Treece Burgess —  Cuda component: Update the error checks in the test test_multipass_event_fail to PASS even when events that do not require multiple passes are provided.
* 2025-04-30 Treece Burgess — Cuda component: Add functionality for a partially disabled Cuda component for CCs >= 7.0 (Perfworks API).
* 2025-04-28 Dong Jun Woun — rocm_smi: Add proper fan_speed access, control, and return
* 2025-04-29 Treece Burgess — Cuda/NVML Components: Check for variation of shared objects e.g. libcudart.so, libcudart.so.1 or libcudart (catch all).
* 2025-04-28 Dong Jun Woun — rocm_smi: Update read/write test
* 2025-04-29 Treece-Burgess — perf_event: Disable component if perf_event_paranoid is set to 4 in /proc/sys/kernel/perf_event_paranoid.
* 2025-04-29 Treece-Burgess — Cuda component: Refactor to support the MetricsEvaluator API (Cuda Versions 11.3 and greater).
* 2025-04-23 Anthony Danalis — ROCP_SDK: Accomodate machines with fewer AMD GPUs.
* 2025-02-26 Yoshihiro Furudera — Remove some preset events for FUJITSU-MONAKA
* 2024-09-19 Akio Kakuno — papi_events.csv: Add preset events support for FUJITSU-MONAKA
* 2025-04-20 Willow Cunningham — topdown: Use librseq to protect rdpmc on het cpus
* 2025-04-22 Dong Jun Woun — cuda: Adding stat|device case to code_to_info
* 2025-04-22 Anthony — .SPEC: Logic for setting rocm_smi env. variables.
* 2025-04-18 Daniel Barry — components: improper usage of PAPI_END macro
* 2024-08-21 Daniel Barry — rocm: add reason for disabled component
* 2025-04-18 Daniel Barry — rocm_smi: updates to Makefile
* 2025-04-17 Treece Burgess — For the stats qualifier check for excess characters
* 2025-01-08 Treece Burgess — Add a check to parse event qualifiers to make sure no excess characters are appended.
* 2024-12-13 Treece Burgess — Add support for Intel Comet Lake S/H in RAPL component.
* 2025-04-16 voidbert — perf_event_uncore: fix compilation when CAP_PERFMON is missing
* 2024-11-04 Daniel Barry — cat: updates in vector-FLOPs benchmarks
* 2025-01-22 William Cohen — Eliminate conflicting type errors generated by GCC15
* 2024-11-09 Dong Jun Woun — Cuda: Statistic Qualifier
* 2024-01-18 Evans, Richard Todd — added Sapphire Rapids (Model 143) support to RAPL component
* 2024-09-25 Willow Cunningham — papi_events.csv: Added preset events for the Arm Cortex A72 processor.
* 2025-02-21 Willow Cunningham — papi_events.csv: Second pass at arm cortex-a76 events
* 2024-10-11 Willow Cunningham — validation_tests: Add load/store ARM assembly testcode
* 2024-10-11 Willow Cunningham — papi_events: Add preset events for the Arm Cortex-A76
* 2025-01-17 Willow Cunningham — topdown: simplified metrics calculation
* 2025-01-07 Willow Cunningham — topdown: relocated core type checks
* 2024-12-17 Willow Cunningham — topdown: stop including x86intrin.h
* 2024-12-11 Willow Cunningham — topdown: Prevent segfault on heterogeneous CPUs
* 2024-12-04 Willow Cunningham — topdown: add arch support based on perfmon-intel
* 2024-11-11 Willow Cunningham — topdown: Created a component for interfacing with Intel's PERF_METRICS MSR
* 2024-06-28 voidbert — perf_event_uncore: consider capabilities for permissions
* 2025-02-27 Dong Jun Woun — rocm_smi: Update readme to note two cases of root path
* 2025-03-27 G-Ragghianti — Include the comp_tests in the list of tests that are enabled by the '--with-tests' configure option
* 2025-03-20 Treece Burgess — Using paths-ignore instead of paths for framework workflow
* 2025-03-18 Treece Burgess — Remove infiniband from the papi_components_comprehensive CI test
* 2025-03-20 Anthony Danalis — ROCP_SDK: Change tests/Makefile for spack builds.
* 2025-03-05 G-Ragghianti — Adding location of rocm_smi header files for newer versions of rocm
* 2025-02-24 Anthony Danalis — Updated Changelog for 7.2.0b2 and RELEASENOTES.
* 2025-02-24 Anthony Danalis — Updated configure.
* 2025-02-24 Anthony Danalis — Updated documentation.
* 2025-02-24 Anthony Danalis — Version updated for releasing 7.2.0b2
* 2025-02-24 Treece Burgess — Add support for heterogeneous systems in the Cuda component.
* 2025-02-21 Anthony — Changing example files to accomodate Windows.
* 2025-02-12 Dong Jun Woun — rocm_smi: Initial event count and event table initialization event count upper bound mismatch & handling unsupported events
* 2025-02-19 Anthony Danalis — Ensure context is valid and active when stopping
* 2025-02-13 Treece Burgess — Remove maxPassCount from calculate_num_passes. Add further documentation for maxPassCount behavior.
* 2025-02-12 Anthony Danalis — Propagate error when obtaining function pointers.
* 2025-02-11 Treece Burgess — Update libpfm4 Current with commit 762ca94010d9a8f21f0440c0b5807e9a2e849420 Author: Stephane Eranian <eranian@gmail.com> Date:   Sat Oct 19 15:34:10 2024 -0700
* 2025-02-10 Anthony Danalis — Updated variable names for uniformity.
* 2025-02-05 Anthony Danalis — Version information.
* 2025-02-05 Anthony Danalis — README file.
* 2025-02-04 Anthony Danalis — rocprofiler_configure() can be called before PAPI_library_init()
* 2025-02-04 Anthony Danalis — Added author information to files.
* 2025-01-31 Anthony Danalis — Default value for qualifier "device".
* 2024-09-23 Anthony Danalis — ROCP_SDK: Enabling device profiling mode.
* 2025-02-10 Bill Williams — rocp_sdk: add missing srcfile
* 2025-01-30 Treece Burgess — Update libpfm4 Current with commit 7750d00833a607eeb53c9a6832ffa8a6b827cdb9 Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Jan 27 16:35:05 2025 -0800
* 2025-01-27 Treece Burgess — Updating error message for function check_exclude_guest() in perf_event.c.
* 2025-01-17 Treece Burgess — Restructure configure and configure.in to avoid errors: cuda.h no such file and integer expression expected on Power 9 and Power 10.
* 2025-01-31 Treece Burgess — Replace actions/upload-artifact@v3 with actions/upload-artifact@v4.
* 2024-12-18 Treece Burgess — Updating papi_events.csv to support addition of L1I_CACHE and deprecation of L1I_CACHE_ACCESS in libpfm4.
* 2024-12-14 Treece Burgess — Update libpfm4 Current with commit d22403ec9bddaf62c59d847904918b30db69550d Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Dec 13 00:42:42 2024 -0800
* 2025-01-28 Treece Burgess — Update run_tests.sh to remove bash specific syntax.
* 2024-10-10 Willow Cunningham — perf_event: Eliminate permission error for check_exclude_guest() with paranoid kernel
* 2024-11-12 Daniel Barry — cat: remove error return value
* 2024-11-12 Daniel Barry — cat: add newlines to error messages
* 2024-11-12 Daniel Barry — cat: remove unnecessary cleanup call
* 2025-01-08 Treece Burgess — Fixing bug in counter analysis toolkit workflow
* 2025-01-06 Treece Burgess — Updating the PAPI GitHub CI, see README for more details on structure.
* 2024-12-11 Daniel Barry — intel_gpu: remove unnecessary linker flags
* 2024-12-11 Daniel Barry — configure: -pthread with intel_gpu
* 2024-12-13 Treece Burgess — Adding tests for the lmsensors component.
* 2024-11-26 Treece Burgess — Update libpfm4 Current with commit 5e26b48b6d9b9d5f8c368c81cfe23a54a129bd24 Author: Yoshihiro Furudera <fj5100bi@fujitsu.com> Date:   Thu Oct 3 16:25:55 2024 +0900
* 2024-11-06 Treece Burgess — Add support for AMD family 25 (19h) processors in the RAPL component. Tested on Family/Model/Stepping: - 25/1/1 - 25/48/1 - 25/17/1 - 25/144/1 - 25/97/2
* 2024-11-21 Treece Burgess — Update all_native_events.c and get_event_component.c to take an optional flag --disable-cuda-events=<yes,no> to disable processing of Cuda native events.
* 2024-12-02 Dong Jun Woun — Disable perf_event, perf_events_uncore, and cpu
* 2024-11-27 Willow Cunningham — rapl: fixed indentation (spaces->tabs)
* 2024-11-14 Willow Cunningham — rapl: Add support for RaptorLake
* 2024-11-12 Willow Cunningham — fixed indentation
* 2024-09-19 Willow Cunningham — rapl: Added RAPL component support for Intel RaptorLake.
* 2024-11-15 Treece Burgess — Update libpfm4 Current with commit 91970fe6eb4e80b63f77fb54a9592e28a207050c Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Oct 4 21:49:47 2024 -0700
* 2024-11-21 Dong Jun Woun — remove unecessary linking
* 2024-10-04 William Cohen — lmsensors: Avoid possible overruns on local variable
* 2024-10-04 William Cohen — thread: Properly free memory in case of malloc failure in allocate_thread
* 2024-10-04 William Cohen — sysdetect: Ensure that a variable in get_cache_type is always initialized
* 2024-10-04 William Cohen — infiniband: Ensure that memory allocated by strdup() freed
* 2024-11-12 Daniel Barry — presets: remove PAPI_FP_OPS from POWER9 & POWER10
* 2024-10-16 Treece Burgess — Removing -lpthread flag inplace of -pthread and adding -pthread to concurrent_profiling to build correctly on glibc < 2.34.
* 2024-11-11 Treece Burgess — Updating gitlog2changelog.py to add command line arguments and updating the text in release_procedures.txt.
* 2024-10-30 Anthony — CAT: More instruction tests and cleaner output.
* 2024-10-29 Anthony — CAT: New instruction benchmarks for FMA and Int.
* 2024-10-29 Jeevitha Palanisamy — PAPI power10 event list presets
* 2024-10-16 Treece Burgess — Allow for a user to supply just the base cuda native event name. Defaults to cuda_ntv_name:device=0.
* 2024-10-24 Treece Burgess — Updating the ordering of conditional checks in functions to load library files.
* 2024-10-17 Willow Cunningham — counter_analysis_toolkit: use 'ifndef' for more idiomatic code
* 2024-10-01 Willow Cunningham — counter_analysis_toolkit: Added automatic architecture detection to the Makefile
* 2024-10-23 Anthony — sysdetect: accounting for missing core ids.
* 2024-10-16 Willow Cunningham — validation_tests: Add -O1 optimization flag to matrix_multiply.o
* 2024-10-17 Anthony Danalis — Sysdetect: allow users to disable component.
* 2024-10-17 Treece Burgess — Update Makefile.in to have PAPI version 7.2.0.0b1.
* 2024-09-20 Heike Jagode — Link with CXX instead of CC macro
* 2024-09-24 Treece Burgess — Update Cuda component to add a device qualifier. As of Cuda Version 12.6, the MetricsContext API has been removed and replaced with the MetricsEvaluator API. Due to this change, the Cuda component will only work with Cuda versions < 12.6. The PAPI team will be working to support both the MetricsContext API and MetricsEvaluator API.
* 2024-10-11 Daniel Barry — run_tests.sh: change libpfm-3.y to libpfm4
* 2024-02-16 Daniel Barry — papi_mem_info: add support for ARM Neoverse V2
* 2024-02-15 Daniel Barry — papi_mem_info: check for newlines in sysfs files
* 2024-02-15 Daniel Barry — papi_mem_info: convert tabs to spaces
* 2024-09-19 Daniel Barry — intel_gpu: properly reset metrics
* 2024-09-19 Daniel Barry — intel_gpu: remove extraneous check for group
* 2024-09-19 Daniel Barry — intel_gpu: allow larger number of groups
* 2024-10-07 William Cohen — high-level: Explicitly use python3 and place shebang on the first line
* 2024-10-02 Treece Burgess — Update papi_hl_output_writer.py to use 4 spaces instead of 2 for code formatting and add Doxygen documentation to classes and functions.
* 2024-10-04 Treece Burgess — Correcting documentation in PAPI_add_named_event.
* 2024-06-26 William Cohen — utils: Include the compiler flags when linking the PAPI utilities
* 2023-03-27 Giuseppe Congiu — rocm_smi: rename special cases to derived events
* 2024-09-23 Treece Burgess — Update disabled reason if rocm init is successful.
* 2024-09-26 Anthony Danalis — CUDA Tests: Conditionally adding -fpic to nvcc.
* 2024-09-23 Treece Burgess — Update libpfm4 Current with commit c89a379175c00a20bbc660ad9b444e8ecc16cd28 Author: Stephane Eranian <eranian@gmail.com> Date:   Sat Sep 21 21:11:10 2024 -0700
* 2024-09-19 Treece Burgess — Update libpfm4 Current with commit 0118612a28d270e78d1f17c24e9db0935e332285 Author: Stephane Eranian <eranian@gmail.com> Date:   Tue Sep 17 16:36:24 2024 -0700
* 2024-09-17 Treece Burgess — Update libpfm4 Current with commit 3724e7ef87e71dd1de46ef4eb4ec2b1be4ea63e5 Author: Stephane Eranian <eranian@gmail.com> Date:   Sun Sep 15 22:29:37 2024 -0700
* 2024-09-05 Anthony Danalis — Better support for multiple eventsets and multiple devices.
* 2024-09-12 Treece Burgess — Update libpfm4 Current with commit 9c5c88e734e866f0801b80c527330ad6dbe21e89 Author: Stephane Eranian <eranian@gmail.com> Date:   Tue Sep 10 23:58:35 2024 -0700
* 2024-08-26 Dong Jun Woun — run_tests.sh : Test only active components
* 2024-08-01 Treece Burgess — Removing unneeded + from NVCFLAGS assignment.
* 2024-07-29 Treece Burgess — Removing conditional check for -arch=native flag.
* 2024-08-26 Daniel Barry — rocm: fix typo in component tests
* 2024-09-03 Treece Burgess — Update libpfm4 Current with commit 0d799b5546477a46b3a52310bbf1884d56e9e37f Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Sep 2 21:51:03 2024 -0700
* 2024-08-19 Daniel Barry — cuda: fix typo in README
* 2024-09-06 djwoun — Update README.md
* 2024-09-05 G-Ragghianti — Fixing cuda version to highest currently supported
* 2024-08-30 Anthony Danalis — Added Changelog and updated release notes.
* 2024-08-30 Anthony Danalis — Updated version in configure.
* 2024-08-30 Anthony Danalis — Updated version in man pages.
* 2024-08-30 Anthony Danalis — Updated version number.
* 2024-08-30 Anthony Danalis — Beta support for AMD ROCprofiler-SDK events.
* 2024-08-28 Treece Burgess — Update libpfm4 Current with commit 3abda5bc6c1af7f1b620dc594a806b3b5a4134cb Author: Stephane Eranian <eranian@gmail.com> Date:   Tue Aug 27 13:52:59 2024 -0700
* 2024-08-02 Treece Burgess — Revert changes to ROCm component to only count the basename for papi_component_avail. This will be the default choice for components with qualifiers.
* 2024-08-01 Treece Burgess — Updating format of export LD_LIBRARY_PATH= in Cuda component README.
* 2024-07-29 Heike Jagode — Updated license.
* 2024-07-25 William Cohen — cuda: When making the cuda tests do not assume nvcc on $PATH is one being used
* 2024-07-25 William Cohen — cuda: Eliminate -Werror=format-security error in cuda_init_private()
* 2024-07-24 Daniel Barry — add presets for Zen5
* 2024-07-16 Treece Burgess — Adding papi_cupti_common.c and papi_cupti_common.h
* 2024-07-16 Treece Burgess — Renaming cupti_common.* to papi_cupti_common.* to avoid file name collision with NVIDIA. Fixes build issues in Cuda >= 12.4.
* 2024-07-23 Heike Jagode — Fixed issue with building CUDA tests when linked with shared PAPI library
* 2024-07-09 Daniel Barry — rocm: fix event count to include qualifiers
* 2024-07-09 Treece Burgess — Update libpfm4 Current with commit 18f2a3e0541cc438094bbf65ebbed2b6742bf0d4 Author: Swarup Sahoo <swarup-chandra.sahoo@amd.com> Date:   Thu Jul 4 13:15:52 2024 -0700
* 2024-06-07 Vince Weaver — papi_internal: don't segfault if event missing from derived event definition
* 2024-06-03 Vince Weaver — perf_event/libpfm4_events: add initial heterogenous CPU support
* 2024-06-03 Vince Weaver — perf_event/libpfm4_events: add some code comments to _pe_libpfm4_init()
* 2024-06-16 William Cohen — perfctr: Remove the obsolete bundled perfctr and libpfm-3.y code
* 2024-06-27 Treece Burgess — Updating documentation for PAPI_read and PAPI_accum based off feedback.
* 2024-06-27 Treece Burgess — Update doxygen documentation to make note of the differences between PAPI_read and PAPI_accum. Specifically the second parameter in PAPI_accum must be initialized.
* 2024-02-29 Daniel Barry — sysdetect: add support for ARM Neoverse V2
* 2024-06-25 Treece Burgess — Update libpfm4 Current with commit 92c52017d7395c4040ec22949ee8c7f17bc5b4f7 Author: Stephane Eranian <eranian@gmail.com> Date:   Sat Jun 22 09:17:23 2024 -0700
* 2024-06-25 Daniel Barry — readme: updated FAQ page
* 2024-06-21 Daniel Barry — FAQ: update outdated links
* 2024-06-21 Daniel Barry — install: remove outdated instructions
* 2024-06-20 Daniel Barry — FAQ: Update to address MacOS question
* 2024-06-15 Treece Burgess — Update libpfm4 Current with commit 4bdeb7e067363013257460bdb6c3dbae778b5634 Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Jun 14 22:14:05 2024 -0700
* 2024-05-13 Treece Burgess — Restructuring conditional check to check for allowed modifiers.
* 2024-04-29 Treece Burgess — Update libpfm4 Current with commit 7c486cf96f9eab7019023d40f9c568486f696c44 Author: Stephane Eranian <eranian@gmail.com> Date:   Wed Apr 24 18:01:23 2024 -0700
* 2024-04-22 Treece Burgess — Adding extra check within conditional statement to avoid entering with the options of --cache or --cnd.
* 2024-04-16 Treece Burgess — Update libpfm4 Current with commit 1c0cdb91bc79eb1bc827e022f0a3738f124796a2 Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Apr 15 17:27:33 2024 -0700
* 2024-04-11 Treece Burgess — Update libpfm4 Current with commit 72866cbc2666820d87ebc0af3b1a16d1d5db6965 Author: Stephane Eranian <eranian@gmail.com> Date:   Thu Apr 11 08:36:50 2024 -0700
* 2024-04-25 William Cohen — SDE_LIB: Build libsde.so.1.0 with the CFLAGS and LDFLAGS passed in
* 2024-04-17 Treece Burgess — Adding PAPI_PRESET_BIT_MEM for correct else if conditional check.
* 2024-03-28 Anthony — SDE_LIB: Allow PAPI_reset() to reset a CountingSet.
* 2024-04-02 Anthony — SDE: Adding ntv_code_to_info functionality.
* 2024-03-26 Anthony — SDE tests: Add more randomness to the test.
* 2024-03-22 Anthony — sde_lib: Improved bucket utilization of hash table.
* 2024-03-20 Treece Burgess — Update libpfm4 Current with commit 33513ef78f0d81edb277e0d0fd16411abb161297 Author: Stephane Eranian <eranian@gmail.com> Date:   Thu Jan 18 21:55:46 2024 -0800
* 2024-03-12 Masahiko, Yamada — Update:Use fgets in place of fscanf functions to avoid possible buffer overflows
* 2024-03-02 Treece Burgess — Update libpfm4 Current with commit f517f1ec8038de00ce8f5fefeeef704e24aa08ae Author: Stephane Eranian <eranian@gmail.com> Date:   Thu Feb 29 23:07:21 2024 -0800
* 2024-02-29 Treece Burgess — Update libpfm4 Current with commit 816bb547f8997b84f7ef70bb99420f40dc8a984d Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Feb 26 22:39:49 2024 -0800
* 2024-02-19 Daniel Barry — presets: add support for Ice Lake ICL
* 2024-02-16 Treece Burgess — Updating CAT Makefile to use PAPI_DIR, to be more inline with the PAPI WIKI documentation.
* 2024-02-08 Treece Burgess — Changing --source flag to --source_dir and update to error output messages. Removed Python doc string and will address docs in another PR.
* 2024-02-06 Treece Burgess — Fixing small typo in parse_source_file docstring.
* 2024-02-06 Treece Burgess — Updating error handling, with updated output messages.
* 2024-02-06 Treece Burgess — Adding support for optional individual file flag to papi_hl_output_writer.py script.
* 2024-02-01 Anthony — SDE: Updated the C++ version of test Simple2.
* 2024-01-30 Anthony — SDE: Updated the C++ version of the minimal test.
* 2024-02-03 Treece Burgess — Update libpfm4 Current with commit 0d4ed0e7b09338e1bb1ab9153beab030c52570fe Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Feb 2 16:26:28 2024 -0800
* 2024-01-29 Treece Burgess — Updating first argument for PAPIF_flops_rate, PAPIF_flips_rate, and PAPIF_epc to use a int * instead of just int.
* 2024-01-22 Treece Burgess — Updating net README to remove unwanted links and rocm README to add correct link for GPU isolation.
* 2024-01-19 Treece Burgess — Updates to individual component README's to fix markdown links.
* 2024-01-12 Daniel Barry — cat: improve progress indicator in d-cache tests
* 2024-01-12 Daniel Barry — cat: optimize data cache benchmarks
* 2024-01-09 Vince Weaver — add initial riscv support
* 2024-01-03 Giuseppe Congiu — libpfm4: update to commit 90f61a0
* 2023-12-27 Todd Gamblin — sysdetect: fix bug where Makefile sets `-ffree-form` everywhere
* 2023-12-14 Giuseppe Congiu — release-7.1.0: update version and documentation
* 2023-12-19 Daniel Barry — cat: fix compile-time error
* 2023-12-19 Giuseppe Congiu — rocm: fix warnings in the rocm tests
* 2023-12-19 Giuseppe Congiu — rocm: search for hipcc in PAPI_ROCM_ROOT instead of using fixed path
* 2023-12-19 Giuseppe Congiu — configure: search for rocm_smi headers in PAPI_ROCMSMI_ROOT
* 2023-12-19 Giuseppe Congiu — cuda: add cudaGetErrorString to generate error messages
* 2023-12-19 Giuseppe Congiu — cuda: refactor get_gpu_compute_capability
* 2023-12-19 Giuseppe Congiu — cuda: refactor util_gpu_collection_kind
* 2023-12-19 Giuseppe Congiu — cuda: refactor cuptic_device_get_count
* 2023-12-14 Giuseppe Congiu — rocm: print all masks descriptors for events that contain them
* 2023-12-14 Giuseppe Congiu — rocm: add coma separator between event descriptor and masks
* 2023-12-18 Florian Weimer — configure: Fix return values in start thread routines
* 2023-12-14 Daniel Barry — presets: various cache presets for SPR CPUs
* 2023-12-08 Daniel Barry — presets: add total cache presets for Zen4 CPUs
* 2023-12-08 Daniel Barry — presets: correction to instr cache preset
* 2023-12-14 Daniel Barry — cat: reduce exec time of instr cache benchmark
* 2023-12-14 Daniel Barry — cat: remove unused variable
* 2023-12-14 Daniel Barry — cat: account for proper number of buffers
* 2023-12-13 Daniel Barry — cat: read values from config file as 'long long'
* 2023-12-13 Daniel Barry — cat: remove unnecessary typecast
* 2023-12-13 Daniel Barry — cat: use macro for LLC factor
* 2023-12-13 Daniel Barry — cat: ensure proper integer arithmetic
* 2023-12-12 Daniel Barry — cat: allocate the proper max buffer size
* 2023-12-12 Daniel Barry — cat: fix erroneous malloc
* 2023-12-12 Daniel Barry — cat: fix memory leak
* 2023-12-12 Daniel Barry — cat: clean-up comments
* 2023-12-06 Daniel Barry — cat: place MPI_Barrier before MPI_Finalize
* 2023-12-06 Daniel Barry — cat: only measure latencies once
* 2023-12-08 Daniel Barry — presets: add instr cache presets for Intel SPR
* 2023-12-08 Daniel Barry — intel_gpu: fix small typo
* 2023-12-06 Daniel Barry — cat: fix memory leak
* 2023-12-06 Daniel Barry — cat: store buffer sizes as 'long long'
* 2023-12-04 Daniel Barry — cat: properly normalize counter values
* 2023-12-04 Daniel Barry — cat: fix logic for memory hierarchy parameters
* 2023-12-04 Daniel Barry — cat: larger default PPB value
* 2023-12-04 Daniel Barry — cat: create parameter for max PPB in config file
* 2023-12-04 Daniel Barry — cat: probe fewer buffers per cache level
* 2023-12-01 Daniel Barry — cat: exclude cache sizes from tests
* 2023-12-01 Giuseppe Congiu — ci: run tests with and without PAPI debug enabled
* 2023-11-15 Aurelian MELINTE — PAPI: ARM Cortexx A76 support (Raspberry Pi 5)
* 2023-11-29 Giuseppe Congiu — rocm: change opt level to user choice for tests
* 2023-11-16 Giuseppe Congiu — rocm: add rocp_evt_code_to_info support
* 2023-11-14 Giuseppe Congiu — rocm: add qualifier support
* 2023-11-14 Giuseppe Congiu — rocm: add finalize_features function
* 2023-11-14 Giuseppe Congiu — rocm: add unique metric utility functions for intercept mode
* 2023-11-14 Giuseppe Congiu — rocm: add event name to info utility functions
* 2023-11-14 Giuseppe Congiu — rocm: remove useless comments
* 2023-11-03 Giuseppe Congiu — rocm: remove useless check for intercept code path
* 2023-11-03 Giuseppe Congiu — rocm: move init_callbacks call
* 2023-11-03 Giuseppe Congiu — rocm: remove intercept global state macros
* 2023-11-21 Giuseppe Congiu — rocm: change type of device id from unsigned int to int
* 2023-11-01 Giuseppe Congiu — rocm: add event identifier utility functions
* 2023-11-13 Giuseppe Congiu — rocm: add bitmap utility functions
* 2023-11-01 Giuseppe Congiu — rocm: change the event id type to uint64_t in backend
* 2023-07-21 Giuseppe Congiu — template: add template for new components
* 2023-12-01 Anthony — CAT: Initialize variables to suppress warnings, and move them to correct scope.
* 2023-11-29 Daniel Barry — presets: add inst cache presets for Zen4 CPUs
* 2023-08-30 Giuseppe Congiu — rocm: extend README with device partitioning information
* 2023-11-01 Giuseppe Congiu — sysdetect: add -ffree-form to silence error in ARM comp
* 2023-11-09 Giuseppe Congiu — rocm: add known problems with some events to README
* 2023-11-17 Giuseppe Congiu — rocm: fix bug in intercept mode reset function
* 2023-11-17 Giuseppe Congiu — rocm: fix bug introduced by commit 4991e1614
* 2023-11-14 Giuseppe Congiu — libpfm4: remove leftover .gitignore file
* 2023-11-14 Giuseppe Congiu — libpfm4: update to commit 535c204
* 2023-11-10 Anthony — CAT: Add information about the cache sizes in the header of the output file.
* 2023-11-22 Daniel Barry — presets: add data cache presets for Zen4 CPUs
* 2023-11-12 Anthony — CAT: Add missing option in the usage output.
* 2023-11-09 Anthony — utils: Fix bogus "Disabled" message in papi_component_avail for the sde component.
* 2023-10-27 Giuseppe Congiu — rocm: fix bug in intercept mode path
* 2023-11-06 Giuseppe Congiu — ci: add --enable-warnings to github actions
* 2023-11-06 Giuseppe Congiu — configure: add -Wall to the --enable-warnings configure flag
* 2023-10-24 Giuseppe Congiu — configure: add --enable-warnings flag
* 2023-11-07 Giuseppe Congiu — rocm: refactor get_context_counters
* 2023-11-07 Giuseppe Congiu — rocm: get rid of asserts
* 2023-11-07 Giuseppe Congiu — rocm: set return code outside fn_fail in init_event_table
* 2023-11-08 Giuseppe Congiu — configure: fix for issue #112
* 2023-09-13 Josh Minor — Set size of perf_attr_struct prior to getting pfm encoding
* 2023-11-07 William Cohen — ctests/thrspecific: Have the threads clean up after themselves
* 2023-11-07 William Cohen — sysdetect: Eliminate file resource leak in get_vendor_id() function
* 2023-11-07 William Cohen — net: Ensure that strings copied are NULL terminated
* 2023-11-07 William Cohen — coretemp: Ensure strings copied during initialization are NULL terminated
* 2023-11-07 William Cohen — coretemp: add closedir operation to function exit
* 2023-10-25 Daniel Barry — rocm: update README
* 2023-09-29 Giuseppe Congiu — sde_lib: do not build with debug symbols by default
* 2023-09-29 Giuseppe Congiu — configure: do not build with debug symbols by default
* 2023-10-19 Anustuv Pal — cuda: Fix papi_command_line segfault when passed non-existent event name
* 2023-10-06 Anustuv Pal — cuda: Improve CUDA component PAPI_read() overhead, issue 85
* 2023-10-06 Giuseppe Congiu — rocm: fix sampling mode multithread issue
* 2023-10-09 Giuseppe Congiu — rocm: fix typo in ctx_open
* 2023-09-08 Giuseppe Congiu — rocm: add logging to component backend
* 2023-09-08 Giuseppe Congiu — rocm: add logging to component frontend
* 2023-09-08 Giuseppe Congiu — rocm: funnel exits through same point in compomnent frontend
* 2023-07-20 Giuseppe Congiu — rocm: refactor rocc_dev_get_{count,id} functions
* 2023-07-20 Giuseppe Congiu — rocm: fix warning in callback function
* 2023-07-18 Giuseppe Congiu — rocm: move thread id get function to roc_common
* 2023-07-17 Giuseppe Congiu — rocm: fix warning in roc_common.c
* 2023-07-17 Giuseppe Congiu — rocm: remove roc_common.h from roc_profiler.h
* 2023-07-17 Giuseppe Congiu — rocm: move agent to id function to roc_common
* 2023-07-14 Giuseppe Congiu — rocm: remove leftover err_get_last function header
* 2023-07-14 Giuseppe Congiu — rocm: rename evt_get_descr to evt_code_to_descr
* 2023-07-13 Giuseppe Congiu — rocm: rename rocp_config.h to roc_profiler_config.h
* 2023-07-13 Giuseppe Congiu — rocm: reformat roc_profiler.c code
* 2023-07-13 Giuseppe Congiu — rocm: remove FIXME comment
* 2023-07-13 Giuseppe Congiu — rocm: use snprintf instead of strncpy
* 2023-07-13 Giuseppe Congiu — rocm: extract all device booking and checking functions
* 2023-07-12 Giuseppe Congiu — rocm: move extern declarations to config header
* 2023-07-12 Giuseppe Congiu — rocm: remove unneeded comments
* 2023-07-12 Giuseppe Congiu — rocm: rename source files for better readability
* 2023-05-17 Giuseppe Congiu — rocm: extract shared functionality
* 2023-07-12 Giuseppe Congiu — rocm: remove ROCM_PROF_ROCPROFILER guard
* 2023-05-16 Giuseppe Congiu — rocm: update returned error codes
* 2023-05-16 Giuseppe Congiu — rocm: remove macros handling error management
* 2023-05-16 Giuseppe Congiu — rocm: rename hsa_agent_arr_t to device_table_t
* 2023-05-16 Giuseppe Congiu — rocm: replace trailing Ptr in rocm functions with _p
* 2023-09-08 G-Ragghianti — changing gcc version for rocm compatibility
* 2023-09-29 Giuseppe Congiu — sysdetect: fix compiler flag selection in tests
* 2023-09-29 Giuseppe Congiu — configure: fix tls detection
* 2023-09-26 Giuseppe Congiu — smoke_tests: fix Makefile
* 2023-09-15 Anustuv Pal — cuda: Revert "utils: papi_component_avail does not support cuda component counters"
* 2023-09-15 Anustuv Pal — lmsensors: Replace numerical literal 1024 with PATH_MAX macro
* 2023-09-05 Anustuv Pal — lmsensors: Add lib/ to explicit search path to .so loader
* 2023-09-15 Anustuv Pal — coretemp: Fix snprintf warnings for gcc 10
* 2023-07-12 Caleb Han — sde_lib: fixed make bug
* 2023-09-18 Anustuv Pal — sde: Fix Minimal_Test.c handle pointer
* 2023-07-06 Giuseppe Congiu — rocm: fix snprintf handling
* 2023-07-06 Giuseppe Congiu — sysdetect: fix snprintf n argument in CUDA backend
* 2023-07-06 Giuseppe Congiu — sysdetect: fix snprintf n argument in ROCm backend
* 2023-07-06 Giuseppe Congiu — sysdetect: do not null terminate manually in CUDA backend
* 2023-07-06 Giuseppe Congiu — sysdetect: do not null terminate manually in ROCm backend
* 2023-07-21 Lukas Alt — rapl: support for icelake-sp
* 2023-07-25 Daniel Barry — cat: add missing entry in usage message
* 2023-07-25 Daniel Barry — cat: add option for conf file path
* 2023-09-06 Giuseppe Congiu — rocm_smi: fix warning "variable might be used uninitialized"
* 2023-09-01 Giuseppe Congiu — rocm: remove openmp dependency
* 2023-09-06 Anustuv Pal — cuda: fix event enumeration
* 2023-08-30 Anustuv Pal — cuda: fix dangerous dl_iterate_phdr operation
* 2023-08-15 Anustuv Pal — utils: papi_component_avail does not support cuda component counters
* 2023-08-24 Anustuv Pal — cuda: Remove x flag from cuda/tests/runtest.sh
* 2023-08-18 Giuseppe Congiu — rocm: fix instanced events
* 2023-08-23 Bert Wesarg — rocm: prefer librocprofiler64.so.1
* 2023-08-14 Giuseppe Congiu — libpfm4: update to commit efd10fb
* 2023-08-22 Anustuv Pal — cuda: fix get linked shared library link error gcc 10.0
* 2023-08-22 Anustuv Pal — cuda: Load cuda shared libraries from linked/rpath/LD_LIBRARY_PATH
* 2023-08-13 Anustuv Pal — papi.h: Fix warnings for -Wstrict-prototypes
* 2023-07-25 Daniel Barry — add more Ice Lake FLOPs presets
* 2023-07-31 Giuseppe Congiu — rocm: temporarely remove all tests from being built
* 2023-07-26 Anustuv Pal — cuda: New cuda component based on NVIDIA PerfWorks API.
* 2023-07-26 Kamil Iskra — powercap: test counter read permissions
* 2023-07-26 Kamil Iskra — powercap: ignore the psys entry
* 2023-07-23 Daniel Barry — add various Sapphire Rapids presets
* 2023-07-11 G-Ragghianti — added support for clang static code analysis
* 2023-06-12 Daniel Barry — cat: put GEMM kernels back in
* 2023-06-28 Giuseppe Congiu — rocm: user HIP_PATH for hipcc compiler in tests Makefile
* 2023-06-21 Daniel Barry — add cycles and instructions presets for Zen4
* 2023-06-30 Anthony Danalis — sde_lib: Fixed bug in hash-table deletion.
* 2023-06-29 Anthony Danalis — sde_lib: Allow group placeholders.
* 2023-06-29 Anthony Danalis — sde_lib: Added reference counts for proper unregistering of groups.
* 2023-06-29 Anthony Danalis — sde_lib: Added locking to sde_ti_read_counter() funtion.
* 2023-06-29 Anthony Danalis — sde_lib: Added function for hash-table serialization.
* 2023-06-28 Vince Weaver — don't use fast rdpmc counter reads in attach or syswide scenarios
* 2023-06-20 Giuseppe Congiu — PR author's checklist
* 2023-07-03 G-Ragghianti — Implemented CI check of spack install
* 2023-07-03 G-Ragghianti — Adding smoke-test code for spack install validation
* 2023-06-23 Giuseppe Congiu — intel_gpu: remove libsupc++ dependency from tests makefile
* 2023-06-23 Giuseppe Congiu — intel_gpu: remove libsupc++ dependency from component makefile
* 2023-06-27 Giuseppe Congiu — sysdetect: replace logic AND with bitwise AND operator
* 2023-06-20 Wileam Y.Phan — sde: fix cray and intel fortran test flag
* 2023-06-20 Wileam Y.Phan — sysdetect: fix cray and intel fortran test flag
* 2023-06-20 Giuseppe Congiu — sysdetect: add include path for cuda headers to makefile
* 2023-06-18 Daniel Barry — pcp: skip test if component is disabled
* 2023-06-12 Daniel Barry — add flops presets for Zen4
* 2023-06-13 Daniel Barry — cat: fix bug in data cache benchmarks
* 2023-06-12 Daniel Barry — remove references to Bitbucket
* 2023-06-08 Giuseppe Congiu — libpfm4: update to commit 70b5b4c
* 2023-06-07 Daniel Barry — add branch presets for Zen3 and Zen4
* 2023-04-07 Giuseppe Congiu — genpapifdef.c: delete file
* 2023-04-05 Giuseppe Congiu — maint/genpapifdef.pl: replacement perl script for genpapifdef.c
* 2023-06-05 G-Ragghianti — changed cuda requirement
* 2023-03-27 G-Ragghianti — CI: creating CI files
* 2023-04-03 John Linford — Update Neoverse V2 events
* 2023-05-17 Giuseppe Congiu — libpfm4: update to commit 533633a
* 2023-05-16 Giuseppe Congiu — buildsystem: fix install target in Makefile
* 2023-05-16 Anthony Danalis — intel_gpu: fix test
* 2023-04-03 Giuseppe Congiu — fort: do not compile fortran code if disabled
* 2023-04-03 Giuseppe Congiu — fort: add --disable-fortran switch
* 2023-05-11 Giuseppe Congiu — rocm_smi: fix bug in get_ntv_events_count
* 2023-05-11 Giuseppe Congiu — memory: fix bug in generic_get_memory_info
* 2023-03-31 Giuseppe Congiu — sysdetect: fix rocm and rocm_smi dlopen logic
* 2023-03-31 Giuseppe Congiu — libpfm4: update to commit 52632c7
* 2023-04-25 Daniel Barry — cat: allow user to specify DCR/DCW sampling
* 2023-04-17 Daniel Barry — cat: non-core events in multithreaded benchmarks
* 2023-03-16 Daniel Barry — cat: refactor flops benchmark
* 2023-04-06 Anthony Danalis — cat: addition of instructions benchmarks
* 2023-04-06 Terry Cojean — SDE: Fix shutdown for a consistent global control struct
* 2023-03-29 AnustuvICL — Fix wrong dlsym for cuptiDisableKernelReplayMode
* 2023-03-20 John Linford — Add minimal events for Arm Neoverse V2
* 2023-03-20 John Linford — Add minimal events for Arm Neoverse N2
* 2023-03-20 John Linford — Add minimal events for Arm Neoverse V1
* 2023-03-20 John Linford — Add minimal events for Arm Neoverse N1
* 2023-01-09 Giuseppe Congiu — Prepare for release 7.0.1
* 2023-03-09 Giuseppe Congiu — tests: fix order of headers in makefile
* 2023-02-14 Giuseppe Congiu — rocm_smi: add support for XGMI events
* 2023-03-06 Giuseppe Congiu — rocm_smi: fix test warning
* 2023-02-14 Giuseppe Congiu — rocm_smi: refactor component to support XGMI events (3/3)
* 2023-02-07 Giuseppe Congiu — rocm_smi: refactor rocm_smi frontend to use rocs API (2/3)
* 2023-01-18 Giuseppe Congiu — rocm_smi: refactor rocm_smi logic into rocs backend (1/3)
* 2023-03-02 Daniel Barry — build system: accommodate Fortran compiler absence
* 2023-03-07 Giuseppe Congiu — libpfm4: update to commit c676419
* 2023-03-07 Anthony — Modified a non-compliant type aliasing code that gcc-12.2 treats as undefined behavior to conform to the C standard and be more portable.
* 2023-02-27 Giuseppe Congiu — rocm: define PAPI_ROCM_PROF if rocm component enabled
* 2023-02-27 Giuseppe Congiu — sysdetect: enable fortran tests rules only if F77 is set
* 2023-02-24 Giuseppe Congiu — libpfm4: update to commit b4361ca
* 2023-02-08 Giuseppe Congiu — rocm: fix intercept mode shutdown bug (2/2)
* 2023-02-08 Giuseppe Congiu — rocm: fix init_private return code bug (1/2)
* 2023-02-20 Giuseppe Congiu — rocm: refactor htable (28/28)
* 2023-01-26 Giuseppe Congiu — rocm: add dispatch layer for future extensions (27/28)
* 2023-01-23 Giuseppe Congiu — rocm: refactor rocp backend header (26/28)
* 2023-01-10 Giuseppe Congiu — rocm: add note to source code (25/28)
* 2023-01-09 Giuseppe Congiu — rocm: remove same-event-number-per-device limitation (24/28)
* 2023-01-05 Giuseppe Congiu — rocm: sort events in component frontend (23/28)
* 2023-01-04 Giuseppe Congiu — rocm: add comments for backend functions (22/28)
* 2022-12-23 Giuseppe Congiu — rocm: refactor static string lengths (21/28)
* 2022-12-19 Giuseppe Congiu — rocm: refactor shutdown function names in backend (20/28)
* 2022-12-16 Giuseppe Congiu — rocm: refactor event verification logic in intercept mode (19/28)
* 2022-12-15 Giuseppe Congiu — rocm: refactor event duplication verification logic (18/28)
* 2022-12-14 Giuseppe Congiu — rocm: refactor dispatch_counter logic (17/28)
* 2022-12-13 Giuseppe Congiu — rocm: refactor rocp_ctx_open function name (16/28)
* 2022-12-09 Giuseppe Congiu — rocm: handle event table in component backend (15/28)
* 2022-12-09 Giuseppe Congiu — rocm: add event counting function in component frontend (14/28)
* 2022-12-09 Giuseppe Congiu — rocm: use rocp API to enumerate events in component (13/28)
* 2022-12-09 Giuseppe Congiu — rocm: add event name tokenizer (12/28)
* 2022-12-09 Giuseppe Congiu — rocm: get errors through rocp_err_get_last (11/28)
* 2022-12-09 Giuseppe Congiu — rocm: add error code to string function (10/28)
* 2022-12-08 Giuseppe Congiu — rocm: refactor rocp_ctx_open function (9/28)
* 2022-12-08 Giuseppe Congiu — rocm: refactor component backend interface (8/28)
* 2022-12-06 Giuseppe Congiu — rocm: refactor user to component event mapping (7/28)
* 2022-12-06 Giuseppe Congiu — rocm: refactor event sorting function name (6/28)
* 2022-12-06 Giuseppe Congiu — rocm: refactor event collision detection (5/28)
* 2022-12-06 Giuseppe Congiu — rocm: refactor intercept_ctx_open (4/28)
* 2022-12-06 Giuseppe Congiu — rocm: quick sort component events by id (3/28)
* 2022-12-05 Giuseppe Congiu — rocm: refactor rocp_ctx_read (2/28)
* 2022-12-13 Giuseppe Congiu — rocm: refactor variable types (1/28)
* 2023-02-21 Giuseppe Congiu — perf_event: used unused attribute in mmap_read_self
* 2023-02-21 Giuseppe Congiu — perf_event: add missing mmap_read_reset_count for non default cpus
* 2023-02-21 Giuseppe Congiu — perf_event: bug fix in mmap_read_self
* 2023-01-26 Daniel Barry — nvml: fix support for multiple devices
* 2023-02-21 Masahiko, Yamada — PAPI_read performance improvement for the arm64 processor
* 2023-02-08 Giuseppe Congiu — libpfm4: update to commit 678bca9
* 2023-01-26 Giuseppe Congiu — ctests/all_native_events: bug workaround
* 2023-02-07 Daniel Barry — build system: workaround for GCC8+CUDA10 bug on POWER9
* 2023-02-07 Daniel Barry — sysdetect: account for older CUDA versions
* 2023-01-26 Daniel Barry — nvml: fix small typo in README
* 2023-01-13 Giuseppe Congiu — rocm: skip sampling multi-thread tests
* 2023-01-09 Giuseppe Congiu — rocm: fix bug in sampling_ctx_open
* 2023-01-06 Giuseppe Congiu — libpfm4: update to commit dd42292
* 2022-12-22 Giuseppe Congiu — net: fix warning in strncpy
* 2022-12-22 Giuseppe Congiu — net: fix warning in snprintf
* 2022-12-22 Giuseppe Congiu — coretemp: fix warning in strncpy
* 2022-12-22 Giuseppe Congiu — powercap_ppc: fix warning in powercap_basic test
* 2022-12-22 Giuseppe Congiu — powercap_ppc: fix bug in powercap_basic test
* 2022-12-20 Giuseppe Congiu — libpfm4: add missing zen 4 files
* 2022-12-15 Giuseppe Congiu — sensors_ppc: fix typo in fall through comment
* 2022-12-15 Giuseppe Congiu — powercap-ppc: fix warning in strncpy
* 2022-12-12 Giuseppe Congiu — libpfm4: update libpfm4 to commit c0116f9
* 2022-12-19 Giuseppe Congiu — sysdetect: fix typo in papi_hardware_avail
* 2022-12-01 Giuseppe Congiu — rocm: give precendence to new dir structure for metrics file
* 2022-11-28 Giuseppe Congiu — rocm: account for new directory tree structure in rocm
* 2022-11-30 Giuseppe Congiu — ftest: fix warning in fortran tests
* 2022-12-08 Daniel Barry — infiniband: fix compiler warnings
* 2022-11-29 Giuseppe Congiu — sysdetect: fix order in include dirs
* 2022-11-29 Giuseppe Congiu — sysdetect: fix typo in makefile Rules
* 2022-11-29 Giuseppe Congiu — sysdetect: explicit cast AMD hsa attributes to hsa_agent_info_t
* 2022-11-28 Florian Weimer — configure: Avoid implicit ints and implicit function declarations
* 2022-12-02 Daniel Barry — infiniband: increase max number of events
* 2022-05-26 Giuseppe Congiu — cuda: remove untested dependency
* 2022-11-29 Giuseppe Congiu — sysdetect: add missing numa memsize attr
* 2022-11-29 Giuseppe Congiu — cuda: use appropriate macro for perfworks API calls
* 2022-11-29 Giuseppe Congiu — rsmi: fix warning in Makefile Rules
* 2022-11-29 Giuseppe Congiu — rsmi: fix warning in strncpy
* 2022-11-29 Giuseppe Congiu — rocm: fix dependency priority in Makefile
* 2022-11-29 Giuseppe Congiu — rocm: fix deprecated warning in tests
* 2022-11-28 Giuseppe Congiu — rocm: fix miscellaneous warnings in rocp.c
* 2022-12-01 Giuseppe Congiu — nvml: also copy null termination character in strncpy
* 2022-11-29 Giuseppe Congiu — nvml: fix warning in strncpy
* 2022-11-29 Giuseppe Congiu — nvml: trim excessive long description string
* 2022-11-29 Giuseppe Congiu — nvml: fix cuInit returned variable type
* 2022-11-22 Giuseppe Congiu — cuda: fix compile error with gcc 10
* 2022-11-22 Giuseppe Congiu — nvml: fix compile error with gcc 10
* 2022-11-19 Giuseppe Congiu — sysdetect: fix compile error with gcc 10
* 2022-11-10 Giuseppe Congiu — Prepare for release
* 2022-11-11 Giuseppe Congiu — high_level: only use PAPI_TOT_CYC as default
* 2022-11-10 Giuseppe Congiu — papi_br_tkn: add not taken branch event to the right eventset
* 2022-11-10 Giuseppe Congiu — sysdetect: add missing fortran man pages
* 2022-11-08 Giuseppe Congiu — sysdetect: update test to reflect 'list' argument removal
* 2022-11-02 Giuseppe Congiu — sysdetect: regenerate man pages for updated attributes
* 2022-11-02 Giuseppe Congiu — sysdetect: remove unused attributes from doc
* 2022-11-02 Giuseppe Congiu — sysdetect: white space cleanup
* 2022-11-02 John Rodgers — CUDA: Align memory zero with pad
* 2022-11-02 John Rodgers — CUDA: CUPTI11 Sporadic Memory Failures
* 2022-11-02 John Rodgers — CUDA: Prevent memory leak
* 2022-11-02 John Rodgers — CUDA: Remove unnecessary code
* 2022-11-02 John Rodgers — CUDA: Prevent component deadlock
* 2022-11-02 John Rodgers — DELAY_INIT: Set disabled for delay init comps
* 2022-10-24 Daniel Barry — pcp: warning instead of error when 'reason' string truncated
* 2022-10-28 Daniel Barry — cat: support to comment-out lines in input file
* 2022-10-27 Anthony Danalis — Improved the branch misprediction validation test.
* 2022-10-27 Anthony — Removed unneeded NULL pointer checks in libsde.
* 2022-09-14 Giuseppe Congiu — doc: regenerate man pages
* 2022-10-25 Giuseppe Congiu — papi_hardware_avail: print thread affinity list for numas
* 2022-10-26 Giuseppe Congiu — sysdetect: add GPU affinity example in tests
* 2022-10-26 Giuseppe Congiu — sysdetect: hook mpi tests to NO_MPI_TESTS
* 2022-10-25 Giuseppe Congiu — sysdetect: add PAPI_DEV_ATTR__CPU_UINT_THR_NUMA_AFFINITY
* 2022-10-25 Giuseppe Congiu — sysdetect: remove builtin support for numa and GPU affinity
* 2022-10-12 Daniel Barry — cat: ifdefs for AVX availability
* 2022-10-12 Daniel Barry — cat: specify architecture in macros
* 2022-10-12 Daniel Barry — cat: remove unused typedef; add used typedef
* 2022-10-11 Daniel Barry — cat: rename macros for POWER architecture
* 2022-10-11 Daniel Barry — cat: remove unused code
* 2022-09-19 Daniel Barry — cat: consolidate 'INTEL' and 'AMD' flags for vector FLOPs benchmark
* 2022-09-19 Daniel Barry — cat: specify architecture vector FLOPs benchmark function names
* 2022-09-07 Daniel Barry — cat: vector FLOPs benchmark for non-x86 architectures bug fix
* 2022-10-13 Daniel Barry — powercap: add new component tests
* 2022-10-26 AnustuvICL — perf_event: Free allocated string in function allocate_native_event
* 2022-10-18 Peinan Zhang — Added support for multiple Intel GPU devices and multiple-tiles per device.
* 2022-10-24 Giuseppe Congiu — sde: make '-sde' option always visible in papi_native_avail
* 2022-10-25 Anthony — Make papi_native_avail support the "-sde" flag only if *both* libsde and the SDE component are configured in.
* 2022-10-25 Anthony — Added path to libpfm4 in the SDE tests Makefile, and further instructions for users in the README.
* 2022-10-24 AnustuvICL — papi.h: Update bit field post removal of members from struct _papi_component_option
* 2022-10-23 William Cohen — Use fgets in place of fscanf functions to avoid possible buffer overflows
* 2022-10-10 AnustuvICL — Remove C++ style commented code
* 2022-08-31 Giuseppe Congiu — perfctr: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — perfmon2: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — papi: do not set disabled flag in framework
* 2022-08-31 Giuseppe Congiu — vmware: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — stealtime: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — sensors_ppc: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — rapl: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — powercap_ppc: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — powercap: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — perf_event_u: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — perf_event: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — pcp: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — net: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — mx: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — lustre: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — lmsensors: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — libmsr: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — io: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — intel_gpu: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — infiniband: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — micpower: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — host_micpower: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — example: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — coretemp_freebsd: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — coretemp: set disabled flag in cmp
* 2022-08-31 Giuseppe Congiu — appio: set disabled flag in cmp
* 2022-10-18 Giuseppe Congiu — rocm: return PAPI_ENOEVNT if event not found
* 2022-10-17 Giuseppe Congiu — rocm: SQ_WAVES does not reflect logical waves
* 2022-10-20 Daniel Barry — cat: fix memory leak from hw_desc alloc
* 2022-10-19 Anthony — Make static libsde.a optional.
* 2022-10-20 Daniel Barry — cat: define default number of OMP threads
* 2022-10-18 William Cohen — Removed unused label and variable from query_device_simple_f.F
* 2022-10-18 William Cohen — Correctly size papi_preset.c array to avoid possible overflow
* 2022-10-13 Daniel Barry — powercap: fix memory leak in test
* 2022-10-11 Giuseppe Congiu — libpfm4: update to commit 8aaaf17
* 2022-10-13 Daniel Barry — powercap: ensure proper string format in test
* 2022-10-11 Daniel Barry — powercap: fix formatting
* 2022-10-10 Daniel Barry — powercap: fix compiler warnings for component test powercap_basic
* 2022-10-10 Daniel Barry — powercap: fix compiler warnings for component
* 2022-10-10 AnustuvICL — Refactor caddr_t to void* vptr_t
* 2022-10-11 Anthony — Missing file that should have been included in PR 349 (commit 89c0f19).
* 2022-10-12 Giuseppe Congiu — sysdetect: fix warning in papi_fwrappers.c
* 2022-09-07 Daniel Barry — cat: add MPI support
* 2022-09-28 Anthony — Scripts and sample data for viewing CAT's dcache output.
* 2022-09-21 Anthony — Removed redundant latency step.
* 2022-09-21 Anthony — Added support for "-quick" flag which skips the latency tests.
* 2022-09-21 Anthony — Force the CPU component to initialize itself.
* 2022-09-21 Anthony — Cleaned up the way we handle the parameters specified via the command line arguments.
* 2022-09-04 Giuseppe Congiu — sysdetect: add fortran bindings and test
* 2022-09-13 Daniel Barry — powercap: fix wrap-around arithmetic
* 2022-10-07 Giuseppe Congiu — infiniband: fix warning in snprintf
* 2022-08-31 Giuseppe Congiu — perfmon2: funnel init_component failures
* 2022-08-31 Giuseppe Congiu — perfctr: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — host_micpower: funnel PAPI_ENOMEM through fn_fail
* 2022-08-28 Giuseppe Congiu — host_micpower: rework error handling in init_component
* 2022-08-28 Giuseppe Congiu — host_micpower: delete empty line
* 2022-08-28 Giuseppe Congiu — host_micpower: add fn_exit point
* 2022-08-28 Giuseppe Congiu — host_micpower: rename disable_me to fn_fail
* 2022-08-28 Giuseppe Congiu — vmware: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — stealtime: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — sensors_ppc: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — rapl: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — powercap_ppc: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — powercap: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — pcp: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — pcp: return PAPI_ECMP on error instead of ctxHandle
* 2022-08-28 Giuseppe Congiu — net: return PAPI_ECMP on error instead of num_events
* 2022-08-28 Giuseppe Congiu — net: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — mx: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — micpower: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — micpower: replace PAPI_ENOCMP with PAPI_ECMP
* 2022-08-28 Giuseppe Congiu — lustre: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — lmsensors: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — libmsr: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — io: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — intel_gpu: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — example: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — coretemp: replace PAPI_ENOCMP with PAPI_ECMP
* 2022-08-28 Giuseppe Congiu — coretemp_freebsd: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — coretemp: funnel init_component failures
* 2022-08-28 Giuseppe Congiu — appio: funnel init_component failures
* 2022-08-27 Giuseppe Congiu — perf_event_u: replace PAPI_ENOCMP with PAPI_ECMP
* 2022-08-27 Giuseppe Congiu — perf_event: replace PAPI_ENOCMP with PAPI_ECMP
* 2022-08-27 Giuseppe Congiu — perf_event_u: funnel init_component failures
* 2022-08-27 Giuseppe Congiu — perf_event: funnel init_component failures
* 2022-09-22 Giuseppe Congiu — rocm_smi: add default rocm path for tests
* 2022-09-29 Anthony — libsde: Passing the CC Makefile variable to the sub-make.
* 2022-09-22 Giuseppe Congiu — rocm: skip multi-threaded high-level API tests
* 2022-09-21 Giuseppe Congiu — rocm: use static libpapi for tests
* 2022-09-21 Giuseppe Congiu — rocm: add default rocm path for tests
* 2022-07-11 Giuseppe Congiu — rocm: account for PAPI defined compilation flags
* 2022-06-02 Giuseppe Congiu — rocm: add Makefile_comp_tests.target dependency in tests
* 2022-09-24 Giuseppe Congiu — meminfo: support POWER10 cache information
* 2022-09-24 Giuseppe Congiu — sysdetect: add POWER10 cache info support
* 2022-09-24 Giuseppe Congiu — sysdetect: update power9 L1 cache info
* 2022-09-04 Giuseppe Congiu — meminfo: add power9 cache info
* 2022-09-21 Giuseppe Congiu — configure: fix tls check logic
* 2022-09-23 Giuseppe Congiu — papi_get_opt: update documentation for PAPI_LIB_VERSION
* 2022-09-23 Giuseppe Congiu — ctests/version: PAPI_library_init does not fail test
* 2022-09-22 Giuseppe Congiu — Return PAPI library version even if PAPI is not initialized
* 2021-12-02 Masahiko, Yamada — ctests: improve all_native_events.
* 2022-09-25 Giuseppe Congiu — libpfm4: update to commit 8c606bc
* 2022-09-22 Giuseppe Congiu — sysdetect: fix problem with missing shutdown_thread implementation
* 2022-09-21 Giuseppe Congiu — configure: add support for automatic ARM cpu detection
* 2022-09-20 Giuseppe Congiu — sysdetect: fix cache info data structure name
* 2022-09-02 Giuseppe Congiu — sysdetect: conditionally build mpi tests
* 2022-09-13 Anthony — Add the tests in the "clean" target in the makefile.
* 2022-09-13 Anthony — More proper handling of special compilation flags for papi_native_avail.
* 2022-04-20 Anthony — libsde: Refactoring the sde code in a standalond library with a clean API.
* 2022-05-17 AnustuvICL — cuda: Raise error when adding metrics that need multiple pass
* 2022-09-03 Giuseppe Congiu — libpfm4: update to commit 11f2d6c
* 2022-09-03 Giuseppe Congiu — papi_native_avail: fix typo in doxygen comment
* 2021-07-13 Masahiko, Yamada — meminfo: Add alloc/write policy for generic_get_memory_info
* 2022-09-02 Giuseppe Congiu — libmsr: improve disabled reason string
* 2022-09-02 Giuseppe Congiu — sysdetect: update power9 cache info
* 2022-08-24 Giuseppe Congiu — ctests: allow access to PAPI_EDELAY_INIT components
* 2022-09-01 Giuseppe Congiu — sysdetect: update README.md
* 2022-08-31 Giuseppe Congiu — sysdetect: warning fix in snprintf
* 2022-09-01 Giuseppe Congiu — errcode: add PAPI_EMULPASS to error codes
* 2022-09-01 Giuseppe Congiu — errcode: add comment for PAPI_EDELAY_INIT in papi.h
* 2022-09-01 Giuseppe Congiu — errcode: add PAPI_EDELAY_INIT to genpapifdef
* 2022-08-31 Giuseppe Congiu — sysdetect: add support for Power8 through 10
* 2022-08-31 Giuseppe Congiu — configure: add support for POWER8 through 10
* 2022-07-17 Giuseppe Congiu — rocm: refactor ntv_name_to_code and ntv_code_to_name
* 2022-07-16 Giuseppe Congiu — rocm: add name_to_code implementation
* 2022-07-16 Giuseppe Congiu — rocm: add hash table for name_to_code fast conversions
* 2022-07-11 Giuseppe Congiu — sysdetect: update tests
* 2022-06-03 Giuseppe Congiu — sysdetect: fix warning in amd gpu probe
* 2022-04-20 Giuseppe Congiu — sysdetect: extend PAPI with system detection and querying APIs
* 2022-08-30 Daniel Barry — papi_avail: add presets for Intel Ice Lake SP
* 2022-08-25 Daniel Barry — cat: remove unused code from vector benchmark
* 2022-08-25 Daniel Barry — cat: format changes to vector benchmark comments
* 2022-08-24 Daniel Barry — cat: extend vector FLOPs benchmark to 128-bit and 512-bit instrinsics
* 2022-06-03 Daniel Barry — sysdetect: modify configure.in logic to parse '--with-CPU=x86'
* 2022-08-22 Giuseppe Congiu — libpfm4: fix broken update
* 2022-07-18 Giuseppe Congiu — libpfm4: update libpfm4 to commit 5140ce5
* 2022-05-26 John Rodgers — CUDA: Add compile/runtime version debug msgs
* 2022-07-12 Giuseppe Congiu — rocm: fix assign eventset to component
* 2022-06-11 Giuseppe Congiu — rsmi: ignore not yet implemented function
* 2022-05-30 Giuseppe Congiu — rocm_smi: account for PAPI_EDELAY_INIT in tests
* 2022-05-28 Giuseppe Congiu — nvml: account for PAPI_EDELAY_INIT in tests
* 2022-06-02 Daniel Barry — powercap: add wrapper function to map event-set entry to counter
* 2022-05-17 Daniel Barry — powercap: fix event lookup in _powercap_read()
* 2022-07-06 Daniel Barry — sysdetect: add support for Fujitsu A64FX
* 2022-06-03 Masahiko, Yamada — papi_mem_info: modify aarch64_get_memory_info by hw_info
* 2022-05-17 Daniel Barry — papi_mem_info: add back support for ARM64 processors
* 2022-04-22 Daniel Barry — papi_mem_info: add support for Fujitsu A64FX
* 2022-06-11 Giuseppe Congiu — rocm: rocp_pool_close double free comment
* 2022-06-11 Giuseppe Congiu — rocm: remove useless comments
* 2022-06-11 Giuseppe Congiu — rocm: adjust for 5.2.0 change of directory structure
* 2022-06-11 Giuseppe Congiu — rocm: check config files are regular
* 2022-06-10 Giuseppe Congiu — rocm: rename dispatch counter functions
* 2022-06-10 Giuseppe Congiu — rocm: fix bug in sampling read
* 2022-06-10 Giuseppe Congiu — rocm: cleanup function signature
* 2022-06-10 Giuseppe Congiu — rocm: wrap sampling/intercept_ctx_init
* 2022-06-11 Giuseppe Congiu — pcp: add how to run on Summit in readme
* 2022-06-10 John Rodgers — CUDA: Update Multi-Kernel Launch Test
* 2022-06-09 Giuseppe Congiu — sensors_ppc: fix test
* 2022-06-08 Giuseppe Congiu — libpfm4: update libpfm4 to commit 322e66c
* 2022-06-02 Giuseppe Congiu — rocm_smi: remove duplicate include Makefile_comp_tests.target
* 2022-06-02 Giuseppe Congiu — rocm: fix rocprofiler load logic
* 2022-06-03 Giuseppe Congiu — sysdetect: add papi_hardware_avail to man pages
* 2022-06-02 Giuseppe Congiu — sysdetect: fix a 'may be used uninitialized' warning
* 2022-06-02 Giuseppe Congiu — cuda: allow for CC 7.0 to use the profiler API
* 2022-05-28 Giuseppe Congiu — libpfm4: update libpfm4 to commit b03a81e
* 2022-05-26 Giuseppe Congiu — sysdetect: fix warning in cpu probe
* 2022-01-12 Giuseppe Congiu — rocm: component rewrite
* 2022-04-18 Giuseppe Congiu — high-level: use _papi_getpid instead of getpid
* 2022-04-18 Giuseppe Congiu — thread: add _papi_getpid() function
* 2022-01-27 Anthony — Integrate the atomic operations of the libatomic_ops library into PAPI.
* 2022-05-23 John Rodgers — CUDA11 Start Variable Update
* 2022-05-23 John Rodgers — CUDA11 Profiler Active Context Sensitivity
* 2022-05-05 John Rodgers — Allow context creation for CUDA11
* 2022-05-05 John Rodgers — Issue102: Remove CUDA11 callback subscriber
* 2022-05-16 John Rodgers — Issue 105: CUDA11 Multi Read Error
* 2022-04-29 John Rodgers — Remove unnecessary calls to `cuptiProfiler{Enable,Disable}Profiling` in CUDA11 `PAPI_read` operations.  Starting and stopping of profiling session now handled in appropriate CUDA11 `PAPI_{start,stop}` operations.
* 2022-05-16 Giuseppe Congiu — cuda: remove leftover cupti11 switching logic
* 2022-05-10 Giuseppe Congiu — cuda: replace cupti_profiler with cupti_api_version
* 2022-04-28 Giuseppe Congiu — cuda: pre-cupti11 backward compatibility fix
* 2022-05-23 AnustuvICL — cuda: Added debug messages to indicate the locations of loaded dynamic CUDA libraries.
* 2022-03-21 Anustuv Pal — cuda: Add support for CUDA version >11.2
* 2022-05-10 Giuseppe Congiu — sysdetect: fix include path of nvidia GPUs
* 2022-04-30 Giuseppe Congiu — sysdetect: fix amd gpu product name
* 2022-05-18 Giuseppe Congiu — perf_event: fix typo in error code handling
* 2022-05-18 Giuseppe Congiu — perf_event: do not set disable string in _pe_libpfm4_init
* 2022-04-21 Giuseppe Congiu — libpfm4: update libpfm4 to commit c779846
* 2022-04-07 Giuseppe Congiu — sysdetect: use PAPI_ROCM_ROOT for rocmsmi dlopen path
* 2022-04-19 Giuseppe Congiu — intel_gpu: remove test/readme.txt from test list
* 2022-04-19 Giuseppe Congiu — Update libpfm4 Current with commit 9580a003d83900569db3f2c7bc41e0e2ea7b88ef Author: Stephane Eranian <eranian@gmail.com> Date:   Wed Apr 20 19:56:03 2022 -0700
* 2022-04-14 Anthony — Refactored unlocking to the end of each function, and replaced tabs with spaces.
* 2022-04-13 Anthony — Cleaning up error messages.
* 2022-04-13 Anthony — Counting Set introduced to sde_lib. Both C and C++ APIs along with tests.
* 2022-04-12 Giuseppe Congiu — high-level: replace flock with fcntl
* 2022-04-05 Giuseppe Congiu — high-level: use variable to select between single and multi-thread mode
* 2022-04-07 Giuseppe Congiu — Update libpfm4 Current with commit eca0a1f2d274ba26e6c24231fdf61b1407e3ed03 Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Apr 11 15:19:40 2022 -0700
* 2022-04-13 Daniel Barry — CAT: Rename printing functions in vector benchmark
* 2022-04-08 Daniel Barry — CAT: Added scalar instrinsics to validate half-precision vector benchmark accuracy
* 2022-03-31 Anthony — Fixed a potential deadlock in the SDE component.
* 2022-03-30 Anthony — Fixed bug in terminating a string in the SDE component.
* 2022-03-30 Daniel Barry — CAT: Added vector FLOPs benchmarks to identify related events
* 2022-03-22 Anthony Danalis — Updated the data cache write benchmark to make it cause one read and one write more reliably.
* 2022-01-23 Giuseppe Congiu — configure: add one lock per components
* 2022-03-28 Masahiko, Yamada — sysdetect: improve processor name for ARM processors
* 2022-03-15 Giuseppe Congiu — sysdetect: fix vendor codes for ARM
* 2022-03-15 Giuseppe Congiu — Update libpfm4 Current with commit ad5c64e1ac2f177e2166bedfd7b679e49017cb55 Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Mar 18 12:25:26 2022 -0700
* 2022-03-14 Giuseppe Congiu — sysdetect: system information queries treat all ARM CPUs the same
* 2022-03-17 Masahiko, Yamada — sysdetect: configure --with-CPU required.
* 2022-03-16 Masahiko, Yamada — sysdetect: Adding Macro Definitions for arm64
* 2022-02-20 Giuseppe Congiu — sysdetect: patch arm to convert vendor id into vendor string
* 2022-02-20 Giuseppe Congiu — sysdetect: get rid of VENDOR_ARM
* 2022-02-16 Giuseppe Congiu — sysdetect: add vendor id field for ARM processors
* 2022-02-17 Giuseppe Congiu — sysdetect: update vendor id codes in cpu probe
* 2022-02-20 Giuseppe Congiu — papi_hardware_avail: only print numa node memory if greater than 0
* 2022-02-20 Giuseppe Congiu — sysdetect: replace assignment to atoi with sscanf
* 2022-02-20 Giuseppe Congiu — sysdetect: fix typo in cpu probe
* 2022-02-20 Giuseppe Congiu — sysdetect: there is at least one numa node in SMPs
* 2022-03-04 Masahiko, Yamada — Add PAPI idle-related preset events for a64fx
* 2022-03-04 Masahiko, Yamada — PAPI_get_hardware_info: improve PAPI_hw_info_t for ARM processors
* 2022-02-20 Giuseppe Congiu — sysdetect/amd: add CPPFLAGS to Rules file
* 2022-02-19 Giuseppe Congiu — sysdetect/amd: use snprintf instead of assignment operator
* 2022-02-19 Giuseppe Congiu — sysdetect/amd: fix hsa_error_string definition and usage
* 2022-02-19 Giuseppe Congiu — papi_component_avail: rename force_lazy_init to force_cmp_init
* 2022-02-18 Giuseppe Congiu — papi_component_avail: force component init only when necessary
* 2022-02-18 Giuseppe Congiu — papi_native_avail: allow for delayed init components
* 2022-02-17 Giuseppe Congiu — Update libpfm4. Tested on orbitty.icl.utk.edu, ARMv8 Processor rev 1 (v8l) Tested on methane.icl.utk.edu, Intel Skylake Xeon(R) Gold 6140 CPU Tested on dopamine.icl.utk.edu, AMD Zen3 EPYC 7413 CPU Current with commit 58efe1f26fe1ca82f8b25b83c1089c5f9eac0f1b Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Feb 28 11:55:13 2022 -0800
* 2022-02-20 Giuseppe Congiu — sysdetect: fix infinite loop bug
* 2022-02-19 Giuseppe Congiu — cuda: fix overcounting of cuda devices
* 2022-02-16 Giuseppe Congiu — rocm_smi: change disabled_reason for delayed init
* 2022-02-16 Giuseppe Congiu — nvml: change disabled_reason for delayed init
* 2022-02-16 Giuseppe Congiu — rocm: change disabled_reason for delayed init
* 2022-02-16 Giuseppe Congiu — cuda: change disabled_reason for delayed init
* 2022-02-15 Giuseppe Congiu — papi_errno: add delay init string error
* 2022-02-15 Giuseppe Congiu — papi: handle delay init for GPU components
* 2022-02-15 Giuseppe Congiu — papi_errno: add PAPI_EDELAY_INIT error for delayed init components
* 2021-12-12 Giuseppe Congiu — papi_get_component_info: remove init_private support
* 2021-12-12 Giuseppe Congiu — papi_vector: remove init_private support
* 2021-12-12 Giuseppe Congiu — papi_component_avail: add lazy init code for components
* 2021-12-12 Giuseppe Congiu — nvml: remove init_private for lazy init
* 2021-12-12 Giuseppe Congiu — rocm_smi: remove init_private for lazy init
* 2021-12-12 Giuseppe Congiu — cuda: remove init_private for lazy init
* 2021-12-12 Giuseppe Congiu — rocm: remove init_private for lazy init
* 2022-02-03 Anthony Danalis — Improved error handling and reporting.
* 2022-01-31 Giuseppe Congiu — cuda: rename device count routine looking into /sys
* 2022-01-28 Giuseppe Congiu — cuda: extend device counting with /proc filesystem
* 2022-01-28 Giuseppe Congiu — high-level: make output writer script python2/3 compatible
* 2022-01-27 Giuseppe Congiu — sysdetect: fix load_mpi_sym signature
* 2022-01-22 Giuseppe Congiu — cuda: fix bug in shut down sequence
* 2022-01-17 Giuseppe Congiu — sysdetect/rocm: explicitly look for rocm in PAPI_ROCM_ROOT
* 2022-01-17 Giuseppe Congiu — sysdetect/rocm: fix hsa_status_string arguments
* 2021-12-08 Masahiko, Yamada — Improve the papi_xml_event_info command.
* 2021-12-03 Giuseppe Congiu — rocm_smi: fix bug in event reporting while running papi_component_avail
* 2021-11-08 Giuseppe Congiu — init_private: fix indentation in order to silence compiler warning
* 2021-07-29 Giuseppe Congiu — Sysdetect: system information detection component
* 2021-10-28 Giuseppe Congiu — init: make init_private exposed by every component
* 2021-10-18 Giuseppe Congiu — papi_lock: fix bug in PAPI_lock and PAPI_unlock
* 2021-10-16 Giuseppe Congiu — RocmCmp: fix bug in event reporting while running papi_component_avail
* 2021-10-13 Anthony Danalis — Added code to set the environment variable "ROCP_HSA_INTERCEPT" which is needed since rocm-4.1, and removed spurious whitespace.
* 2021-10-03 Giuseppe Congiu — PAPI_accum: documentation bug fix
* 2021-09-01 Daniel Barry — Modified the PCP component to use the local host as the PMAPI context. These changes are compatible with both RHEL 7 and 8.
* 2021-08-30 Vince Weaver — linux-memory: change cache parsing so it works on ARM servers
* 2021-08-24 Anthony Castaldo — Added CUPTI_PROFILER=-1 for no PAPI_CUDA_ROOT set at ./configure time. Disables the CUDA component with the message "Environment variable \ PAPI_CUDA_ROOT must be specified before ./configure is executed."
* 2021-08-24 Anthony Castaldo — Changes to ensure PAPI_CUDA_ROOT was set BEFORE ./configure was run, to ensure we distinguish between CUPTI11, Legacy, and misconfigured.
* 2021-08-24 Masahiko, Yamada — Fix the PAPI_FUL_CCY setting for a64fx
* 2021-08-23 Anthony Castaldo — Removed extraneous comments.
* 2021-08-23 Anthony Castaldo — Changed the error messages about the Legacy/Cupti11 failures to better distinguish the exact cause of failure, and updated several possible exits of the initialization that might cause an empty "Disabled" message on papi_component_avail.
* 2021-08-20 Daniel Barry — Fixed a bug regarding race conditions in a parallel construct in the CAT data cache benchmarks.
* 2021-08-19 Anthony — Updates to the C++ API based on early-adopter feedback.
* 2021-08-12 Anthony Castaldo — Corrected shutdown code to work correctly if delayed init never executes (due to shutdown without using the component).
* 2021-08-11 Anthony Castaldo — In scanning system devices to find GPUs, added Guiseppe's recommendation to also check device class to filter out all but Display Controllers; which are GPUs.
* 2021-08-10 Anthony Castaldo — Added checks for Nvidia devices up front by scanning /sys/class/drm/card files. This is necessary to avoid cuInit() which is needed to run cuDeviceGetCount(). Also corrected a bug in delayed init, in case it was called more than once after already being disabled.
* 2021-08-09 Anthony Castaldo — Second change, needed proper printf format code.
* 2021-08-09 Anthony Castaldo — Fixed a compile bug in CUDA that only shows with later modules.
* 2021-08-07 Anthony Castaldo — Changes necessary to sort out at runtime what to do if we were compiled with one cuda module loaded, but run with a different cuda module loaded.
* 2021-08-06 Anthony Castaldo — Change to reject if compiled in headers have structures of different sizes than the version of the cuda_runtime library we found. Also rejecting libraries <11.0, they don't contain CounterAvailability functions that we currently must use in setting up events; i.e. the 10.x API differs slightly from the 11.x API. API differ
* 2021-08-05 Tony Castaldo — Update libpfm4, to be current with the following commit. Tested on orbitty.icl.utk.edu, ARMv8 Processor rev 1 (v8l). commit 790451411d481492b6a3b94077b543c3e68c6d2b Author: Stephane Eranian <eranian@gmail.com> Date:   Wed Aug 4 00:04:44 2021 -0700
* 2021-08-05 Daniel Barry — Added feature to CAT data cache benchmark to print a header line in the output files. This header shows the ID of the CPU core to which each thread was pinned. This provides more detail of the hardware context for reproducibility.
* 2021-07-30 Anthony — Cleanup.
* 2021-07-30 Anthony — C++ interface for the library-side API of papi-sde and examples that demonstrate its usage.
* 2021-07-29 Heike Jagode — Added missing changes for 'delayed init' feature to ensure that our PAPI utilities still report the correct number of native events and counters.
* 2021-07-28 Anthony Castaldo — Minor changes to Macros so merge is not confused.
* 2021-07-29 Daniel Barry — Added feature to CAT data cache benchmark to measure data read latencies for each worker thread. This allows us to observe additional data-access nuance for each core in the socket.
* 2021-07-28 Anthony Castaldo — Moved test for CUpti 11 to configure, out of Rules.cuda. Modified HelloWorld and simpleMultiGPU.cu to work properly with Legacy CUpti. Added simpleMultiGPU_CUPTI11.cu, because CUcontext monitoring requires a different protocol for managing CUcontexts. Adjusted Makefile accordingly.
* 2021-07-28 Daniel Barry — Added feature to CAT data cache benchmark to measure event occurrences for each worker thread. This allows us to accurately measure a chip's region-specific events.
* 2021-07-27 Anthony Castaldo — Changes to compile clean on Legacy Cupti.
* 2021-07-27 Anthony — Converted libsde into a header-only library to ease integration into third part software. Now the only thing a third party code needs in order to export SDEs is to #include "sde_lib.h". This change also simplified the integration into the PAPI utility papi_native_avail so "linking tricks" and weak symbols are not needed anymore.
* 2021-07-26 Anthony Castaldo — Changes to make the test code work as expected in CUpti 11, with the CUpti callback monitoring of CUcontext activity.
* 2021-07-15 Anthony Castaldo — On A100 CC 8.0, details on some events fails; and caused debug errors to print that should have been suppressed. Corrected this.
* 2021-07-15 Anthony Castaldo — disabled some debug messages.
* 2021-07-15 Anthony Castaldo — Legacy CUPTI was failing if PAPI user already had a context set.
* 2021-07-15 Anthony Castaldo — Clean up some debug code, and extraneous code in cuda_shutdown that belonged in cuda11_shutdown.
* 2021-07-12 Anthony Castaldo — Retested with valgrind for memory leaks; removed redundant code in the cuda11_read(), and corrected HelloWorld_CUPTI11.cu to use a single pass event, instead of my test 2-pass event.
* 2021-07-09 Anthony Castaldo — Corrected a bug in description formation; had HelloWorld_CUPTI11.cu report in both decimal and hexadecimal.
* 2021-07-09 Anthony Castaldo — Corrected problems with correctly choosing Legacy or CUpti-11, and issues about what to include/exclude to be compatible with previous Nvidia distributions without profile headers and libraries.
* 2021-07-09 Anthony Castaldo — Updates in commentary and documentation.
* 2021-07-07 Anthony Castaldo — All CUPTI11 code works, legacy cupti still works, on xsdk. However, configure and build still needs work, it will fail without a PerfWorks directory.
* 2021-07-08 Daniel Barry — Increased the minimum number of pointer chain accesses in the CAT data cache benchmark. This yields more stable measurements when using smaller buffer sizes.
* 2021-06-23 Anthony Castaldo — Extensive changes linux-cuda.c to use CUpti-11 when CC >= 7.0; this has been tested and seems to work on ICL xsdk, but is not optimized. Adding a changed Makefile and HelloWorld_CUPTI11.cu to better test various scenarios of cuda_context arrangements.
* 2021-06-17 Anthony Castaldo — Update libpfm4, to be current with the following commit. Tested on icl.utk.edu machines xsdk (Intel Xeon Gold 6254), morphine (AMD EPYC 7301), histamine dopamine (AMD EPYC 7402) guyot (AMD EPYC 7742).
* 2021-06-15 William Cohen — Use numeric local labels to allow compilation with LTO enabled
* 2021-06-10 Heike Jagode — Rebase to remove commit 1f48bb7 since there appear to be issues with this.
* 2021-05-28 Anthony Castaldo — Update libpfm4, to be current with the following commit: Tested on Histamine (Zen2) Dopamine (Zen2) Morphine (Zen1) XSDK (Intel).
* 2021-05-22 Anthony Castaldo — Reposting changes made by Damien Genet, with bug corrections, to delay component initialization until necessary. For CUDA, NVML, ROCM and ROCM_SMI components. CUDA and NVML components tested on XSDK, ROCM and ROCM_SMI components tested on Caffeine.
* 2021-05-17 Daniel Barry — Added feature to CAT to collect latency data for the entire parameter sweep used in the data cache reading benchmark.
* 2021-05-18 Swarup Sahoo — Added AMD Zen3 preset events. Refer section 2.1.17.2 of PPR for AMD family 19h model 01h, https://www.amd.com/system/files/TechDocs/55898_pub.zip
* 2021-05-04 Anthony Castaldo — Corrected an error discovered by Tristan Konolige; pushing the retained context when it is identical to the current context causes an error. Also updated all error exits to properly restore user context.
* 2021-05-04 Anthony Castaldo — Update libpfm4, to be current with the following commit: The ZEN3 modification cannot be tested; we have no ZEN3 machine. The other changes are not machine specific; we did a smoke test (compile and execute papi_component_avail, papi_native_avail) on ICLs xsdk machine.
* 2021-05-03 Anthony Castaldo — Correcting a typo that can cause a segfault.
* 2021-04-29 Anthony Castaldo — Using macros (like papi_debug.h) instead of if (0).
* 2021-04-28 Anthony Castaldo — Additional context cleanup in _cuda_update_control_state() to accomodate issues with non-primary contexts.
* 2021-04-23 Anthony Castaldo — Deleted an extraneous paranoid line of code.
* 2021-04-22 Anthony Michael Castaldo — Improved automatic detection of ROCM root directory, so exporting PAPI_ROCM_ROOT is not always necessary on systems that load modules. We recognize environment variables ROCM_PATH, ROCM_DIR, and ROCMDIR. At compile time, we have code in Rules.rocm that can examine the LD_LIBRARY_PATH variable and extract possible -Iinclude_paths for the compile. This uses 'awk', but if 'awk' is not present on the system it won't cause an error message. We will also still use PAPI_ROCM_ROOT at compile time, preferentially, when specified. README.md has been updated to reflect these changes.
* 2021-04-22 William Cohen — Correct warning message to 'make dist-targz'.
* 2021-04-20 William Cohen — Check to ensure that mallocs allocated memory in papi_multiplex_cost.c
* 2021-04-13 Anthony Castaldo — This code corrects an oversight and works if the application has already created a non-primary context before calling PAPI_library_init(). A modification of HelloWorld.cu, HelloWorld_NP_Ctx.cu, will test if if the code works with a non-primary context created; HelloWorld.cu tests without creating a non-primary context. This was tested on XSDK with two Titan V GPUs.
* 2021-04-12 Anthony — Changes to the configure script to accommodate the (upcoming) intel_gpu component.
* 2021-04-07 Anthony Castaldo — The following fixes are for AMD Zen3 CPUs, untested by ICL, we have no access to Zen3 processors at this time.
* 2021-04-06 Anthony — Adjust cache leves based on information in config file, and make the default config file empty.
* 2021-04-05 Anthony — Changed CAT code to enable dynamic discovery of cache sizes, and also user provided values (through .cat_cfg file).
* 2021-03-24 Anthony Castaldo — This affects the processor AMD Zen2, we tested on it. It affects the following processors we do not have to test on; A64FX (Fujitsu ARM),AMD Zen3, Intel TigerLake and RocketLake.
* 2021-03-11 Frank Winkler — Improved randomization of rank id.
* 2021-03-10 Frank Winkler — Added more hardware information in hl performance output.
* 2021-03-09 Frank Winkler — Improved hl performance output for parallel programs.
* 2021-02-24 Anthony Castaldo — Corrects a sequence error in the use of cuda context that was causing an issue on Summit.
* 2021-02-24 Anthony Castaldo — interim commit for merge
* 2021-02-22 Frank Winkler — Improved hl output.
* 2021-02-22 Anthony Castaldo — Modifications to commentary in instructional example code, for accuracy and clarity.
* 2021-02-19 Anthony Castaldo — Deleting obsolete ROCM_Makefile.
* 2021-02-19 Anthony Castaldo — Re-adding components/rocm/tests/ROCM_Makefile to resolve merge conflict. It is obsolete, and will be deleted in a future update.
* 2021-02-19 Anthony Castaldo — ROCM_Makefile is obsolete; incorporated into Makefile.
* 2021-02-19 Anthony Castaldo — Restoring ROCM_Makefile to deal with merge conflictt. Adding sensor 0-relative, 1-relative fix.
* 2021-02-19 Frank Winkler — Revised hl output.
* 2021-02-19 Anthony Castaldo — Clean up code and library search for both components. For ROCM, automatically set rocprofiler environment variables if missing.
* 2021-02-18 Frank Winkler — Fixed raw output.
* 2021-02-18 Frank Winkler — Added component name to event definitions.
* 2021-02-16 Masahiko, Yamada — remove PAPI_L1_TCA and PAPI_L1_TCH for a64fx
* 2021-02-15 Daniel Barry — Modified the multi-threaded CAT data cache benchmark so that each thread's memory buffer is allocated in separate threads.
* 2021-02-14 Frank Winkler — Modified recording of regions. - All regions have an unique region ID - Added hierarchy for nested regions - List regions that have the same name separately in the JSON output
* 2021-02-12 Masahiko, Yamada — remove PAPI_L1_DCA and PAPI_L1_DCH for a64fx
* 2021-02-11 Daniel Barry — Implemented a multi-threaded version of the CAT data cache benchmarks.
* 2021-02-10 Daniel Barry — Removed the CAT data cache benchmarks from running in a separate, stand-alone thread.
* 2021-02-04 Anthony Castaldo — Minor modifications to comments and report code.
* 2021-02-03 Anthony Castaldo — In ROCM and ROCM_SMI, deleted specialty Makefiles and incorporated all makes into .../tests/Makefile. This required minor mods to existing files to get a clean compile without warnings. Added two files, rocm_example.cpp and rocmsmi_example.cpp, that are coding tutorials with heaving commenting for programmers new to PAPI; these will also be used for video tutorials by AMD.
* 2021-01-29 Anthony — Added the directory lib under sde/tests
* 2021-01-29 Anthony — Cleaned up the stand alone sde code. Now it does not need to be built into a separate library, the sources/objects can be integrated into third party libraries directly.
* 2021-01-20 Anthony — Removed trailing white spaces.
* 2020-09-03 Anthony — + Major restructuring of the libsde code, so that it can be used more easily by external projects. + Changes to the tests so they conform to the rest of PAPI's testing infrastructure.
* 2020-05-30 Anthony — Fixed a problem occuring in non-debug builds and updated the README file.
* 2020-05-29 Anthony — Better header organization.
* 2020-05-29 Anthony — New test with no libpapi.so linkage was added.
* 2020-05-29 Anthony — More complete support for overflowing. Now, case r5 is supported.
* 2020-05-29 Anthony — Support for overflow for the case of created counters as well as r[1-4].
* 2020-05-28 Anthony — Pushing the library interface of SDEs into a stand-alone library (libsde.so).
* 2021-01-26 Masahiko, Yamada — Add string length check before strncpy() and strcat() calls in _mx_init_component()
* 2021-01-21 William Cohen — Only check for libpfm.a if static libraries are being used.
* 2021-01-22 Frank Winkler — Improved performance report script.
* 2021-01-18 Frank Winkler — Fixed real time measurement.
* 2021-01-07 Damien Genet — Merged in feature/pr_nec (pull request #157)
* 2021-01-05 Masahiko, Yamada — Get model_string for ARM processor from pfm_get_pmu_info() function
* 2020-12-23 Peinan Zhang — Changed query based data read with timeout rather than blocked till data available.
* 2020-12-18 Peinan Zhang — Add intel_gpu component to collect Intel GPU performance metrics
* 2020-12-17 Heike Jagode — Deleting Tony's hard failure for check_exclude_guest() if perf_event_open fails. There shouldn't be a failure since exclude_guest_unsupported is already set before perf_event_open is called. At this point, if perf_event_open fails it should just return but not result in a hard failure.
* 2020-12-15 Masahiko, Yamada — modify PAPI_FP_INS and PAPI_VEC_INS for A64FX supports
* 2020-12-14 Masahiko, Yamada — Add or modify various A64FX support events, including floating point events (PAPI_FP_OPS, PAPI_SP_OPS, PAPI_DP_OPS).
* 2020-12-14 Masahiko, Yamada — Corrected typo for A64FX support (PAPI_L2_DCH is a typo of PAPI_L2_DCA)
* 2020-12-11 Anthony Castaldo — Update libpfm4, to be current with the following commit:
* 2020-12-07 Anthony Castaldo — Update libpfm4, to be current with the following commit: --------------------------------------------------------------
* 2020-11-30 William Cohen — Remove mention of the removed iozone test in the appio README.md.
* 2020-11-30 William Cohen — Remove bundled iozone due to incompatible license.
* 2020-11-25 Masahiko, Yamada — fix for performance improvement of _mx_init_component() function
* 2020-11-18 Gerald Ragghianti — Typo in library file name
* 2020-11-17 Damien Genet — Fix: location is not stored, so mark that location is broken
* 2020-11-17 Anthony Castaldo — Removed debug messages.
* 2020-11-17 Anthony Castaldo — Removing debug messages.
* 2020-11-17 Anthony Castaldo — Improved argument handling in nvlink_all.cu and nvlink_bandwidth.cu.
* 2020-11-06 Anthony Michael Castaldo — Changed ROCM_Makefile to require PAPI_ROCM_ROOT; and to cross-compile for all "Instinct" GPUs.  Code in component to set needed environment variables if not defined, or ensure definition meets expectations.
* 2020-11-05 Anthony Michael Castaldo — First draft of changes to automatically find and set environment variables automatically.
* 2020-11-03 Daniel Barry — Added checks for the return values of calls to malloc(), calloc(), and realloc(). This way, the user will know if there are issues with allocating memory.
* 2020-11-02 Daniel Barry — Increase buffer size for larger input files to CAT. Since the number of qualifier counts is equal to the number of event names in the input file, the size of the buffer containing the qualifier counts should be equal to the size of the buffer containing the event names. This change is necessary to accommodate large input files. This change was tested on the IBM POWER9 architecture.
* 2020-10-27 Anthony Castaldo —     Added explicit Compute Capability retrieval and checking to disable component if CC>=7.5 and cannot work with Legacy CUPTI.
* 2020-10-26 Anthony Castaldo — Added explicit Compute Capability retrieval and checking; also added a filter to exclude multipass metrics; as well as timing (if a #define is made) of how long that takes. On 1 V100 device, 95-98ms additional time in init_component().
* 2020-10-23 Björn Dick — adapted setting FFLAGS in src/components/sde/tests/Makefile in order to make it work with flang (otherwise crashes due to unknown flag '-free')
* 2020-10-22 Anthony Castaldo — Just the compute capability check.
* 2020-10-20 Anthony Castaldo — Thread Safety is added to the cuda component; protecting functions with PAPI locks: _papi_hwi_lock(COMPONENT_LOCK) and _papi_hwi_unlock(COMPONENT_LOCK).  The BlackScholes directory is added; a slightly modified version of an Nvidia sample program, used to exercise a great deal of computation.  This includes new code, in particular thr_BlackScholes.cu uses phtreads and executes the kernel from several threads, using PAPI_read() in each, to test the above thread safety. Also tested with helgrind (tool within valgrind to test for threading synchronization issues).
* 2020-10-19 Anthony Castaldo — Changes to init_component() to properly set the component vector element disabled_reason() if init fails. Also changes to eliminate compiler warnings for failing to process return codes from string functions (strcpy and snprintf and variants), and to check for alloc() failures; but only in the init_component() functions and any functions it invokes.
* 2020-10-15 Anthony Castaldo — Update libpfm4, to be current with the following commits: --------------------------------------------------------------
* 2020-10-12 Frank Winkler — Fixed bug in summary mode 2. Each region can have a different number of ranks and threads.
* 2020-10-12 Frank Winkler — Fixed bug in summary mode. Starting from the second region all events were ignored by a wrong indented break statement.
* 2020-10-09 Frank Winkler — Fixed bug for IPC metric.
* 2020-10-09 Frank Winkler — Revised performance output.
* 2020-10-08 Anthony Castaldo — Got rid of unnecessary PAPI_MAX_STR_LEN-2, replaced with PAPI_MAX_STR_LEN.
* 2020-10-08 Sebastian Mobo — Added instruction-cache preset events for the Zen2.
* 2020-10-08 Heike Jagode — For zen2, since FP_OPS counts both single- and double-prec operations correctly, we don't need to confuse the user with additional DP_OPS and SP_OPS events. So, I'm taking them out.
* 2020-10-08 Anthony Castaldo — Brought appio and coretemp in line with other components for standardization.
* 2020-10-08 Anthony Castaldo — In addition to init_component() changes to ensure all possible failing return paths set a disable_reason; added testing for string functions; strncpy and snprintf, to avoid compiler warnings about uninterpreted return values.
* 2020-10-08 Frank Winkler — Added derived events for summary report.
* 2020-10-06 Anthony Castaldo — Most changes here ensure that any exit from the init_component() function that disables the component will give a sensible reason for the disable in the component vector string, which is reported by papi_component_avail.  Additional changes were made to prevent compiler warnings on various issues; such as unused values or incompatible formatting.
* 2020-10-04 Frank Winkler — Several improvements.
* 2020-10-02 Frank Winkler — Started with summary output format.
* 2020-10-01 Damien Genet — Fixing the infiniband component for the 3 counters that are misplaced in the filesystem and thus wrongfully listed as 32 bits
* 2020-09-24 Heike Jagode — Added missing 'PRESET' to csv file.
* 2020-09-24 Heike Jagode — Added presets for floating-point instructions (FP_INS, VEC_DP, VEC_SP) for AMD zen2.
* 2020-09-24 Heike Jagode — Added presets for floating-point operations (FP_OPS, DP_OPS, SP_OPS) for AMD zen2.
* 2020-09-18 Frank Winkler — Added min, avg, and max for instantaneous events.
* 2020-09-17 Frank Winkler — Fixed bug for empty strings in PAPI_EVENTS.
* 2020-09-11 Frank Winkler — Improved coding style.
* 2020-09-11 Frank Winkler — Simplified event definitions.
* 2020-09-09 Daniel Barry — Added __FILE__ and __LINE__ to the error messages which are shown depending on the return value of snprintf(). This way, the user will know from where the error message originated.
* 2020-09-09 Anthony Castaldo — Uninitialized retcode variables caused problems on Power 9.
* 2020-09-09 Frank Winkler — Added event definitions to performance report.
* 2020-09-08 Daniel Barry — Added if-statements to check whether the number of characters intended to be written to the destination buffer exceed the size of the buffer. This prevents GCC 9.1.0 from warning that the destination buffer may not be large enough to store the contents of the source buffers.
* 2020-09-08 Anthony Castaldo — Corrected a too-specific reference in Makefile; and changed a #define from CamelCase to all caps.
* 2020-08-28 Anthony Castaldo — Capitalized #defines.
* 2020-08-27 Anthony Castaldo — Moved structure typedef definitions ahead of their use in the source file; and changed references to structures within structures to use the typedef type. Removed '#if 0' test code for the binary search function.
* 2020-08-26 Anthony Castaldo — This modifies PAPI_library_init() to initialize components in two classes, separated by the initialization of the papi thread structure.  The first class is those that need no thread structure, currently everything but perf_event and perf_event_uncore. Following the init of the threading structure, we init the second class (perf_event and perf_event_uncore) that DOES need the thread structure to successfully init_component().  This required a change to _papi_hwi_init_global(), to add an argument to distinguish which class it should initialize.
* 2020-08-26 Anthony Castaldo — Update libpfm4, to be current with the following commit: --------------------------------------------------------------
* 2020-08-25 Anthony Castaldo — Implement cumulative counters (as per PAPI specification) for cuda events and metrics. It includes two #define controlled diagnostics that may prove necessary on other models of GPUs. 'Produce_Event_Report' will print (to stderr) all the events discovered, and 'Expose_Unenumerated_Events' will add as PAPI events (beginning 'cuda:::unenum_event:0x...') those events used by cuda metrics that are not reported by nvidia's event enumeration routines. These are explained further in code comments.
* 2020-08-21 William Cohen — Makefile to generate papi-x.y.z.tar.gz directly from git repo
* 2020-08-14 Anthony Castaldo — Update libpfm4, to be current with the following commit: -------------------------------------------------------------- commit e162519d26d313860a9e69889bcc67406f92edc9 Author: Stephane Eranian <eranian@gmail.com> Date:   Wed Aug 12 15:23:27 2020 -0700
* 2020-07-27 Anthony Castaldo — Update libpfm4, to be current with the following commits: -------------------------------------------------------------- commit 2c3d94eb306e52a48fe881c8c5d68fd8849bccc0 Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Jul 24 15:52:03 2020 -0700
* 2020-07-24 Anthony Castaldo — Added an extra HSA_TOOLS_LIB export that is required to read counters.
* 2020-07-23 Frank Winkler — Revised previous push.
* 2020-07-23 Frank Winkler — Some events like power, temperature or all nvml events are always considered instantaneous.
* 2020-07-17 Anthony — Separated the cache preset events of AMD Zen1 and Zen2 and added some more.
* 2020-07-17 Frank Winkler — Revised configure script.
* 2020-07-14 Anthony Castaldo — Added two utilities that perform event reading for AMD GPUs without any use of the PAPI interface. To prove that PAPI is not the problem when events are not working correctly.
* 2020-07-03 Frank Winkler — Added instructions how to find the correct paths of all required shared libraries at runtime.
* 2020-06-24 Steve Kaufmann — Added PAPI preset support for Fujitsu A64FX.
* 2020-06-23 Anthony Castaldo — commit 5a623727cf7111afd09df2cdb0ff4b294d31efa7 Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Jun 19 15:07:01 2020 -0700
* 2020-06-23 Frank Winkler — README.md edited online with Bitbucket
* 2020-06-18 Heike Jagode — README.md edited online with Bitbucket
* 2020-06-18 Frank Winkler — README.md edited online with Bitbucket
* 2020-06-18 Frank Winkler — README.md edited online with Bitbucket
* 2020-06-18 Frank Winkler — README.md edited online with Bitbucket
* 2020-06-12 Anthony Castaldo — Added an include directory to the Rules file, to fix a coding error on including a new file, kfd_ioctl.h. (The #include statement includes the directory rocm_smi when it should not.)
* 2020-06-12 Frank Winkler — Generated new configure file with autoconf 2.69 on saturn.icl.utk.edu.
* 2020-06-12 Frank Winkler — Added rpath and runpath to find libpfm.so and libpapi.so if not specified via LD_LIBRARY_PATH. The search path at runtime can be overriden by LD_LIBRARY_PATH.
* 2020-06-12 Frank Winkler — README.md edited online with Bitbucket
* 2020-06-12 Frank Winkler — README.md edited online with Bitbucket
* 2020-06-12 Frank Winkler — README.md edited online with Bitbucket
* 2020-06-10 Anthony Castaldo — Update libpfm4, to be current with the following commit: -------------------------------------------------------------- commit c99ed181402b21e74744d5f602aceb6a320c7ded Author: Stephane Eranian <eranian@gmail.com> Date:   Sat May 30 18:08:52 2020 -0700
* 2020-06-03 Heike Jagode — Bug fix for architectures with more than 40 PMUs (e.g. KNL has > 40 uncore PMUs).
* 2020-05-29 Frank Winkler — README.md edited online with Bitbucket
* 2020-05-29 Frank Winkler — Added FAQ entry for component perf_event_uncore.
* 2020-05-29 Frank Winkler — New readme files for the components in markdown format (2/2).
* 2020-05-29 Frank Winkler — README.md edited online with Bitbucket
* 2020-05-28 Anthony Castaldo — Improved _init_component() code in rocm, rocm_smi to populate the disabled reason if library failures are encountered during initialization. Per Steve Kaufmann request 05/28/2020.
* 2020-05-28 Frank Winkler — New readme files for 16 components in markdown format.
* 2020-05-22 Anthony Castaldo — Removed some leftover development lines from nvml/tests/Makefile
* 2020-05-21 Anthony Castaldo — Changes to make rocm_smi have its own PAPI_ROCMSMI_ROOT variable, and given PAPI_ROCM_SMI_LIB as an override environment variable.
* 2020-05-21 Anthony Castaldo — Changed files to Markup versions, matched templates, for five components; cuda, nvml, pcp, rocm, rocm_smi.
* 2020-05-19 Anthony Castaldo — Update libpfm4, to be current with the following commit: --------------------------------------------------------------
* 2020-05-15 Frank Winkler — Generated new configure file with autoconf (2.69) on saturn.
* 2020-05-07 Anthony — Avoid creating a variable for something that is only used for a debug message. Otherwise we create compiler warnings when debug is not enabled.
* 2020-05-07 Frank Winkler — Added CFLAG -DSDE.
* 2020-04-30 Frank Winkler — Fixed static build. - SDE component is disabled - "ctest" shlib is disabled
* 2020-04-27 Anthony Castaldo — Update libpfm4, to be current with the following commit: --------------------------------------------------------------
* 2020-04-24 Frank Winkler — Another test for "--with-static-tools".
* 2020-04-24 Frank Winkler — Fixed configure options for shared and static builds.
* 2020-04-24 Frank Winkler — Modified instructions for release procedure.
* 2020-04-24 Frank Winkler — Generated new configure file with autoconf 2.69 on saturn.
* 2020-04-19 Frank Winkler — Fixed bug for MPI tests.
* 2020-04-17 Anthony Castaldo — Repaired error code and error reporting on the check for compute capability >= 7.5. An uninitialized variable.
* 2020-04-14 Anthony Castaldo — Changed component to handle mis-numbered sensors coming from driver. Cleaned up commenting in power_monitor_rocm.cpp.
* 2020-04-13 Anthony Castaldo — Update libpfm4, to be current with the following commit: -------------------------------------------------------------- commit 34164d84bba9794c75b4ce643ad74aad1362e97a Author: Stephane Eranian <eranian@gmail.com> Date:   Wed Apr 8 01:02:22 2020 -0700
* 2020-04-03 Frank Winkler — Added text for bug fix release procedure.
* 2020-04-03 Frank Winkler — Fixed typo.
* 2020-04-02 Anthony — Added example that shows how to implement Created Counters in a library and how to use PAPI_overflow() to monitor an SDE.
* 2020-04-01 Frank Winkler — Fixed bug in install process. Create BINDIR before copying the hl python script to BINDIR.
* 2020-03-30 Anthony Castaldo — Changed to report a useful disabled reason when devices with compute capability >=7.5 are present; these no longer support the CUPTI interface.
* 2020-03-24 Anthony Castaldo — New code for power monitoring, replaces rocmcap_plot.cpp. Extensive new command line options.
* 2020-03-19 Anthony Castaldo — Update libpfm4, to be current with the following commit: -------------------------------------------------------------- NOTE: Intel Tremont and IceLake changes have not been tested; due to lack of hardware at this time.
* 2020-03-18 Frank Winkler — Some modifications.
* 2020-03-17 Frank Winkler — Generated configure via autoconf 2.69.
* 2020-03-17 Frank Winkler — Put paranoid check message at the end of configure.
* 2020-03-16 Frank Winkler — Replaced paranoid check error with warning.
* 2020-03-14 Frank Winkler — Added paranoid check at configuration.
* 2020-03-14 Frank Winkler — Removed linux condition.
* 2020-03-14 Frank Winkler — Added several thread identification functions for PAPI_thread_init (2).
* 2020-03-13 Frank Winkler — Added several thread identification functions for PAPI_thread_init.
* 2020-03-05 Anthony Castaldo — Further clarifications in release_procedure.txt
* 2020-03-04 Anthony Castaldo — Updated release_procedure.txt, fixed Notes, changed version to 6.0.1.
* 2020-02-28 Anthony Castaldo — Changes to keep runstatedir lines in papi/src/configure, instructions in release_procedure.txt describing how to accomplish that.
* 2020-02-28 Anthony Castaldo — Changes necessary for PAPI release 6.0.0.
* 2020-02-27 Steven Kaufmann — Making MPI tester optional
* 2020-02-22 Frank Winkler — Added fortran wrappers for PAPI_rate_stop and PAPI_hl_stop. Also fixed doxygen documentation for PAPI_flops_rate.
* 2020-02-21 Anthony Castaldo — Deleted test files from the repository, and commented-out debug lines from rocm_smi.
* 2020-02-21 Anthony Castaldo — Added patches provided by Evgeny Shcherbakov (AMD), and corrected bugs in rocm_all.cpp. Tested and now functions as expected.
* 2020-02-20 Anthony — Added -lrt to LIBS (if needed) so that it propagates into the pkg-config file papi.pc. Also, removed the explicit flag from the SDE tests Makefile.
* 2020-02-19 Anthony — Enabled overflow by default in SDE and added -lrt detection in the configure script.
* 2020-02-19 Anthony Castaldo — Reconciling this version of rocm_all.cpp with another pull request.
* 2020-02-18 Anthony Castaldo — ---Correct cuda push/pop context consistency---
* 2020-02-16 Daniel Barry — Added check for whether or not the user provided a benchmark category.
* 2020-02-13 Frank Winkler — Little change in test script based on commit 14cebbc.
* 2020-02-13 Anthony Castaldo — Modifications for more thorough error-checking in routines before using pointers (ensuring they are non-NULL). Suggested by Steve Kaufmann.
* 2020-02-11 Anthony Castaldo — Removed a debug message.
* 2020-02-10 Anthony Castaldo — Corrects a problem producing a segfault. The function MakeRoomAllEvents() can realloc() a table, but this can make the use of a pointer into the former area produce a segfault.
* 2020-01-31 Anthony Castaldo — A new utility added to tests, and debug lines (commented out) in component code until SMI library problem with power events is sorted out.
* 2020-01-31 Anthony Castaldo — We have to fopen/fclose the system file for every read; otherwise Linux caches the file and reports the same values every time.
* 2020-01-30 Anthony — Turned verbosity of HL API off by default.
* 2020-01-30 Anthony Castaldo — Rewrite to use ctx and ctl structures for thread safety.
* 2020-01-29 Anthony Castaldo — Corrected a typo in Rules.rocm, and cleaned up a test program rocm_all.cpp.
* 2020-01-29 Anthony Castaldo — Provided some insurance that io component initialization occurs only once.
* 2020-01-29 Daniel Barry — Removed unnecessary error reporting.
* 2020-01-28 Anthony — Avoid computing the latencies twice.
* 2020-01-28 Anthony — Updated the info that is reported by the component about itself.
* 2020-01-28 Daniel Barry — Fixed bug in FLOPS benchmark.
* 2020-01-28 Anthony — Added code to show progress if the user asks for it (-verbose flag), and removed confusing error messages and dead code.
* 2020-01-28 Daniel Barry — Per the sscanf man page, it is unnecessary to call free() in this block since memory for the string would not be allocated.
* 2020-01-27 Daniel Barry — Added checks for negative amounts of qualifers provided by the user.
* 2020-01-27 Anthony — Fixed problems with debug macro.
* 2020-01-24 Damien Genet — Adds missing rule for compilation of MPI test
* 2020-01-24 Anthony Castaldo — New libpfm4 contains "aliased" pmus for backward compatibility, amd64_fam17h == amd64_fam17h_zen1; this causes us to put BOTH pmus into the PMUs supported string and double the events in native_avail. This update recognizes when aliases exist (the names must be hard-coded) and uses only one of the most recent name.
* 2020-01-24 Frank Winkler — Removed email address in readme.
* 2020-01-24 Frank Winkler — Use new API call PAPI_rate_stop to stop a running rate event set.
* 2020-01-24 Frank Winkler — Added new API calls to stop running event sets of rate and high-level functions.
* 2020-01-23 Anthony — Removed spurious check that was preventing closing the output file properly.
* 2020-01-23 Heike Jagode — Retirement of infiniband_umad component.
* 2020-01-23 Frank Winkler — Added option to specify presets for flips and flops.
* 2020-01-22 Damien Genet — Propagating MPICC to components tests
* 2020-01-22 Damien Genet — snprintf return value, a classic now. And the 3-space indentation.
* 2019-09-04 Rizwan-ICL — Added descriptions for events of infiniband component using documentation provided by Mellanox; Added test code to test the various events in infiniband component and modified Makefile to compile the test code;
* 2020-01-22 Damien Genet — Merged in feature/powercap_ppc (pull request #34)
* 2020-01-22 Frank Winkler — Fixed bug for python3.
* 2020-01-22 Frank Winkler — Revised Matlab wrapper.
* 2020-01-22 Frank Winkler — Bug fix that was caused by commit db01193.
* 2020-01-22 Frank Winkler — Improved some comments.
* 2020-01-21 Damien Genet — Adds missing checks for snprintf. A return value larger than the buffer is not really an error, just a poor design, but whatever.
* 2020-01-20 Frank Winkler — Renamed papi_rate_stop to papi_stop_events.
* 2020-01-20 Frank Winkler — Fixed bug. Check for empty string in PAPI_EVENTS.
* 2020-01-20 Frank Winkler — Fixed typo.
* 2020-01-20 Frank Winkler — Improved cleanup function.
* 2020-01-18 Frank Winkler — Added examples that show how to mix hl, ll, and rate functions.
* 2020-01-17 Anthony Castaldo — Update libpfm4, to be current with the following commit: --------------------------------------------------------------
* 2020-01-17 Frank Winkler — Added feature that allows mixing of rate functions and hl functions.
* 2020-01-16 Anthony Castaldo — Added two machine types to papi_events.csv to be in line with libpfm4 update to support amd64_fam17h_zen1 and zen2.
* 2020-01-16 Anthony — Fixed dependency in Makefile.
* 2020-01-16 Frank Winkler — Added PAPI_rate_stop() that stops any rate function.
* 2020-01-16 Damien Genet — Add new component for sensors reading on PowerPC 9 Enable with ./configure --with-components="sensors_ppc"
* 2020-01-16 Frank Winkler — Fixed little bug in test script.
* 2020-01-16 Anthony Castaldo — Changed Rules file to look in multiple places for rocm_smi.h, it moved between rocm releases. Rewrote a routine to be more efficient and eliminate a string-size warning. Made some diagnostic outputs that were left active in previous commit dependent on #ifdef macros.
* 2020-01-15 Frank Winkler — Fixed memory leak in high-level API.
* 2020-01-14 Anthony — Added new tests/examples under the SDE component and organized them based on complexity.
* 2020-01-14 Anthony — Improved and corrected the checks that relate to counter groups and recorders.
* 2020-01-13 Anthony — Added the weak symbols for SDE to papi_native_avail, so the utility works when PAPI is not configured with the SDE component.
* 2020-01-13 Anthony — Improved the code that checks the command-line arguments.
* 2020-01-13 Anthony Castaldo — Update libpfm4, to be current with the following commits: --------------------------------------------------------------
* 2020-01-06 Anthony — Moved the responsibility of listing SDEs of a library/executable to papi_native_avail instead of the SDE component.
* 2020-01-06 Anthony — Updated the variables that are used in the debug messages in accordance to a previous commit that made these variables thread safe.
* 2020-01-03 Frank Winkler — Changed name of some derived metrics.
* 2020-01-03 Frank Winkler — Added new derived metrics.
* 2020-01-03 Frank Winkler — Little format changes.
* 2020-01-03 Frank Winkler — Fixed bug in high-level API caused by commit ff8ff65.
* 2020-01-02 Frank Winkler — Revised default events for flops and flips.
* 2019-12-20 Frank Winkler — papi.c edited online with Bitbucket
* 2019-12-20 Frank Winkler — high_level.c edited online with Bitbucket
* 2019-12-20 Frank Winkler — PAPI_ipc.c edited online with Bitbucket
* 2019-12-20 Frank Winkler — PAPI_flops.c edited online with Bitbucket
* 2019-12-20 Frank Winkler — PAPI_flips.c edited online with Bitbucket
* 2019-12-20 Frank Winkler — PAPI_epc.c edited online with Bitbucket
* 2019-12-19 Anthony — Fixed issues in the SDE component unveiled by Coverity.
* 2019-12-19 Daniel Barry — Fixed typo in comment for argument parsing.
* 2019-12-19 Frank Winkler — Fixed typo.
* 2019-12-19 Frank Winkler — Further clean-up.
* 2019-12-19 Daniel Barry — Removed unnecessary variables and checks. Refactored code blocks. Added comments in the main driver file.
* 2019-12-19 Frank Winkler — Clean-up of old high-level functions.
* 2019-12-18 Frank Winkler — Fixed typo in papi_component_avail.1. See pull request #2.
* 2019-12-17 Anthony Castaldo — Debugging line removed.
* 2019-12-16 Anthony — Renamed cit_collect to cat_collect.
* 2019-12-16 Anthony Castaldo — A rewrite of linux-io.c to make it dynamic and work like other components. Removal of linux-io.h. Remove of the test io_multiple_components.c.
* 2019-12-16 Anthony — Clarified comment.
* 2019-12-16 Anthony — Removed unnecessary work when setting up the list of events, and minor cosmetic changes.
* 2019-12-16 Daniel Barry — Cleaned up comments.
* 2019-12-16 Anthony Castaldo — Update libpfm4, to be current with the following commit: --------------------------------------------------------------
* 2019-12-16 Anthony Castaldo — Corrected a working but convoluted line of code.
* 2019-12-13 Frank Winkler — Minor documentation corrections.
* 2019-12-13 Frank Winkler — Fixed some thread definitions.
* 2019-12-13 Frank Winkler — Revised documentation of high-level API.
* 2019-12-13 Frank Winkler — Renamed the output directory of the high-level API from 'papi' to 'papi_hl_output'.
* 2019-12-13 Frank Winkler — Revised documentation.
* 2019-12-13 Frank Winkler — Adjusted doxygen documentation.
* 2019-12-12 Frank Winkler — Reimplemented rate functions and adjusted examples.
* 2019-12-11 Daniel Barry — Added PAPI_cleanup_eventset() call to each of the benchmarks. This removes events from the event set.
* 2019-12-10 Anthony Castaldo — Minor changes to text and a setting that was for development only.
* 2019-12-10 Frank Winkler — Made rate functions thread safe.
* 2019-12-09 Anthony — Changed the order of the linker flags so that -ldl is at the end since libpapi.a needs libdl.so but not the other way around.
* 2019-12-06 Heike Jagode — README.md edited online with Bitbucket
* 2019-12-06 Steve Kaufmann — The changes here are based on a patch provided by Steve Kaufmann; to correct a misnamed event in papi_events.csv, and prevent a segfault in rocm when a context pointer is null. Additional changes by Tony Castaldo check to see if the necessary rocprofiler environment variables have been set; and disable the component if they are not, with an informative reason to be reported by papi_component_avail. (The component will not work without them).
* 2019-12-05 Frank Winkler — Replaced HighLevelInfo with RateInfo.
* 2019-12-03 Anthony Castaldo — extra '#' in "%#p" print formats, using just '%p'.
* 2019-12-03 William Cohen — Use the noreturn attribute only when the compiler support GNU C extensions.
* 2019-12-03 William Cohen — Properly mark some test_utils.c functions with noreturn attributes
* 2019-12-02 Anthony Castaldo — The code in this commit all failed a Coverity scan (a code consistency tool) that correctly identified memory leaks, potential buffer overflows, and failures to close a file or directory that had been opened.
* 2019-12-02 Frank Winkler — Reimplemented rate calls such as PAPI_flips, PAPI_flops, etc.
* 2019-11-20 William Cohen — Limit Fortran 90 compilers options to SDE component Fortran 90 code
* 2019-11-21 Heike Jagode — README.md edited online with Bitbucket
* 2019-11-15 Anthony Castaldo — Current With the following 3 commits:
* 2019-11-14 Daniel Barry — Swapped lines 268 and 269 of main.c so that the appropriate memory allocation is freed, and the pointer is then set to NULL.
* 2019-11-13 Anthony Castaldo — For consistency with powercap and rapl components, moved nvmlcap_plot.cu to a new nvml/utils/ directory. New Makefile in nvml/utils/ and adjusted Makefile in nvml/tests/. Created a new README for nvmlcap_plot. No code changes; but tested configure and make of PAPI and nvmlcap_plot.
* 2019-11-08 Anthony Castaldo — Fixed an inaccurate comment.
* 2019-11-08 Anthony Castaldo — Added a paragraph of usage info to README; also reformatted existing comments to comply with 80 char line limit; without changing their content. rapl_overflow.c was confusing, it was not using the PACKAGE_ENERGY_CNT event to test for overflow, and the scaled value seemed to wrap in 85ms. This seemed to conflict with the results of rapl_wraparound; which computes a wraparound time in 85 minutes. rapl_overflow.c is now in line with an 80-90 minute wraparound vaue.
* 2019-11-07 Anthony Castaldo — Changes to properly mask energy values to uint32, and accumulate them to return a 64-bit accumulator. Verified wraparound time at approx 85 minutes (for a 32 bit read). That is the maximum allowed time between reads; the 64-bit value returned should never wrap. (Some tabs converted to spaces in changed code.)
* 2019-11-01 Frank Winkler — Removed Doxygen documentation for internal functions and moved code block for multiplex initialization.
* 2019-10-31 Anthony Castaldo — Fixed a typo in the error message.
* 2019-10-31 Anthony Castaldo — The changes to papi.c, papi_internal.c, threads.h and threads.c correct a race condition that was the result of all threads using the same two static variables (papi_event_code and papi_event_code_changed) to temporarily record a state of operation. The solution was to make these variables unique per thread, using the ThreadInfo_t structure already provided in PAPI for such purposes. The file krentel_pthread_race.c is a stress test to produce race conditions. filter_helgrind.c reduces the volume of --tool-helgrind output to a more manageable summary. Both are added to Makefile.recipies.
* 2019-10-31 William Cohen — This code is a modification of krentel_pthreads.c, to better test some race conditions. It is not included in the standard tests; it is a diagnostic that should be run with "valgrind --tool=helgrind".
* 2019-10-31 Anthony Castaldo — Changed SUBDBG error reporting in new code to a single message instead of two, before the unlock code (so no race condition on variables in report). Cosmetics.
* 2019-10-28 Anthony Castaldo — Update libpfm4, current with: -------------------------------------------------------------------------------- commit b4facf3117e7ead093935266c4f0115396c09f24 Author: Stephane Eranian <eranian@gmail.com> Date:   Sat Oct 26 09:11:17 2019 -0700
* 2019-10-28 Daniel Barry — Added checks for improperly formatted lines in the user-provided event list.
* 2019-10-25 Anthony Castaldo — In two places, we exited the routine allocate_native_event() because we could not find a mask or attribute in an event name (because the event was supported but the given mask was not), and failed without unlocking the NAMELIB_LOCK, or cleaning up allocated memory.
* 2019-10-24 Anthony Castaldo — New events added, some bugs corrected. ROCM_SMI_Makefile is modified to use env variable $PAPI_ROCM_ROOT to make it easier to compile with a local version of the rocm_smi library. rocm_smi_all.txt is the output of a run of rocm_smi_all.cpp, which has been modified to handle strings, and skip testing of events that bomb (unhandled exceptions in library code). NOTE this code may still contain debug printing to stderr, to be removed in the final version after all issues are corrected. -Tony
* 2019-10-24 Frank Winkler — Removed TLS definitions.
* 2019-10-24 Frank Winkler — Replaced PAPI_TLS_KEYWORD with THREAD_LOCAL_STORAGE_KEYWORD due to ABI conflicts.
* 2019-10-18 Anthony Castaldo — This is a first installment of the rewrite of the rocm_smi component. It currently requires a private install of the updated library (with iterators), and a special Rules.file, PAPI_ROCM_ROOT, and PAPI_ROCM_SMI_MAIN. It works as far as executing utils/papi_native_avail; but none of the events have been tested yet by reading with PAPI code. -TC
* 2019-10-15 Damien Genet — Merged in dgenet/papi/fix/nvml-rules (pull request #14)
* 2019-10-09 Heike Jagode — Cleaning up README file.
* 2019-10-09 Heike Jagode — README.md edited online with Bitbucket
* 2019-10-09 Heike Jagode — README edited online with Bitbucket
* 2019-10-09 Heike Jagode — README.md edited online with Bitbucket
* 2019-10-08 Steve Kaufmann — Corrected several cosmetic issues and typos, standardized naming, used PATH_MAX instead of literal, and PAPI_MAX_STR_LEN instead of PAPI_MIN_STR_LEN.
* 2019-10-08 Frank Winkler — Removed blank line.
* 2019-10-08 Frank Winkler — Replaced spaces with underscores in event name.
* 2019-10-07 Anthony Castaldo — Updated libpfm4 consistent with
* 2019-10-06 Frank Winkler — Corrected Doxygen documentation.
* 2019-10-06 Frank Winkler — Removed advanced functions from the new high-level API.
* 2019-10-03 Damien Genet — Adding Checks
* 2019-10-04 Anthony Danalis — Fixed inconsistency in component name.
* 2019-09-30 Anthony Danalis — Software Defined Events (SDE) component.
* 2019-09-30 Anthony Danalis — Counter Analysis Toolkit.
* 2019-09-30 Anthony Castaldo — Corrected typos, replacing "optimal" with "optional."
* 2019-09-18 Anthony Castaldo — We no longer check the error on setting CUPTI_EVENT_COLLECTION_MODE_CONTINUOUS, it only works on Tesla devices (and is preferred there) but fails on other models, they don't support the feature. We do not fail if they reject it.
* 2019-09-17 Kevin Huck — Adding I/O component to read from /proc/self/io.
* 2019-09-13 Steve Kaufmann — Changes to make these components (ROCM, ROCM_SMI) have naming consistency with others; fixed numerous minor formatting issues and comments. Compiled and checked on ICL Caffeine.
* 2019-09-13 Anthony Castaldo — Revert changes, used wrong author (Should be Steve Kaufmann).
* 2019-09-12 Anthony Castaldo — Changes suggested by Steve Kaufmann (Cray) to make these components have naming consistency with others; fixed numerous minor formatting issues. Reviewed, accepted, compiled, checked.
* 2019-09-09 Frank Winkler — Little format changes for markdown documentation files.
* 2019-09-09 Frank Winkler — Updated code and documentation for component libmsr to get compliance with the new component setup standard.
* 2019-09-09 Frank Winkler — Updated code and documentation for component infiniband_umad to get compliance with the new component setup standard.
* 2019-09-08 Frank Winkler — Updated code and documentation for component lmsensors to get compliance with the new component setup standard.
* 2019-09-05 Anthony Castaldo — Corrected an issue with Rules, changing the name of macro that conflicted with other potential macros.
* 2019-09-04 Anthony Castaldo — Corrected an incompatibility in multiple Rules files when multiple components are included. Rules files cannot all use the same "MACRODEF" variable for different purposes; each needs a unique ID, like CUDA_MACS, NVML_MACS, etc.
* 2019-09-04 Anthony Castaldo — Changes to make rocm_smi component compliant with new component setup standard; changes to rocm component to correct bugs in compatibility and comments.
* 2019-09-04 Anthony Castaldo — Modified documentation, Rules and code for ROCM component to comply with new setup standards. It now requires PAPI_ROCM_ROOT as an environment variable.
* 2019-09-04 Anthony Castaldo — Code and documentation to get component PCP into compliance with the new component setup standard; PAPI_PCP_ROOT is only environmental variable required.
* 2019-09-03 Anthony Castaldo — NVML component README, Rules and code updated to reflect new setup policy, relies on PAPI_CUDA_ROOT only. Adds a new override, PAPI_NVML_MAIN. Instructions improved in Rules.cuda, Rules.nvml.
* 2019-08-29 Anthony Castaldo — Corrected comments.
* 2019-08-29 Anthony Castaldo — The changes make the cuda component reliant on a single environment variable, PAPI_CUDA_ROOT, allowing overrides specified in Rules.cuda if the necessary libraries are not in their expected locations. Detailed instructions are in README, and for overrides in Rules.cuda.
* 2019-08-28 Anthony Castaldo — Bug fixes, for missing eventName in debug mode; also for failure to clear internal 'usage' flags when destroying an event set.
* 2019-08-14 Carl Love — Per Carl Love, "The POWER9 event PM_BR_TAKEN_CMPL includes conditional and unconditional branches. The equation for event PAPI_BR_NTK should not include the event PM_BR_UNCOND as PM_BR_TAKEN_CMPL already counts unconditional branches. The POWER9 event PM_LD_REF_L1 includes hits and misses to the L1. Thus we should not be adding PM_LS_MISS_L1_ALT when calculating PAPI_LD_INS on POWER9."
* 2019-08-12 Anthony Castaldo — Adding $(LDL) to LDFLAGS in Rules.x files when it was missing, on PCP and ROCM components.
* 2019-08-09 Anthony Castaldo — The PCP component changed to use the new standard for PAPI environment variables; there are now no necessary environment variables, and no need to change LD_LIBRARY_PATH. The rules file was streamlined.  The code was tested on Peak and Summit. We do allow overrides for non-standard installations of PCP, the variables PAPI_PCP_ROOT, PAPI_PCP_LIBS, PAPI_PCP_INC and PAPI_PCP_LIBNAME can be set by users to specify non-standard locations or library names. The README file in components/pcp/ contains detailed instructions on their use.
* 2019-08-09 Anthony Castaldo — Update libpfm4, to be current with the following commit: --------------------------------------------------------------
* 2019-08-08 Anthony Castaldo — Components ROCM and ROCM_SMI have been changed to adhere to our recent standardization of using environment variables. README files are updated with detailed information, and we have both simplified and extended the capabilities with new env vars. It is simplified because for a standard install of the rocm or rocm_smi software puts it in the default directories, PAPI will find the libraries and include files without any configure step. But it is more powerful because we allow overrides to the defaults, including overrides to the necessary library names. We also no longer require the LD_LIBRARY_PATH environment variable be modified, or exist at all. If it is there and we don't find a library in a path given by the user, we will still search it, and the default search directories. The Rules.rocm and Rules.rocm_smi are changed to use defaults, and their linker commands changed to allow the specification of a non-standard library name; e.g. a versioned library that does not end in ".so". These changes were tested and verified on the ICL machine Caffeine.
* 2019-08-04 Frank Winkler — Added "$(LDL)" to LDFLAGS of components lmsensors and infiniband_umad.
* 2019-08-04 Frank Winkler — Fixed bug in high-level API.
* 2019-08-01 Frank Winkler — Changed configuration mechanism for components lmsensors and infiband_umad.
* 2019-07-25 Anthony Castaldo — A continuation of a previous commit prematurely pushed. Same commentary:
* 2019-07-24 Anthony Castaldo — The CUDA and NVML components have a revamped Environment Variable processing; we have simplified this for users, made it more flexible, and standardized on environment variables beginning with "PAPI_".
* 2019-07-19 Frank Winkler — Removed function "error_at_line" (declared in error.h), since it is not portable.
* 2019-07-17 Anthony Castaldo — Changes explaining the issues with libnvidia-ml.so in detail; and the new facility for changing the default name using the environment variable PAPI_NVML_LIBNAME.
* 2019-07-17 Anthony Castaldo — linux-nvml.c is changed to allow the nvml library name to be set by an environment variable, PAPI_NVML_LIBNAME. If this is not present, the default 'libnvidia-ml.so' is used. Also, misspellings in error messages were corrected.
* 2019-07-16 Anthony Castaldo — Update libpfm4 to bring it current with the three following closely spaced commits:
* 2019-07-15 Anthony Castaldo — To avoid confusion, we no longer print an empty "PMUs supported:" line for components for which Performance Monitoring Units do not apply (or are not exposed through its device interfaces). We also corrected minor bugs in computing the display length to limit output lines to 130 characters (when listing PMUs); this was most evident on the perf_event_uncore component.
* 2019-07-12 Anthony Castaldo — linux-rocm-smi.c (for the rocm_smi component) was fixed to not expose globals other than the _rocm_smi_vector.
* 2019-06-27 Frank Winkler — Added multiplexing support for high-level API.
* 2019-06-26 Daniel Barry — Changed the dummy function call in papi_vector.c and created a function to wrap the call to omp_get_thread_num() in ctests/zero_omp.c. These allow the function castings in the respective files to operate properly without warnings from GCC 8.3.0. These changes were tested on the Intel Haswell architecture.
* 2019-06-25 Anthony Castaldo — linux-nvml.c is modified to accept an alternate name for the nvml library, which will default to the standard 'libnvidia-ml.so'. This is necessary on a system (Summit in particular) that doesn't have the standard link file to the current versioned lib. It will also provide flexibility for testing previous versions or new versions of the library. The library file name can be specified in Rules.nvml, as a compiler-line Define of NVML_LIBNAME.
* 2019-06-18 Vince Weaver — rapl: quiet a strncpy() warning in the rapl_basic test
* 2019-06-18 Vince Weaver — papi: fix some strncpy() related warnings reported by gcc 8.3
* 2019-06-10 Daniel Barry — Changed the sprintf() call to snprintf() and added an if-statement to check whether the number of characters intended to be written to the destination buffer exceed the size of the buffer. This prevents GCC 8.3.0 from warning that the destination buffer may not be large enough to store the contents of the source buffers. These changes were tested on the Intel Haswell architecture.
* 2019-06-05 Daniel Barry — Added a second buffer in the perf_event_uncore test. This prevents GCC 8 from complaining about the source and destination buffers overlapping. Per the sprintf man-page (release 3.53 of the Linux man-pages project), "the standards explicitly note that the results are undefined if source and destination buffers overlap when calling sprintf()."
* 2019-06-05 Anthony Castaldo — Added a direct file system search for AMD GPU peripherals; vendor ID 0x1002. We search up to 64 /sys/class/drm/card?/device/vendor files; (card0, card1, ... card 63). Also corrected a typo in an event name. Tested and worked on ICL Caffeine system; correctly excluded card0 (display card) and found two AMD GPUs on card1, card2.
* 2019-05-25 Yunqiang Su — [mips] replace beqzl with beqzc for r6
* 2019-05-20 Daniel Barry — I have added PAPI POWER9 event definitions for PAPI_L2_DCR, PAPI_L2_DCW, PAPI_BR_CN, PAPI_BR_NTK, PAPI_BR_UCN, and PAPI_BR_TKN. These events have been tested. Their patterns of behavior were measured during the execution of performance benchmarks on Summit's POWER9 processors. The patterns of behavior for the corresponding events on Intel Haswell processors were measured during the execution of the same performance benchmarks. The respective events from each architecture behave similarly.
* 2019-05-17 Anthony Castaldo — Added missing "rsmi_init(0)" call to component_init() function.
* 2019-05-17 Anthony Castaldo — Modifications to support indexed variables; requires different names be used for PAPI users and the request to the RocProfiler (it interprets the index within the name). Updated notes in README, and additional potential -I include paths in Rules.rocm.
* 2019-05-14 Anthony Castaldo — Update libpfm4 with:
* 2019-05-14 Anthony Castaldo — Improved error reporting when libraries are not found, or the cuda initialization function fails. No changes to function.
* 2019-05-07 Heike Jagode — More clean up of carriage return character (^M) throughout the code base.
* 2019-05-07 Anthony Castaldo — I fixed linux-rocm-smi.c to include an event per device called rocm_smi:::device=?:busy_percent; I overlooked this event in the first draft of the component.
* 2019-05-07 Heike Jagode — Clean up of carriage return character (^M) from previous patch (commit 5434010).
* 2019-05-06 Andreas Beckmann — [PATCH] set SONAME to libpapi.so.$(PAPIVER).$(PAPIREV)
* 2019-05-03 Daniel Barry — Prevented another warning about buffer size potentially being to small.
* 2019-04-25 Frank Winkler — Fixed "format-overflow" warning detected by gcc/8.1.0.
* 2019-04-24 Anthony Castaldo — Major addition: a component to access the rocm_smi library; this is the System Management Interface for AMD GPU devices. It allows monitoring of hardware elements; like power consumption, memory usage, PCIe throughput, fan speed, etc. It allows control for some hardware functions as well, via PAPI_write(), although these are untested (write requires root privileges to test). Included here are the component code, a tester for all readable events, and an incomplete tester for writing control values.
* 2019-04-24 Frank Winkler — Fixed warnings detected by gcc/8.3.0 when using "-Wrestrict" or "-Wall".
* 2019-04-24 Frank Winkler — Replaced "get_current_dir_name()" with "getcwd(NULL,0)".
* 2019-04-24 Frank Winkler — Replaced bash statements with shell statements.
* 2019-04-22 Frank Winkler — Corrected data type declaration according to the return value of C library function fgetc.
* 2019-04-18 Daniel Barry — Prevented warnings about buffer sizes of length PAPI_MAX_STR_LEN potentially being too small.
* 2019-04-18 Frank Winkler — Replaced old high-level API with a new high-level API.
* 2019-04-02 Anthony Castaldo — NOTE: This component is still not functional! Added missing code to prevent hsa_shut_down() call from segfaulting. Changed skip table for testing code rocm_all.cpp.
* 2019-04-01 Al Grant — The logic in linux-memory.c generic_get_memory_info() isn't correct.
* 2019-03-28 Anthony Castaldo — linux-rocm.c updated with PAPI standard component function names, beginning '_rocm', and events named '..:device=n:...' instead of 'device:n'. New files and utilities are added in the test/ directory. The ROCM_Makefile is used to compile cpp code using the AMD HIPCC compiler; e.g. 'make -f ROCM_Makefile rocm_all.out', in order to compile code that uses the AMD GPUs.
* 2019-03-18 Stephane Eranian — Mar 14 2019 update of libpfm4. remove MERGE event from AMD Fam17h table
* 2019-03-18 Anthony Castaldo — This is the ROCM component (linux_rocm.c) with the minimal changes needed to compile with the PAPI standard GCC flags and settings. This version is functional; it shows up on papi_components_avail, and papi_native_avail shows rocm::: events. However, the compile still produces warnings for unused variables (they are used in debug mode but the code using them is suppressed in production mode). These are corrected in the next commit; and a '/tests' directory will be added.
* 2019-03-18 Evgeny Shcherbakov — These are the original files produced by Evgeny Shcherbakov for the ROCM PAPI component; this component allows PAPI to access to AMD GPU events. Note that linux-rocm.c will not compile using the PAPI default settings for GCC; it has 3 lines of code that require a C99 flag (e.g. -std=gnu99). We do not wish to mix standards, so the next commit will revise these lines to standard C that will compile clean with our standard settings.
* 2019-03-07 Heike Jagode — Updated version to 5.7.1 after the release.
* 2019-03-04 Heike Jagode — Minor updates to release procedure text.
* 2019-03-04 Heike Jagode — Updated release notes for 5.7.0 release.
* 2019-02-22 Anthony Castaldo — Fixing updates to manual; incorrectly done for release 5.7.0.0.
* 2019-02-21 Anthony Castaldo — Updated release procedure with additional instructions on final steps.
* 2019-02-18 Anthony Castaldo — Changed version to 5.7.1 after release.
* 2019-02-18 Anthony Castaldo — Corrected directory entry typo.
* 2019-02-18 Anthony Castaldo — New ChangeLogP570.txt for new release, updated RELEASENOTES.txt
* 2019-02-17 Vince Weaver — ctests: attach_cpu_*validate: fix buffer overrun
* 2019-02-15 Anthony Castaldo — Added a 'priming' call of the naive matrix multiply, before counting the cycles on the second call. This is to overcome any first-time system overhead in the procedure, like loading the program, so the cycles will better match the 3rd and 4th calls. This corrects an error (and failure of the test) in which the first call to the routine takes over 10% more cycles to complete than the subsequent calls.
* 2019-02-15 Anthony Castaldo — Added new message to test_fail, so users will not think a test failure means their PAPI install is unusable, or that the failure should be reported to the PAPI development team.
* 2019-02-15 Anthony Castaldo — Added new memleak_check.c in validation_tests; it is not a standalone test, but a utility to be run by valgrind when checking for memory leaks.
* 2019-02-15 Anthony Castaldo — Release guidance improved with more details on testing.
* 2019-02-11 Frank Winkler — Fixed warnings detected by clang. Replaced abs with llabs.
* 2019-02-11 Frank Winkler — Fixed unused warnings.
* 2019-02-08 Anthony Castaldo — revert change that repaired a memory leak; it caused a problem with ARM systems, per Vince Weaver.
* 2019-02-08 Vince Weaver — arm64: update the ARM family configuration to work with newer Linux kernels.
* 2019-02-08 Frank Winkler — Fixed linking error.
* 2019-02-08 Frank Winkler — Fixed "this statement may fall through" warning.
* 2019-02-08 Frank Winkler — Fixed sprintf warnings by replacing them with the safer method snprintf.
* 2019-02-08 Frank Winkler — Fixed warning: '%s' directive output may be truncated.
* 2019-02-07 Anthony Castaldo — After PAPI_shutdown free(_papi_native_events); must reset variables and counts to ensure next PAPI_library_init() from same code will realloc() and rebuild the table.
* 2019-02-07 Anthony Castaldo — improve top makefile by separating targets
* 2019-02-06 Anthony Castaldo — memleak_check is a new simple test file to help expose memory leaks in PAPI main and components.
* 2019-02-06 Anthony Castaldo — Patches provided by Jiali Li. Added cleanup code to prevent memory leaks.
* 2019-02-06 Anthony Castaldo — Patches provided by Jiali Li. Added cleanup code to prevent memory leaks.
* 2019-02-06 Anthony Castaldo — Patches provided by Jiali Li. Added cleanup code to prevent memory leaks.
* 2019-02-06 Anthony Castaldo — Added cleanup code to prevent some of the memory leaks. Dynamic-library related calls leak, but we cannot prevent all of those leaks.
* 2019-02-06 Anthony Castaldo — Patches provided by Jiali Li. Added cleanup code to prevent memory leaks.
* 2019-02-06 Anthony Castaldo — Patches provided by Jiali Li. Added cleanup code to prevent memory leaks.
* 2019-02-06 Anthony Castaldo — Added cleanup code to prevent some of the memory leaks. Dynamic-library related calls leak, but we cannot prevent all of those leaks.
* 2019-02-06 Anthony Castaldo — Added cleanup code to prevent memory leaks.
* 2019-02-06 Anthony Castaldo — Added cleanup code to prevent some of the memory leaks. Dynamic-library related calls leak, but we cannot prevent all of those leaks.
* 2019-02-06 Anthony Castaldo — Added cleanup code to prevent some of the memory leaks. Dynamic-library related calls leak, but we cannot prevent all of those leaks.
* 2019-02-06 Heike Jagode — Added more details to the license statement for cuda tests.
* 2019-02-05 Anthony Castaldo — Expanded description of NVML component and usage.
* 2019-02-05 Anthony Castaldo — Expanded notes to guide releases.
* 2019-02-01 Anthony Castaldo — Corrected name of component to distinguish this one from the 'infiniband' component.
* 2019-02-01 Anthony Castaldo — Had a problem with undefined variables; added notes to README.
* 2019-02-01 Frank Winkler — Suppress "unused" warnings.
* 2019-02-01 Frank Winkler — Get rid of "use of uninitialized variable" warnings.
* 2019-02-01 Frank Winkler — Added component instructions.
* 2019-02-01 Frank Winkler — Commented out target "native_clean" since it is used twice.
* 2019-02-01 Frank Winkler — Added build instructions for component lmsensors.
* 2019-02-01 Frank Winkler — Suppress "unused variables" warnings.
* 2019-01-31 Anthony Castaldo — New Doc Files in preparatoin for release 5.7.0.0.
* 2019-01-30 Anthony Castaldo — For new version 5.7.0.0
* 2019-01-30 Anthony Castaldo — Changing version number to 5.7.0.0.
* 2019-01-30 Anthony Castaldo — Corrected a path name.
* 2019-01-30 William Cohen — Elimininating some of the SHELLCHECK_WARNINGS. Removing unused variables. Correcting printf arguments.
* 2019-01-29 Konstantin Stefanov — Change method for detecting available NVML component events
* 2019-01-28 Anthony Castaldo — Added (void)s to eliminate warnings about unused variables.
* 2019-01-28 Anthony Castaldo — Corrected field-name typo in a SUBDBG message that was not previously being compiled.
* 2019-01-28 Anthony Castaldo — Changes about accessing to cupti libs and includes.
* 2019-01-28 Anthony Castaldo — Corrected compile warnings for deprecated routines or compiler complaints.
* 2019-01-23 Vince Weaver — papi_events: the skylake events are actually split in two, make sure cascadelake gets both cases too
* 2019-01-23 Anthony Castaldo — structure member name was misspelt; 'cmpinfo->disabled_resaon' instead of 'cmpinfo->disabled_reason'.
* 2019-01-23 Anthony Castaldo — Code was missing the 'string.h' include necessary for use of 'strstr() function'.
* 2019-01-23 Anthony Castaldo — Header file changed; fixed prototypes for umad_get_ca() to use 'const char*' instead of 'char*'.
* 2019-01-22 Vince Weaver — papi_events: add cascade lake X support
* 2019-01-22 Anthony Castaldo — linux-cuda.c and cudaTest_cupti_only.cu have cosmetic changes. the pfmlib changes were committed by Stephane to simplify cpuid; The push/pop were causing problems with some compiler optimizations.
* 2019-01-22 Gerald Ragghianti — Typo in nvml component code caused test failure.
* 2019-01-16 Anthony Castaldo — Three patches to libpfm4. (1) Add Intel CascadeLake X core PMU support. (2) Add get_num_events() support for Intel X86 (3) Check PMU models when validating event codes.
* 2019-01-16 Anthony Castaldo — Example file to run simpleMultiGPU.
* 2019-01-16 Anthony Castaldo — Example file for running cudaTest_cupti_only
* 2019-01-16 Anthony Castaldo — Example script to run nvlink_bandwidth on PEAK.
* 2019-01-16 Anthony Castaldo — Example script to run nvlink_all on PEAK.
* 2019-01-16 Anthony Castaldo — This is a PAPI version of an NVIDIA cupti-only sample program; it is a useful starting point to test a variety of metrics or events, which are specified in a simple internal table.
* 2019-01-16 Anthony Castaldo — This program (likeComp = likeComponent) tested if the events in a metric could be harvested and put into an event group, read and re-ordered to provide data to cuptiMetricGetValue. They can; we did this before rewriting the component to do all Metrics in this way.
* 2019-01-16 Anthony Castaldo — This is a tester for just 4 NVLINK bandwidth metrics. It moves data from CPU (host) to GPU, or GPU to GPU. Reporting of intermediate steps has been increased, and we retrieve the number of Async engines dynamically to optimize the number of streams used in the copies. It was previously hard-coded.
* 2019-01-16 Anthony Castaldo — This utility will iterate through all the available NVLINK metrics in the PAPI system, and run a test program for each of them, and report the results to stdout. The test program is memory movement, a command line argument can test CPU(host) to GPU memory movement, or GPU to GPU movement amongst available GPU devices.
* 2019-01-16 Anthony Castaldo — This program will test a single performance metric or event that is provided on the command line, on one or more GPUs. Only cupti is used. The exercise will include both extensive memory moves NOT executed by kernel, and a kernel. Options allow the user to skip the kernel execution if desired, and to optionally use cuInit() and reset the devices before beginning the test. Reports of the steps in the process are output to stdout. The purpose of this program is to show what a cupti-only result looks like, in order to see if issues with an event are in the PAPI implementation only, or also exist in a cupti-only implementation.
* 2019-01-16 Anthony Castaldo — Several targets were added for new test and utility programs.
* 2019-01-16 Anthony Castaldo — Several changes were made to more efficiently (and correctly) read and compute metrics, including the newly added nvlink metrics. The previous method was not reading groups properly; and though this did not cause an error, it could result in zeros being read instead of actual values. The change is to break down all metrics and events for a device into global event list (without duplicates) and build a single event group set for everything the user has added. We repeat this each time the user adds an event; on the assumption that this overhead is less likely to occur during a performance critical time than when the user reads the event set. After reading all the resultant groups we then re-order the events and values to compute each metric, then store those values (and any other event values) back into the user-provided order.
* 2019-01-10 Vince Weaver — ctests: add an attach_cpu_sys test
* 2019-01-10 Vince Weaver — perf_event: fix granularity setting for attached processes
* 2019-01-10 Vince Weaver — perf_event: properly fall back to read() if rdpmc read attempt fails
* 2019-01-10 Vince Weaver — perf_event: internally indicate we need fallback when rdpmc not available
* 2018-12-07 Vince Weaver — ctests: attach_cpu_validate: fail test if all values are close to the same
* 2018-12-07 Vince Weaver — ctests: add attach_cpu_validate test
* 2018-12-03 Vince Weaver — ctests/branches: remove code to set "sleep time" which is no longer used
* 2018-12-03 Vince Weaver — ctests/branches: make the failure message more verbose
* 2018-12-03 Vince Weaver — ctests: branches, update code comments to explain what test is doing
* 2018-11-20 Anthony Castaldo — Several files modified to properly utilize the NVLINK metrics added to the linux-cuda.c component. Commenting improved to aid my own understanding of the existing code.  Tony C.
* 2018-11-20 Terry Cojean — Improved error handling. Fixed typos. Added details to component README files.
* 2018-11-05 Anara Kozhokanova — Revert "Temporary Fix: The powercap component does not properly"
* 2018-11-05 Anara Kozhokanova — Fix the bug in powercap component introduced in 2231b36. The reported values by powercap component were not correct (read values were not subtracted from start values and without wraparound).
* 2018-11-04 Frank Winkler — Fixed a bug that occurred when compiling with debug flag. - papi_pe_buffer was undeclared
* 2018-10-26 Anthony Castaldo — repairs, new features, run files, a new utility in nvlink_all.
* 2018-10-10 Anthony Castaldo — Added several files, and rewrote the tests. I created a new test, nvlink_all.cu, with a new approach to test all nvlink events present in the component standalone, and I rewrote the original nvlink_bandwidth.cu to make it work properly with PAPI. I also added some testing scripts needed to function on the PEAK supercomputer; where this code was tested.
* 2018-10-03 Anara Kozhokanova — Add a note to the output of "papi_avail -e <preset_event>" if preset event is not available at the host architecture.
* 2018-09-28 Anthony Castaldo — New and debugged files for NVML and CUDA testing.
* 2018-09-28 Vince Weaver — perf_event: remove debug printf from libpfm4 error handling code
* 2018-09-28 Vince Weaver — papi_avail: fix the -e option to not print spurious message
* 2018-09-27 Vince Weaver — perf_event: avoid floating point exception if running is 0
* 2018-09-25 Heike Jagode — Temporary Fix: The powercap component does not properly report energy values. At some point in Nov 2017, the read() function was rewritten, which resulted in numerous errors, such as: +++ the energy start values are not subtracted from the read values. +++ wraparound is no longer working properly. etc.
* 2018-09-21 Anthony Castaldo — Corrected a bug in the CUPTI_ONLY version of simpleMultiGPU.cu. This manifested specifically if the node has multiple GPUs and they are of different models or types; in which case they can have differently numbered PAPI events. We converted a scalar storing the eventID to a vector with one eventID per GPU.
* 2018-09-19 Anthony Castaldo — new test files, more cleanup on failure reporting.
* 2018-09-19 Anthony Castaldo — Additions to Makefiles, and several changes to power limiting testing to correct errors when multiple GPUs are present, remove extraneous code, and provide greater clarity in output and error messages.
* 2018-09-14 Heike Jagode — Minor fix: return correct error message if libcupti.so not found.
* 2018-09-13 Heike Jagode — minor fix
* 2018-09-13 Heike Jagode — Bug fix: Instead of normalizing all the event values to represent the total number of domain instances on the device, only the last event value was normalized.
* 2018-08-28 Anara Kozhokanova — Update libpfm4
* 2018-08-27 Vince Weaver — rapl: add support for AMD Fam17h (Zen) CPUs
* 2018-08-01 Anthony Castaldo — benchmarking files and README.
* 2018-07-23 Tony Castaldo — 8 patches to make system from Andreas Beckmann
* 2018-06-27 Anthony Castaldo — Removed a duplicated IF statement. No difference in execution.
* 2018-06-25 Anthony Castaldo — fixed pcp_init_component to show any errors in reason for a disabled PCP component.
* 2018-06-22 Anthony Castaldo — fixed a debug print, added 'timescope' to testPCP output, completed README.
* 2018-06-22 Anthony Castaldo — fixed up README file.
* 2018-06-21 Anthony Castaldo — removed debug code, added non-zeroing on instantaneous variables.
* 2018-06-19 Heike Jagode — Add cuda/lib64/stubs to linker for cuda tests to link with libcuda.so.
* 2018-06-19 Anthony Castaldo — Code changes necessary to work on Power9.
* 2018-06-18 Anthony Castaldo — Corrections to allow compile and execution on Power9.
* 2018-06-15 Anthony Castaldo — Initial coding of pcp component and tester completed.
* 2018-06-14 Anara Kozhokanova — Update libpfm4
* 2018-06-13 Anara Kozhokanova — Update libpfm4
* 2018-06-12 Vince Weaver — ctests: add new attach_validate test
* 2018-06-11 Anara Kozhokanova — Update libpfm4
* 2018-06-08 Steve Walk — enable Cavium ThunderX2 support
* 2018-06-07 Anara Kozhokanova — Update README in CUDA component: added '-i' flag to grep. Add a note about verifying whether the component is active or not before using it.
* 2018-06-07 Anara Kozhokanova — Update libpfm4
* 2018-06-05 Anara Kozhokanova — Update libpfm4
* 2018-06-01 Heike Jagode — Fixed 'make dist' step.
* 2018-05-31 Anara Kozhokanova — Update libpfm4
* 2018-05-25 Vince Weaver — ftests: add an openmp test
* 2018-04-30 Vince Weaver — ctests: add destroy test
* 2018-04-26 Heike Jagode — Update libpfm4
* 2018-04-20 Heike Jagode — Update libpfm4
* 2018-04-02 Heike Jagode — PAPI preset event support for Intel Knights Mill.
* 2018-04-02 Heike Jagode — Update libpfm4
* 2018-02-28 John Henry — Fixed typo --with_bitmode=32 changed to --with-bitmode=32
* 2018-02-23 Vince Weaver — ctests: change a few more test results from FAIL to SKIP when paranoid=3
* 2018-02-23 Vince Weaver — ctests: attach tests, skip instead of fail if not enough permissions
* 2018-02-23 Vince Weaver — papi_internal: whitespace cleanup (no code changes)
* 2018-02-23 Vince Weaver — utils: papi_avail/native_avail suggest papi_component_avail if no events detected
* 2018-02-23 Vince Weaver — papi_internal: comment the error generation code
* 2018-02-23 Vince Weaver — add new PAPI_ECMP_DISABLED error
* 2018-02-23 Vince Weaver — ctests: zero: print full error message if cannot add
* 2018-02-21 Vince Weaver — utils: papi_component_avail: fix the NAME field in the auto-generated manpage
* 2018-02-16 Heike Jagode — Fixed compilation error that occurs with deprecated option '-openmp' when using a more current icc compiler.
* 2018-02-08 John Henry — Update libpfm4 Current with commit 8f2653b8e2e18bad44ba1acc7f92c825f226ef71 Author: Hendrik Brueckner <brueckner@linux.vnet.ibm.com> Date:   Fri Oct 13 16:57:32 2017 +0200
* 2018-01-26 John Henry — Update libpfm4 Current with commit 18e3c1f0254ab9323ac848643b8e042e65cf5259 Author: Stephane Eranian <eranian@gmail.com> Date:   Thu Jan 25 19:23:45 2018 -0800
* 2018-01-24 Vince Weaver — build: fix various LDFLAGS/CFLAGS issues
* 2018-01-22 Vince Weaver — utils: papi_cost: uset getopt() to parse command line rather than open-coding one
* 2018-01-22 Vince Weaver — utils: papi_cost: various minor cleanups to the code
* 2018-01-22 Vince Weaver — utils: papi_cost: add -p option for printing boxplot percentages
* 2018-01-05 John Henry — Fix typo in release_procedure.txt. Missing do
* 2017-12-20 John Henry — Updated version to 5.6.1 after the release
* 2017-12-19 John Henry — Commit changes to create 5.6.0
* 2017-12-18 John Henry — Updated gitlog2changelog.py for new git
* 2017-12-06 John Henry (jhenry@icl.utk.edu) — Update libpfm4 Current with commit 206dea666e7c259c7ca53b16f934660344293475 Author: William Cohen <wcohen@redhat.com> Date:   Tue Dec 5 20:10:50 2017 -0800
* 2017-11-16 Will Schmidt — revised papi_derived patch.
* 2017-12-05 Heike Jagode (jagode@icl.utk.edu) — Updated notes for release procedure.
* 2017-12-05 Vince Weaver — extras.c: add string.h include to make the ffsll warning go away
* 2017-12-04 Heike Jagode (jagode@icl.utk.edu) — Fixed configure bug:
* 2017-12-04 Vince Weaver — ctests: locks_pthreads: adjust run count again
* 2017-12-04 Vince Weaver — ctests: locks_pthreads, minor cleanups
* 2017-11-20 William Cohen — Keep locks_pthreads test's amount of work reasonable on many core machines
* 2017-12-04 Vince Weaver — Revert change that added ffsll to papi.h
* 2017-12-04 Vince Weaver — revert part of patch that added extra attributes to ffsll
* 2017-12-03 Heike Jagode (jagode@icl.utk.edu) — Updated libpfm4
* 2017-11-28 Heike Jagode (jagode@icl.utk.edu) — Fixed utility option inconsistencies between papi_avail and papi_native_avail. There are more inconsistencies with other PAPI utilities, which will be addressed eventually.
* 2017-11-28 Heike Jagode — README.md edited online with Bitbucket
* 2017-11-28 Heike Jagode — README.md edited online with Bitbucket
* 2017-11-28 Heike Jagode — README.md edited online with Bitbucket
* 2017-11-28 Heike Jagode — README.md edited online with Bitbucket
* 2017-11-27 Heike Jagode — More clean-ups and checking of return values.
* 2017-11-27 John Henry (jhenry@icl.utk.edu) — Update libpfm4” > /tmp/commit-libpfm4-header.txt echo “Current with commit f5331b7cbc96d9f9441df6a54a6f3b6e0fab3fb9 Author: Thomas Richter <tmricht@linux.vnet.ibm.com> Date:   Sat Nov 18 00:37:10 2017 -0800
* 2017-11-19 Asim YarKhan — CUDA component: Bug fix for releasing and resetting event list
* 2017-11-17 Asim YarKhan — Powercap component: Updated tests to handle no-event-counters (num_cntrs==0) and skip some compiler warnings (argv, argc unused)
* 2017-11-16 William Cohen — Make more of lmsensors component internal state hidden
* 2017-11-16 William Cohen — Make internal cached_counts variable static
* 2017-11-15 William Cohen — Avoid statically limiting the number of lmsensor events allowed
* 2017-11-15 William Cohen — Use correct argument order for calloc function calls
* 2017-11-15 Philip Vaccaro — Updates and changes to the powercap component to address a few areas.. Various things were changed but mainly things were simplified and made more streamlined.  Main focus was on simpifying managing the sytem files.
* 2017-11-14 Asim YarKhan — Update libpfm4
* 2017-11-13 Vince Weaver — pe_libpfm4_events: properly notice if trying to add invalid umask
* 2017-11-13 Vince Weaver — perf_event/tsts: add broken event name test
* 2017-11-13 Philip Mucci — Removed extraneous colon in VM vendor output
* 2017-11-10 Vince Weaver — validation_tests: fix compiler warnings on arm32
* 2017-11-09 Vince Weaver — validation_tests: papi_l2_dca fix crash on ARM32
* 2017-11-09 Vince Weaver — linux-common: remove warning on not finding mhz in cpuinfo
* 2017-11-09 Vince Weaver — perf_event: disable the old pre-Linux-2.6.34 workarounds by default
* 2017-11-09 Vince Weaver — perf_event: decrement the available counter count if NMI_WATCHDOG is stealing one
* 2017-11-09 Vince Weaver — perf_event: move the paranoid handling code to its own function
* 2017-11-09 Vince Weaver — perf_event: centralize fast_counter_read flag
* 2017-11-09 William Cohen — Make the fallback generic_get_memory_info function more robust
* 2017-11-09 Asim YarKhan — Enable icc and nvcc to work together in cuda and nvml components.
* 2017-11-09 Asim YarKhan — Minor correction to mpifirst.c test
* 2017-11-09 Vince Weaver — utils: print fast_counter_read (rdpmc) status in the utils header
* 2017-11-08 William Cohen — Ensure access to array within bounds
* 2017-11-08 William Cohen — Eliminate coverity overflow warning about expression
* 2017-11-08 William Cohen — Remove dead code from perf_event_uncore_lib.c
* 2017-11-09 Vince Weaver — perf_event: don't initialize globals statically
* 2017-11-08 phil@minimalmetrics.com — linux-common: clean up the /proc/cpuinfo parsing code
* 2017-11-08 phil@minimalmetrics.com — perf_event: clean up _papi_libpfm4_shutdown()
* 2017-11-08 phil@minimalmetrics.com — utils: clean up the cpuinfo header
* 2017-11-08 phil@minimalmetrics.com — papi_internal: add PAPI_WARN() function
* 2017-11-08 phil@minimalmetrics.com — perf_event: clean up pe_libpfm4_events
* 2017-11-08 Vince Weaver — utils/papi_avail: update the manpage info
* 2017-11-08 Vince Weaver — perf_event tests: perf_event_system_wide: don't fail if permissions restrict system-wide events
* 2017-11-08 Vince Weaver — ctests/locks_pthreads: avoid printing values when in quiet mode
* 2017-08-31 phil@minimalmetrics.com — Better symlink creation for shared library in make phase
* 2017-08-28 phil@minimalmetrics.com — Full cleanup, including removal of .gitignore files that prevented us from realizing we were really cleaning/clobbering properly
* 2017-08-28 phil@minimalmetrics.com — .gitignore Makefile.target
* 2017-08-28 phil@minimalmetrics.com — Remove PAPI_VERB_ECONT setting by default from initialization path. This prints all kinds of needless errors on virtual platforms.
* 2017-08-28 phil@minimalmetrics.com — Remove leftover printf
* 2017-08-21 phil@minimalmetrics.com — Test now performs a fixed number of iterations, and reports lock/unlock timings per thread.
* 2017-08-21 phil@minimalmetrics.com — Added more descriptive error message to exclude_guest check
* 2017-08-21 phil@minimalmetrics.com — Removed leading newline and trailing . from error messages
* 2017-08-21 phil@minimalmetrics.com — Updated message for derived event failures
* 2017-11-07 Vince Weaver — tests: make sure DESTDIR and DATADIR are passed in when doing an install
* 2017-11-07 Vince Weaver — ctests/ftests/utils/validation_tests: get shared library linking working again
* 2017-11-07 Vince Weaver — validation_tests: add an installation target
* 2017-11-07 Vince Weaver — ctests/ftests: fix "install" target
* 2017-11-07 Asim YarKhan — Bitbucket pipeline testing: Inspired by Phil Mucci's branch; copied the functionalty tests run in that branch.
* 2017-11-07 Asim YarKhan — lmsensors component: Changed event names to use lm_sensors (only once) instead of LM_SENSORS (twice) to be consistent with other events
* 2017-11-02 William Cohen — gnu3d.dem should not be executed by the test framework
* 2017-11-02 William Cohen — Gnuplot.txt should not be executed by the test framework
* 2017-11-02 William Cohen — Fix perl scripts so they run on Linux machines
* 2017-11-07 Asim YarKhan — lmsensors component: Regenerate the configure file for the component
* 2017-11-02 William Cohen — Make the lmsensors dynamically load the needed shared library
* 2017-11-06 Asim YarKhan — CUDA component: On architectures without CUDA Metrics (e.g. Tesla C2050), skip metric registration rather than returning errors
* 2017-11-06 Vince Weaver — validation_tests: make the papi_l2 tests fail with warnings
* 2017-11-05 Vince Weaver — perf_event: enable rdpmc support by default
* 2017-11-03 Vince Weaver — ctests: sdsc: fix issue where the error message is not printed correctly
* 2017-11-01 Heike Jagode — Intermediate check-in: Fixed a whole bunch of careless file handling (missing closing of open files, missing setting of open/close flag, etc). Still more rigorous checks needed.
* 2017-11-01 Hanumantharayappa FNU (fhanuman@vols.utk.edu) — Update libpfm4\n\nCurrent with\n commit 21405fb3c247a0d16861483daf0696cf4fa0cc43 Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Oct 30 17:16:32 2017 -0700
* 2017-10-30 Vince Weaver — validation_tests: add cycles_validation test
* 2017-10-30 Vince Weaver — papi: c++11 fixes: fix various ctests that c++ complains on
* 2017-10-30 Vince Weaver — papi: c++11 conversion: PAPI_get_component_index()
* 2017-10-30 Vince Weaver — papi: c++11 conversion: convert PAPI_perror()
* 2017-10-30 Vince Weaver — papi: start converting papi.h to be C++11 clean
* 2017-10-30 Vince Weaver — validation_tests/papi_l2_dca: update some comments
* 2017-10-30 Vince Weaver — ctests/zero: make test pass on recent intel machines
* 2017-10-27 Philip Vaccaro — updated powercap README to be more concise. includes more details on interacting with energy counters and power limits.
* 2017-10-27 Asim YarKhan — CUDA/NVML components: Handled segfault which can occur when dlclosing libcudart from both components by adding an additional flag to dlopen
* 2017-10-24 Asim YarKhan — CUDA component: Clean up fulltest by moving some output from stdout to SUBDBG, removed some commented out lines
* 2017-10-24 Asim YarKhan — nvml component: To support V100 (Volta) updated to get nvmlDevice handle ordered by index rather than pci busid.
* 2017-10-23 Asim YarKhan — CUDA component: Minor fix to remove some unneeded stdout which shows up during fulltest
* 2017-10-20 Asim YarKhan — CUDA component test update: Remove some debug output.  Do not build cupti_only test binary.
* 2017-10-19 Hanumantharayappa FNU (fhanuman@vols.utk.edu) — Update libpfm4\n\nCurrent with\n commit 2e98642dd331b15382256caa380834d01b63bef8 Author: Stephane Eranian <eranian@gmail.com> Date:   Thu Oct 19 11:23:44 2017 -0700
* 2017-10-17 Vince Weaver — ctests: version, add INCREMENT field
* 2017-10-17 Vince Weaver — ctests: re-enable version test
* 2017-10-17 Vince Weaver — ctests: alphabetize SERIAL tests in Makefile.recipes
* 2017-10-13 Philip Vaccaro — added simple limit test for the powercap component.
* 2017-10-09 Asim YarKhan — Big Fix NVML component: Fix problem with names when there are multiple identical GPUs
* 2017-10-05 Hanumanth — Update libpfm4\n\nCurrent with\n commit d1e7c96df60a00a371fdaa3b635ad4a38cee4c2f Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Sep 29 00:25:09 2017 -0700
* 2017-10-05 Asim YarKhan — Update NVML component: Support for power limiting using NVML
* 2017-10-04 Asim YarKhan — Style consistency and refactoring via astyle command.  No changes to the actual code were made here.
* 2017-10-04 Vince Weaver — rapl: add support for some Intel Atom models Goldmont / Gemini_Lake / Denverton
* 2017-10-04 Vince Weaver — rapl: fix skylake SoC measurement support
* 2017-10-04 Vince Weaver — rapl: add support for skylake SoC energy measurements
* 2017-10-04 Vince Weaver — rapl: add Skylake-X / Kabylake support
* 2017-10-04 Vince Weaver — rapl: centralize the "different DRAM units" code
* 2017-10-04 Vince Weaver — rapl: merge like processors
* 2017-10-04 Vince Weaver — rapl: convert chip detection to a switch statement
* 2017-10-04 Vince Weaver — rapl: update the whitespace a bit
* 2017-09-12 Heike Jagode (jagode@icl.utk.edu) — Fixed papi_vector for infiniband_umad component.
* 2017-09-11 Hanumanth — Updating man and help pages for papi_avail and papi_native_avail
* 2017-09-07 Asim YarKhan — Update to CUDA component to support NVLink.
* 2017-08-31 Phil Mucci — Updating options for papi_avail/native_avail as well as all references to old mailing list
* 2017-08-31 Asim YarKhan — Minor updates to NVML component to enable it to compile and run without complaints
* 2017-08-30 Vince Weaver — validation: update papi_br_prc and papi_br_tkn for amd fam15h
* 2017-08-30 Vince Weaver — papi_events: add PAPI_BR_PRC event to amd fam15h
* 2017-08-30 Vince Weaver — papi_events: update PAPI_BR_PRC and PAPI_BR_TKN on sandybridge/ivybridge
* 2017-08-30 Vince Weaver — validation_tests: papi_br_tkn: update to only count conditional branches
* 2017-08-30 Vince Weaver — validation_tests: papi_br_prc: make sure it is comparing conditional branches
* 2017-08-24 Hanumanth — Update libpfm4\n\nCurrent with\n commit a290dead7c1f351f8269a265c0d4a5f38a60ba29 Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Aug 21 23:55:46 2017 -0700
* 2017-08-20 Vince Weaver — ctests: add failed_events test
* 2017-08-19 Vince Weaver — perf_event_uncore: tests: update perf_event_uncore to use :cpu=0
* 2017-08-19 Vince Weaver — perf_event_uncore: tests: update uncore events for recent processors
* 2017-08-19 Vince Weaver — ctests: zero_pthreads: remove extraneous printf when in quiet mode
* 2017-08-19 Vince Weaver — perf_event_uncore: event list, add recent processors
* 2017-08-19 Vince Weaver — perf_event_uncore: tests: print a message indicating the problem on skip
* 2017-08-19 Vince Weaver — perf_event: tests: update event_name_lib for recent Intel processors
* 2017-08-19 Vince Weaver — perf_event: tests: event_name_lib, clean up whitespace
* 2017-08-19 Vince Weaver — perf_event: tests: update perf_event_offcore_response test
* 2017-08-19 Vince Weaver — ctests: zero_shmem: document the code a little better
* 2017-08-19 Vince Weaver — ctests: zero_smp: make it actually do something on Linux
* 2017-08-19 Vince Weaver — ctests: zero_shmem: minor cleanups
* 2017-08-19 Vince Weaver — ctests: zero_omp and zero_pthread were skipping due to a typo
* 2017-08-19 Vince Weaver — papi_events: the skylake fixes broke hsw/bdw
* 2017-08-19 Vince Weaver — papi_events: on skylake the SNP_FWD umask was renamed to SNP_HIT_WITH_FWD
* 2017-08-19 Vince Weaver — perf_event: fix uninitialized descr issue reported by valgrind
* 2017-08-18 Vince Weaver — perf_event: clean up some whitespace in pe_libpfm4_events.c
* 2017-08-18 Vince Weaver — linux-memory: various errors when compiling with debug enabled
* 2017-08-17 Vince Weaver — papi_events: missed one of the skx event locations
* 2017-08-16 Vince Weaver — papi_events: enable Skylake X support
* 2017-08-16 Hanumanth — Update libpfm4\n\nCurrent with\n commit efd16920194999fdf1146e9dab3f7435608a9479 Author: Stephane Eranian <eranian@gmail.com> Date:   Sun Aug 6 00:22:52 2017 -0700
* 2017-08-07 Vince Weaver — papi_events: add initial AMD fam17h support
* 2017-08-07 Vince Weaver — papi_events: fix the amd_fam16h PMU name
* 2017-08-07 Asim YarKhan — Update libpfm4
* 2017-08-04 Vince Weaver — validation_tests: for the DCM tests up the allowed error to 5%
* 2017-08-04 Vince Weaver — linux-memory: add fallback generic Linux /sys cache size detection
* 2017-08-04 Vince Weaver — validation_tests: don't crash if cachesize reported as zero
* 2017-08-04 Vince Weaver — branches_testcode: add arm64 support
* 2017-07-27 Vince Weaver — validation_tests: trying to find out why PAPI_L2_DCA fails on Haswell
* 2017-07-27 Vince Weaver — validation_tests: papi_l2_dcw: shorten a warning message
* 2017-07-27 Vince Weaver — papi_events: note that libpfm4 Kaby Lake support is treated as part of Skylake
* 2017-07-27 Vince Weaver — validation_tests: add PAPI_L2_DCW test
* 2017-07-27 Vince Weaver — validation_tests: add PAPI_L2_DCR test
* 2017-07-27 Vince Weaver — validation_tests: PAPI_L2_DCM
* 2017-07-27 Vince Weaver — validation_tests: add PAPI_L1_DCM test
* 2017-07-27 Vince Weaver — validation_tests: first attempt at papi_l2_dcm test
* 2017-07-26 Vince Weaver — ctests: clean up the exec/child overflow tests
* 2017-07-21 Vince Weaver — validation_tests: add PAPI_L2_DCA test
* 2017-07-21 Vince Weaver — validation_tests: PAPI_L1_DCA fixes
* 2017-07-21 Vince Weaver — validation_tests: papi_br_prc, properly skip if event not found
* 2017-07-21 Vince Weaver — validation_tests: add PAPI_L1_DCA test
* 2017-07-20 Vince Weaver — validation_tests: add PAPI_BR_PRC test
* 2017-07-20 Vince Weaver — validation_tests: add PAPI_BR_TKN test
* 2017-07-20 Vince Weaver — validation_tests: add PAPI_BR_NTK test
* 2017-07-07 Vince Weaver — papi_events: move haswell, skylake, and broadwell to traditional PAPI_REF_CYC
* 2017-07-07 Vince Weaver — linux-timer: fix build warning on non-power build
* 2017-07-07 Vince Weaver — validation: make the flops tests handle that POWER has fused multiply-add
* 2017-07-07 Vince Weaver — POWER8: add a few branch preset events
* 2017-07-07 Vince Weaver — validation: add POWER branches testcode
* 2017-07-07 Vince Weaver — POWER: fix some compiler warnings
* 2016-10-18 Phil Mucci — Ensure stdint gets included for all Linuxen.
* 2016-10-18 Phil Mucci — Some Linuxen need stdint to get the uint64_t type.
* 2016-10-14 Phil Mucci — Restructured unlock code to avoid warnings. Tested against 80 threads on Power8
* 2016-10-12 Phil Mucci — PPC64/PPC fast timer fixup.
* 2017-07-07 Vince Weaver — linux-timer: allow using fast timer for get_real_cycles() on POWER
* 2016-07-12 Phil Mucci — First pass at good rdtsc for Power7/8
* 2017-07-03 Vince Weaver — validation_tests: add tests for PAPI_SP_OPS and PAPI_DP_OPS
* 2017-07-03 Vince Weaver — validation_tests: papi_ref_cyc: update test to work on older systems
* 2017-07-02 Vince Weaver — validation_tests: move cycle_ratio test to be papi_ref_cyc test
* 2017-07-02 Vince Weaver — ctests: rewrite cycle_ratio test
* 2017-07-01 Vince Weaver — ctests: migrate all other users of dummy3() workload
* 2017-07-01 Vince Weaver — ctests: move the "dummy3" workload to the common workload library
* 2017-07-01 Vince Weaver — ctests: sdsc4-mpx: fix failing on recent Intel machines
* 2017-06-30 Vince Weaver — ctests: catch lack of CPU component earlier
* 2017-06-30 Vince Weaver — tests:cuda: make the HelloWorld test more like a standard PAPI test
* 2017-06-30 Vince Weaver — validation_tests: fix linking against a CUDA enabled PAPI
* 2017-06-30 Vince Weaver — testlib: make it so it can compile with c++
* 2017-06-30 Vince Weaver — tests: cuda: fix sampling/gpu_activity to compile without warnings
* 2017-06-30 Vince Weaver — tests: make the component tests build command be the same as ctests/ftests
* 2017-06-30 Vince Weaver — ctests: calibrate: turn off printf if TEST_QUIET
* 2017-06-29 Vince Weaver — testlib: remove the hack where all printf's are #defined to something else
* 2017-06-29 Vince Weaver — tests: set the ctest debug mode to VERBOSE by default for tests
* 2017-06-29 Vince Weaver — perf_event: properly initialize the mmap_addr structure
* 2017-06-29 Vince Weaver — tests: enable color in test status messages
* 2017-06-29 Vince Weaver — validation_tests: always include -lrt on the tests
* 2017-06-29 Vince Weaver — ctests: make the fork/exec tests only print "PASSED" once
* 2017-06-29 Vince Weaver — tests: make the output from run_tests.sh more compact
* 2017-06-28 Vince Weaver — perf_event: tests, make perf_event_system_wide use INS rather than CYC
* 2017-06-28 Vince Weaver — validation_tests: add tests for PAPI_BR_CN and PAPI_BR_UCN
* 2017-06-28 Vince Weaver — validation_tests: flops: wasn't falling back properly if no FLOPS event
* 2017-06-28 Vince Weaver — tests: clean up the Makefiles
* 2017-06-28 Vince Weaver — utils: print_header: print the operating system version in the header
* 2017-06-28 Vince Weaver — perf_event_uncore: the perf_event_amd_northbridge test wasn't working
* 2017-06-28 Vince Weaver — ctests: zero: complete transition from FLOPS to INS as metric
* 2017-06-28 Vince Weaver — validation_tests: move the unused vector.c code
* 2017-06-28 Vince Weaver — validation_tests: add a generic flops test based on hl_rates
* 2017-06-28 Vince Weaver — ctests: hl_rates: clean up and fix extraneous error message
* 2017-06-28 Vince Weaver — ctests: all_events: issue warning if preset cannot be created
* 2017-06-28 Vince Weaver — validation_tests: papi_hw_int explicitly mark large constant as ULL
* 2017-06-28 Vince Weaver — validation_tests:  a few tests had the !quiet check inverted
* 2017-06-28 Vince Weaver — validation_tests: fix papi_hw_int looping forever
* 2017-06-28 Vince Weaver — validation_tests: add PAPI_SR_INS test
* 2017-06-28 Vince Weaver — validation_tests: add PAPI_LD_INS test
* 2017-06-28 Vince Weaver — validation_tests: add PAPI_HW_INT test
* 2017-06-27 Vince Weaver — run_tests_exclude: add attach_target
* 2017-06-27 Vince Weaver — ctests/prof_utils: remove prof_init() helper
* 2017-06-27 Vince Weaver — ctests: skip rather than fail if no events available
* 2017-06-26 Vince Weaver — testlib: fix add_two_events()
* 2017-06-26 Vince Weaver — ctests: compiler warning caught two lack-of-braces mistakes
* 2017-06-26 Vince Weaver — tests: more changes to skip instead of fail if no events available
* 2017-06-26 Vince Weaver — ctests: break up the for_exec_overflow test
* 2017-06-26 Vince Weaver — ctests: have attach tests cleanly skip if no events available
* 2017-06-26 Vince Weaver — testlib: update add_two_events to skip() if not events found
* 2017-06-26 Vince Weaver — testutils: remove init_multiplex() test helper
* 2017-06-26 Vince Weaver — tests: try to "skip" rather than "fail" if no events available
* 2017-06-26 Vince Weaver — ctests: derived: fix warning found on older gcc
* 2017-06-26 Vince Weaver — ctests: clean up high-level2 test
* 2017-06-26 Vince Weaver — components test: fix another build issue
* 2017-06-26 Vince Weaver — component tests: fix build issue
* 2017-06-26 Vince Weaver — components: update component test Makefiles to include Makefile_comp_test.target
* 2017-06-26 Vince Weaver — components: update Makefile_comp_test.target.in
* 2017-06-26 Vince Weaver — ctests: nmi_watchdog is a perf_event specific test, move it there
* 2017-06-26 Vince Weaver — components: update the autoconfigure to generate more useful Makefile.target.in
* 2017-06-26 Asim YarKhan — CUDA component update: Support for CUPTI metrics (early release)
* 2017-06-23 Vince Weaver — validation: papi_fp_ops, skip (not fail) if PAPI_FP_OPS unavailable
* 2017-06-23 Vince Weaver — ctests: flops, update to use some of the validate_tests infrastructure
* 2017-06-23 Vince Weaver — validation_tests: add papi_fp_ops test
* 2017-06-23 Vince Weaver — powercap: fix compiler warnings in the powercap_basic test
* 2017-06-23 Vince Weaver — ctests: update flops test
* 2017-06-23 Vince Weaver — ctests: update api test
* 2017-06-23 Vince Weaver — ctests: update all_native_events
* 2017-06-23 Vince Weaver — ctests: clean up all_events test
* 2017-06-23 Vince Weaver — testlib: remove the "free variables" option from test_pass()
* 2017-06-23 Vince Weaver — ctests: zero: start cleaning up this test
* 2017-06-23 Vince Weaver — validation_tests: clock_gettime() requires -lrt on older versions of glibc
* 2017-06-22 Will Schmidt — PAPI power9 event list presets
* 2017-06-22 Vince Weaver — ftests: fortran tests weren't getting the TOPTFLAGS var set
* 2017-06-22 Vince Weaver — testlib: fix colors not turning off in pass/fail indicator
* 2017-06-22 Vince Weaver — testlib: update the way pass/fail is printed
* 2017-06-22 Vince Weaver — run_tests.sh: run the validation tests too
* 2017-06-22 Vince Weaver — Makefile.inc: make it compile the validation_tests
* 2017-06-22 Vince Weaver — validation-tests: add papi_br_msp test
* 2017-06-22 Vince Weaver — validation_tests: add papi_br_ins test
* 2017-06-22 Vince Weaver — validation_tests: add papi_tot_cyc test
* 2017-06-22 Vince Weaver — fix "make install-all"
* 2017-06-22 Vince Weaver — validation_tests: update configure so it sets up the Makefile
* 2017-06-22 Vince Weaver — testlib: papi_print_header() lives with the utils code now
* 2017-06-22 Vince Weaver — testlib: make tests_quiet() return an integer
* 2017-06-22 Vince Weaver — validation_tests: add initial papi_tot_ins test
* 2017-06-22 Vince Weaver — ctests: more printf/TESTS_QUIET conversions
* 2017-06-22 Vince Weaver — ftests: missing define was making second.F fail
* 2017-06-22 Vince Weaver — ctests: more printf/TESTS_QUIET fixes
* 2017-06-21 Vince Weaver — ctests: explicitly block printfs with TESTS_QUIET
* 2017-06-21 Vince Weaver — testlib: minor papi_test.h cleanups
* 2017-06-21 Vince Weaver — testlib: more papi_test.h reduction
* 2017-06-21 Vince Weaver — testlib: turn off optimization on the validation loops
* 2017-06-21 Vince Weaver — testlib: start splitting the validation code off from the pass/fail code
* 2017-06-21 Vince Weaver — testlib: remove include of papi.h
* 2017-06-21 Vince Weaver — utils: remove last uses of testlib
* 2017-06-21 Vince Weaver — utils: update papi_hybrid_native_avail to not depend on testlib
* 2017-06-21 Vince Weaver — utils: clean up papi_multiplex_cost
* 2017-06-21 Vince Weaver — testlib: more header removal from papi_test.h
* 2017-06-21 Vince Weaver — testlib: remove a few more includes from papi_test.h
* 2017-06-21 Vince Weaver — testlib: split some headers out of papi_test.h
* 2017-06-21 Vince Weaver — testlib: let testlib build properly from within the testlib directory
* 2017-06-21 Vince Weaver — testlib: clockcore wasn't protecting all the output with !quiet
* 2017-06-21 Vince Weaver — ctests: make sure tests link against the right papi.h file
* 2017-06-21 Vince Weaver — ctests: allow running "make" in the ctests directory to work
* 2017-06-20 Vince Weaver — update the ptools-perfapi e-mail address
* 2017-06-20 Vince Weaver — docs: fix the manpage build after renaming the utils
* 2017-06-20 Vince Weaver — utils: papi_native_avail: remove extraneous testing code
* 2017-06-20 Vince Weaver — utils: papi_mem_info: remove extraneous test code
* 2017-06-20 Vince Weaver — utils: papi_xml_event_info: remove extraneous test code
* 2017-06-20 Vince Weaver — utils: papi_decode: remove extraneous test code
* 2017-06-20 Vince Weaver — utils: papi_error_codes: remove extraneous test code
* 2017-06-20 Vince Weaver — utils: papi_component_avail: remove extraneous test code
* 2017-06-20 Vince Weaver — utils: papi_clockres, remove extraneous test code
* 2017-06-20 Vince Weaver — utils: update papi_avail to not depend on testlibs
* 2017-06-20 Vince Weaver — utils: add target for papi_hybrid_native_avail
* 2017-06-20 Vince Weaver — utils: rename the utils so the executable matches the filename
* 2017-06-20 Vince Weaver — utils: rename version.c to papi_version.c
* 2017-06-20 Vince Weaver — utils: clean up Makefile and build process of utils
* 2017-06-20 Vince Weaver — perf: fall back to operating system default events if libpfm4 lacks support
* 2017-06-20 Vince Weaver — perf: report better errors if libpfm4 initialization fails
* 2017-06-20 Vince Weaver — perf: pe_libpfm4_events: minor whitespace fixup
* 2017-06-20 Vince Weaver — perf: pe_libpfm4_events: whitespace changes to make code easier to follow
* 2017-06-19 Vince Weaver — ctests/code2name: fix uninitialized variable warning
* 2017-06-19 Vince Weaver — ctests/calibrate: fix uninitialized variable warning
* 2017-06-19 Vince Weaver — ctests: thrspecific fix so it finishes
* 2017-06-19 Vince Weaver — ctests: fix tests using "dummy3()" as a workload
* 2016-10-12 Phil Mucci — Regenerated configure with recent autoconf
* 2016-10-12 Phil Mucci — By default, we want -O1 on tests (TOPTFLAGS). -O0 is too literal and causes a number of tests who depend on peephole optimization to run.
* 2016-10-12 Phil Mucci — Utils are installed therefore they should be built with production flags not test/debug flags
* 2016-10-12 Phil Mucci — Make clean should not clean up libpfm. Thats for make distclean. We're not developing libpfm!
* 2016-07-04 Phil Mucci — Moved functions definitions to top of file to eliminate non-ANSI-C prototypes inside main. Modified message in zero to not turbo boost will also cause errors (cycles > real-time-cycle
* 2016-07-04 Phil Mucci — Remove EXTRA_CFLAGS, now CFLAGS. Added FTOPTS so compiling Fortran tests have same flags as ctests. Fix proper testing at configure time of libpfm for proper combinations of libpfm options
* 2016-07-04 Phil Mucci — Homogenize include flags
* 2016-07-04 Phil Mucci — Homogenize include flags
* 2016-07-04 Phil Mucci — Removed unnecessary defs and options
* 2016-07-04 Phil Mucci — Removed unnecessary definitions and compiler options
* 2016-07-01 Phil Mucci — Makefile.in: - Removed DEBUGFLAGS, NOTLS, PAPI_EVENTS_TABLE from being generated. These were not properly used. - Added LIBCFLAGS generated from configure for CFLAGS that ONLY apply to the library and the library code. NOT tests nor utilities. Previously we were propagating all kinds of bogus flags to the tests and utils. - CFLAGS is now properly set for compiler flags not defines etc.
* 2016-06-27 Phil Mucci — Added explicit target for libtestlib.a. The all target should have been markted as .PHONY as to avoid constant rebuilding.
* 2017-06-16 Vince Weaver — fwrappers: papif_unregister_thread was misspelled as papif_unregster_thread
* 2017-06-16 Vince Weaver — papi_preset: fix compiler warning
* 2017-06-16 Asim YarKhan — Update libpfm4
* 2017-06-15 Vince Weaver — perf_event: merge the libpfm4 helper libraries
* 2017-06-15 Vince Weaver — perf_event_uncore: make the libpfm4 routines match even more
* 2017-06-15 Vince Weaver — perf_event: make perf_event and perf_event uncore libpfm4 more similar
* 2017-06-15 Vince Weaver — perf_event: Avoid unintended libpfm build dependency due to PFM_PMU_MAX enum
* 2017-06-15 Heike Jagode (jagode@icl.utk.edu) — Updated infiniband component so that it works for mofed driver version 4.0, where directory counters_ext in sysfs fs has changed to hw_counters.
* 2017-05-04 Vince Weaver — rapl: broadwell-ep DRAM units are special (like Haswell-EP)
* 2017-04-24 Hanumanth — Update libpfm4\n\nCurrent with\n commit 8385268c98553cb5dec9ca86bbad3e5c44a2ab16 Author: William Cohen <wcohen@redhat.com> Date:   Fri Apr 21 17:33:15 2017 -0700
* 2017-04-20 Stephen Wood — cast pointers appropriately to avoid warnings and errors
* 2017-04-19 Sangamesh Ragate — Mapped PAPI_L2_ICM preset event to PM_INST_FROM_L2MISS native event for Power8
* 2017-04-06 Asim YarKhan — Fixed: This fortran test exceeded 72 columns and made the default Intel ifort compilation unhappy
* 2017-04-06 Hanumanth — Update libpfm4\n\nCurrent with\n commit 71a960d9c17b663137a2023ce63edd2f3ca115f5 Author: Andreas Beckmann <a.beckmann@fz-juelich.de> Date:   Wed Apr 5 23:35:44 2017 -0700
* 2017-03-30 William Cohen — Eliminate warnings about implicit type conversions in Fortran tests
* 2017-04-05 Hanumanth — Update libpfm4\n\nCurrent with\n commit 5e311841e5d70efb93d11826109cb5acab6e051c Author: Stephane Eranian <eranian@gmail.com> Date:   Tue Apr 4 09:42:25 2017 -0700
* 2017-03-29 Vince Weaver — perfctr: fix perfctr component to actually work
* 2017-03-28 Vince Weaver — papi_events: add AMD fam16h jaguar events
* 2017-03-27 Vince Weaver — events: p4: change the PAPI_TOT_CYC event
* 2017-03-27 Vince Weaver — perf_event: fix warning when compiling with debug enabled
* 2017-03-22 Vince Weaver — perf_event: don't allocate a mmap page if not rdpmc or sampling
* 2017-03-22 Vince Weaver — perf_event: only allocate 1 mmap page (rather than 3) if not sampling
* 2017-03-22 Vince Weaver — perf_event: update the _pe_set_overflow() call
* 2017-03-22 Vince Weaver — perf_event: turn off fast_counter_read if mmaps fail
* 2017-03-21 Asim YarKhan — configure script updated using autoconf-2.59
* 2017-03-20 Vince Weaver — configure: enable rdpmc with --enable-perfevent-rdpmc=yes
* 2017-03-16 Vince Weaver — perf_event: try to work around exclude_guest issue
* 2017-03-14 Vince Weaver — tests: multiattach: whitespace/comments/clarifications
* 2017-03-09 Vince Weaver — perf_event: can't mmap() an inherited event
* 2017-03-09 Vince Weaver — perf_event: add rdpmc support (but disabled)
* 2017-03-09 Vince Weaver — perf_event: make all events come with a mmap buffer
* 2017-03-09 Vince Weaver — perf_event: add check for paranoid==3
* 2017-03-09 Vince Weaver — perf_event: split close_pe_events() into two functions
* 2017-03-09 Vince Weaver — perf_event: more whitespace / rearrangement
* 2017-03-08 Vince Weaver — perf_event: more whitespace/comment cleanups
* 2017-03-07 Vince Weaver — perf_event: rdpmc: need to sign extend offset too
* 2017-03-07 Vince Weaver — perf_event: split up _pe_read()
* 2017-03-07 Vince Weaver — perf_event: clean up whitespace in _pe_read
* 2017-03-08 Vince Weaver — ctests: first: white space cleanups
* 2017-03-07 Vince Weaver — perf_event: recent changes broke build on non-x86
* 2017-03-07 Vince Weaver — perf_event: update rdpmc detection
* 2017-03-07 Vince Weaver — utils: component_avail: clean up -d (detailed) results
* 2017-03-07 Vince Weaver — utils: component_avail: whitespace/grammar fixes
* 2017-03-07 Vince Weaver — perf_event: add mmap/rdpmc routine
* 2017-03-06 Vince Weaver — perf_event: add rdtsc() and rdpmc() inline-assembly
* 2017-03-06 Vince Weaver — perf_event: move perf_event_open() code to a helper file
* 2017-03-03 Vince Weaver — perf_event: move bug_sync_read() check out of line
* 2017-03-03 Vince Weaver — perf_event: remove _pe_libpfm4_get_cidx() helper function
* 2017-03-03 Vince Weaver — perf_event: wakeup_mode field is no longer used
* 2017-03-03 Vince Weaver — perf_event: remove WAKEUP_MODE_ defines
* 2017-03-03 Vince Weaver — perf_event.c: split setup_mmap() to its own function
* 2017-03-03 Vince Weaver — perf_event: rename tune_up_fd to configure_fd_for_sampling
* 2017-03-03 Vince Weaver — perf_event: remove extraneous whitespace
* 2017-02-24 Vince Weaver — papi_cost: wasn't properly resetting the event search after POSTFIX
* 2017-02-22 Hanumanth — Update libpfm4\n\nCurrent with\n commit 1bd352eef242f53e130c3b025bbf7881a5fb5d1e Author: Stephane Eranian <eranian@gmail.com> Date:   Wed Feb 22 01:16:42 2017 -0800
* 2017-02-17 Vince Weaver — papi_cost: clear eventset before derived add test
* 2017-01-23 Asim YarKhan — Fixing the date in the RELEASENOTES file.
* 2016-11-18 Asim YarKhan — Bump papi version to 5.5.2 after release.
* 2016-11-18 Asim YarKhan — Changelog for 5.5.1 release
* 2016-11-18 Asim YarKhan — Update RELEASENOTES for 5.5.1
* 2016-11-18 Asim YarKhan — Small update to FAQ to fix mailing list references
* 2016-11-18 Asim YarKhan — Add the bitbucket-pipelines.yml to the list of files to be deleted
* 2016-11-18 Asim YarKhan — Update the URLS for PAPI in papi.spec
* 2016-11-18 Asim YarKhan — Make README the same as README.md
* 2016-11-17 Asim YarKhan — Generate man pages for 5.5.1 release
* 2016-11-17 Asim YarKhan — Handing some of the problems exposed by Coverity
* 2016-11-15 Asim YarKhan — Fulltest disabled in bitbucket-pipelines.yml (edited online with Bitbucket)
* 2016-11-15 Asim YarKhan — Fulltest enabled in bitbucket-pipelines.yml (edited online with Bitbucket)
* 2016-11-15 David Abdurachmanov — Enable RAPL for Broadwell-EP
* 2016-11-11 Asim YarKhan — README.md edited online with Bitbucket
* 2016-11-11 Asim YarKhan — bitbucket-pipelines.yml created online with Bitbucket
* 2016-11-11 Asim YarKhan — Update libpfm4
* 2016-11-04 Asim YarKhan — Minor change: Removed unneeded characters in src/Makefile.inc.  (Thanks to Steve Kaufmann)
* 2016-10-24 Asim YarKhan — Increase PERF_EVENT_MAX_MPX_COUNTERS to 384 to support KNL uncore events
* 2016-10-24 Asim YarKhan — Update libpfm4
* 2016-10-19 Asim YarKhan — README.md edited online with Bitbucket
* 2016-10-19 Asim YarKhan — README.md edited online with Bitbucket
* 2016-10-19 Asim YarKhan — Make it cleaner
* 2016-10-19 Asim YarKhan — Adding markdown README.md to make Bitbucket interface nicer
* 2016-09-18 Phil Vaccaro — changed the tool in /powercap/utils to behave as the similiar tool in /rapl/utils does. removed the old code residing in /powercap/utils.
* 2016-09-16 Vince Weaver — threads: silence compiler warning
* 2016-09-16 Vince Weaver — papi_preset: quiet a compiler warning
* 2016-09-16 Vince Weaver — tests/zero_omp: fix warning in zero_omp
* 2016-09-16 Vince Weaver — componensts/rapl: fix compiler warning in rapl_basic test
* 2016-09-16 Asim YarKhan — Tweak release procedure instructions
* 2016-09-15 Asim YarKhan — Updated PAPI version to 5.5.1 after the release
* 2016-09-14 Asim YarKhan — Generated man files for release
* 2016-09-14 Asim YarKhan — Generated man files for release
* 2016-09-14 Asim YarKhan — Release notes and ChangeLogP550 for 5.5.0 release
* 2016-09-14 Asim YarKhan — Update to return PAPI_ENOSUPP when the user cannot count events in kernel space
* 2016-09-13 Asim YarKhan — Return EPERM (rather than EINVAL) when the user cannot count events in kernel space.
* 2016-09-08 Asim YarKhan — Generated man files for release
* 2016-09-06 Asim YarKhan — Update libpfm4
* 2016-08-23 Heike Jagode — Update libpfm4
* 2016-08-18 Heike Jagode — ctests all_native: Make sure we count all native events for KNL.
* 2016-08-18 Heike Jagode — perf_event_uncore tests: KNL has uncore support.
* 2016-08-18 Heike Jagode — perf_event tests: add KNL offcore event.
* 2016-08-18 Heike Jagode — Added preset definitions for KNL.
* 2016-08-12 Vince Weaver — linux-rapl: update KNL support
* 2016-08-04 Vince Weaver — testlib: give better error message if component failed to initialize
* 2016-07-25 Heike Jagode — Update libpfm4
* 2016-07-25 pvaccaro — add William Cohen's rewrite of the _papi_hwi_postfix_calc function which corrects the parsing and makes the parser more robust by catching any errors in the parsing early with asserts in the code rather than silently corrupting memory.
* 2016-07-22 Heike Jagode — Update libpfm4
* 2016-07-22 Phil Mucci — This was another bug of smashing the stack. This code declared the stack as: 	static char stack[PAPI_HUGE_STR_LEN];
* 2016-07-21 Heike Jagode — Update libpfm4
* 2016-07-11 Heike Jagode — Update libpfm4
* 2016-07-01 Heike Jagode — Update libpfm4
* 2016-06-30 Heike Jagode — Updated PAPI version to 5.5 for upcoming release.
* 2016-06-29 Asim YarKhan — cuda/sampling, cuda: Move sampling build rules to the cuda component.  Minor bugfix in linux-cuda.c to check ok return status.
* 2016-06-28 Asim YarKhan — cuda/sampling: Removing generated files that should not be in the repository
* 2016-06-27 Asim YarKhan — Adding the missing Makefile for cuda/sampling.
* 2016-06-22 William Cohen — Correct IBM Power7 and Power8 computation of PAPI_L1_DCA
* 2016-06-23 Asim YarKhan — Cleanup powercap component.
* 2016-06-23 Heike Jagode — Added FP (SP, DP) presets for Broadwell. NOT TESTED yet due to lack of access to bdw hardware
* 2016-06-22 Heike McCraw — add Intel Skylake and Knights Landing RAPL support
* 2016-06-22 William Cohen — Eliminate the sole use of ftests_skip subroutine
* 2016-06-21 William Cohen — Correct the event string names for tenth.c
* 2016-06-21 William Cohen — Have Fortran test support code report errors more clearly
* 2016-06-17 Heike McCraw — Added FP (SP, DP) presets for Skylake. Corrected L1_LDM|STM, L2_DCW|TCW, PRF_DM, STL_ICY presets for Skylake.
* 2016-06-17 Asim Yarkhan — Bugfix: libmsr component can now disable itself without printing an error message to the screen
* 2016-06-17 Asim Yarkhan — Bugfix: CUDA component can now disable itself without printing an error message to the screen
* 2016-05-19 William Cohen — Force all processors to check event schedulability by reading the counters
* 2016-05-31 sangamesh — Update libpfm4 current with - Log ----------------------------------------------------------------- commit bfb9baf1c8a9533fde271d0436ecd465934dfa17 Author: Stephane Eranian <eranian@gmail.com> Date:   Sat May 28 04:20:14 2016 +0200
* 2016-04-25 sangamesh — Update libpfm4 current with - Log ----------------------------------------------------------------- commit f009e5b7e06c611321c553aed3c0864d59536f32 Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Apr 25 17:22:54 2016 +0200
* 2016-04-18 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit 9603a098df47994a03ffb0c4fdaed5a94fbf1c6f Author: Stephane Eranian <eranian@gmail.com> Date:   Sat Apr 16 05:26:11 2016 +0200
* 2016-03-30 Vince Weaver — update the caddr_t compatability hack in papi.h
* 2016-03-29 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit ec6289ddde0a8826f16158e00fb45636e25f0d06 Author: Stephane Eranian <eranian@gmail.com> Date:   Thu Mar 24 07:48:30 2016 +0100
* 2016-03-16 William Cohen — Only expose the shared libary symbols listed *papi.h files
* 2016-03-14 sangamesh — Update libpfm4 Current with This is an automated email from the git hooks/post-receive script. It was generated because a ref change was pushed to the repository containing the project libpfm4.
* 2016-03-10 Will Schmidt — Fix leftover doxygen reference in INSTALL file.
* 2016-03-10 Will Schmidt — Fix a bashism found in Makefile.inc
* 2016-02-29 William Cohen — Make coretemp internal functions static where possible
* 2016-02-26 sangamesh — Removed the re declaration of the static functions in the perf_event_lib.h
* 2016-02-26 sangamesh — Thanks to William Cohen of RedHat for providing the patches with following description  Make perf_event and perf_event_uncore internal functions static where     possible   Make appio component internal functions static where possible   Make example component internal functions static where possible   Make lmsensors component internal functions static where possible   Make lustre component internal functions static where possible   Make micpower component internal functions static where possible   Make mx component internal functions static where possible   Make net component internal functions static where possible   Make rapl component internal functions static where possible   Make stealtime component internal functions static where possible
* 2016-02-24 sangamesh — Thanks to William Cohen of RedHat for providing a patch that limits shared library soname naming to major version number with following description commit f4ec143eef added versioning to the soname of libpapi.so. However, that previous patch make the soname versioning so detailed that any code linked with that particular version of libpapi.so would only run with that particular version of the library.  If the libpapi.so is replaced with a newer release with minor bug fixes and a minor version number change, the code linked with the older version of the papi library cannot use the newer library because of the change in the shared library soname.
* 2016-02-24 Asim YarKhan — Fixed cuda component README to use the correct configure flags.
* 2016-02-19 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit 756658bff2e346b72d54ae569a68ae4028cf541e Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Feb 19 20:12:23 2016 +0100
* 2016-02-15 Asim YarKhan — Cleanup powercap utility.  Removed mention of libmsr and no-longer-needed union type left over from the libmsr example
* 2016-02-11 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit ebb8be7b1a456431971b3cd173aa1796962dafc8 Author: Stephane Eranian <eranian@gmail.com> Date:   Thu Feb 11 18:00:02 2016 +0100
* 2016-02-09 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit 2f1a62b51666e59c0211e73bb3d8a4ba07093b00 Author: William Cohen <wcohen@redhat.com> Date:   Tue Feb 9 05:55:30 2016 +0100
* 2016-01-31 Phil Vaccaro — added intial powercap write test and readme
* 2016-01-26 Phil Vaccaro — added power cap read test
* 2016-01-26 Phil Vaccaro — added PAPI component
* 2016-01-26 Asim YarKhan — PAPI 5.4.3 release (releasenotes, changelog, man files, ...)
* 2016-01-25 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit 161e12fce382e04d647f3517d92f7f20f6591c89 Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Jan 25 08:33:02 2016 +0100
* 2016-01-15 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit cf9726e3fea23870403a3fa28e01fd6cc3d3d93a Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Jan 15 09:24:50 2016 +0100
* 2016-01-13 sangamesh — Update libpf4 current with - Log ----------------------------------------------------------------- commit 8660f7a66c0e39880cd18145d66d9d59d883f2bd Author: Stephane Eranian <eranian@gmail.com> Date:   Sun Jan 3 17:35:12 2016 +0100
* 2016-01-07 Asim YarKhan — Free allocated memory in the stealtime component when component is shutdown
* 2016-01-06 Asim YarKhan — Fixed memory leak in papi_preset.c by updating the infix_to_postfix function.
* 2015-12-30 Asim YarKhan — Added "-check" flag to papi_avail and papi_native_avail to test counter availability/validity"
* 2015-12-29 Asim YarKhan — Fixed minor error with multiple initializers for lmsensors_vector .default_granularity.
* 2015-12-15 Asim YarKhan — Updated configure script to match configure.in for PAPI 5.4.3
* 2015-12-15 Asim YarKhan — Updating PAPI version to 5.4.3 in configuration files
* 2015-12-14 Asim YarKhan — Update libpfm4 to commit dda280eba8a26fcb006bac29a72805d5f1e8f868
* 2015-12-07 Asim YarKhan — papi_avail to test actual availability of counters using "papi_avail --avail-test"
* 2015-12-04 sangamesh — changed #if (!defined(HAVE_FFSLL) || defined(__bgp__)) int ffsll( long long lli ); #endif --- to --- extern int ffsll( long long lli  in extras.c to avoid warning when --with-ffsll is used as config option
* 2015-12-03 Asim YarKhan — For 5.4.2 release
* 2015-12-03 Asim YarKhan — Updating man pages for 5.4.2 release
* 2015-11-30 Asim YarKhan — For libmsr graph, clean up labels and size of axes in graph
* 2015-11-30 Asim YarKhan — The libmsr component is updated to match major changes in LLNL libmsr library and the LLNL msr-safe kernel module
* 2015-11-30 Asim YarKhan — Minor fix reported by a compiler
* 2015-11-18 sangamesh — Added papi_cuda_sampling utility in /src/components/cuda/sampling changed src/Makefile.inc , src/components/cuda/configure.in to build the utiltiy during PAPI installation
* 2015-11-03 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit daa942846dd0fec5c8fbf2ec8b3ce386dc053c9d Author: Elif Aslan <elas@linux.vnet.ibm.com> Date:   Mon Nov 2 11:44:05 2015 +0100
* 2015-10-30 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit 52bcd7550f495c3e9b11d2848a20389454814b64 Author: Josh Zimmerman <joshz@google.com> Date:   Thu Oct 29 20:27:18 2015 +0100
* 2015-10-21 Vince Weaver — papi_events: add Intel Skylake presets
* 2015-10-19 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit 25ba7ef4afccbaa7dcdf3d6a1958c34e404c3dda Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Jun 29 20:41:24 2015 +0200
* 2015-10-08 sangamesh — Thanks to David Eberius of ICL for reporting a bug in PAPI_get_event_info() in papi_internal.c, (info->component_index = (unsigned int) cidx) was missing at line 2554, of papi_internal.c
* 2015-10-08 sangamesh — Udate libpfm4 Current with  Log ----------------------------------------------------------------- commit 4bfde434d7aae7b6c74dfc0d7c045a0aeea8d7d8 Author: Stephane Eranian <eranian@gmail.com> Date:   Thu Oct 8 06:52:54 2015 +0200
* 2015-10-02 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit ac60b46f0ea8cf8cad3502b87c1311ceae08cbac Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Oct 2 07:54:44 2015 +0200
* 2015-09-08 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit a67b3d427e75d31f3bfe7e072a1e557b0ecb4c57 Author: Steve Kaufmann <sbk@cray.com> Date:   Mon Sep 7 13:43:07 2015 +0200
* 2015-08-27 sangamesh — Thanks to Steve Kaufmann for reporting about the redundant () paramater in the OBJECTS expression of src/Makefile.inc file. Updated Makefile.inc by removing the redundant paramater
* 2015-08-24 sangamesh — Thanks to Harald Servat for reporting the PAPI_overflow issue for multiple eventsets. The problem was in the PAPI_start() function in the branch at line-2166:papi.c , if(is_dirty). After update_control_state(), it is required to re-initialize the overflow settings using set_overflow()
* 2015-08-17 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit cd6fdb01378cc498d637ae2590c07f1b9799c913 Author: Noor <noor_ahsan@mentor.com> Date:   Thu Aug 13 15:44:03 2015 +0500
* 2015-07-29 Vince Weaver — perf_event: update the ARM domain workaround
* 2015-07-29 Vince Weaver — linux-common: clean up ARM cpu detection
* 2015-07-29 Vince Weaver — linux-common: split up x86, power and arm cpuinfo parsing
* 2015-07-29 Vince Weaver — linux-common: clean up and comment the cpuinfo parsing code
* 2015-07-16 Asim YarKhan — Create libmsr component for reading power information and writing power constraints using MSRs on some Intel processsors
* 2015-07-15 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit 62316d35d1f880a944d5f972db32165952d47905 Author: Stephane Eranian <eranian@gmail.com> Date:   Wed Jul 15 08:00:16 2015 +0200
* 2015-07-13 sangamesh — Thanks to Steve Kaufman for providing a patch that increases the PERF_EVENT_MAX_MPX_COUNTERS to 192 from 128 and enhances the corresponding warning message in papi_internal.c
* 2015-07-13 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit 3f97d130cd154c68ee1ee96e01c06c59755ab186 Author: Deepthi Dharwar <deepthi@linux.vnet.ibm.com> Date:   Fri Jul 10 15:36:36 2015 +0530
* 2015-06-29 sangamesh — Update libpfm4 Current with  Log ----------------------------------------------------------------- commit d8eacf68666bd5da5419e6ec2f777b6432d9ffe1 Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Jun 29 20:46:36 2015 +0200
* 2015-06-29 Asim YarKhan — Example of using LD_PRELOAD with the CUDA component.
* 2015-06-26 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit 37dd035818a1852ec92bd689623977248f5b9d1f Author: Stephane Eranian <eranian@gmail.com> Date:   Fri Jun 26 02:56:02 2015 +0200
* 2015-06-26 Vince Weaver — Add future broadwell-ep support.
* 2015-06-25 Vince Weaver — add broadwell predefined events
* 2015-06-25 Heike McCraw — Added definitions to Power8 for PAPI_SP_OPS, PAPI_DP_OPS.
* 2015-06-18 sangamesh — Added [case 63: /*Haswell EP*/] line the src/components/perf_event/tests/event_name_lib.c file to support offcore for haswell EP
* 2015-06-18 sangamesh — Added suuport for Haswell-EP processor with model-63 in src/components/perf_event_uncore/tests/perf_event_uncore_lib.c and src/components/perf_event_uncore/tests/perf_event_uncore_cbox.c files. As a result perf_event_uncore, perf_event_uncore_multiple and perf_event_uncore_cbox tests get passed. Tested and verified on Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz with linux kernel 4.0.4-1.el6.elrepo.x86_64
* 2015-06-17 sangamesh — Thanks to Garry Mohr for the patch that removes the error message (PAPI Error: Error Code -7,Event does not exist) on executing papi_native_avail in PAPI built with lustre component
* 2015-06-16 Vince Weaver — rapl: allow DRAM to have separate scaling factor from CPU
* 2015-06-16 Vince Weaver — rapl: add support for Broadwell
* 2015-06-11 sangamesh — Thanks to William Cohen for the patch which does the following: Checking the cpu family and module number is not sufficient to determine whether RAPL can be used.  If the papi is running inside a guest VM, the MSR used by the PAPI RAPL component may not be available.  There should be a simple read test to verify the RAPL MSR registers are available.  This allows the component to more clearly report that RAPL is unsupported rather than just exiting program when the RAPL
* 2015-06-08 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit a0045ed9b2d45369e73684f987f7a66841738b27 Author: Stephane Eranian <eranian@gmail.com> Date:   Sat Jun 6 00:07:11 2015 +0200
* 2015-06-04 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit 5c42ba825598ac2edd2b6a6e84bd724172264619 Author: Stephane Eranian <eranian@gmail.com> Date:   Mon Nov 24 15:23:06 2014 +0100
* 2015-05-28 Heike McCraw — Temporary workaround: exclude_guest and exclude_host bits have to be zero in the attribute structure (via :mg=1:mh=1).
* 2015-05-26 sangamesh — Update libpfm4 Current with  Log ----------------------------------------------------------------- commit c5d54340ed8c351341fafbe4b8704d94021c338c Author: Stephane Eranian <eranian@gmail.com> Date:   Sun May 24 11:28:16 2015 +0200
* 2015-05-19 Heike McCraw — Updated rapl_plot utility so that the correct values/units are reported (e.g. scaled and fixed value counts should not be converted)
* 2015-05-14 Asim YarKhan — Remove mention of the PAPI TRAC
* 2015-05-13 sangamesh — Update libpfm4 Current with - Log ----------------------------------------------------------------- commit 6331fae94fd0c47c2b0e73d67b24a2959fe21e6a Author: Stephane Eranian <eranian@gmail.com> Date:   Tue May 12 23:09:43 2015 +0200
* 2015-05-05 sangamesh — update libpfm4 Current with - Log ----------------------------------------------------------------- commit be2d5200d9511bfe34ad2b675f1dce64a0fbe080 Author: Stephane Eranian <eranian@gmail.com> Date:   Sat May 2 08:09:46 2015 +0200
* 2015-05-04 Vince Weaver — papi_events.csv: typo in the ARM Cortex A53 definitions
* 2015-04-30 Vince Weaver — papi_events.csv: add preset events for ARM Cortex A53
* 2015-04-24 sangamesh — Updated libpfm: commit 886b1d0338aeac8dc4e7fb69ad50ab21a4856ba1 Author: Stephane Eranian <eranian@gmail.com> Date:   Sun Apr 19 10:47:28 2015 +0200
* 2015-04-20 sangamesh — Inverted comma missing in prev commit -added compile incantation for compiling programs that offload code to MIC
* 2015-04-20 sangamesh — added compile inacntation for compiling programs that offload code to MIC
* 2015-04-16 sangamesh — Bug reported by William Cohen in papi_events.csv for the event PAPI_L1_TCM
* 2015-03-31 Asim YarKhan — Updated the NVML configure script which requires an autoconf and an updated configure script
* 2015-03-31 Asim YarKhan — Updated the NVML configure script to allow separate include and library paths
* 2015-03-30 Asim YarKhan — Bugfix linux-infiniband_umad.c to include linux-infiniband_umad.h rather than linux-infiniband.h.
* 2015-03-30 Asim YarKhan — Corrected function name in _vmware_vector from _vmware_init to _vmware_init_thread.
* 2015-03-24 Asim YarKhan — Regenerated configure to match the PAPI_GRN_SYS patch
* 2015-03-24 Asim YarKhan — Support PAPI_GRN_SYS granularity for perf component, updating the system wide test (patch 2 of 2).
* 2015-03-24 Asim YarKhan — Support PAPI_GRN_SYS granularity for perf component, picking a sane CPU number (patch 1 of 2).
* 2015-03-24 Asim YarKhan — Added call to unregister the overflow handler.. plus small code cleanup
* 2015-03-05 Asim YarKhan — Clean output from papi_avail tools when there are no user defined events
* 2015-03-05 Asim YarKhan — Regenerate configure using autoconf 2.59
* 2015-03-03 Asim YarKhan — Do not generate an error if the CUDA libraries cannot be loaded, just write a debug message
* 2015-03-03 Asim YarKhan — Updating the number to 5.4.1
* 2015-03-02 Asim YarKhan — Minor change to specify locations of some files
* 2015-03-02 Asim YarKhan — Updating the release number to 5.4.2 after a release
* 2015-03-02 Asim YarKhan — Fixed a missing -to-
* 2015-03-02 Asim YarKhan — Updated ChangeLog and release notes for 5.4.1
* 2015-03-02 Asim YarKhan — Updating the documentation for the 5.4.1 release
* 2015-03-02 Heike McCraw — Clean up papi.pc when 'make clobber' is called.
* 2015-03-02 Heike McCraw — Thanks much to Gary Mohr for the patch:
* 2015-03-02 Heike McCraw — Update libpfm4
* 2015-03-02 Asim YarKhan — Generating pkg-config files for papi
* 2015-02-28 Vince Weaver — Add support for ARM 1176 cpus
* 2015-02-27 Vince Weaver — Add ARM Cortex A7 support.
* 2015-02-27 Heike McCraw — Update libpfm4
* 2015-02-25 Asim YarKhan — Sync thread exit in krental_threads.c
* 2015-02-20 Asim YarKhan — Added additional notes and examples for the MIC.  Specify how to use qualifiers to set exclude_guest and exclude_host bits to 0.  Use micnativeloadex to run the utilites.
* 2015-02-11 Asim YarKhan — Change papi_native_avail to refer to event qualifiers (qual) rather than event masks.
* 2015-02-10 Asim YarKhan — Test case for attaching an eventset to a single CPU rather than a thread (attach_cpu)
* 2015-02-02 Asim YarKhan — Updated CUDA component supporting multiple GPUs and multiple CUDA contexts.
* 2015-02-02 Heike McCraw — Reported by Mark Maurice:
* 2015-01-20 Heike McCraw — Update libpfm4
* 2015-01-20 sangamesh — Thanks to Gary Mohr for the patch:The patch provided solves the segmentation faults produced by the lustre component.The changes done by the patch are in the _lustre_shutdown_component() by adding lustre_native_table=NULL statement and Later num_events=0 and table_size=32 were added in the same function to fully solve the segmentation faults
* 2014-12-17 Asim YarKhan — User defined events: Enhance PAPI preset events allow user defined events via a user event definition file.
* 2014-12-15 Vince Weaver — perf_event tests: add sample haswell offcore event
* 2014-12-11 Heike McCraw — Update presets for Intel Haswell and Haswell-EP (according to the updates of the libpfm4 event table for Intel Haswell and Haswell-EP). These mods have not been tested due to lacking access to an Intel Haswell system.
* 2014-12-09 Heike McCraw — Update libpfm4
* 2014-12-01 Heike McCraw — Uncore component fix (Cont.) (the patch committed on Sep 8 only applied the changes to the perf_event_uncore but not to the perf_event component)
* 2014-11-15 Heike McCraw — Update release procedure
* 2014-11-14 Heike McCraw — Bump master to 5.4.1, we just released out of the stable-5.4 branch.
* 2014-11-13 Heike McCraw — Generate a changelog for 5.4.0
* 2014-11-13 Heike McCraw — Revert "added micflag to stop arg_check for ffsll,walltimer,tls and virtual timer"
* 2014-11-13 Heike McCraw — Revert "Generate a changelog for 5.4.0"
* 2014-11-13 Heike McCraw — Generate a changelog for 5.4.0
* 2014-11-13 sangamesh — added micflag to stop arg_check for ffsll,walltimer,tls and virtual timer
* 2014-11-13 Heike McCraw — Prepare release notes for a 5.4.0 release
* 2014-11-13 Heike McCraw — The python script that is used to create a ChangeLog for the current release (gitlog2changelog.py) does only list commits that change more than one file.
* 2014-11-12 Heike McCraw — Rebuild the doxygen manpages
* 2014-11-12 Asim YarKhan — Remove omptough from standard run_tests.sh testing
* 2014-11-11 Heike McCraw — Fix number of counters and events for each of the 5 BGPM units as well as emon on BG/Q
* 2014-11-07 Asim YarKhan — Patch linux-timer.c to provide cycle counter support on aarch64 (64-bit ARMv8 architecture)
* 2014-11-06 Heike McCraw — Extension of the RAPL energy measurements on Intel via msr-safe.     (https://github.com/scalability-llnl/msr-safe)
* 2014-11-06 Heike McCraw — Fixed string null termination.
* 2014-10-30 Asim YarKhan — Patch to reduce cost of using PAPI_name_to_code and add list of supported pmu names to papi_component_avail output
* 2014-10-28 Asim YarKhan — This patch file contains additional changes to resolve defects reported by Coverity.
* 2014-10-23 Asim YarKhan — This patch file fixes a few problems in the core and uncore components.
* 2014-10-22 Asim YarKhan — Fix percent error calculation in ctests/tenth.c
* 2014-10-22 Asim YarKhan — PPC64, fix L1 data cache read, write and all access equations.
* 2014-10-22 Asim YarKhan — This patch file fixes two problems and adds a performance improvement in "papi_native_avail.
* 2014-10-22 Asim YarKhan — Fix build error when no fortan is installed
* 2014-10-16 Asim YarKhan — PPC64 add support for the Power non virtualized platform
* 2014-10-16 Asim YarKhan — byte_profile.c: PPC64 add support for PPC64 Little Endian to byte_profile.c
* 2014-10-15 Asim YarKhan — PPC64 add support for PPC64 Little Endian to sprofile.c
* 2014-10-15 Asim YarKhan — PPC64 sys_mem_info array size is wrong
* 2014-10-15 Asim YarKhan — Remove stray Intel Haswell events from Intel Ivy Bridge presets
* 2014-10-14 Asim YarKhan — Update papi_events.csv to match libpfm support for Intel family 6 model 63 (hsw_ep)
* 2014-10-14 Asim YarKhan — Support for the ARM X-Gene processor.
* 2014-10-14 Heike McCraw — Thanks to Gary Mohr for the patch
* 2014-10-14 Heike McCraw — Update libpfm4
* 2014-10-09 Asim YarKhan — Record encode_failed error by setting attr.config to 0xFFFFFFF.
* 2014-09-25 Asim YarKhan — Based on Gary Mohr's suggestion.  If an event fails when we try to add it (encode_failed), then we note that error by setting attr.config = 0xFFFFFF for that event.  Then, if there is a later check to validate this event, the check will correctly return an error.
* 2014-09-25 Asim YarKhan — Adding the NativeAvailValidate patch provided by Gary Mohr.
* 2014-09-24 James Ralph — Emon power component for BG/Q
* 2014-09-23 James Ralph — perf_event_uncore.c: Check scheduability of events
* 2014-09-19 James Ralph — Address coverity defects in src/components
* 2014-09-19 James Ralph — Address coverity reported issues in src/
* 2014-09-12 James Ralph — Update release procedure, check buildbot!
* 2014-09-11 James Ralph — Update libpfm4: catches HSW updates
* 2014-09-08 James Ralph — Uncore component fix:
* 2014-09-02 Heike Jagode — Thanks to Gary Mohr for the patch --------------------- Fix in papi_internal.c where it was trying to look up the event name.  The RAPL component found the event and returned a code but papi_internal.c  exited the enum loop for that component but failed to exit the loop that checks all of the components.  This caused it to keep looking at other components until it fell out of the outer loop and returned an error. In addition to the actual change, some formatting issues were fixed. ---------------------
* 2014-09-02 James Ralph — Bump NUM_MPX_COUNTERS for linux-perf
* 2014-09-02 James Ralph — ctests/ Address coverity reported defects
* 2014-08-29 James Ralph — testlib/test_util.c: Check enum return value
* 2014-08-29 James Ralph — event_info utility: address coverity defect
* 2014-08-28 Heike Jagode — Extend 'papi_native_event --validate' to check for umasks.
* 2014-08-27 James Ralph — perf_event[_uncore]: switch to libpfm4 extended masks
* 2014-08-27 James Ralph — Libpfm update
* 2014-08-20 James Ralph — General code cleanup and improved debugging
* 2014-08-11 James Ralph — error_codes utility: remove internal bits
* 2014-08-04 James Ralph — Update nvml README
* 2014-07-30 James Ralph — Libpfm4 update: catch the cpu= modifier update
* 2014-07-25 James Ralph — perf_event.c: cleanup error messages
* 2014-07-24 James Ralph — Update HSW presets
* 2014-07-24 James Ralph — papi.c: Add information to API entry debuging
* 2014-07-23 James Ralph — run_tests.sh: more exclude cleanups
* 2014-07-23 James Ralph — papi_internal.c: change SUBDBG to INTDBG
* 2014-07-23 James Ralph — native_avail.c: Bug fixes and updates
* 2014-07-23 James Ralph — Update libpfm4
* 2014-06-30 James Ralph — Generate a changelog for 5.3.2
* 2014-06-30 James Ralph — Prepare release notes for a 5.3.2 release
* 2014-06-30 James Ralph — Regenerate man pages for version number bump
* 2014-06-30 James Ralph — Bump version numbers for a pending release
* 2014-06-27 James Ralph — Update libpfm4
* 2014-06-27 James Ralph — Fix a warning in component initialization
* 2014-06-27 James Ralph — Update preset mappings for Intel Haswell
* 2014-06-24 James Ralph — run_tests_exclude: exclude longer tests
* 2014-06-24 James Ralph — Fix excluded files for run_tests
* 2014-06-15 James Ralph — Fix a precidence issue
* 2014-06-10 James Ralph — Update libpfm4
* 2014-05-28 William Cohen — Add aarch64 Cortex A57 presets
* 2014-05-19 James Ralph — peu_libpfm4_events.c: remove unused variable
* 2014-05-19 James Ralph — threads.h: fix a typo in format specifier
* 2014-05-12 James Ralph — Printf formatting change...
* 2014-05-12 James Ralph — x86_cpuid_info: Better preprocessor macro
* 2014-05-05 James Ralph — x86_cpuid_info.c:
* 2014-05-07 James Ralph — papi.c: Debuging improvements.
* 2014-05-05 James Ralph — component tests' include: Help find -lpapi
* 2014-04-24 James Ralph — Update libpfm4
* 2014-04-16 James Ralph — Bump libpfm4
* 2014-04-15 James Ralph — native_avail: Add a --validate flag
* 2014-04-10 James Ralph — papi_internal: Print event code in hex
* 2014-04-09 James Ralph — Add x87 counts to FP_INS and FP_OPS on [S|I]VB
* 2014-04-08 James Ralph — appio: cleanup a memory leak
* 2014-04-04 James Ralph — libpfm4 update
* 2014-04-03 Vince Weaver — perf_event: update error returns
* 2014-04-01 James Ralph — perf_event_uncore: Improve debugging info
* 2014-04-01 James Ralph — perf_event_uncore: More work on Uncore enum
* 2014-03-31 Vince Weaver — rapl: drop the comments saying rapl is specific to sandybridge
* 2014-03-31 Vince Weaver — rapl: enable DRAM measurement for all Haswell
* 2014-03-28 James Ralph — perf_event_uncore: fixes SNBEP UNC event listing
* 2014-03-27 James Ralph — perf_event_uncore:Support events from several PMUs
* 2014-03-26 Vince Weaver — ctests/inherit: fall back on PAPI_TOT_INS if PAP_FP_INS not available
* 2014-03-26 Vince Weaver — ctests/attach3: fall back to PAPI_TOT_INS if PAPI_FP_INS not available
* 2014-03-26 Vince Weaver — remove Hawell PAPI_L1_TCA predefined event
* 2014-03-26 Vince Weaver — ctests/attach2: fall back on PAPI_TOT_INS if PAPI_FP_INS not available
* 2014-03-26 James Ralph — Add units to NVML component
* 2014-03-17 James Ralph — Move ib_sysfs to infiniband
* 2014-03-14 James Ralph — Initial import of Gabriel's infiniband rewrite
* 2014-03-17 James Ralph — Move the infiniband component out of the way.
* 2014-02-26 James Ralph — configure: respect --with-walltimer and virtualtimer
* 2014-02-26 James Ralph — RAPL component: support Haswell-EP
* 2014-02-21 James Ralph — Update libpfm4 to release version 4.5
* 2014-01-30 William Cohen — Remove unused variable value from the appio_values_by_code.c test
* 2014-01-30 William Cohen — Use correct specification for signed and unsigned int
* 2014-02-07 James Ralph — buildbot_onfigure: Build more components
* 2014-02-05 James Ralph — libpfm4 update: add ARM Qualcomm Krait support
* 2014-02-05 Vince Weaver — add ARM Qualcomm Krait predefined events
* 2014-02-04 James Ralph — Update appio grn and dom fields
* 2014-02-04 James Ralph — Update the domain/granularity of many components
* 2014-01-16 James Ralph — Libpfm4: Update for RAPL GPU counters
* 2014-01-03 James Ralph — PAPI_Matlab: Change outdated API call
* 2013-12-30 James Ralph — coretemp_freebsd: Cleanups
* 2013-12-30 James Ralph — ctests/attach[2,3]: Fix ptrace call for BSD
* 2013-12-30 James Ralph — Configure.in: Remove Bash-isms from comp selection
* 2013-12-30 James Ralph — Configure.in: Correctly detect FreeBSD OS version
* 2013-12-20 James Ralph — RAPL component: minor house keeping
* 2013-12-06 Vince Weaver — papi_events.csv : add initial atom silvermont support
* 2013-12-06 James Ralph — Update libpfm4: catch several haswell model numbers
* 2013-12-03 James Ralph — Libpfm4 update: Catches  the Intel Silvermont manpage
* 2013-12-02 James Ralph — Libpfm4 Update
* 2013-12-02 James Ralph — Update the 5.3 ChangeLog
* 2013-11-25 James Ralph — nvml component: Add missing }
* 2013-11-25 James Ralph — nvml component: modify api checks
* 2013-11-21 James Ralph — libpfm4: Pull in the latest updates
* 2013-11-21 James Ralph — Update Changelog
* 2013-11-21 James Ralph — Kill the .gitignore files in delete_before_release
* 2013-11-21 James Ralph — command_line utility: Initialize a variable
* 2013-11-20 William Cohen — Make data_range test use prginfo
* 2013-11-20 William Cohen — Check the return values of PAPI_start() and PAPI_stop() for the data_range test
* 2013-11-19 James Ralph — configure: Build fpapi.h and co for mic
* 2013-11-18 James Ralph — Update INSTALL.txt with instructions for mic offload.
* 2013-11-18 James Ralph — Update release notes for a 5.3
* 2013-11-18 James Ralph — Generate a changelog for 5.3
* 2013-11-18 James Ralph — Rebuild the man pages for a 5.3 release
* 2013-11-18 James Ralph — Bump version numbers for a pending 5.3
* 2013-11-18 James Ralph — Makefile.inc: Pass LINKLIB, not SHLIB to the comp_tests
* 2013-11-18 James Ralph — ctests/Makefile.target.in: Properly catch LINKLIB
* 2013-11-18 James Ralph — ctests/Makefile.target.in: Respect static-tools
* 2013-11-18 James Ralph — ctests/Makefile: Don't clobber value of LIBRARY
* 2013-11-18 James Ralph — Makefile.inc: Add enviro vars to fulltest recipe
* 2013-11-17 James Ralph — Switch LINKLIB to not have relative pathing
* 2013-11-15 James Ralph — Fix a typo in the lustre tests' Makefile
* 2013-11-13 James Ralph — papi_preset.c: Fix _papi_load_preset_table func
* 2013-11-12 James Ralph — more doxygen xml tag cleanup
* 2013-11-12 James Ralph — Fix doxygen Unsupported xml/html tag warnings
* 2013-11-12 James Ralph — micpower: fix doxygen warning
* 2013-11-12 James Ralph — host_micpower: update docs
* 2013-11-11 James Ralph — ctests/p4_lst_ins: Narrow scope of test
* 2013-11-11 James Ralph — Libpfm4 update
* 2013-11-10 Heike Jagode — Added energy consumption to host_micpower utility.
* 2013-11-08 James Ralph — shlib.c: Check for NULL
* 2013-11-08 James Ralph — perf_event.c: Check return value of ioctl
* 2013-11-08 James Ralph — multiplex_cost: check return value on PAPI_set_opt
* 2013-11-08 James Ralph — Ignore component target makefile
* 2013-11-08 Dan Terpstra — Modify linux-rapl to support one wrap-around of the 32-bit registers for reading energy. This insures availability of the full 32-bit dynamic range. However, it does not protect against two wrap-arounds. Care must be taken not to exceed the expected dynamic range, or to check reasonableness of results on completion. Modifications were also made to report rapl events as unscaled binary values in order to compute dynamic ranges. Modify rapl-basic to add a test (rapl_wraparound) to estimate maximum measurement time for a naive gemm. With a -w option, measurement for this amount of time will be performed. The gemm can be replaced with a user kernel for more accurate time estimates. Makefile was modified to support the new test case.
* 2013-11-07 James Ralph — Modernize some ctests
* 2013-11-06 James Ralph — More MPICC checking
* 2013-11-06 James Ralph — zero_shmem.c: Fix compiler warning
* 2013-11-06 James Ralph — ctests/Makefile.recipies: conditionally build the MPI test
* 2013-11-06 James Ralph — Check for mpicc at configure time
* 2013-11-05 Vince Weaver — Add floating point events for IvyBridge
* 2013-11-04 James Ralph — Libpfm4 update: catches ivy bridge updates
* 2013-11-01 James Ralph — micpower: check return of fopen before use
* 2013-11-01 Heike Jagode — Add host_micpower utility to gather power (and voltage) measurements on Intel Xeon Phi chips using MicAccessAPI.
* 2013-11-01 Heike Jagode — Added more detailed event description and correct units to host mic power events.
* 2013-11-01 James Ralph — host_micpower: Better error reporting
* 2013-10-31 James Ralph — host_micpower: Fix some makefile bits
* 2013-10-30 James Ralph — host_micpower: fix function signature
* 2013-10-28 James Ralph — Update release_procedure.txt
* 2013-10-28 James Ralph — host_micpower: Add a README file.
* 2013-10-25 James Ralph — Make the testsuite as a stand-alone copy-able directory of code
* 2013-10-25 James Ralph — Refactor the driver in do_loops.c into its own file.
* 2013-10-23 Heike McCraw — Passing BGPM errors up to PAPI.
* 2013-10-22 Heike McCraw — Fixed the behavior in BGQ's NWunit component after attaching an event set to a specific thread that owns the target recourse counting
* 2013-10-08 William Cohen — ctests/sdsc4-mpx and ctests/sdsc2-mpx trigger an assert in sw_multiplex.c when tests do cleanup
* 2013-10-22 James Ralph — CUDA component: Set the number of native events
* 2013-10-11 William Cohen — add preliminary aarch64 (arm64) support
* 2013-10-01 James Ralph — zero_shmem: cleanup compiler warnings
* 2013-10-01 James Ralph — ctests/earprofile.c: Fix compiler warning
* 2013-09-30 James Ralph — ctests/p4_lst_ins.c: Fix the P4 load test.
* 2013-09-30 James Ralph — ctests/Makefile: Remove reference to acpi.c
* 2013-09-30 James Ralph — ctests/zero_shmem: Update the test
* 2013-09-27 James Ralph — zero_shmem: Include pthread.h
* 2013-09-27 James Ralph — zero_smp: Change a compile time error to a test_skip
* 2013-09-26 James Ralph — ctests/Makefile: Default to building everything
* 2013-09-26 James Ralph — testlib, ftests Makefiles: cleanup ifort generated files
* 2013-09-26 James Ralph — Coretemp tests: Fix skipping logic
* 2013-09-26 James Ralph — configure: refactor CTEST_TARGETS
* 2013-09-25 James Ralph — configure: Remove -openmp from CFLAGS under icc
* 2013-09-26 James Ralph — testlib: Fix the Makefile variable assignment
* 2013-09-17 James Ralph — perf_event_uncore: cleanup a compiler warning
* 2013-09-17 James Ralph — papi_events.csv: Add PAPI_L1_ICM for Haswell
* 2013-08-28 James Ralph — testlib: library-ify testlib
* 2013-08-26 James Ralph — Gabrial's mic with icc changes to configure.
* 2013-08-26 James Ralph — papi_events.csv: First draft preset events on HSW
* 2013-08-20 James Ralph — command_line util: Fix skipping event bug.
* 2013-08-16 James Ralph — lustre component: fix memory leak
* 2013-08-13 James Ralph — Close resource leaks
* 2013-08-07 James Ralph — Doxygen makefile: update dependencies
* 2013-08-06 James Ralph — Clarify the release procedure's wording a little.
* 2013-08-06 James Ralph — Update RELEASENOTES and create a Changelog for 5.2
* 2013-08-02 James Ralph — Update the manpages for a pending 5.2 release.
* 2013-08-02 Vince Weaver — try to properly detect number of sockets
* 2013-08-02 Vince Weaver — perf_event_uncore: have tests skip if component disabled rather than fail
* 2013-08-02 Vince Weaver — perf_event_uncore: change order of uncore detection logic
* 2013-08-02 Vince Weaver — perf_event: fix papi_native_avail output
* 2013-08-02 Vince Weaver — papi_native_avail: fix empty component case
* 2013-08-02 Vince Weaver — perf_event_uncore: disable component if no events found
* 2013-08-02 James Ralph — Update libpfm4:
* 2013-08-01 James Ralph — Components: Use the cuda dlopen fix all cases.
* 2013-07-31 Vince Weaver — perf_event libpfm4 events -- correctly handle invalid events
* 2013-07-31 Vince Weaver — perf_event_uncore: remove check_permissions() test
* 2013-07-31 Vince Weaver — perf_event_uncore: remove unused kernel workarounds
* 2013-07-25 James Ralph — Trial fix for the cuda component static libc linking issue.
* 2013-07-24 Vince Weaver — Add linux-pfm-ia64 to configure
* 2013-07-24 Heike Jagode — Fixed tests for example component. Both tests failed due to incorrect check of the components PAPI has been configured with.
* 2013-07-23 Maynard Johnson — Add initial support for IBM POWER8 processor
* 2013-07-22 James Ralph — Rerun autoconf
* 2013-07-22 William Cohen — Correct versioning of libpapi.so
* 2013-07-19 James Ralph — Attempt to fix a memory leak in fork2 test.
* 2013-07-19 Peter Bailey — Fix a deadlock in _papi_hwi_lookup_cpu().
* 2013-07-19 James Ralph — micpower: fix return value check
* 2013-07-16 James Ralph — configure: Fix AIX build
* 2013-07-16 James Ralph — micpower: update some indexing code
* 2013-07-15 James Ralph — INSTALL.txt: typo
* 2013-07-15 James Ralph — papi_libpfm_events: needs include files for types.
* 2013-07-15 James Ralph — perfctr: cleanup a warning
* 2013-07-15 James Ralph — perfctr: remove dead code.
* 2013-07-15 James Ralph — perfctr: refactor out setup_x86_presets
* 2013-07-15 James Ralph — perfctr: cleanup unused parameter warning.
* 2013-07-15 James Ralph — configure: remove debugging message
* 2013-07-12 James Ralph — lustre: use whole directory name as event
* 2013-07-15 Vince Weaver — allow more than one EventSet attach to a CPU at a time
* 2013-07-15 Vince Weaver — perf_event_uncore: remove perf_event_uncore_nogran test
* 2013-07-15 Vince Weaver — perf_event_uncore: add perf_event_uncore_cbox test
* 2013-07-15 Vince Weaver — linux: properly set hwinfo->socket value
* 2013-07-13 Vince Weaver — perf_event_uncore: properly report number of total counters available
* 2013-07-13 Vince Weaver — perf_event/perf_event_uncore/libpfm4 -- rearrange files
* 2013-07-12 Vince Weaver — papi_libpfm4: properly call pfm_terminate() in papi_libpfm4_shutdown
* 2013-07-12 Vince Weaver — split papi_libpfm4_init()
* 2013-07-12 Vince Weaver — perf_event: on old kernels if SW Multiplex enabled, then report proper number of MPX counters available
* 2013-07-12 Vince Weaver — Revert "perf_event: use PERF_IOC_FLAG_GROUP when resetting events"
* 2013-07-12 Vince Weaver — perf_event: use PERF_IOC_FLAG_GROUP when resetting events
* 2013-07-12 Vince Weaver — Add reset_multiplex.c
* 2013-07-12 James Ralph — lustre: botched a conflict resolution
* 2013-07-12 Vince Weaver — perf_event: move overflow and profile code out of common lib
* 2013-07-12 Vince Weaver — perf_event_uncore: remove profiling and overflow code
* 2013-07-12 James Ralph — lustre component: Several fixes
* 2013-07-12 Vince Weaver — perf_event_uncore: remove dispatch timer call
* 2013-07-12 Vince Weaver — perf_event: move rdpmc detection back into perf_event.c
* 2013-07-12 Vince Weaver — perf_event_uncore: check the paranoid file
* 2013-07-12 Vince Weaver — perf_event and paranoid level 2
* 2013-07-12 Vince Weaver — rename sys_perf_event_open2() call back to sys_perf_event_open()
* 2013-07-11 James Ralph — configure: libpfm selection logic rework
* 2013-07-10 James Ralph — Component: host_micpower
* 2013-07-10 William Cohen — Fwd: Re: [Ptools-perfapi] ctests/shlib FAILED
* 2013-07-09 Andi Drebes — Perf_event_amd_northbridge_test: Use buffer event_name instead of uncore_event
* 2013-07-08 James Ralph — micpower:
* 2013-07-08 James Ralph — Micpower: fix a typo
* 2013-07-08 James Ralph — INSTALL.txt: update instructions for MIC.
* 2013-07-08 Vince Weaver — Add perf_event_amd_northbridge test
* 2013-07-08 Vince Weaver — Make perf_event_uncore tests use PAPI_get_component_index()
* 2013-07-05 Vince Weaver — avoid having a "default" PMU for the uncore component
* 2013-07-05 Vince Weaver — Update perf_event_uncore tests to properly fail if they don't have enough permissions
* 2013-07-05 Vince Weaver — perf_event_uncore_test : properly use uncore component
* 2013-07-05 Vince Weaver — have _papi_libpfm4_ntv_name_to_code properly check pmu_type
* 2013-07-03 Vince Weaver — perf_event_uncore: fix ivb event in uncore test
* 2013-07-03 James Ralph — libpfm4: Update
* 2013-07-01 William Cohen — Clean up option handling in papi_cost
* 2013-07-01 William Cohen — Clean up option handling for papi_native_avail
* 2013-07-01 William Cohen — Clean up option handling in papi_decode
* 2013-07-01 William Cohen — Improve option matching in papi_component and add "--help" option
* 2013-07-01 William Cohen — Add options to papi_command_line man page and improve opt handling
* 2013-07-01 William Cohen — Add information for papi_version to be complete
* 2013-07-01 Vince Weaver — add a --disable-perf-event-uncore option to configure
* 2013-06-29 Vince Weaver — remove syscalls.h
* 2013-06-29 Vince Weaver — move perfmon modules to their own component directory
* 2013-06-29 Vince Weaver — move perfctr files to components/perfctr directory
* 2013-06-27 Dan Terpstra — debugged versions of these files
* 2013-06-27 James Ralph — native_avail: Fix parse_unit_mask code
* 2013-06-26 James Ralph — fork2: Return fork2 test to its old functionality
* 2013-06-26 James Ralph — Revert "fork2 ctest: remove; was an exact duplicate of fork"
* 2013-06-25 Dan Terpstra — Modify PAPI_list_events functionality to match documentation. You can now pass in a NULL event array and a zero count to get back the valid number of events. This can then be used to allocate the array and retrieve the exact number of events. Thanks to Nils Smeds and Alain Miniussi for pointing this out.
* 2013-06-25 Dan Terpstra — Modify PAPI_list_events functionality to match documentation. You can now pass in a NULL event array and a zero count to get back the valid number of events. This can then be used to allocate the array and retrieve the exact number of events. Thanks to Nils Smeds and Alain Miniussi for pointing this out.
* 2013-06-25 Vince Weaver — zero_fork ctest : make documentation match code
* 2013-06-25 Vince Weaver — forkexec ctest : make comments match code
* 2013-06-25 Vince Weaver — forkexec4 ctest : make comments match the code
* 2013-06-25 Vince Weaver — forkexec3 ctest : make documentation match code
* 2013-06-25 Vince Weaver — forkexec2 ctest: have comments match what source does
* 2013-06-25 Vince Weaver — fork2 ctest: remove; was an exact duplicate of fork
* 2013-06-25 Vince Weaver — fork ctest: make comments match what file actually does
* 2013-06-24 Vince Weaver — perf_event: fix failure on ARM due to domain settings
* 2013-06-24 Vince Weaver — perf_event: fix failure on ARM due to domain settings
* 2013-06-20 James Ralph — lustre component: fix a free issue.
* 2013-06-18 James Ralph — ctests: Skip calling into disabled components.
* 2013-06-14 James Ralph — testlib: don't change the iter count
* 2013-06-12 James Ralph — Infiniband component: switch over to weak linking
* 2013-06-11 Vince Weaver — rapl tests: make the error messages a little more verbose
* 2013-06-11 James Ralph — run_tests_exclude files: Exclude a template file
* 2013-06-11 James Ralph — run_tests.sh: fix exclude check.
* 2013-06-10 James Ralph — cuda component: Address a coverity issue
* 2013-06-10 Vince Weaver — coretemp_basic: update test to properly enumerate events
* 2013-06-10 James Ralph — rapl component: address potential looping issue in test.
* 2013-06-10 James Ralph — rapl components: coverity fixes
* 2013-06-10 James Ralph — net components: coverity fixes
* 2013-06-07 James Ralph — nvml: Apply Gary Mohr's dlopen patch.
* 2013-06-07 Vince Weaver — rapl: update the rapl_plot utility
* 2013-06-07 Vince Weaver — rapl: add better error messages on component init failure
* 2013-06-07 Dan Terpstra — First round of changes to implement a PAPI high level event per cycle call. Untested.
* 2013-06-05 James Ralph — rapl: Add Ivb-EP support
* 2013-05-31 Gary Mohr — cpus.c: Don't run init_thread/shutdown_thread for disabled components.
* 2013-05-29 James Ralph — Grab the updated ChangeLog from 5.1.1
* 2013-05-29 James Ralph — Update libpfm4
* 2013-05-24 Vince Weaver — Add perf_event user/kernel domain test
* 2013-05-24 Vince Weaver — Add perf_event offcore response test
* 2013-05-24 Vince Weaver — Some more ctest fixes involving disabled components.
* 2013-05-24 James Ralph — Bump version numbers
* 2013-05-24 Vince Weaver — Disallow enumerating events on disabled components.
* 2013-05-24 Vince Weaver — perf_event_system_wide: SKIP instead of FAIL if we don't have proper permissions
* 2013-05-24 Vince Weaver — move the perf_event specific tests to be with their component
* 2013-05-24 Vince Weaver — ctests/perf_event_uncore_multiple: Improve this test a bit
* 2013-05-24 Vince Weaver — Remove the no-longer needed perf_events files
* 2013-05-24 Vince Weaver — Split up CPUCOMPONENT configure variable
* 2013-05-24 Vince Weaver — configure: have --with-components append comonents to existing value
* 2013-05-24 Vince Weaver — add perf_event and perf_event_uncore components
* 2013-05-22 James Ralph — Libpfm4 update: Grab some IVB-EP updates.
* 2013-05-21 Heike McCraw — eliminate warnings of unused vars
* 2013-05-21 Heike McCraw — eliminate warnings of unused vars
* 2013-05-21 Heike McCraw — Problem with cleanup_eventset(): after destroying the CUDA eventset, update_control_state() is called again which operates on the already destroyed eventset.
* 2013-05-17 Heike McCraw — When adding multiple CUDA events to an event set, PAPI_add_event() error 14 (CUPTI_ERROR_NOT_COMPATIBLE) is being raised from the CUPTI library.
* 2013-05-17 Vince Weaver — perf_event: allow running with perf_event_paranoid is 2
* 2013-05-16 James Ralph — papi_events.csv Revert a little mishap in adding ivbep support
* 2013-05-16 Dan Terpstra — Add identifier for ivb_ep
* 2013-05-16 Vince Weaver — papi_libpfm4_events: allow specifying core/uncore/os_generic PMUs
* 2013-05-16 Vince Weaver — papi_libpfm4_events.c: only enable presets for component 0
* 2013-05-16 Vince Weaver — PAPI_get_component_index() was matching names improperly
* 2013-05-16 Vince Weaver — papi_hl.c : fix IPC calculation
* 2013-05-16 Vince Weaver — papi_libpfm4_events: code changes to allow multiple component access
* 2013-05-16 Vince Weaver — cpus: fix debug compile
* 2013-05-15 James Ralph — Libpfm4 update add Intel IvyBridge EP core PMU support
* 2013-05-15 Vince Weaver — cpus.c: Add reference count to cpu structure
* 2013-05-15 Vince Weaver — more cleanup of the cpus.c file
* 2013-05-15 Vince Weaver — cleanup cpus.h
* 2013-05-15 Vince Weaver — papi.c: add some extra debug messages
* 2013-05-15 Vince Weaver — Clean up cpus.c a bit
* 2013-05-15 Vince Weaver — ctests/perf_event_system_wide: much improved output
* 2013-05-15 James Ralph — Cuda component: Update library search path
* 2013-05-15 Vince Weaver — ctests/perf_event_system_wide: clean up the output a lot
* 2013-05-15 Vince Weaver — perf_event_system_wide: testing various DOMAIN and GRANULARITY settings
* 2013-05-14 James Ralph — CUDA component: Update description field
* 2013-05-14 Vince Weaver — Add AMD fam15h northbridge event to ctests/perf_event_uncore_lib.c
* 2013-05-13 Vince Weaver — perf_event component: update error returns
* 2013-05-13 Vince Weaver — Update the perf_event specific tests.
* 2013-05-08 Vince Weaver — Force the use of pthread_mutexes on ARM
* 2013-05-08 William Cohen — Commit 59d3d7584b2925bd05b4b5d0f4fe89666eb8494a removed the definition of mb().  mb() was defined as rmb().  This just corrects it back.
* 2013-05-06 James Ralph — NVML: Update wording for configure options.
* 2013-05-06 James Ralph — Infiniband component: use dlopen/dlsym for symbols
* 2013-05-02 Dan Terpstra — Add two command line switches: -i EVENTSTR includes only events whose names contain EVENTSTR; -x EVENTSTR excludes all events whose names contain EVENTSTR.
* 2013-05-01 Vince Weaver — ctests/perf_event_uncore: add IvyBridge support
* 2013-04-30 James Ralph — Examples: Missed two instances of %x printf formating.
* 2013-04-29 James Ralph — Address TRAC 174: Let printf do the formatting
* 2013-04-25 James Ralph — Rules.vmware: Use $(LDL) no -ldl
* 2013-04-26 Vince Weaver — papi_hl: Use PAPI_get_virt_usec() for process time
* 2013-04-25 Vince Weaver — ctests/perf_event_uncore: make more modular
* 2013-04-25 James Ralph — Rules.cuda:
* 2013-04-25 James Ralph — Cuda component enhancement.
* 2013-04-23 James Ralph — papi_internal.c: Print an eventcode in hex vs decimal.
* 2013-04-22 Dan Terpstra — The test for determining whether to run valgrind was backwards. Correcting that allow the run_test.sh script to stay the same and one just needs to define "VALGRIND=yes" (or any non-null string) to make run_test.sh use valgrind.
* 2013-04-19 Dan Terpstra — Restructure README files for components so that the file in the components directory doesn't document individual component details. Add README files to each component directory that requires further installation detail. Update RAPL instructions to capture how to enable reading the MSRs. These files are supposedly configured with Doxygen markup, but I don't think the master README ever got built. It probably should.
* 2013-04-17 James Ralph — cuda/tests/HelloWorld.cu: workaround a segfault.
* 2013-04-15 Heike McCraw — When creating two event sets - one for the CUDA and one for the CPU component  - the order of event set creation appears crucial. When the CPU event set has been created before the CUDA event set then PAPI_start() for the CUDA event set works fine. However, if the CUDA event set has been created before the CPU event set, then PAPI_start(CUDA_event_set) forces the CUDA control state to be updated one more time, even if the CUDA event set has not been modified. The CUDA control state function did not properly handle this case and hence cause PAPI_start() to fail. This has been fixed.
* 2013-04-15 Heike McCraw — linux-cuda.c
* 2013-03-28 James Ralph — run_tests.sh: further refine component test find
* 2013-03-25 James Ralph — run_tests.sh: File mode changes.
* 2013-03-18 Vince Weaver — perfctr: don't read in event table multiple times
* 2013-03-18 Vince Weaver — Fix segfault in perfctr.c
* 2013-03-15 James Ralph — Libpfm4 update.
* 2013-03-14 Heike McCraw — If a counter is not set to overflow (threshold==0; happens when PAPI_shutdown is called) then we do not want to rebuild the BGPM event set, even if the event set has been used previously and hence "applied or attached". Usually if an event set has been applied or attached prior to setting overflow, the BGPM event set needs to be deleted and recreated (which implies malloc() from within BGPM). Not so, though, if threshold is 0 which is the case when PAPI_shutdown is called.
* 2013-03-13 Heike McCraw — Overflow issue on BG/Q resolved. Overflow with multiple components worked; overflow with multiple components and multiple events did not work as supposed to.
* 2013-03-13 Heike McCraw — Added one more library to linker command.
* 2013-03-12 James Ralph — NVML component: build system work
* 2013-03-11 James Ralph — mx component: Modernize init routine.
* 2013-03-11 Heike McCraw — Resolve configure issues for CUDA component.
* 2013-03-07 Vince Weaver — Fix the build on Linux-SPARC
* 2013-03-07 Vince Weaver — More comprehensive sys_perf_open to PAPI error mappings
* 2013-03-07 Vince Weaver — Return proper error codes for sys_perf_event_open
* 2013-03-06 James Ralph — Coverity fixes:
* 2013-02-14 James Ralph — Add component tests' to the install-[all|tests] target.
* 2013-03-04 Dan Terpstra — Remove a stray debug statement. Thanks to Harald Servat for catching this.
* 2013-03-01 Dan Terpstra — Wrestled some horribly convoluted indexing into shape. The -u and -x options now print as expected (I think).
* 2013-01-31 James Ralph — linux-nvml.c: Fix type warning.
* 2013-01-29 Dan Terpstra — General doxygen cleanup: remove all "No known bugs" messages; correct and cleanup examples for PAPI_code_to_name and PAPI_name_to_code
* 2013-01-23 James Ralph — ia64 fixes.
* 2013-01-16 James Ralph — nvml component: cleanup a memory leak
* 2013-01-15 James Ralph — papi.h bump version number.
* 2013-01-15 James Ralph — Buildbot configure script.
* 2013-01-15 James Ralph — Turns out we are calling this 5.1.0.2
* 2013-01-15 Heike McCraw — Cleaned up compiler warning (gcc version 4.4.6)
* 2013-01-15 Heike McCraw — Cleaned up compiler warnings on BG/Q (gcc version 4.4.6 (BGQ-V1R1M2-120920))
* 2013-01-14 James Ralph — libpfm4: remove extraneous build artifacts.
* 2013-01-11 William Cohen — Clean up armv7 cortex a15 presets
* 2013-01-11 James Ralph — Prepare the repo for a 5.1 release.
* 2013-01-11 James Ralph — Update INSTALL.txt
* 2013-01-11 James Ralph — Remove TEST.TXT
* 2013-01-11 James Ralph — Update libpfm4.
* 2013-01-11 Philipp Thomas — Fix build on ia64
* 2013-01-11 Vince Weaver — Fix kernel warning in _papi_hwi_stop_timer()
* 2012-11-30 James Ralph — MIC power component
* 2013-01-08 James Ralph — configure: Add shortcut for mic support.
* 2013-01-07 William Cohen — Add preset events for ARM Cortex A15
* 2012-12-19 James Ralph — Doxygen: Turn off macro expansion for html config.
* 2012-12-14 James Ralph — Doxygen: Add a new API entry
* 2013-01-02 James Ralph — Doxygen: Cleanup generated man pages.
* 2013-01-02 James Ralph — Doxygen: Cleanup some of the markup
* 2012-12-07 James Ralph — Doxygen: Cleanup papi.c
* 2012-12-20 James Ralph — RAPL test code: Add flexibility to the test code.
* 2012-12-19 Tushar Mohan — Added events for seek statistics and support for intercepting lseek() calls.
* 2012-12-14 James Ralph — Rules.perfctr-pfm: pass CC in all cases.
* 2012-12-05 James Ralph — papi_internal.c: Refactor dublicated code in cleanup and free eventset.
* 2012-12-13 James Ralph — configure: Change fortran compiler search order.
* 2012-12-12 Vince Weaver — ivy_bridge: remove PAPI_HW_INT event
* 2012-12-10 James Ralph — Makefile.inc: Fix library link ordering.
* 2012-12-12 James Ralph — Makefile.in: export CC_COMMON_NAME
* 2012-12-11 James Ralph — Cleanup icc build
* 2012-12-10 James Ralph — configure: Attempt to better detect which C compiler we are using.
* 2012-12-10 James Ralph — Libpfm4 import.
* 2012-12-10 Dan Terpstra — Minor Coverity fixes. Thanks, Will Cohen.
* 2012-12-07 James Ralph — papi_user_events.c: Fix memory leak.
* 2012-12-07 Jens Lang — nvml component: fix detectDevices()
* 2012-12-07 Jens Lang — nvml component: add missing variable declaration
* 2012-12-06 Dan Terpstra — Fix warning messages issued by gfortran 4.6.x regarding loss of precision when casting REAL to INT. Thanks to Heike for identifying the proper intrinsics.
* 2012-12-06 Dan Terpstra — Add PAPI_get_eventset_component() to get the component index from an event set. This is symmetric with PAPI_get_event_component which extracts the information from an event. In response to a request from John Mellor-Crummey.
* 2012-12-06 Dan Terpstra — Fix a compiler warning about a possibly uninitialized return value.
* 2012-12-05 Dan Terpstra — Reformat the floating point output string to recognize that you can't cast the *value* of a long long to a double and expect to get the right answer; you need to cast the *pointer* to a double, then everything works.
* 2012-12-05 Dan Terpstra — Incorporated use of the new PAPI_add_named_event API. Restructured output to support formatted printing of built-in DATATYPEs: UINT64 prints as unsigned followed by (u); INT64 prints as signed; FP64 prints as float (but I don't like the default format); BIT64 prints a hex, prefixed by '0x'. Also if info.units is not empty, units are appended to output values. These features can be demo'd with the RAPL component.
* 2012-12-05 Dan Terpstra — Rearranged DATATYPE enums so INT64 is now default (0) value. Also added a BIT64 type for unspecified bitfields.
* 2012-12-04 Heike McCraw — Resolved multiple components conflict on BG/Q when overflow is enabled for multiple events from different components at the same time.
* 2012-12-04 Dan Terpstra — Add -x and -u options to papi_command_line to allow printing counter values in hexadecimal and unsigned formats.
* 2012-11-30 James Ralph — Cleanup unused variable warnings in user_events code.
* 2012-11-28 James Ralph — Cleanup the build under icc.
* 2012-11-28 Tushar Mohan — - added the ability to distinguish between writes to files and sockets.   (related to previous commit for reads). - fixed bug in appio_values_by_code, where hardwired constant was too low - added an event to count interrupted writes.
* 2012-11-27 Vince Weaver — Fix the perfctr build that was breaking due to missing CPU
* 2012-11-21 Vince Weaver — perf_events: get rid of "PAPI Error: Didn't close all events" error
* 2012-11-21 Vince Weaver — papi_command_line: fix error output
* 2012-11-21 Vince Weaver — Fix _papi_hwi_add_event to report errors back to user.
* 2012-11-21 Vince Weaver — Have perf_event return PAPI_EPERM rather than PAPI_ECNFLCT if the kernel itself returns EPERM
* 2012-11-21 Vince Weaver — Work around kernel issue with PERF_EVENT_IOC_REFRESH
* 2012-11-21 Tushar Mohan — - added support distinguishing between network and file I/O. - added events to measure statistics for sockets - updated README
* 2012-11-15 Vince Weaver — Update x86_cpuid_info code for KNC.
* 2012-11-08 Heike McCraw — There was more cleaning up necessary in order to get PAPI compiled on BG/P. It should work now with the recommended configure steps described in INSTALL.
* 2012-11-07 Vince Weaver — Make BGP use papi_events.csv
* 2012-11-07 Vince Weaver — Fix some linux-bgp build issues.
* 2012-11-07 James Ralph — Fix type warnings in perf_event_uncore test.
* 2012-11-07 James Ralph — Put a bandaid on the perf_event_uncore test.
* 2012-09-27 James Ralph — Mark some comments @htmlonly.
* 2012-11-07 William Cohen — Factor out duplicate install code from Rules.pfm4_pe
* 2012-10-30 Vince Weaver — Add PAPI_HW_INT event for IvyBridge
* 2012-10-26 Vince Weaver — MIC: update PAPI_FP_INS / PAPI_VEC_INS instruction
* 2012-10-25 Vince Weaver — perf_event: fix granularity bug
* 2012-10-25 Vince Weaver — Add perf_event_uncore ctest
* 2012-10-25 Vince Weaver — perf_event: add PAPI_DOM_SUPERVISOR to allowed perf_event domains
* 2012-10-25 Vince Weaver — perf_event enable granularity support
* 2012-10-18 Vince Weaver — Update the memory barriers
* 2012-10-08 Vince Weaver — perf_event: clarify an error message
* 2012-10-02 Vince Weaver — Update memory barries for Knights Corner
* 2012-10-01 Vince Weaver — Merge libpfm4 with Knights Corner Support
* 2012-10-01 Vince Weaver — Change "phi" to "knc" to match libpfm4 for Xeon Phi / Knights Corner support
* 2012-09-20 James Ralph — Update releasenotes and add a changelog for 5.0.1
* 2012-09-20 James Ralph — Rebuild the manpages for a 5.0.1 release.
* 2012-09-20 Vince Weaver — Add event support for MIC / Xeon-Phi
* 2012-09-19 James Ralph — Regenerate the version number for configure.
* 2012-09-19 James Ralph — Bump the version number for a 5.0.1 release.
* 2012-09-19 James Ralph — Update patching methodology for git.
* 2012-09-19 James Ralph — Create a .gitattributes file.
* 2012-09-19 James Ralph — Cleanup a botched libpfm4 update.
* 2012-09-19 James Ralph — Revert 'Revert "Remove the changelog generation script."'
* 2012-09-19 James Ralph — Import the latest libpfm4 sources.
* 2012-09-18 James Ralph — Revert "Remove the changelog generation script."
* 2012-09-18 James Ralph — Remove a trailing slash in libpfm4 pathing.
* 2012-09-17 Vince Weaver — rapl: add Ivy Bridge support
* 2012-09-17 Heike McCraw — Re-created the CUDA component configure script with an older version (GNU Autoconf 2.59) as requested by Steve Kaufmann.
* 2012-09-17 Heike McCraw — Minor changes to CUDA configure necessary to get it running smoothly on the Kepler architecture.
* 2012-09-17 James Ralph — Remove duplicate definition of PAPI_num_hwctrs.
* 2012-09-12 Vince Weaver — Revert "Fix memory leak in sowtware multiplex events (sw_multiplex.c)"
* 2012-09-12 Vince Weaver — papi.h: re-add PAPI_descr_error() support
* 2012-09-11 Vince Weaver — perf_events.c: fix pe_read debug message
* 2012-09-11 Vince Weaver — perf_events.c: better debug of pe_read()
* 2012-09-11 Vince Weaver — papi_internal.c: more consistent use of PAPI_NULL
* 2012-09-11 Vince Weaver — Fix preset bug
* 2012-09-11 Vince Weaver — debug: add messages to papi_internal.c
* 2012-09-11 Vince Weaver — debug: papi_preset.c
* 2012-09-11 Vince Weaver — debug messages: reduce messages from papi_libpfm4_events.c
* 2012-09-11 Vince Weaver — Debug cleanup: papi_preset.c
* 2012-09-11 Vince Weaver — Cleanup debug: libpfm4_events.c
* 2012-09-09 Dan Terpstra — Remove doubly defined events from the combined Sandy / Ivy Bridge event table to fix my previous commit.
* 2012-09-06 Dan Terpstra — Fix event name issue for Ivy Bridge that surfaced in a recent libpfm4 commit.
* 2012-09-04 Matthew Ryan Johnson — Fix memory leak in sowtware multiplex events (sw_multiplex.c)
* 2012-08-30 Matthew Ryan Johnson — Revert a typo in recent change
* 2012-08-30 Matthew Ryan Johnson — Update enum_cmp_event to check for if the component is disabled.
* 2012-08-29 Vince Weaver — configure: fix autodetect perfmon case
* 2012-08-29 Vince Weaver — Update libpfm4 included with papi to 4.3
* 2012-08-28 Vince Weaver — configure: don't check for libpfm if incdir specified
* 2012-08-28 Vince Weaver — perf_events: fix some PAPI Error: close of fd = -1 errors
* 2012-08-28 Vince Weaver — Add some spacing to the Rules.pfm4_pe
* 2012-08-28 Vince Weaver — Fix compiling with separate libpfm4
* 2012-08-28 James Ralph — Missed an instance of if() SUBDBG();
* 2012-08-27 James Ralph — Hack around debugging macros.
* 2012-08-27 James Ralph — Disappear the TOTAL Memory Leak message from the AIX run.
* 2012-08-27 James Ralph — Remove the changelog generation script.
* 2012-08-23 James Ralph — Typo in releasenotes.
* 2012-08-23 James Ralph — Update releasenotes for a pending 5.0 release.
* 2012-08-08 James Ralph — Changelog for PAPI5
* 2012-08-23 James Ralph — Rebuild the manpages for the PAPI 5.0 release.
* 2012-08-08 James Ralph — Bump version numbers in prep for a 5.0 release.
* 2012-08-08 James Ralph — Update release_procedure.txt
* 2012-04-17 James Ralph — Pickup the changelog from papi 4.4
* 2012-08-23 James Ralph — Take debug out of the with several components build test config.
* 2012-08-22 Dan Terpstra — Reversing a previous debug commit that replaced PAPI_FP_INS with PAPI_REF_CYC.
* 2012-08-22 Dan Terpstra — Move find_nonderived_event() from overflow_twoevents to test_utils and call it from overflow2 and overflow_single_event to insure that we're not trying to overflow on a derived event.
* 2012-08-22 James Ralph — Fix a memory leak reported on the aix power7 machine.
* 2012-08-22 Vince Weaver — perf_events: fix segfault if DEBUG is enabled
* 2012-08-21 John Nelson — Take #2. Changing len_trim function in ftests to last_char. This time, I respect 72 char line limit.
* 2012-08-21 Heike McCraw — overflow_force_software was the only test that used a different hard_tolerance value (0.25) than the other overflow tests (0.75). This caused trouble on Power7/AIX. Now we are using the same hard_tolerance value in all overflow tests.
* 2012-08-21 John Nelson — Revert "Changed name of function len_trim to last_char."
* 2012-08-21 John Nelson — Changed name of function len_trim to last_char.
* 2012-08-21 James Ralph — Cleanup cuda shutdown code.
* 2012-08-21 Matthew Ryan Johnson — Fix memory leaks in pthread multiplex tests.
* 2012-08-21 James Ralph — Remove an outdated comment about _papi_hwi_free_EventSet holding INTERNAL lock
* 2012-08-21 Vince Weaver — perf_events: fix issue where we dereference a pointer before NULL check.
* 2012-08-21 Dan Terpstra — Modify warning message to eliminate the word "error" Hopefully this will suppress it in buildbot outputs.
* 2012-08-21 James Ralph — Cleanup a few more warnings from the PAPI_perror change.
* 2012-08-21 James Ralph — Missed an instance of perror in the fortran code.
* 2012-08-21 James Ralph — Fix warning in ftest_util.F
* 2012-08-20 Vince Weaver — perf_events: Update multiplexing code
* 2012-08-20 Dan Terpstra — Change error reporting so FLOPS > 100% above theoretical FAIL and FLOPS > 25% above theoretical WARN.
* 2012-08-18 Vince Weaver — papi_internal: fix memory leak
* 2012-08-17 Vince Weaver — perf_events: more cleanups and comments
* 2012-08-17 Vince Weaver — perf_events: more cleanups and comments
* 2012-08-17 Vince Weaver — perf_events: disable kernel multiplexing before 2.6.34
* 2012-08-17 Vince Weaver — perf_events: more cleanup and comments
* 2012-08-17 Vince Weaver — perf_events: more cleanup and commenting
* 2012-08-17 Vince Weaver — perf_events: more cleanup and comments
* 2012-08-17 Vince Weaver — perf_events: more cleanups and comments
* 2012-08-17 Vince Weaver — perf_events: cleanup and comment the kernel bug workarounds
* 2012-08-17 Vince Weaver — perf_events: minor cleanups and new comments
* 2012-08-17 Vince Weaver — perf_events: fix some debug messages
* 2012-08-17 Vince Weaver — perf_events: enable new read_code
* 2012-08-17 James Ralph — Fix warning in all_events and all_native_events.
* 2012-08-16 Vince Weaver — perf_events: always enable kernel multiplexing
* 2012-08-16 Vince Weaver — Rewrite multiplex support.
* 2012-08-16 Vince Weaver — Fix strtest.F ftest
* 2012-08-16 Vince Weaver — Missing code to set num_error_chunks to 0
* 2012-08-02 James Ralph — Remove usage of _papi_hwi_err.
* 2012-08-10 Vince Weaver — perf_event: rename BRAINDEAD_MULTIPLEXING
* 2012-08-10 Vince Weaver — perf_event: remove context "cookie" field
* 2012-08-10 Vince Weaver — perf_event: move all event specific info to the control state
* 2012-08-09 Vince Weaver — perf_event: rename evt_t to perf_event_info_t
* 2012-08-09 Vince Weaver — perf_event: remove the superfluous per_event_info_t structure
* 2012-07-27 James Ralph — Change the calling signature of PAPI_perror.
* 2012-08-08 Vince Weaver — Fix warnings about PAPI_enum_cmp_event() return not being checked
* 2012-08-08 Vince Weaver — Fix unused value in papi_user_events.c
* 2012-08-08 Vince Weaver — remove unused PAPI_get_component_info() call in event_chooser
* 2012-08-07 Heike McCraw — tests/zero fails on Power7 due to PAPI_FP_INS Error of 50%. Preset definition has been redefined and test now passes.
* 2012-08-07 Tushar Mohan — We now intercept recv(). The support for recv() requires dynamic linkage. For static linkage, recv is not intercepted.
* 2012-08-06 Vince Weaver — perf_events: some whitespace cleanup and extra comments
* 2012-08-06 Vince Weaver — perf_events: MAX_READ was no longer being used, remove it
* 2012-08-06 Vince Weaver — perf_event event_id is actually 64-bit, so make our copy match
* 2012-08-06 Vince Weaver — Rename context_t pe_context_t in perf_events.c
* 2012-08-06 Vince Weaver — Rename control_state_t pe_control_state_t
* 2012-08-03 Dan Terpstra — Beef up error reporting.
* 2012-08-03 James Ralph — Have the cycle_ratio test skip if PAPI_REF_CYC event is not defined.
* 2012-08-02 Dan Terpstra — Removed all TESTS_QUIET blocks. They aren't needed because tests_quiet() overloads printf. We should probably remove TEST_QUIET blocks in ALL tests at some point for code clarity…
* 2012-08-02 Dan Terpstra — Fixed error reporting. The error computation was inside a TESTS_QUIET block and wasn't getting executed when run quietly. Thus this test always passed on buildbot, even when it didn't.
* 2012-08-02 Dan Terpstra — Fix typo in cycle_ratio make line.
* 2012-08-02 Heike McCraw — Setting number of multiplex counters back to 32 for AIX. Before it was set equal to number of max HW counters. This caused ctests/sdsc-mpx to fail.
* 2012-08-02 Heike McCraw — ctests/calibrate on Power7/AIX failed with a 50% error all the way through. Updated the preset FP_OPS with a more appropriate definition. Now the calibrate errors range from 0.0002 to 0.0011% for double and single precision
* 2012-08-02 Dan Terpstra — Modify calibrate test in two ways: 1. add a -f flag to suppress failures and allow test to run to completion; 2. change error detection to allow warnings above MAX_WARN and failures above MAX_FAIL. Currently set to 10% and 80% respectively. This allows speculative over counting to pass with warning rather than fail completely.
* 2012-08-02 Heike McCraw — LST_INS for Power7 was defined from 3 native events that cannot be counted together at the same time. Caused ctests/all_events to fail. Updated the preset with a more appropriate definition.
* 2012-08-02 Heike McCraw — L1_DCA for Power7 was defined from 3 native events that cannot be counted together at the same time. That caused ctests/tenth to fail. Updated the preset with a more appropriate definition.
* 2012-08-02 John Nelson — Forgot quotes to concatenate exclude lists on last commit. Added them in.
* 2012-08-01 John Nelson — icc does not like arithmetic on void pointers. Added cast to unsigned char* when arithmetic was being performed on void pointers in papi_internal and perf_events.
* 2012-08-01 Dan Terpstra — Modify tests that FAIL if PAPI_FP_OPS or PAPI_FP_INS not implemented. Now they will warn and continue. This is specifically to accommodate the brain-dead IvyBridge implementation.
* 2012-08-01 Heike McCraw — Re-writing of test_utils introduced new bugs that caused ctests/tenth to fail. test_events struct lists the same event twice (MASK_L1_DCW), hence PAPI_add_event() fails because it's forced to add the same preset twice.
* 2012-08-01 John Nelson — run_tests.sh was clobbering $EXCLUDE variable if $CUDA was defined. Changed to add entries from run_tests_exclude_cuda.txt to $EXCLUDE which should already contain entries from run_tests_exclude.txt instead of replacing the entries already contained.
* 2012-08-01 John Nelson — Added check in libpfm4/config.mk to check if using icc. If so, the -Wno-unused-parameter flag will no longer be used because icc does not provide it and provides no alternative.
* 2012-08-01 Dan Terpstra — fget() returns an int it should be treated as an int
* 2012-08-01 Dan Terpstra — Check return values of PAPI_get_cmp_opt() and calloc
* 2012-08-01 Dan Terpstra — Clean up test_print_event_header()
* 2012-08-01 Dan Terpstra — Eliminate deadcode from threads.h
* 2012-08-01 Dan Terpstra — Eliminate unused variable in ctests/all_native_events.c
* 2012-08-01 Dan Terpstra — A couple places in appio.c used the FD_SET() without initializing the variable. Coverity scan pointed out this issue.
* 2012-08-01 Dan Terpstra — A Coverity scan pointed out that read_msr() could potentially use an invalid value of fd for pread().  Need to check the value of fd before using it.
* 2012-08-01 Dan Terpstra — The arrays used for initialization were hard coded to 1024 packages. Want to avoid hard coding that so the day when machines with 1025 packages are available is a non-event.  Also changed the initialization code to avoid having the initialization be O((number of packages)^2) in time complexity.
* 2012-07-27 James Ralph — Fix the component name predending code.
* 2012-07-27 James Ralph — Fix a warning in cuda.
* 2012-07-26 Dan Terpstra — Add a test to compute nominal CPU MHz from real cycles and use PAPI_TOT_CYC and PAPI_REF_CYC to compute effective MHz. Warns if PAPI_REF_CYC is zero, which can happen on kernels < ~3.3.
* 2012-07-26 Dan Terpstra — Add PAPI_REF_CYC preset event. Define it as UNHALTED_REFERENCE_CYCLES for all Intel platforms on which this native event is supported.
* 2012-07-25 Dan Terpstra — Modify SandyBridge and IvyBridge tables: SandyBridge FP_OPS only counts scalars; SP_OPS and DP_OPS now count correctly, including SSE and AVX. IvyBridge can't count FP at all; adjustments made to eliminate event differences with SandyBridge.
* 2012-07-26 James Ralph — Fix the cuda component.
* 2012-07-25 Heike McCraw — Added 2 new preset definitions for BGQ. Note, these presets use the new feature where a generic event mask together with an ORed opcode string is used. This won't work until the new Q driver is released (currently scheduled for end of August).
* 2012-07-24 James Ralph — Enforce all our components to use the same naming.
* 2012-07-23 James Ralph — Prepend component .short_name to each event name.
* 2012-07-24 Vince Weaver — Fix multiplex2 test
* 2012-07-24 Vince Weaver — Add sanity check at component init time
* 2012-07-24 Vince Weaver — Rename PAPI_MAX_HWCTRS to PAPI_EVENTS_IN_DERIVED_EVENT
* 2012-07-24 Vince Weaver — Change EventInfoArrayLength to always return num_mpx_cntrs
* 2012-07-24 Vince Weaver — Fix sw_multiplex bug when max SW counters is less than max HW counters
* 2012-07-24 Vince Weaver — Remove PAPI_MPX_DEF_DEG
* 2012-07-24 Vince Weaver — Split NativeBits off of NativeInfoArray in EventSet
* 2012-07-24 Vince Weaver — Clean up EventSet creation
* 2012-07-24 Vince Weaver — Rename the multiplex files to be sw_multiplex
* 2012-07-24 Vince Weaver — Move some sw-multiplex specific terms out of papi_internal.h and into multiplex.h
* 2012-07-23 Heike McCraw — Added note that lmsensors component requires lmsensors version >=3.0.0
* 2012-07-23 Tushar Mohan — proper checking of return codes in response to tests using coverity
* 2012-07-23 Tushar Mohan — As component name in table has been changed from appio.c to appio, we now use appio in the tests.
* 2012-07-20 James Ralph — Add .short_name entries to each component.
* 2012-07-20 Vince Weaver — Fix use-after-free bug in perf_events.c
* 2012-07-20 Vince Weaver — Update perf_event.c rdpmc support
* 2012-07-20 Vince Weaver — Import current libpfm4 from libpfm4 git
* 2012-07-17 William Cohen — Reorder statements to ensure the fclose() are performed
* 2012-07-18 William Cohen — Ensure that load_user_event_table() frees files and memory on error
* 2012-07-17 William Cohen — Ensure that read_stealtime() closes the file in case of an error condition
* 2012-07-18 Vince Weaver — Fix warning in papi_libpfm4_events.c
* 2012-07-18 Vince Weaver — Remove unused variable in test_utils.c
* 2012-07-18 Vince Weaver — Add missing papi_vector.h include to linux-timer.c
* 2012-07-17 Vince Weaver — Fix perf_events.c warnings reported by ICC
* 2012-07-17 Vince Weaver — Fix perfctr-x86 build with debug enabled
* 2012-07-17 Vince Weaver — Attempt to fix linux-bgq compilation error.
* 2012-07-17 Heike McCraw — Made check for opcodes more robust.
* 2012-07-17 Vince Weaver — More cleanups of perf_events.c file
* 2012-07-17 Vince Weaver — Fix FreeBSD compile warnings
* 2012-07-17 Vince Weaver — Fix AIX build warnings
* 2012-07-17 Vince Weaver — Remove papi_vector.h include from papi_internal.h
* 2012-07-16 Dan Terpstra — Modify zero test to warm up processor before measuring events, and report timing errors as signed deviations. Modify test_utils add_two_events code to check for errors after adding nominally valid events. This is a more rigorous test than just counting available registers.
* 2012-07-16 Vince Weaver — Remove perf_events.h module header
* 2012-07-16 Vince Weaver — Remove perf_event SYNCHRONIZED_RESET code
* 2012-07-16 Vince Weaver — Remove papi_pe_allocate_registers
* 2012-07-16 Vince Weaver — Remove "include CPUCOMPONENT" from papi_internal.h
* 2012-07-16 Vince Weaver — Make perf_event libpfm4 only
* 2012-07-13 Vince Weaver — Add init time error messages to perf_event component
* 2012-07-13 Vince Weaver — Add perf_event rdpmc / fast_real_timer detection
* 2012-07-13 Vince Weaver — Read in paranoid info on perf_events
* 2012-07-13 Vince Weaver — Add proper perf_event detection
* 2012-07-13 Heike McCraw — Updated BGQ opcode stuff; cleaned up code.
* 2012-07-11 Vince Weaver — Minor documentation improvements
* 2012-07-10 James Ralph — Standardize component names.
* 2012-07-09 Vince Weaver — Minor cleanups to perf_events.c
* 2012-07-09 Vince Weaver — Change return value for .allocate_registers
* 2012-07-09 Dan Terpstra — Fixed the print_header routine to report an error message if counters are not found, instead of a negative counter number. Tested by forcing the return value negative; not by running on a Mac, where the error first appeared.
* 2012-07-09 Vince Weaver — Add remove_events test
* 2012-07-09 Vince Weaver — Clean up, rename, and comment _papi_hwi_remap_event_position
* 2012-07-09 Vince Weaver — Remove unused variable in papi.c
* 2012-07-09 Vince Weaver — Update commens in papi_internal.h
* 2012-07-09 Vince Weaver — Remove unused paramater from _papi_hwi_remap_event_position
* 2012-07-09 Vince Weaver — Clean up and comment add_native_events in papi_internal.c
* 2012-07-09 Vince Weaver — Fix coverity warning in papi_event_chooser
* 2012-07-09 James Ralph — RIP Java.
* 2012-07-09 Vince Weaver — Update cmpinfo->num_preset_events properly
* 2012-07-09 Vince Weaver — Have papi_component_avail report counter and event info
* 2012-07-09 Vince Weaver — Remove counter number from the testlib header.
* 2012-07-09 Vince Weaver — Improve OSX support
* 2012-07-08 Vince Weaver — Add Mac OSX support
* 2012-07-06 Heike McCraw — missed to delete a debug output.
* 2012-04-17 James Ralph — Release notes for the 4.4 release.
* 2012-07-06 James Ralph — Add a PAPI_disable_component_by_name entry point.
* 2012-07-06 Vince Weaver — Fix FreeBSD to work
* 2012-07-06 Vince Weaver — Fix FreeBSD build
* 2012-07-06 Heike McCraw — Added BGQ's opcode and generic event functionality to PAPI. For BGQ there are multiple ways to define presets. The naive way is to derive from multiple events. This eats up multiple counters and we lose sample capability as well as overflow capability. On the other side, some events come with multiple InstrGroup derived in the field. If that's the case we can use a generic event and opcodes to filter multiple groups in a single counter. This is not working properly yet due to a known error in BGPM. Bgpm_AddEvent() does not work properly when multiple generic events are added to an EventSet. The BGPM folks have been made aware of this issue, they confirmed the error, and they are currently working on a fix.
* 2012-07-06 Dan Terpstra — Make this script robust enough to handle any line ending, including CR (Mac), CRLF (Windows), and LF (Unix). It appears that google mail now automagically converts attached files to CRLF format.
* 2012-07-06 James Ralph — Fix a type warning in the UE code.
* 2012-07-06 Vince Weaver — Remove the MACROS file
* 2012-07-06 Vince Weaver — Move the clockcore.c file from ctests to testlib
* 2012-07-06 Vince Weaver — Make papi_lock.h changes for non Linux architectures
* 2012-07-05 Vince Weaver — Make the PAPI locks be tied to OS, not to CPU
* 2012-07-05 Vince Weaver — Fix spurious init_thread call in threads.c
* 2012-07-05 Vince Weaver — Replace SUBSTRATE with CPUCOMPONENT in build
* 2012-07-05 Vince Weaver — Move some common solaris code to solaris-common
* 2012-07-05 Vince Weaver — Merge solaris-memory.c and solaris-niagara2-memory.c
* 2012-07-05 Vince Weaver — Remove solaris-ultra/get_tick.S
* 2012-07-05 Vince Weaver — Remove papi_sys_headers.h
* 2012-07-05 Vince Weaver — Move move OS specific code into the new OSFILESSRC
* 2012-07-05 James Ralph — Re-run autoconf to pickup the substrate=>component change.
* 2012-07-05 Vince Weaver — Remove MEMSUBSTR
* 2012-07-05 Vince Weaver — Separate out MEMSUBSTR and make it per-OS
* 2012-07-05 James Ralph — RIP Windows, remove the windows support code.
* 2012-07-03 James Ralph — Change PAPI_strerror and PAPI_perror to behave more like thir POSIX namesakes.
* 2012-07-03 James Ralph — Default to building user events support.
* 2012-07-05 Vince Weaver — Move uses of PAPI_ESBSTR to PAPI_ECMP
* 2012-07-03 Vince Weaver — A few more substrate removals
* 2012-07-03 Vince Weaver — Fix bugs introduced by substrate -> component change
* 2012-07-03 Vince Weaver — More substrate -> component changes
* 2012-07-03 Vince Weaver — Rename "substrate" to "component"
* 2012-07-02 Vince Weaver — Minor documentation fixes
* 2012-06-30 Vince Weaver — Fix vmware component
* 2012-06-22 Vince Weaver — Fix libpfm4 ntv_event_to_info event_info_t on other components
* 2012-06-22 Vince Weaver — Properly fix libpfm4 ntv_event_to_info event_info_t event value
* 2012-06-22 Vince Weaver — Clean up overflow_allcounters code
* 2012-06-22 Vince Weaver — Fix libpfm4 ntv_event_to_info event_info_t event value
* 2012-06-22 Vince Weaver — Add PAPI_get_component_index() and PAPI_disable_component()
* 2012-06-22 Vince Weaver — Standardize component names to not end in .c
* 2012-06-22 James Ralph — Doctor configure to 'just work' if no substr is found.
* 2012-06-21 Vince Weaver — Fix cut-and-paste error in the vmware component Makefile
* 2012-06-21 Vince Weaver — Update papi_event_chooser to work with components
* 2012-06-21 Vince Weaver — Hook up .ntv_code_to_info on perf_event
* 2012-06-21 Vince Weaver — Enable support for showing extended umasks on perf_event
* 2012-06-21 Vince Weaver — Fix cut-and-paste error  in linux-coretemp.c that could lead to wrong size being copied
* 2012-06-21 Vince Weaver — Import most recent libpfm4 git
* 2012-06-21 Tushar Mohan — - Fixed tests verbosity by using TESTS_QUIET macro - Fixed Makefile to only include necessary tests for automatic builds   (skip blocking tests that read from stdin)
* 2012-06-21 Tushar Mohan — Added polling of read/write descriptor to check which operations would block.
* 2012-06-21 Vince Weaver — Add back PAPI_COMPONENT_INDEX() for backward compatability
* 2012-06-21 Vince Weaver — Add PAPI_get_event_component()
* 2012-06-20 Vince Weaver — Add component_type field to .cmp_info
* 2012-06-20 Vince Weaver — Another lmsensors build fix
* 2012-06-20 Vince Weaver — Update lmsensors component to actually compile.
* 2012-06-20 Vince Weaver — Update lmsensor component
* 2012-06-20 Vince Weaver — Add some extra debugging to _papi_hwi_get_native_event_info
* 2012-06-20 Vince Weaver — Remove cntr_groups from .cmp_info
* 2012-06-20 Vince Weaver — Cleanup and comment event_chooser code
* 2012-06-20 Vince Weaver — Cleanup and add comments to all_native_events.c
* 2012-06-20 Vince Weaver — Remove profile_ear from .cmp_info
* 2012-06-20 Vince Weaver — Add comments to the PAPI_sprofil code.
* 2012-06-20 Vince Weaver — Minor papi.c cleanups
* 2012-06-20 Vince Weaver — Remove opcode_match_width field from .cmp_info
* 2012-06-20 Vince Weaver — Remove cntr_OPCM_events field from .cmp_info
* 2012-06-20 Vince Weaver — Remove cntr_DEAR_events field from .cmp_info
* 2012-06-20 Vince Weaver — Remove cntr_IEAR_events field from .cmp_info
* 2012-06-20 Vince Weaver — Remove instr_address_range from .cmp_info
* 2012-06-20 Vince Weaver — Remove data_address_range field from .cmp_info
* 2012-06-19 Vince Weaver — Change Linux from using "struct siginfo" to "siginfo_t"
* 2012-06-18 James Ralph — Fix the perfctr-pfm build; for buildbot, mostly.
* 2012-06-17 Heike McCraw — Update BGQ presets
* 2012-06-17 Heike McCraw — Update bgpm components according to the papi5 changes
* 2012-06-17 Heike McCraw — Merging the BG/Q stuff from stable_4.2 to PAPI 5 did break it. It's corrected now; also predefined events are now working.)
* 2012-06-15 Heike McCraw — Merging the BG/Q stuff from stable_4.2 to PAPI 5 did break it. It's corrected now (almost); predefined events are not working yet.)
* 2012-06-15 Vince Weaver — Re-enable PAPI_event_name_to_code() optimization
* 2012-06-14 Vince Weaver — Remove the 16-component limit
* 2012-06-13 Vince Weaver — Fix for the PAPI_COMPONENT_MASK change
* 2012-06-13 Heike McCraw — Updating the Q substrate according to the PAPI 5 changes
* 2012-06-13 Vince Weaver — First steps of removing 16-component limit
* 2012-06-13 James Ralph — Exclude iozone helper scripts from run_tests.
* 2012-06-12 Heike McCraw — reverse test2-2
* 2012-06-12 Heike McCraw — test2
* 2012-06-12 Heike McCraw — reverse test
* 2012-06-12 Heike McCraw — test
* 2012-06-12 Heike Jagode — Configure does not work on BGQ due to missing subcomp feature. It worked for stable-4.2 but got lost in current git origin.
* 2012-06-12 Vince Weaver — Update hw_info_t CPU frequency reporting.
* 2012-06-11 Vince Weaver — Initial PAPI Ivy Bridge Support
* 2012-06-11 Vince Weaver — Merge in updated libpfm4 from git
* 2012-06-11 Vince Weaver — Revert "Import libpfm4 git snapshot"
* 2012-06-11 Vince Weaver — Import libpfm4 git snapshot
* 2012-06-11 James Ralph — Fix a libpfm3 example program for icc, local fix because libpfm3 is deprecated.
* 2012-06-06 James Ralph — The user events code had a call to exit, this was bad...
* 2012-06-04 James Ralph — Further the hack for testing for perf SW events.
* 2012-06-04 James Ralph — Cleanup nvml code a little.
* 2012-06-01 James Ralph — Rewrite and merge of the nVidia Management library component.
* 2012-05-23 Vince Weaver — At units to stealtime component
* 2012-05-23 Vince Weaver — Add units to stealtime
* 2012-05-23 Vince Weaver — Minor cleanup of RAPL code
* 2012-05-23 Vince Weaver — More vmware component fixes.
* 2012-05-23 Tushar Mohan — added code to intercept and time select() calls.
* 2012-05-22 Vince Weaver — Some more minor fixes to VMware component
* 2012-05-22 Vince Weaver — More vmware component fixups
* 2012-05-22 Vince Weaver — More cleanup of vmware component
* 2012-05-22 Vince Weaver — Make vmware test a bit more complete
* 2012-05-22 Vince Weaver — Add a test for the vmware component
* 2012-05-22 Vince Weaver — Clean up the vmware component.
* 2012-05-22 Vince Weaver — Add a stealtime component
* 2012-05-22 Tushar Mohan — Use a non-blocking select to determine which reads and writes would block
* 2012-05-19 Tushar Mohan — Interception of close() implemented. This allows us to correctly determine the number of currently open descriptors.
* 2012-05-17 Vince Weaver — Update libpfm4 to current git tree
* 2012-05-17 Vince Weaver — Skip rapl_overflow test if RAPL not available
* 2012-05-17 Vince Weaver — Fix some component warnings.
* 2012-05-17 Vince Weaver — Make build not stall if PAPI_EVENTS_CSV not set
* 2012-05-17 Vince Weaver — Fix typo in linux-timer.h
* 2012-04-14 Heike Jagode — Removed CVS stuff from Q code.
* 2012-04-14 Heike Jagode — Removed papi_events.csv parsing from Q code. (CVS stuff still needs to be taken care of.)
* 2012-04-12 Heike Jagode — Updated INSTALL notes for Q
* 2012-05-17 Vince Weaver — Added missing files for Q merge.
* 2012-04-12 Heike Jagode — Added PAPI support for Blue Gene/Q.
* 2012-05-14 Vince Weaver — Properly accumulate RAPL results
* 2012-05-14 Vince Weaver — Fix some warnings in rapl_overflow test
* 2012-05-14 Vince Weaver — Add rapl_overflow test
* 2012-05-14 Vince Weaver — Remove derived "uncore" values from rapl tool
* 2012-05-09 James Ralph — Bump the version number to 4.9.0.0
* 2012-05-09 Vince Weaver — Fix perfctr build
* 2012-05-08 Vince Weaver — Fix PAPI event enumeration inside of VMware
* 2012-05-07 Vince Weaver — Fix event enumeration on FreeBSD
* 2012-05-07 Vince Weaver — Add Virtual Machine detection support to FreeBSD
* 2012-05-07 Vince Weaver — Add x86_cacheinfo support to FreeBSD
* 2012-05-07 Vince Weaver — Re-enable predefined events on FreeBSD
* 2012-05-07 Vince Weaver — Modify FreeBSD to use _papi_load_preset_table
* 2012-05-07 Vince Weaver — Cleanup the freebsd code a bit.
* 2012-05-07 Vince Weaver — re-run autoconf for updated configure
* 2012-05-07 Vince Weaver — Make sure a proper dependency for papi_events_table.h exists
* 2012-05-07 Vince Weaver — Make papi_events_table.h build normally, not by configure.
* 2012-05-07 Vince Weaver — Another place papi_events_table.sh is called
* 2012-05-07 Vince Weaver — Make papi_events_table.sh take a command line argument
* 2012-05-07 Vince Weaver — Remove unused freebsd/memory.c file
* 2012-05-07 Vince Weaver — Make freebsd_events.csv a valid PAPI event file
* 2012-05-07 Vince Weaver — Fix FreeBSD build on head.
* 2012-05-01 George Neville-Neil — Update build system for FreeBSD
* 2012-05-01 George Neville-Neil — Fix various compiler warnings on FreeBSD
* 2012-05-01 George Neville-Neil — Enable new Westmere events on FreeBSD
* 2012-05-01 George Neville-Neil — Add Westmere event support for FreeBSD
* 2012-05-01 George Neville-Neil — Fix the inherit ctest to compile on FreeBSD
* 2012-05-01 Tushar Mohan — - change in appio component (appio.c): 	removed reference to .ntv_bits_to_info  as it doesn't exist 	in the PAPI component interface.
* 2012-04-27 James Ralph — Add the libpfm -Wno-override-init bandaid to the other rules files.
* 2012-04-27 James Ralph — Cleanup the perf events Rules files.
* 2012-04-26 Vince Weaver — Add memory barries for ia64
* 2012-04-24 Vince Weaver — Import libpfm4 git snapshot
* 2012-04-20 Vince Weaver — Some BG/P cleanups.
* 2012-04-20 Vince Weaver — Fix PAPI compile on BG/P
* 2012-04-19 James Ralph — Modified release_procedure.txt to push tags.
* 2012-04-18 James Ralph — Have clean remove the doxygen error file.
* 2012-04-18 James Ralph — Fix an error in the Doxygen config files.
* 2012-04-17 James Ralph — Update the release machinery for git.
* 2012-04-17 James Ralph — Cover up an instance of doxygen using full paths.
* 2012-04-13 Vince Weaver — Add missing update to libpfm3
* 2012-04-13 Vince Weaver — Fix max_multiplex case on perf_event/libpfm3
* 2012-04-12 Vince Weaver — Fix minor typo in a comment
* 2012-04-12 Vince Weaver — Fix potential fd leak
* 2012-04-12 Vince Weaver — Improve max_multiplex ctest
* 2012-04-11 Vince Weaver — Fix the perfmon substrate.
* 2012-04-09 James Ralph — Revert "Catch a few libpfm-3.y files up to libpfm-3.10."
* 2012-04-09 James Ralph — Catch a few libpfm-3.y files up to libpfm-3.10.
* 2012-04-04 Vince Weaver — Add the rapl_plot utility to the RAPL component.
* 2012-04-04 Vince Weaver — Check if a component is disabled at init time.
* 2012-04-04 Tushar Mohan — Added support to count reads that are interrupted or would block.
* 2012-04-03 Dan Terpstra — Change chmod flags for doxygen stuff from 755 to 775 to allow group write permissions.
* 2012-03-30 Vince Weaver — Add new PAPI_enum_cmp_event() function
* 2012-03-30 Vince Weaver — Place all compiled-in components in the _papi_hwd[] array.
* 2012-03-30 Vince Weaver — Documentation was referring to nonexistent "PAPI_enum_events()"
* 2012-03-30 Vince Weaver — Add support for reporting reason for failed component initialization.
* 2012-03-29 Vince Weaver — Add a SandyBridge RAPL (Running Average Power Level) Component
* 2012-03-26 Tushar Mohan — Added support for intercepting open calls.
* 2012-03-23 James Ralph — Fix the test case in configure at 0cea1848
* 2012-03-23 James Ralph — Doctor CFLAGS when testing for a gcc warning.
* 2012-03-22 James Ralph — Fix initialized field overwritten warning when building libpfm4 on some gcc versions.
* 2012-03-21 James Ralph — Delete an old comment.
* 2012-03-21 fike — testing gitpoller
* 2012-03-21 fike — test
* 2012-03-21 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 James Ralph — Move the user events code over to using the new preset event data structure.
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — test
* 2012-03-20 fike — testing both
* 2012-03-20 fike — testing
* 2012-03-20 fike — tedting
* 2012-03-20 fike — update and post-receive
* 2012-03-20 fike — update
* 2012-03-20 fike — update for email
* 2012-03-20 fike — using post-receive for buildbot
* 2012-03-20 fike — using update
* 2012-03-20 fike — trying update again
* 2012-03-20 fike — trying update
* 2012-03-20 fike — trying post-update
* 2012-03-20 fike — removed exec
* 2012-03-20 fike — trying exec
* 2012-03-20 fike — email and buildbot
* 2012-03-19 fike — email vs buildbot test
* 2012-03-19 fike — buildbot test
* 2012-03-19 fike — buildbot call test
* 2012-03-19 fike — perl sux
* 2012-03-19 fike — buildbot echo
* 2012-03-19 fike — perl
* 2012-03-19 fike — perl
* 2012-03-19 fike — l Please enter the commit message for your changes. Lines starting
* 2012-03-19 fike — perl calling buildbot
* 2012-03-19 fike — using perl,
* 2012-03-19 fike — testing shell script
* 2012-03-16 fike — added sleep
* 2012-03-16 fike — test for email still works
* 2012-03-16 fike — testi8ng
* 2012-03-16 fike — test
* 2012-03-16 fike — testing while loop
* 2012-03-16 fike —  ticks
* 2012-03-16 fike —  email vs buildbot
* 2012-03-16 fike — buildbot is called twice in the email hook
* 2012-03-16 fike — using & on buildbot call
* 2012-03-16 fike — buildbot embedded in email
* 2012-03-16 fike — testing email and buildbot
* 2012-03-16 fike — email now works, buildbot doesnt
* 2012-03-16 fike — email first, then buildbot
* 2012-03-16 fike — test email hook
* 2012-03-16 fike — t both email and buildbot
* 2012-03-16 fike — email and buildbot called from same script
* 2012-03-16 fike — test both buildbot and email post commit hooks
* 2012-03-16 fike — script 1, 2, 3 test
* 2012-03-16 fike — google help
* 2012-03-16 fike — rev tests
* 2012-03-16 fike — echo tests
* 2012-03-16 fike — test
* 2012-03-16 fike — testing params passed by hook
* 2012-03-16 fike — echo test
* 2012-03-16 James Ralph — One more check of the git hook.
* 2012-03-16 fike — testing buildbot hardcoded values
* 2012-03-16 fike — buildbot hook test
* 2012-03-16 fike — buildbot commit hook test
* 2012-03-16 fike — testing buildbot trigger
* 2012-03-16 James Ralph — Testing the buildbot submit change hook in git.
* 2012-03-14 James Ralph — test
* 2012-03-14 Vince Weaver — Fix a small memory leak.
* 2012-03-13 Vince Weaver — Remove last MY_VECTOR usage.
* 2012-03-13 Vince Weaver — Clean up the papi_libpfm3_events.c code.
* 2012-03-13 Vince Weaver — Fix some libpfm3 warnings.
* 2012-03-13 Vince Weaver — Fix a few compiler warnings in the tests.
* 2012-03-13 Vince Weaver — Fix another linux-timer.c compile problem.
* 2012-03-12 Vince Weaver — Fix typo in the linux-timer.h header
* 2012-03-12 Vince Weaver — Fix timer compile on Power machines
* 2012-03-12 Vince Weaver — Another fix for non-POSIX timers
* 2012-03-12 Vince Weaver — Fix a warning in the libpfm3 code.
* 2012-03-12 Vince Weaver — Fix build when not using POSIX timers
* 2012-03-09 Vince Weaver — Add Linux posix gettime() nanosecond functions
* 2012-03-09 Vince Weaver — Add ->get_virt_nsec() and ->get_real_nsec() OS vectors
* 2012-03-09 Vince Weaver — Clean up ->get_virt_usec()
* 2012-03-09 Vince Weaver — Cleanup the Linux timer code.
* 2012-03-09 Vince Weaver — Change a strcpy() to strncpy() just to be a bit safer.
* 2012-03-09 Vince Weaver — Fix buffer overrun in lmsensors component
* 2012-03-09 Vince Weaver — Update to current git libpfm4 snapshot
* 2012-03-09 Vince Weaver — Fix segfault on AIX
* 2012-03-08 Vince Weaver — Make "native_avail -d" report units if available
* 2012-03-08 Vince Weaver — Add new ntv_code_to_info vector
* 2012-03-08 Vince Weaver — Add new event_info fields
* 2012-03-08 Vince Weaver — Restore fields to event_info structure
* 2012-03-08 Vince Weaver — Remove ->ntv_bits_to_info vector from component interface
* 2012-03-08 Vince Weaver — Remove invert and edge_detect fields from component info
* 2012-03-08 Vince Weaver — We had the PAPI_VEC_INS preset wrong on amd fam12h llano
* 2012-03-08 Vince Weaver — Fix preset adding code to be more robust.
* 2012-03-08 James Ralph — Remove the hw_info field from add_two_events calls.
* 2012-03-08 Vince Weaver — Fix segfault seen on an AMD fusion machine
* 2012-03-07 James Ralph — Fix a compile error on aix.
* 2012-03-06 Vince Weaver — Revert "Make libpfm4 a "git submodule""
* 2012-03-06 Dan Terpstra — Add support for {add, remove, query}_named to Fortran interface; add zero named.F test case; modify ftests Makefile to support "all" tag.
* 2012-03-06 Dan Terpstra — Modify configure to define the default FTEST_TARGETS as "all"
* 2012-03-06 Vince Weaver — Make libpfm4 a "git submodule"
* 2012-03-06 Matthew R. Johnson (Matt) — Changed tri8ggering environment variable to PAPI_VMWARE_PSEUDOPERFORMANCE per Vince's earlier email. This should complete all the VMware component changes.
* 2012-03-05 Vince Weaver — Add missing MISCSRCS line to Makefile.inc
* 2012-02-01 tmohan — updated these tests to print timing information
* 2012-02-01 tmohan — Added support for timing I/O calls. Updated tests and README.
* 2012-01-31 tmohan — added the latest stable iozone to the appio tests.
* 2012-01-31 tmohan — added a hook to run the appio test for iozone.
* 2012-01-21 tmohan — Removed stray 'net' references. All remaining references are only for the purpose of giving credit. Updated change log.
* 2012-01-20 tmohan — - general cleanup - improved tests to be quiet and be conform to other PAPI tests - replaced hardwire constants in appio.c with symbolic ones - tests will now write to /dev/null to avoid filling the terminal   screen with useless text - more comments added - @author added to files - updated README
* 2012-01-18 tmohan — - Added support to measure bytes/calls/eof/short calls for read/write calls. - Interception of read/write and fread/fwrite calls. - Works for static and dynamic linkage (without need for LD_PRELOAD) - Tested OK on 32-bit i686 Linux 2.6.38.
* 2011-12-08 tmohan — Trial commit. Just making sure, I'm able to write to the repository.
* 2011-12-03 Philip Mucci — *** empty log message ***
* 2011-12-03 Philip Mucci — file appio_values_by_name.c was added on branch appio on 2011-12-03 05:22:06 +0000
* 2011-12-03 Philip Mucci — file appio_values_by_code.c was added on branch appio on 2011-12-03 05:22:06 +0000
* 2011-12-03 Philip Mucci — file appio_list_events.c was added on branch appio on 2011-12-03 05:22:06 +0000
* 2011-12-03 Philip Mucci — file Makefile was added on branch appio on 2011-12-03 05:22:06 +0000
* 2012-03-05 Matthew R. Johnson (Matt) — Remove old configuration parameters from vmware/configure
* 2012-03-02 Vince Weaver — Add a new max_multiplex test
* 2012-03-02 Vince Weaver — Fix issue when using more than 32 multiplexed events on perf_event
* 2012-03-02 Vince Weaver — Remove the acpi.c file from ctests
* 2012-03-02 Matthew R. Johnson (Matt) — Removed all old references to #define VMWARE_PSEUDO_PPERF and switched over to getenv
* 2012-03-01 Dan Terpstra — Three new APIs: PAPI_query_named_event PAPI_add_named_event PAPI_remove_named_event  and a new test: zero_named Still to do: maybe test named native events and support Fortran
* 2012-03-01 Dan Terpstra — First pass implementation of {add, remove, query}_named_event
* 2012-03-01 Matthew R. Johnson (Matt) — Add functionality to getenv selectors
* 2012-03-01 Vince Weaver — Fix possible race in _papi_hwi_gather_all_thrspec_data
* 2012-03-01 Vince Weaver — Add some locking in _papi_hwi_shutdown_global_internal
* 2012-03-01 James Ralph — Cleanup the oxygen markup for the utilities.
* 2012-03-01 James Ralph — Missed a recursive tag for the html config file.
* 2012-03-01 Vince Weaver — Fix segfaults in tests on AMD machines
* 2012-03-01 James Ralph — Touch 'virtual_vendor_name' to cleanup a warning on bluegrass.
* 2012-02-29 Vince Weaver — Merge the contents of papi_libpfm_presets.c into papi_preset.c
* 2012-02-29 Vince Weaver — Fix Fortran breakage after the preset event changes
* 2012-02-29 Vince Weaver — Simplify papi_libpfm_presets.c
* 2012-02-29 Vince Weaver — Make the internal preset_info match the one exported by papi.h
* 2012-02-29 Vince Weaver — Merge the 4 separate preset structs into one.
* 2012-02-29 James [nobody] Ralph — Testing git notification script.
* 2012-02-29 fike —  testing committername
* 2012-02-29 fike — committername test
* 2012-02-28 Dan Terpstra — Removing remaining vestiges of references to bipartite routines. Now the only references are in papi_bipartite.h, perfctr-x86.c and winpmc-p3.c.
* 2012-02-28 James [nobody] Ralph — This is another test, hi Morgan, Bryan et al.
* 2012-02-28 fike — testing hell
* 2012-02-28 Dan Terpstra — These changes implement the bipartite allocation routine as a header file to be included in whatever cpu component needs it. Right now, that's just perfecter-x86 and windows. Both components have been modified and perfecter-86 compiles cleanly. Neither has been tested since I don't have access to a test bed.
* 2012-02-28 James Ralph — This is just a test; hi Bryan =)
* 2012-02-28 Vince Weaver — Merge the hwi_dev_notes structure into hwi_preset_data
* 2012-02-28 Matthew R. Johnson (Matt) — add getenv
* 2012-02-28 James Ralph — This is just a test.
* 2012-02-28 Dan Terpstra — Merge bipartite routine into perfecter-x86 component, since this is effectively the only place it is used.
* 2012-02-28 Vince Weaver — Remove a reference to PAPI_set_event_info() which was removed for PAPI 4
* 2012-02-28 Vince Weaver — Convert PAPI_event_info_t to separate preset event info
* 2012-02-28 Dan Terpstra — Move bipartite stuff to perfctr_x86 since that's really the only place it's currently used.
* 2012-02-28 Matthew R. Johnson (Matt) — Add env_var definition to vmware.h
* 2012-02-28 Matthew R. Johnson (Matt) — Remove all unneeded cases
* 2012-02-28 Dan Terpstra — Remove more unused references to .bpt_ routines in preparation for refactoring.
* 2012-02-28 Matthew R. Johnson (Matt) — Remove uneeded defines from vmware.h header
* 2012-02-28 Dan Terpstra — Remove unused references to .bpt_ routines in preparation for refactoring.
* 2012-02-27 Vince Weaver — Have separate concept of "compiled-in" versus "active" components
* 2012-02-27 Vince Weaver — Split the contents of papi_data.c to various other files.
* 2012-02-27 Vince Weaver — Remove the BGL and BGP specific pre-defined events.
* 2012-02-27 Vince Weaver — Add names and descriptions for components.
* 2012-02-27 Vince Weaver — Add names and descriptions to all of the CPU substrates.
* 2012-02-27 Vince Weaver — Add new "description" and "short_name" fields to .cmp_info structure
* 2012-02-27 James Ralph — Refactor the doxygen config files.
* 2012-02-27 Vince Weaver — Split papi_data.c into two parts
* 2012-02-27 Vince Weaver — Remove unncessary extern declarations from solaris-ultra.c.
* 2012-02-27 Vince Weaver — Remove unncessary extern declarations from sys_perf_event_open.c
* 2012-02-27 James Ralph — Create a common config file for doxygen.
* 2012-02-27 Vince Weaver — The vector pre-definition should be in the .c file, not the .h file
* 2012-02-27 Vince Weaver — Remove unnecessary extern declarations in perf_events.c
* 2012-02-27 Vince Weaver — Remove unnecessary extern declarations in perfmon.c
* 2012-02-27 Vince Weaver — Remove unnecessary extern declarations from papi_preset.c
* 2012-02-27 Vince Weaver — Remove extraneous extern declarations from papi_libpfm_presets.c
* 2012-02-27 Vince Weaver — remove extraneous extern declarations from extras.c
* 2012-02-27 Vince Weaver — Remove unncessary extern declarations from aix.c
* 2012-02-27 Vince Weaver — Remove unncessary extern declarations in papi_internal.c
* 2012-02-27 Vince Weaver — remove unnecessary extern definitions from papi.c
* 2012-02-24 Vince Weaver — Add a --with-pthread-mutexes option to enable using pthread mutexes rather than PAPI custom locks
* 2012-02-24 Vince Weaver — Fix broken Pentium 4 Prescott support
* 2012-02-24 Vince Weaver — Fix build on POWER, broken by the virtualization change.
* 2012-02-24 Vince Weaver — Fix some warnings that have appeared due to recent changes.
* 2012-02-24 Vince Weaver — Clean up the Linux lock files
* 2012-02-23 Vince Weaver — Remove _papi_cleanup_all_memory define from papi_memory.h
* 2012-02-23 Vince Weaver — Fix some missing includes found after the header cleanup.
* 2012-02-23 Vince Weaver — Header file cleanup
* 2012-02-23 Vince Weaver — Clean up the papi_vector code.
* 2012-02-23 Vince Weaver — Fix a missing "return 1" which meant that the virtualization flag wasn't being set right.
* 2012-02-23 Vince Weaver — Remove the ->add_prog_event function vector
* 2012-02-23 Vince Weaver — Reduce the usage of MY_VECTOR whenever possible.
* 2012-02-23 Vince Weaver — Missed removing any-null.h during the any-null removal.
* 2012-02-23 Vince Weaver — Somehow missed an include during the virtualization addition.
* 2012-02-23 James Ralph — Removes the last of the binary files from perfctr2.6.x
* 2012-02-23 Vince Weaver — Add support for reporting if we are running in a virtualized environment to the PAPI_hw_info_t structure.
* 2012-02-22 Vince Weaver — Remove the freq.c file as nothing seemed to be using it.
* 2012-02-22 Vince Weaver — Made a stupid typo when converting perfctr to call libpfm functions with the component id.
* 2012-02-22 Vince Weaver — When updating the preset code to take a component index I missed a few callers.
* 2012-02-22 Vince Weaver — Remove any-null component
* 2012-02-22 Vince Weaver — Remove the any-null component.
* 2012-02-22 Dan Terpstra — Saving another version of the FAQ after adding a git section, and removing several obsolete sections. These questions still need detailed review for relevance and timeliness.
* 2012-02-22 Vince Weaver — Fix overflow_allcounters which was making assumptions about component 0 existing.
* 2012-02-22 Vince Weaver — Make the hwinfo test not bail out if no counters are available.
* 2012-02-22 Vince Weaver — Make sure the memory ctest runs even if no components are available.
* 2012-02-22 Vince Weaver — Make sure the system info init happens at os init time.
* 2012-02-22 Vince Weaver — Make sure that _papi_hwi_assign_eventset() does the right thing if no components are available.
* 2012-02-22 Vince Weaver — The api test would fail in the no cpu component case.
* 2012-02-22 Vince Weaver — Fix code that was depending on _papi_hwd[0] existing.
* 2012-02-22 Vince Weaver — Fix up papi_vector to get rid of some warnings introduced on AIX.
* 2012-02-22 Vince Weaver — Fix two last substrates where I missed some fields in the OS structure conversion.
* 2012-02-22 Vince Weaver — Missed a cmp_info field in perfmon.c
* 2012-02-22 Dan Terpstra — Saving the latest version of the FAQ before undertaking major revisions.
* 2012-02-22 Vince Weaver — Fix the perfctr code to compile if configured with    --with-virtualtimer=perfctr
* 2012-02-22 Vince Weaver — Missed two OS vector calls in the perfctr code during the conversion.
* 2012-02-22 Heike Jagode — Removed one of the two instances of MISCOBJS listed in Makefile.inc.
* 2012-02-21 Vince Weaver — Remove now-unused OS vectors from the main papi vector table.
* 2012-02-21 Vince Weaver — Convert PAPI to use the _papi_os_vector for the operating-system specific function vectors.
* 2012-02-21 Vince Weaver — Add new _papi_os_vector structure to hold operating-system specific function vectors.
* 2012-02-21 Vince Weaver — Missed removing a field from the subinfo ctest.
* 2012-02-21 Vince Weaver — Remove fields now in PAPI_os_info_t from the component_info_t struct.
* 2012-02-21 Vince Weaver — Remove fields now in PAPI_os_info_t from the example component.
* 2012-02-21 Vince Weaver — Modify all the substrates to use _papi_os_info. instead of _papi_hwd[0]->cmp_info for the values moved to the OS struct
* 2012-02-21 Vince Weaver — Add padding for future expansion to PAPI_os_info_t
* 2012-02-21 Vince Weaver — Add new PAPI_os_info_t structure to papi_internal.h
* 2012-02-21 Vince Weaver — Modify multiplex_cost to properly use the API_get_opt() interface to get itimer data, rather than directly accessing the fields from the cmp_info structure.
* 2012-02-21 Vince Weaver — subinfo was printing itimer data from the cmpinfo structure.
* 2012-02-21 Matthew R. Johnson (Matt) — Clean up the VMware Header a bit
* 2012-02-20 fike — testing error 22
* 2012-02-20 Dan Terpstra — This is a test.
* 2012-02-20 fike — testing author email
* 2012-02-18 fike — testing mail from
* 2012-02-17 Vince Weaver — The git conversion reset all of the CVS $Id$ lines to just $Id$
* 2012-02-17 James Ralph — Remove a few binary files in perfctr-2.6.x
* 2012-02-17 James Ralph — More cleanups from the migration, latest version of libpfm-3.y perfctr-2.[6,7]
* 2012-02-17 James Ralph — Testing SourceTree gui
* 2012-02-17 James Ralph — Explicitly state that 3.7 was the last version of PAPI with good windows support.
* 2012-02-17 fike — testing email via commit/push
* 2012-02-17 Heike Jagode — Modified CUDA component so that a PAPI version - that was configured with CUDA - will successfully build on a machine that does not have GPUs.
* 2012-02-16 Vince Weaver — Add a .gitignore file with the files that PAPI autogenerates.
* 2012-02-15 James Ralph — Repository works, remove test.txt file.
* 2012-02-15 fike — test 1
* 2012-02-15 James Ralph — The git cvsimport didn't get the latest version of the libpfm4 import. This should be the versions as were in cvs now.
* 2012-02-14 Dan Terpstra — Added note on Jose Pedro Oliveira's contribution to the rewrite of the net component. Thanks, Jose!
* 2012-02-13 Dan Terpstra — Update Change Log and release notes for 421 release.
* 2012-02-13 Dan Terpstra — Repairing more coverity warnings.
* 2012-02-11 James Ralph — Missed an instance of CPUs yesterday.
* 2012-02-11 Vince Weaver — This changes fixes two race conditions that are probably the cause of the pthrtough double-free error.
* 2012-02-11 Vince Weaver — ix one more case of "CPU's" in the print header code.
* 2012-02-10 Vince Weaver — Fix one more case of "CPU's" in the print header code.
* 2012-02-10 James Ralph — take infiniband out of the buildbot test.
* 2012-02-10 Dan Terpstra — Fix coverity errors reported by Will Cohen.
* 2012-02-10 James Ralph — Address Redhat bug 785975. The plural of CPU appears to be CPUs
* 2012-02-10 James Ralph — Patch to cleanup dependencies, allowing for parallel makes. Patch due to Will Cohen from redhat
* 2012-02-09 James Ralph — Add infiniband and mx component to buildbot component tests.
* 2012-02-09 Dan Terpstra — Apply patch suggested by Will Cohen to check for system return values.
* 2012-02-09 Heike Jagode — Added missing string header
* 2012-02-08 Dan Terpstra — Final documentation changes for PAPI 4.2.1.
* 2012-02-08 Dan Terpstra — update man pages one more time for 4.2.1 release
* 2012-02-08 James Ralph — Make sure generated html has papi group id.
* 2012-02-07 James Ralph — Fix the @file matching multiple files warning.
* 2012-02-07 James Ralph — Cleanup doxygen errors.
* 2012-02-07 James Ralph — Typo introduced by the last commit.
* 2012-02-07 James Ralph — Exclude linux-bgp.c from doxygen.
* 2012-02-07 James Ralph — Make sure the component README file gets included in doxygen.
* 2012-02-07 James Ralph — Cleanup doxygen warnings in freebsd coretemp component.
* 2012-02-07 James Ralph — Cleanup some doxygen warnings related to the groupings.
* 2012-02-07 Vince Weaver — fix doxygen warning in the example component
* 2012-02-07 James Ralph — Remove some cruft from doxygen config file.
* 2012-02-07 Heike Jagode — Cleaned up some doxygen issues
* 2012-02-07 Heike Jagode — Removed long forgotten debug outputs
* 2012-02-07 Vince Weaver — Fix minor doxygen typos.
* 2012-02-07 Matt Johnson — Add params for doxygen
* 2012-02-07 Dan Terpstra — update man pages
* 2012-02-06 James Ralph — Fix a typo in a doxygen config file.
* 2012-02-03 James Ralph — Rework the doxygen configuration files.
* 2012-02-03 Dan Terpstra — Update for the impending release.
* 2012-02-03 Dan Terpstra — Updates for the impending release.
* 2012-02-02 Dan Terpstra — Minor tweaks for doxygen errors
* 2012-02-02 Dan Terpstra — Minor tweaks for doxygen errors
* 2012-02-01 Dan Terpstra — Fixed configure error message and rules link error for shared object linking. Thanks Will Cohen.
* 2012-02-01 Dan Terpstra — Correct pathing
* 2012-02-01 Philip Mucci — One minor tiny fix to check for PAPI_ENOEVNT when testing PAPI_flops. If PAPI_FP_OPS does not exist on the processor (like many of em), then this tests fails.
* 2012-02-01 Philip Mucci — Increase acceptance criteria for cycles.
* 2012-01-31 Dan Terpstra — Update version number to 4.2.1 in preparation for release.
* 2012-01-31 James Ralph — Correct a warning on 32bit builds about casting caddr_t to (long long)
* 2012-01-30 James Ralph — Add the correct path for doxygen on ICL machines.
* 2012-01-30 Vince Weaver — Modify Intel Sandybridge PAPI_FP_OPS and PAPI_FP_INS events to not count x87 fp instructions.
* 2012-01-30 Vince Weaver — Some really minor cleanups to the lustre and mx components.
* 2012-01-28 Vince Weaver — Update example component
* 2012-01-27 James Ralph — Minor cleanups for user events.
* 2012-01-27 Vince Weaver — Fix "conflicts" in git import of libpfm4.
* 2012-01-27 Vince Weaver — Initial revision
* 2012-01-26 James Ralph — Escape the include directives in the documentation.
* 2012-01-26 Matt Johnson — Adding vmware to component README
* 2012-01-26 Matt Johnson — merge vmware branch to head
* 2012-01-26 James Ralph — Remove acpi from the buildbot configure script.
* 2012-01-26 Vince Weaver — Re-write of the MX component
* 2012-01-25 Vince Weaver — Remove the ACPI component.
* 2012-01-23 Dan Terpstra — Restored Phil's changes that I inadvertently clobbered with my last commit :(
* 2012-01-23 Dan Terpstra — Remove a warning about an uninitialized variable.
* 2012-01-23 Vince Weaver — Update the Doxygen comments on these utilities to have the command line options listed in a list like the other utils.
* 2012-01-23 Philip Mucci — More improvements to the read path for multiplexed counters. Now the case for bad kernel behavior is built in, and is not required with a #define.
* 2012-01-23 Vince Weaver — Major re-write of the papi_xml_event_info program. + Remove event code numbers, as they are not stable run-to-run + Add some Doxygen comments + Remove some wrong assumptions that could cause potential buffer overflows + Improve usage information
* 2012-01-20 Vince Weaver — Finish the re-write of the lustre component.
* 2012-01-20 Vince Weaver — Update the component initialization code so that it can handle a PAPI ERROR return gracefully.  Previously there was no way to indicate initialization failure besides just setting num_native_events to 0.
* 2012-01-19 Vince Weaver — First pass at cleaning up the lustre component.
* 2012-01-11 Vince Weaver — Add AMD fam12h support to the events file.  Right now it is just an alias to the similar fam10h event list; this can be split out if necessary once we find a tester with the hardware.
* 2012-01-11 Vince Weaver — Fix "merge" conflicts with libpfm4 merge.
* 2012-01-11 Vince Weaver — Initial revision
* 2012-01-11 Vince Weaver — Properly use the  pfm_get_event_next() iterator to find next event.
* 2012-01-11 Vince Weaver — Update the coreduo (not core2) events.  Most notably the FP events were wrong.
* 2012-01-05 Vince Weaver — Make the api test actually test PAPI_flops() as it claims to do, rather than PAPI_flips().
* 2012-01-05 Vince Weaver — Fix some copy-and-paste documentation remnants in the papi_hl.c file, mostly where it said FLIPS where it meant FLOPS.
* 2012-01-04 Vince Weaver — Update papi_native_avail to *not* print the event codes, as these are not guaranteed to be stable from run to run.
* 2012-01-04 James Ralph — Respect a FORCED option in configure.
* 2011-12-22 James Ralph — Remove perfmon.h from MISCHDRS.
* 2011-12-20 Philip Mucci — Merry Christmas ARM users.
* 2011-12-15 Dan Terpstra — Change PAPI_PERFMON_EVENT_FILE environment variable name to PAPI_CSV_EVENT_FILE since it's not just for perfmon anymore.
* 2011-12-15 James Ralph — Open mouth, insert foot; fix perfctr configure by not testing a library we have not built yet.
* 2011-12-14 James Ralph — Missed one more place where we tested perfctr != "no"
* 2011-12-14 James Ralph — Fix a typo in the perfctr section; it was causing a machine to default to perfctr when it had no performance interface. ( a centos vm image with a 2.6.18 kernel )
* 2011-12-08 Heike Jagode — Added auto-detection of CUDA version to PAPI CUDA Component. Reason is, the interface has changed between CUDA/CUPTI 4.0 and 4.1. PAPI now supports both CUDA versions without any exposure to the users. Configure step is unchanged and no additional knowledge of which CUDA version is installed is required.
* 2011-12-03 Philip Mucci — *** empty log message ***
* 2011-11-25 Vince Weaver — Fix compilation warning if you specify --with-walltime=gettimeofday
* 2011-11-25 Vince Weaver — Fix the build on Linux systems using mmtimer
* 2011-11-25 Vince Weaver — Update the linux MHz detection code to use bogoMIPS when there is no MHz field available in /proc/cpuinfo.
* 2011-11-23 James Ralph — Fix compile errors in a debug message. (pathname didn't exist but we are working on NET_PROC_FILE)
* 2011-11-22 Vince Weaver — Change the ping command in the net tests to not use &> to redirect to NULL.
* 2011-11-22 Vince Weaver — Fix slight bug in the net component, where a memset() had the wrong arguments.  This made for weird results in the case where we start/stop quickly enough that we return the initial data.
* 2011-11-22 Vince Weaver — Replace net component with updated version written by    Jose Pedro Oliveira
* 2011-11-16 James Ralph — Fix the exclude libpfm/perfctr config.
* 2011-11-10 Philip Mucci — Only scale when running != enabled.
* 2011-11-10 Philip Mucci — Further tuneups for mpx'ing.
* 2011-11-09 Heike Jagode — For the CUDA Component, PAPI_read() now accumulates event values. This has to be explicitly done in PAPI because CUPTI automatically resets all counter values to 0 after a read. (PAPI_start()/stop() continues to reset the values to 0)
* 2011-11-09 Philip Mucci — Last of the multiplex fixes to perf events. The root of all evil was this:
* 2011-11-09 Philip Mucci — Made sure that PAPI_TOT_CYC is the first event added to multiplexing event set.
* 2011-11-09 Heike Jagode — Updated CUDA component for CUPTI 4.1 (RC1). Note, SetCudaDevice() should now work with the latest CUDA 4.1 version.
* 2011-11-08 Vince Weaver — Update coretemp to better handle sparse numbering of the inputs.
* 2011-11-07 James Ralph — Exclude the libpfm* and perfctr-* directories from consideration when generating Doxygen docs.
* 2011-11-07 James Ralph — Place a space in < your name here > to cleanup doxygen warnings.
* 2011-11-07 Philip Mucci — Only perf event systems that have FAST counter reads and FAST hw timer access are x86...
* 2011-11-07 Philip Mucci — MIPS clock and Linux fixup code
* 2011-11-07 Vince Weaver — A little more documentation on which of the component vector function pointers are relevant.
* 2011-11-07 James Ralph — Tested the dummy get_{real,virt}_{cyc,usec} functions on zeus, they appear to work.
* 2011-11-07 Vince Weaver — Another fix to properly skip the multiple component case if CPU component not available.
* 2011-11-07 Vince Weaver — Skip the test if no CPU component enabled, rather than fail.
* 2011-11-04 James Ralph — Free example_native_table with papi_free, glibc didn't like it if we just called free. (we allocate it with papi_calloc)
* 2011-11-04 James Ralph — Version number bump. (since the pages are quantifiably different from those released in 4.2.0 )
* 2011-11-04 James Ralph — Bump version number in the doxygen config files.
* 2011-11-04 James Ralph — _papi_example_shutdown_substrate does not have any arguments.
* 2011-11-04 James Ralph — Include ctype.h for isspace().
* 2011-11-04 James Ralph — release_procedure now reflects the correct version of doxygen to use.
* 2011-11-04 James Ralph — Do not always configure with not cpu counters, allow this to be passed in. Allows us to use one script for both types of builds we test.
* 2011-11-04 James Ralph — Create a script for buildbot to configure with several components.
* 2011-11-04 James Ralph — Rebuild the manpages with doxygen 1.7.4 to remove the 's at the end of sentances.
* 2011-11-03 Vince Weaver — Fix some gcc-4.6 compile warnings complaining that retval was being set but not used.
* 2011-11-03 Vince Weaver — Add some extra comments to the PAPI_num_cmp_hwctrs() code that describe its limitations a bit better.
* 2011-11-02 Vince Weaver — Add lots of debugging to make results of overflow_allcounters test a bit more clear.
* 2011-11-02 Vince Weaver — coretemp_pretty wasn't printing the description for fan inputs.
* 2011-11-02 Vince Weaver — Make the coretemp code a bit pickier about which events it supports. Add descriptions to the events. Also add support for Voltage (in*) events.
* 2011-11-02 Vince Weaver — Cut and paste error slipped in to that last commit. Fixes a build issue.
* 2011-11-02 Vince Weaver — Clean up coretemp with same cleanups done in example component.
* 2011-11-02 James Ralph — Rebuild the man pages with a newer version of doxygen. ( older versions of doxygen had a nasty bug in man output. )
* 2011-11-02 Vince Weaver — Add a test that makes sure you can have active EventSets on multiple components at the same time.
* 2011-11-02 Dan Terpstra — Change PATH specification to include tcsh syntax; other minor syntax corrections.
* 2011-11-02 Vince Weaver — More cleanups and documentation for the example component.
* 2011-11-01 Vince Weaver — Some more major overhaul of the example component. A lot more documentation, plus make is behave a lot more like a real component would.
* 2011-11-01 James Ralph — Turn off undocumented warnings for the utils. doxygen run.
* 2011-11-01 James Ralph — Add spaces to the comments so doxygen doesn't think <event> is an xml tag.
* 2011-10-31 James Ralph — Remove the @file directive from the doxygen comment blocks for the utilities. This cleans up the generated man pages. ( we nolonger build *.c.1 )
* 2011-10-31 Vince Weaver — Clarify in the example component that ->reset only gets called if an eventset is currently running.
* 2011-10-31 James Ralph — Fix a maketarget typo.
* 2011-10-31 James Ralph — We now have a good version of doxygen installed on most icl run machines. ( /mnt/scratch/sw/doxygen-1.7.5.1 )
* 2011-10-31 James Ralph — *** empty log message ***
* 2011-10-31 James Ralph — Update release_procedure to inform how to update the website documentation link.
* 2011-10-28 Vince Weaver — Correct the RELEASENOTES for some things I missed when reviewing it.
* 2011-10-28 Vince Weaver — Have coretemp set the num_native_events field.
* 2011-10-28 Vince Weaver — Update example test to print num_native_events, to help debug issues with other components not updating the value.
* 2011-10-28 Vince Weaver — Fix typo enent -> event Also remove residual LMSENSOR mentions from the coretemp header.
* 2011-10-28 Vince Weaver — Fix two memory leak locations.
* 2011-10-28 Vince Weaver — The change to pass the PAPI CC/CFLAGS to the component tests broke the nvidia test as it wants CC to be nvcc.  So update that Makefile to use nvcc instead.
* 2011-10-27 Vince Weaver — Improve the example_basic component test to be much more comprehensive.
* 2011-10-27 Vince Weaver — Cleanup the example test.  Fix various mistakes in the comments as well as add better error checking.
* 2011-10-27 Vince Weaver — The coretemp_test target was example_test due to cut-and-paste error.
* 2011-10-27 Vince Weaver — Add a component_tests dependency so that the component_tests are made during a make -j build
* 2011-10-27 Vince Weaver — Make sure the component test makefiles get passed the CC and CFLAGS definitions.
* 2011-10-27 Vince Weaver — Fix up the coretemp component some more.  Make sure the enumerate function returns PAPI_ENOEVNT if no events are available.
* 2011-10-27 Vince Weaver — The solaris-ultra substrate was still broken. This is because recent changes to component bind time explictly used the ->set_domain() call, and this vector was not set up in solaris_ultra.
* 2011-10-26 Vince Weaver — The Solaris build was broken.
* 2011-10-26 Dan Terpstra — Updates for the 4.2.0 release.
* 2011-10-26 Dan Terpstra — Remove extraneous and deprecated documentation files.
* 2011-10-26 Dan Terpstra — Commits for the 4.2.0 release.
* 2011-10-25 James Ralph — Update doxygen_procedure to note that we need a recent version of doxygen.
* 2011-10-25 James Ralph — Update doxygen generated man-pages for the pending release.
* 2011-10-25 Vince Weaver — The nmi_watchdog test should report a Warning if nmi_watchdog is enabled   not an error.  (Since we do work around it, even if performance is   likely impacted).
* 2011-10-25 Vince Weaver — I think the nmi_watchdog stuff is going to cause us problems down the road.
* 2011-10-25 Vince Weaver — The nmi_watchdog workaround is needed for multiplexing too.
* 2011-10-25 Vince Weaver — Yesterday's coverity fix to make sure the cleanup and destroy rerturn values were checked ended up over-writing "retval" in a way that broke the sdsc4-mpx test.  Fix things so that doesn't happen.
* 2011-10-25 Vince Weaver — Some changes for perf_event MIPS support
* 2011-10-25 James Ralph — Remove the old html documentation and assorted helper files.
* 2011-10-25 Vince Weaver — Fix a possible directory stream leak in the coretemp component.
* 2011-10-25 Vince Weaver — Properly free the arrays in calibrate, introduced by yesterdays coverity fix.
* 2011-10-25 Vince Weaver — Fix coretemp to not fail if /sys/class/hwmon doesn't exist.
* 2011-10-24 Vince Weaver — Patch coretemp to only free the initialized data in shutdown_substrate (once per PAPI_init) rather than shutdown (once per thread).
* 2011-10-24 Vince Weaver — Fix various calls to PAPI_start() and PAPI_stop() in multiplex_cost that didn't check the return value.  Took care to try to avoid changing timing measurements.  Noticed by coverity checker.
* 2011-10-24 Vince Weaver — In one case, cost was not checking the return of PAPI_start()/PAPI_stop(). This change makes it does so, while being careful not to interfere with the timing that is going on.
* 2011-10-24 Vince Weaver — pthrtough and pthrtough2 were not checking the return value for pthread_attr_setscope().  Reported by coverity checker.
* 2011-10-24 Vince Weaver — multiplex1_pthreads was not checking the return from PAPI_library_init() as flagged by coverity checker.
* 2011-10-24 Vince Weaver — inherit.c wasn't checking the result of the waitpid() call, as reported by coverity checker.
* 2011-10-24 Vince Weaver — Check the return of pthread_create().
* 2011-10-24 Vince Weaver — Fix an actual bug (reported as deadcode by coverity) where _papi_hwd_ntv_code_to_descr was appending extraneous ", masks:" strings into an event description.
* 2011-10-24 Vince Weaver — Fix cases where PAPI_*() functions were called without checking the return for an error.
* 2011-10-24 Dan Terpstra — Update version to 4.2.0 for pending release.
* 2011-10-24 Vince Weaver — Fix some code that could potentially dereference a null pointer.
* 2011-10-24 Vince Weaver — Remove a dead code case as reported by coverity.  Shouldn't break anything as I can't find anywhere that vector_print_table() is actually called.
* 2011-10-24 James Ralph — Update release_procedure to reflect another file that needs a version number bump. (Doxyfile.utils)
* 2011-10-24 Vince Weaver — Fix some weird code that was sharing a memory allocation for both double and floats.  This was really ugly and made the coverity checker sad.
* 2011-10-24 Vince Weaver — Fix a signed/unsigned comparison bug I introduced.
* 2011-10-24 Vince Weaver — Fix the test so it correctly iterates all of the components.
* 2011-10-24 Vince Weaver — Fix a potential memory leak in coretemp (flagged by coverity).
* 2011-10-24 James Ralph — Remove const decleration from get_virt_* in solaris substrate. Vince removed this from papi_vector.h back in June.
* 2011-10-24 Vince Weaver — Improce the add_two_events() code in the test library. Before it was possible to overrun a buffer if none of the potential predefined events were available.
* 2011-10-24 Dan Terpstra — Update version to 4.2.0 for pending release.
* 2011-10-22 James Ralph — Merge in the user events code , protected by a configure option. ( --with-user-events )
* 2011-10-21 Vince Weaver — We now ensure that test_fail() always exits. There was some code around that tracked the number of times test_fail() was called. Remove that, as I think it was confusing the coverity checker and causing a huge number of false positives for NULL pointer dereferences.
* 2011-10-21 Vince Weaver — Some minor cleanups to the acpi component.  It was choking a bit if ACPI didn't provide thermal information, and also fix a few coverity bugs involving not checking the result of a dup() call.
* 2011-10-21 Vince Weaver — Another problem with negative numbers, this time one could potentially be passed to a malloc call.
* 2011-10-21 Vince Weaver — We were indexing an array with a returned value that could be negative on failure. Add a check to avoid that.
* 2011-10-21 Vince Weaver — perf_events.c was setting variables to -1 and then potentially using them to index arrays or call close() on them.
* 2011-10-21 James Ralph — Include stdint.h and ctype.h; needed for uint64_t and isspace() respectivly.
* 2011-10-21 Vince Weaver — Fix problem where we try to manipulate a NULL directory entry.
* 2011-10-21 Vince Weaver — We were opening a file but not checking for failure before reading from it.
* 2011-10-21 Vince Weaver — Both gcc and coverity were complaining about using an uninitialized pointer. This makes sure it's not dereferenced if not initialized.
* 2011-10-21 Vince Weaver — Stop doing unnecessary pointer math in a print statement.
* 2011-10-21 Vince Weaver — Fix some wrong buffer sizes in the coretemp component.
* 2011-10-21 Vince Weaver — add some extra debug info for sdsc test failures.
* 2011-10-21 Dan Terpstra — Add comment to PAPI_num_counters() documentation about use of PAPI_num_cmp_hwctrs() for component counters.
* 2011-10-19 Dan Terpstra — Correct documentation errors for PAPI_strerror.
* 2011-10-19 James Ralph — Under a no-cpu-counters build, still build all of the utils. We probably want to rethink some of the cost util details.
* 2011-10-12 Vince Weaver — Remove an unneeded call to "cat".  For some reason it was printing pointless warnings that needlessly cluttered the buildbot logs.
* 2011-10-11 Philip Mucci — -lpapi should never be a dependency. -I.. is missing in makefile
* 2011-10-10 Vince Weaver — The multiplex1_pthreads test was reporting a memory leak.
* 2011-10-07 Vince Weaver — Merge the "conflicts" from the libpfm4 merge
* 2011-10-07 Vince Weaver — Fix the MEMORY LEAK errors involving the attach ctests (as seen on buildbot)
* 2011-10-06 Dan Terpstra — Add Fortran reference to  doxygen main page.
* 2011-10-05 Vince Weaver — There has been some ongoing speculation about what would happen if you enabled Multiplexing and Overflow at the same time.
* 2011-10-05 Philip Mucci — Moved cpu and inherit bits to end of structure for compat across all 4.x lines. Found by Will Cohen.
* 2011-10-04 James Ralph — Enable macro expansion in the doxygen preprocessor step.
* 2011-10-04 Dan Terpstra — make "* #include" into "* \#include" so doxygen doesn't treat it as a command.
* 2011-10-04 Dan Terpstra — Added all doxygen stubs to the PAPIF group.
* 2011-10-03 Vince Weaver — My previous "fix" for the array bounds issue in ipc.c had multiple embarassing bugs.
* 2011-10-03 Vince Weaver — Additionally remove the now extraneous papi_libpfm_preset definition from the other Rules files too.
* 2011-10-03 Vince Weaver — The change to make the preset code generic accidentally ended up defining the build rules for the file in duplicate places.  This fixes that.
* 2011-09-30 Vince Weaver — Fix two unused variable warnings.
* 2011-09-30 Vince Weaver — We were allocating the "values" array but never freeing it.
* 2011-09-30 Vince Weaver — The SDSC tests could walk off the end of an array.
* 2011-09-30 Vince Weaver — We could potentially access outside an array boundary in overflow_twoevents.
* 2011-09-30 Vince Weaver — ipc was also abusing array boundaries.
* 2011-09-30 Vince Weaver — The flops.c ctest was abusing the notion of C arrays, by writing INDEX*INDEX values to mresult[0][i], I suppose "knowing" that this would fill in the whole array.  Fix things to use an additional iterator.
* 2011-09-30 Vince Weaver — The coverity checker rightly points out that the last argument to strncat should be buffersize-1.
* 2011-09-30 Vince Weaver — Coverity flagged that there were some tests that had no effect. In particular the are tests that the pointers are non-null. However, they are arrays rather than pointers. This patch make it clear that arrays are being used in the code.
* 2011-09-30 Vince Weaver — This is a relatively minor patch that ensures that all the allocated memory is initialized to zero before it is used.  Coverity might not be smart enough to determine whether the test actually wrote into all the locations because of the case statement. This is make it easier for coverity to determine that the memory has been initialized.
* 2011-09-30 Vince Weaver — Coverity scan showed that MPX_cleanup() function was blindly accessing a value through a pointer and then checking to see that the pointer was null.  This patch makes sure that the pointer is checked before it is used.
* 2011-09-30 Vince Weaver — Coverity found that the sizeof argument for pthrtough2.c and pthrtough.c was using sizeof(pthread *) rather than sizeof(pthread). This patch fixes that problem.
* 2011-09-30 Vince Weaver — This change moves the setting for default domain to be enforced at eventset add time, rather than eventset creation time.
* 2011-09-30 Vince Weaver — One more file that is no longer needed.
* 2011-09-30 Vince Weaver — Clean up the now not-needed pmapi-ppc64_events.c file.
* 2011-09-30 Vince Weaver — Finalize the merge of the preset code.
* 2011-09-30 Vince Weaver — Fix a missing include.
* 2011-09-30 Vince Weaver — Move more code to its proper place.
* 2011-09-30 Vince Weaver — Move the ppc64_setup_native_table() routines out of the preset code.
* 2011-09-30 Vince Weaver — move pmapi_find_full_event to be _aix_ntv_name_to_code() as it probably always should have been.
* 2011-09-30 Vince Weaver — Make papi_libpfm_presets more generic by calling    _papi_hwi_native_name_to_code() rather than a substrate-specific call.
* 2011-09-30 Vince Weaver — I was mainly doing this to aid debugging, but now the papi_libpfm_presets.c file and pmapi-ppc64_events.c file are close enough to being identical I might try to merge them.
* 2011-09-29 Vince Weaver — The files are almost the same now.
* 2011-09-29 Vince Weaver — More making these files the same, including some memory leak fixes that made it to the former but not the latter.
* 2011-09-29 Vince Weaver — Tracking down problems on AIX can be a bit of a pain because   papi_libpfm_presets.c and pmapi-ppc64_events.c are almost (but not quite)   the same.  This change makes the files more similar, mostly by   cleaning up whitespace and normalizing comments and debugging statements   between the two.
* 2011-09-29 Vince Weaver — Ugh, obvious typo in that last commit.
* 2011-09-29 Vince Weaver — In ppc64_setup_gps() the current code sometimes walks off the end of the group array and trashes unrelated memory.
* 2011-09-29 Vince Weaver — No one seems to remember the last time this file was used, so let's remove it.
* 2011-09-28 Vince Weaver — Remove the "u" option to the "ar" command that links libpapi.a, as it was breaking the build on MIPS.
* 2011-09-28 Vince Weaver — Fix up the "collisions" from the libpfm4 import
* 2011-09-26 Vince Weaver — We would like to use parallel make on packages to speed things up. However, when this was tried with papi the "make -j4" failed (https://bugzilla.redhat.com/show_bug.cgi?id=740909). I took a look through the code and found that some of dependencies were not quite right. Turns out that $(papiLIBS) is substituted during the configure, but it isn't available for the actual make. Attached is the patch that ensures that the $(LIBS) are built before utils and tests.
* 2011-09-26 Vince Weaver — Modify run_tests.sh so that you can set the VALGRIND command externally via environment variable without having to edit run_tests.sh itself.
* 2011-09-26 Vince Weaver — If we have no Fortran compiler available, then our current build system tries to build the Fortran examples with an empty compiler string which just generates strange errors.
* 2011-09-26 Vince Weaver — The build on power6 was warning in a DEBUG statement because sizeof() returns an int rather than a long.  So use a cast to avoid this.
* 2011-09-26 Vince Weaver — The move to use pid_t for pid values caused warnings on a --with-debug build due to the lack of a way to print a pid_t value without a cast.
* 2011-09-23 Vince Weaver — Rename the "perfmon_idx" structure field the more evocative "libpfm4_idx" value.
* 2011-09-23 Vince Weaver — Fix problem where we were passing a pointer to an EventSet rather than the actual EventSet number to PAPI_cleanup_eventset().
* 2011-09-23 Vince Weaver — Make the perf_event ctl structure have more explicit data types.
* 2011-09-23 Vince Weaver — Add bare minimal MIPS74k support, enough to compile.
* 2011-09-23 Vince Weaver — Add MIPS 74k pre-defined events
* 2011-09-22 James Ralph — Heike's cleanup_eventset work allows the calling of PAPI_cleanup_eventset with cuda, so uncomment the eventset cleanup code in all_native_events.
* 2011-09-22 Vince Weaver — Update papi.h to properly detect if being built with a C99 compiler.
* 2011-09-22 Vince Weaver — Update PAPI_FP_INS event name on amd_fam14h as it was changed in the most recent libpfm4 merge
* 2011-09-22 Vince Weaver — Fix the "conflicts" from the libpfm4 git import
* 2011-09-22 Vince Weaver — Initial revision
* 2011-09-21 Vince Weaver — Fix problem where we were freeing a singly-linked list in a for loop, possibly free()ing the allocation before dereferencing ->next
* 2011-09-21 Vince Weaver — Fixed uninitialized data problem in papi_cost
* 2011-09-21 Vince Weaver — Fix problem where we were copying around chunks of memory that were not initialized yet.
* 2011-09-21 Vince Weaver — Fix two cases where we were dereferencing a pointer without checking for NULL.
* 2011-09-21 Vince Weaver — We were opening files but not properly closing them if we returned early with an error condition.
* 2011-09-21 Vince Weaver — The coverity tool noticed that we allocate and populate a cpu node info structure, but we never pass any info on this structure outside of the cpu detection routine, in effect leaking the allocation.
* 2011-09-21 Vince Weaver — The coverity checker was reporting we forgot to fclose() /proc/cpuinfo in papi.c
* 2011-09-21 Vince Weaver — In various places we were using MAX_COUNTER_TERMS (defined by substrate) rather than PAPI_MAX_COUNTER_TERMS (a papi predefined event define). This could cause buffer overruns.
* 2011-09-21 Vince Weaver — Avoid case where we could have been dereferencing a NULL pointer in MPX_stop()
* 2011-09-21 Vince Weaver — Fix problem where thread and cpu could be dereferenced as NULL in PAPI_start()
* 2011-09-21 Vince Weaver — Update the AMD Family 14h (Bobcat) pre-defined events.
* 2011-09-21 Vince Weaver — Recent Ubuntu versions use the ld flag --as-needed by default.
* 2011-09-19 James Ralph — When building testlib dependencies from ctests/ ftests/ and utils/ call $(MAKE) and not make, this should fix aix.
* 2011-09-15 Heike Jagode — Change initialization of function pointer cleanup_eventset() from vec_int_dummy to vec_int_ok_dummy so that it returns PAPI_OK by default. Roll back initialization for every substrate. AGAIN, keep an eye on builtbot.
* 2011-09-14 Philip Mucci — Merged with HEAD, still passing all tests
* 2011-09-13 Vince Weaver — The libpfm4 code was doing a full call to    pfm_get_os_event_encoding() during every call to update_control_state().
* 2011-09-13 Vince Weaver — Missed a $
* 2011-09-13 Vince Weaver — Update run_tests.sh to run component tests, and update the example test to act more like a ctest.
* 2011-09-13 Vince Weaver — Fix warnings generated by the example component.
* 2011-09-13 Vince Weaver — ctests, ftests, utils, and the component tests were all using some files in ctests.
* 2011-09-13 Vince Weaver — When compiling with --with-no-cpu-counters configure would report the platform as linux-perfctr-x86.  This changes it to report as linux-no-counters
* 2011-09-12 Heike Jagode — Initialize new function pointer cleanup_eventset() for every substrate. Keep an eye on builtbot.
* 2011-09-12 Heike Jagode — Cannot override void* definitions from PAPI framework layer (e.g. hwd_control_state_t) with typedefs to conform to PAPI Component layer code if this technique has already been used in another substrate (e.g. perfctr-x86). Or short: #undef and typedef can't be done twice.
* 2011-09-12 Vince Weaver — Fix bug caused by forgetting to drop the stream name when converting a fprintf() into a SUBDBG()
* 2011-09-12 Vince Weaver — Patch from William Cohen fixing a potential problem found by a static analysis tool where we could possibly pass a NULL pointer to free_notes().
* 2011-09-12 Vince Weaver — Some memory leak fixes made to libpfm3 papi_pfm_events.c by Robert Richter were lost when the libpfm4/libpfm4 presets merge was done.
* 2011-09-10 Heike Jagode — Cleaned up old comment regarding CUDA pre-4.0 when it was not possible to access a GPU from multiple CPU threads.
* 2011-09-10 Heike Jagode — Deleted function pointer destroy_eventset from the PAPI vector table, and added cleanup_eventset instead. PAPI_destroy_eventset() requires an empty EventSet. Hence, usually PAPI_cleanup_eventset() is called before PAPI_destroy_eventset(); which also sets the CompIdx to -1. This means, PAPI_destroy_eventset() won't have any knowledge about components. However, in order to disable CUDA eventGroups and to free perfmon hardware on the GPU, knowledge about the CUDA component index is required. Hence, I replaced CUDA_destroy_eventset() with CUDA_cleanup_eventset() in the CUDA component. NOTE: Please make sure you call PAPI_cleanup_eventset() before calling PAPI_shutdown().
* 2011-09-09 Heike Jagode — CUDA component is now thread-safe. Starting in CUDA 4.0, multiple CPU threads can access the same CUDA context. This is a much easier programming model then pre-4.0 as threads - using the same CUDA context - can share memory, data, etc. Note, it's possible to create a different CUDA context for each thread, but then we are likely running into a limitation that only one context can be profiled at a time.
* 2011-09-07 Vince Weaver — Apply fixes to problems noticed by a static analysis tool.
* 2011-09-07 Vince Weaver — Update SandyBridge preset events.
* 2011-09-07 Philip Mucci — MIPS 74K little endian perf event support, requires 3.0.3+ kernel
* 2011-09-06 Vince Weaver — The warning I had print on nmi_watchdog being found was a bit much, make it a SUBDBG() call instead.
* 2011-09-06 Vince Weaver — On newer Linux kernels (2.6.34+) the nmi_watchdog counter can   steal one of the counters, reducing by one the total available.
* 2011-09-06 Vince Weaver — We were missing a proper libpfm4 interlagos CPU name in the papi_events.csv file
* 2011-09-02 Vince Weaver — Fix "conflicts" from the libpfm4 import
* 2011-09-02 Vince Weaver — Explicitly set num_native_events to zero at init time.
* 2011-09-02 Vince Weaver — Set FD_CLOEXEC on the overflow signal handler fd.
* 2011-09-02 Vince Weaver — Remove the "unexport CFLAGS" lines from the Rules files.
* 2011-09-02 Vince Weaver — Fix a few warnings reported by gcc-4.6
* 2011-09-02 Vince Weaver — Override auto-detection of substrate if the user specifies what they want to build with.  This allows building perfctr and perfmon2 PAPI on systems auto-detected as having perf_event support.
* 2011-09-02 Vince Weaver — Add a "--with-libpfm3" argument to configure that lets us specify libpfm3 for testing purposes.
* 2011-09-02 Vince Weaver — Fix solaris niagara2 build problems reported by tigrage on the PAPI forum.
* 2011-08-30 Philip Mucci — Regen
* 2011-08-29 Philip Mucci — Check for a requested interface to tweak build flags
* 2011-08-29 Philip Mucci — Last bit for cross compiling...
* 2011-08-29 Philip Mucci — Better double quotes
* 2011-08-29 Philip Mucci — Further refinement of the combinations of --with-perfctr --with-perfmon and --with-perf-events
* 2011-08-29 Philip Mucci — Some fixes for cross compiling and not including x86_cache_info.c when not ensured an x86.
* 2011-08-29 James Ralph — Surround component tests and cleanup recipies with a conditional, the version of sh that our aix machine has does not handle          for i in {Empty set};
* 2011-08-29 Dan Terpstra — Update Release Notes and add ChangeLog for PAPI 4.1.4.
* 2011-08-29 Dan Terpstra — Rebuild from configure.in with version number bump to 4.1.4 in advance of pending internal vendor release for Cray.
* 2011-08-26 James Ralph — Update rel procedure to mention building the man pages before a release.
* 2011-08-26 James Ralph — Switch over to doxygen generated man pages.
* 2011-08-26 James Ralph — Remove the old manpages in preperation for defaulting to doxygen generated ones.
* 2011-08-25 Vince Weaver — Block all PERF_COUNT_SW events from overflow_allcounters test,   as overflow on software counter can crash perf_event kernels pre 3.1
* 2011-08-25 Vince Weaver — Fix the "conflicts" from the import
* 2011-08-25 Dan Terpstra — Bump version number to 4.1.4 in advance of pending internal vendor release for Cray.
* 2011-08-23 Dan Terpstra — Removed all references to Fortran APIs. These are now all in papi_fwrappers.c Also normalized syntax for many doxygen headers.
* 2011-08-23 Dan Terpstra — Added doxygen skeleton for all remaining Fortran functions in this file. Also added wrappers for four additional APIs: PAPI_get_real_nsec PAPI_read_ts PAPI_lock PAPI_unlock
* 2011-08-19 Dan Terpstra — Stubbed out doxygen pages for Fortran functions. About half way done!
* 2011-08-19 Vince Weaver — Finish up the documentation/cleanup pass through the libpfm4 code.
* 2011-08-18 Vince Weaver — Fix code so we no longer get warnings that 'setup_preset_term' and '_pfm_get_counter_info' are defined but not used
* 2011-08-18 Vince Weaver — Consolidate use of _papi_libpfm_init() and pass in MY_VECTOR when necessary.
* 2011-08-18 Vince Weaver — Dynamically allocate the libpfm4 native events, rather than having a fixed array allocated at init time.
* 2011-08-18 Vince Weaver — Some more minor cleanups and documentation in the libpfm4 code.
* 2011-08-18 James Ralph — Fixup for linux coretemp component, it pays to check cvs status once in a while...
* 2011-08-16 Vince Weaver — Update the PAPI_enum_event() Doxygen comments to reflect modern   values for the "modifier" parameter.
* 2011-08-16 Vince Weaver — Clean up code and add documentation for all the functions involved in libpfm4's _papi_libpfm_ntv_enum_events() function.
* 2011-08-15 Vince Weaver — Updat the rmb() barrier for ARM.
* 2011-08-15 Vince Weaver — Update SandyBridge EP support to match that of mainline libpfm4
* 2011-08-15 Vince Weaver — Merge conflicts
* 2011-08-15 Vince Weaver — Cleanup libpfm4 code, and add more comments to code.
* 2011-08-15 Vince Weaver — Fix bug where umask support was disabled.
* 2011-08-15 Vince Weaver — Make the perfctr code use the merged preset event code.
* 2011-08-15 Vince Weaver — Have libpfm3 use the merged preset code.
* 2011-08-15 Vince Weaver — Move the libpfm presets code to its own file, and modify the libpfm4 code to use it.
* 2011-08-15 Vince Weaver — Make the libpfm3 predefined events parser identical to the libpfm4 one, in preparation for a merge.
* 2011-08-15 Vince Weaver — Move vendor fixups into the substrate and out of the naming library code.
* 2011-08-15 Vince Weaver — Rename papi_pfm_events.c to papi_libpfm3_events.c to make it more clear what is in the file.
* 2011-08-15 Vince Weaver — Fixup perfmon2 case for the libpfm renaming
* 2011-08-15 Vince Weaver — Fix perfctr breakage from the libpfm rename.
* 2011-08-15 Vince Weaver — The PAPI code uses _pfm_ in function names to mean *both* perfmon2 code and libpfm3/4 code.  This can cause a lot of confusion.
* 2011-08-15 Vince Weaver — Fix build error on perfmon2 due to movement of the _papi_pfm_shutdown()
* 2011-08-05 Heike Jagode — Added generic implementation that makes it possible to add tests to components without modifying any PAPI-specific code (other than adding the tests and a makefile to the component directory). All component tests will be compiled together with PAPI when typing 'make' (as well as cleaned up when 'make clean' or 'make clobber' is typed). +++ Also added tests to 2 components, the example and cuda component.
* 2011-08-05 Vince Weaver — Add locking to papi_pfm4_events so that adding/looking up event names doesn't have a race condition when multiple threads are doing it at once.
* 2011-08-05 Vince Weaver — Add a _papi_pfm_shutdown() function and have it clear out the native events array at PAPI_shutdown().
* 2011-08-05 Philip Mucci — Added some PAPI_set_domain's inside of #if 0's for testing.
* 2011-08-03 Vince Weaver — Use the new ARM vendor code to force the proper default domain on ARM cpus.
* 2011-08-03 Vince Weaver — Add an ARM vendor string and have it properly set.
* 2011-08-03 Vince Weaver — Clean up some comments, add a few debug messages.
* 2011-08-02 Vince Weaver — The ARM warning for memory hierarchy not being implemented was in the wrong place.
* 2011-08-02 Vince Weaver — Fix some misleading debug messages.
* 2011-08-02 Vince Weaver — Update ARM Cortex A9 preset events, and add ARM Cortex A8 events
* 2011-07-28 Vince Weaver — Add remaining changes needed for ARM compilation. This is enough for "papi_avail" and "papi_native_avail" to work.
* 2011-07-28 Vince Weaver — Add ARM Cortex A9 preset events to the CSV file.
* 2011-07-28 Vince Weaver — Add the perf_event syscall number for ARM
* 2011-07-28 James Ralph — Create PAPIF group in doxygen, for the papi fortran interface.
* 2011-07-27 Vince Weaver — My changes yesterday broke on the --with-debug case, as noticed by buildbot.
* 2011-07-26 Dan Terpstra — Implement doxygen comments for PAPI_get_opt; Implement doxygen comments for PAPIF_accum in papi_fwrappers.c. This is a first step in providing separate independent Fortran documentation.
* 2011-07-26 James Ralph — Have doxygen parse papi_fwrappers.c for comments.
* 2011-07-26 Vince Weaver — The last checkin broke papi_native_avail on libpfm4.  Fix it.
* 2011-07-26 Vince Weaver — Cleanup some code in papi_pfm4_events.c to avoid gcc-4.6 warnings
* 2011-07-26 Vince Weaver — Fix some warnings in src/x86_cache_info.c reported by gcc-4.6
* 2011-07-21 James Ralph — Change all_native_events test to create an eventset for each native event it finds. Also becomes a good test of the number of outstanding eventsets allowed.
* 2011-07-19 Dan Terpstra — Doxygen rewrite for PAPI_set_opt.
* 2011-07-13 Vince Weaver — A few more commits that get SandyBridge mostly working.
* 2011-07-13 James Ralph — Include a comment to the prototype for PAPI_read_ts. This is apparently a requirement to get doxygen to link from the prototype to the doc block for the function (a link shows up in the low_api group now).
* 2011-07-12 Vince Weaver — Temporarily add missing SandyBridge FP events until support gets merged upstream.
* 2011-07-12 Vince Weaver — Some minor Doxygen fixes.  This was my run through the HTML output produced by my assigned functions.
* 2011-07-11 Vince Weaver — Temporarily add model 45 Sandy Bridge to our copy of libpfm4 until we can get this merged upstream.
* 2011-07-11 Vince Weaver — Fix all the remaining users of the ctests add_two_events() helper
* 2011-07-11 Vince Weaver — Fix first test bug due to add_two_events() change.  Clean up validation of results.
* 2011-07-11 Vince Weaver — Some cleanups I made to the testing routine add_two_events() a while ago broke the zero test.  (the cycles result was swapped with the other counter result).
* 2011-07-11 Vince Weaver — Patch from William Cohen that sets LD_LIBRARY_PATH and LIBPATH to include libpfm4/lib.
* 2011-07-11 James Ralph — High level interface Doxygen comments updated to include interface overview
* 2011-07-11 Vince Weaver — Fix conflicts from libpfm4-git import
* 2011-07-11 Vince Weaver — Initial revision
* 2011-07-08 James Ralph — Add in the PAPI component development page. Currently not linked to by anything yet, but can be found at file://$(html_dir)/CDI or http://web.eecs.utk.edu/~ralph/html/CDI for an already built page.
* 2011-07-07 Heike Jagode — Add doxygen comments for PAPI_get_executable_info(), PAPI_exe_info_t and PAPI_address_map_t
* 2011-07-07 Heike Jagode — Add doxygen comments for PAPI_event_code_to_name() and PAPI_event_name_to_code()
* 2011-07-07 Heike Jagode — Add doxygen comments for PAPI_enum_event()
* 2011-07-07 Heike Jagode — Add doxygen comments for PAPI_create_eventset()
* 2011-07-07 Heike Jagode — Add doxygen comments for PAPI_cleanup_eventset() and PAPI_destroy_eventset()
* 2011-07-07 Heike Jagode — Add doxygen comments for PAPI_attach() and PAPI_detach()
* 2011-07-07 Heike Jagode — Add doxygen comments for PAPI_assign_eventset_component()
* 2011-07-05 Heike Jagode — missing parentheses added in CUDA_Shutdown() which caused a seg fault.
* 2011-07-01 Heike Jagode — Add doxygen comments for PAPI_add_event()
* 2011-07-01 Heike Jagode — Add doxygen comments for PAPI_add_events() +++ Updated PAPI_accum()
* 2011-07-01 Heike Jagode — Add doxygen comments for PAPI_accum()
* 2011-07-01 Vince Weaver — Some more ia64 ctests fixes
* 2011-07-01 Vince Weaver — Add doxygen comments for   PAPI_register_thread()
* 2011-07-01 Vince Weaver — Add doxygen comments for:  PAPI_read()  PAPI_read_ts()
* 2011-07-01 Vince Weaver — Another attempt at fixing earprofile on ia64.
* 2011-07-01 Vince Weaver — PAPI for ia64 compiles now, and now it's some of the ia64-specific ctests that are broken.
* 2011-06-30 Dan Terpstra — Doxygen for: PAPI_set_multiplex PAPI_shutdown PAPI_sprofil_t PAPI_start (int EventSet) PAPI_state (int EventSet, int *status) PAPI_stop (int EventSet, long long *values) PAPI_strerror (int)
* 2011-06-30 Vince Weaver — more ia64 fixes
* 2011-06-30 Vince Weaver — doxygen comments for:  PAPI_query_event()
* 2011-06-30 Vince Weaver — Some more ia64 fixes.
* 2011-06-30 Vince Weaver — add doxygen comments for  PAPI_profil()
* 2011-06-30 Vince Weaver — More ia64 fixes.  Getting closer.
* 2011-06-30 Vince Weaver — One more try at fixing ia64.
* 2011-06-29 Vince Weaver — Add doxygen comments for: * PAPI_num_events() * PAPI_overflow() * PAPI_perror()
* 2011-06-29 Dan Terpstra — Doxygen for PAPI_set_domain and PAPI _set_granularity. Unfortunately, this seems to have raised more issues about Fortran support...
* 2011-06-29 Vince Weaver — Add doxygen comments to * PAPI_list_threads() * PAPI_lock() * PAPI_multiplex_init() * PAPI_num_hwctrs() * PAPI_num_cmp_hwctrs()
* 2011-06-29 Dan Terpstra — Doxygen for PAPI_set_debug and minor tweaks to other function documentation.
* 2011-06-28 Vince Weaver — some more itanium fixes.  This won't be enough to fix things but it is a start.
* 2011-06-28 James Ralph — Check in Kiran's doxygen work. This time hopefully not clobbering anyone.
* 2011-06-28 Vince Weaver — Attempt to fix the build for itanium systems.
* 2011-06-28 Dan Terpstra — Fix comments embedded in doygen source to be C++ single line format.
* 2011-06-27 Dan Terpstra — Commit documentation changes for PAPI_reset, PAPI_set_thr_specific, and PAPI_get_thr_specific. The last one wasn't on my list, but it mirrored _set_ so I did it anyway.
* 2011-06-27 James Ralph — *** empty log message ***
* 2011-06-27 James Ralph — Commit Kiren's updates to the code documentation.
* 2011-06-24 James Ralph — One got left behind... ( see previous commit about redoing doxygen procedures )
* 2011-06-24 James Ralph — Update install process for man-pages, install from pre-built pages living in $(PAPI_DIR)/man and update $(PAPI_DIR)/doc to generate doxygen pages and copy them to $(PAPI_DIR)/man.
* 2011-06-24 Dan Terpstra — Updates to doxygen stuff for PAPI_remove_event{s}
* 2011-06-24 Vince Weaver — When I made the multiattach change I forgot to update _papi_hwi_lookup_thread calls on all architectures.  This should get the ones I missed.
* 2011-06-23 Vince Weaver — For libpfm4 we were setting available counters to the number of generic counters.
* 2011-06-22 Vince Weaver — One more fix to the byte_profile code
* 2011-06-22 Vince Weaver — Fix byte_profile ctest, as it was breaking on libpfm4.
* 2011-06-22 Vince Weaver — Add support for handling multiattach properly.
* 2011-06-13 Vince Weaver — Fix the libpfm4 enumerate code.
* 2011-06-13 Vince Weaver — Make "test_fail()" actually fail.
* 2011-06-10 James Ralph — Add example code to the high level interface docs
* 2011-06-10 Vince Weaver — Add initial Sandy Bridge event support.
* 2011-06-10 James Ralph — Added an example of how to embed example code in PAPI_stop_counters documentation.
* 2011-06-09 James Ralph — Makefile fix for fortran wrapper files on case-insensitive filesystems. During build, it renames the preprocessed file PAPI_FWRAPPERS.c to upper_PAPI_FWRAPPERS.c
* 2011-06-08 James Ralph — Have configure check that doxygen is installed, and have make install only attempt to build the doxygen docs if we found doxygen.
* 2011-06-07 Heike Jagode — ctests/thrspecific works now too with the CUDA component
* 2011-06-07 Heike Jagode — clean up and indent
* 2011-06-07 Heike Jagode — Added CudaRemoveEvent functionality (was broken in earlier CUDA RC versions). ctests/all_native_events works now (at least for the default CUDA device). +++ Minor exit/return mods in CUDA component
* 2011-06-07 James Ralph — Rework doxygen to better generate manpages from code comments.
* 2011-06-03 Dan Terpstra — Incorporate a note about using 2.59 autoconf to build configure.
* 2011-06-02 Dan Terpstra — Tweak the doxygen title text.
* 2011-06-01 Dan Terpstra — Modified configure.in to look for a 2.59 autoconf prerequisite. Rebuilt configure with 2.59. We'll try this out on buildbot.
* 2011-05-31 Heike Jagode — 2 things: (1) Bug in CUDA v4.0 fixed. It caused a threaded application to hang when parent called cuInit() before fork() and child called also cuInit().  All fork ctests pass now if papi is configured with cuda component. (2) If running a threaded application, we need to make sure that a thread doesn't free the same memory location(s) more than once. Now all pthread ctests pass, too (again, if papi is configured with cuda component).
* 2011-05-27 Vince Weaver — It turns out our FORMAT_ID workaround detection code was identical to FORMAT_GROUP (and not really necessary) so merge the two.
* 2011-05-26 Vince Weaver — One last try at the cray compile fix, this time using a suggestion from Steve Kaufmann.
* 2011-05-26 Vince Weaver — Update some comments on the workarounds.
* 2011-05-26 Vince Weaver — Now fix libpfm4.  I think they should all be fixed now.  Too many permutations.
* 2011-05-26 Vince Weaver — One last try at fixing the perfmon2 build.
* 2011-05-26 Vince Weaver — Fix the perfmon2 build that broke with the libpfm4 merge. The previous fix only fixed perfctr, not perfmon2
* 2011-05-24 James Ralph — Add doxygen comments to components.c
* 2011-05-24 Vince Weaver — Fix the PAPI_TOT_INS instruction for Atom, as well as update the floating point events.
* 2011-05-24 Vince Weaver — We were using some of the perf_event functionality in an susupported way   and this broke recently when the perf_event interface was made more strict.
* 2011-05-23 Dan Terpstra — New utility to display PAPI error codes and description strings. There was no API to access error descriptions, so I created PAPI_descr_error( int error_code ) too. I also updated the error table to provide strings for all defined codes.
* 2011-05-23 James Ralph — Define aix's .cmp_info.itimer_ns value to a default. The multiplexing tests are happy on power7 aix now.
* 2011-05-23 Vince Weaver — cleanup some debug messages
* 2011-05-23 Vince Weaver — The overflow test depends on the exact ordering of the flags in the   add_test_event() code.  So my previous changes broke the test.   This commit fixes the test case again.
* 2011-05-23 Vince Weaver — ctests:  remove the "hw_info" field from the profile setup functions,          as the field isn't used.
* 2011-05-23 James Ralph — Introduce a component avail utility, lists the components we were built with, optionally with native/preset counts and version number.
* 2011-05-23 James Ralph — Add number of 'native' events to the component info structure in example component.
* 2011-05-23 Vince Weaver — Clean up the ctest profile event section code some more.
* 2011-05-23 Vince Weaver — Initial PAPI Fam14h Bobcat support.
* 2011-05-20 Vince Weaver — Fix byte_profile to work on Nehalem.  Still needs some more work   to print the result properly.
* 2011-05-20 Vince Weaver — Some cleanups to the ctests/test_utils.c code + Remove the hw_info field from the add_two_events() and   add_two_nonderived_events() functions, as it wasn't used. + Make the add_test_events() function loop through all the masks,   insteading having a hardcoded test for each possible mask
* 2011-05-20 Vince Weaver — buildbot didn't like the colored test messages (despite the code   having fancy checks for "isatty()").
* 2011-05-19 Vince Weaver — Add color to the testsuite results if we are running at a console. This makes is much easier to see FAILED results.
* 2011-05-19 Vince Weaver — Fix the build with perfctr introduced by libpfm4 changes.
* 2011-05-19 James Ralph — Documentation for the AIX heap fix.
* 2011-05-19 Vince Weaver — power6 doesn't work with libpfm4, as it reports num_cntrs=0
* 2011-05-19 James Ralph — On aix one has to ask really nicely for a usable ammount of heap space. The omp tests should run now.
* 2011-05-19 Vince Weaver — This is the last commit needed to get libpfm4 support going.
* 2011-05-19 Vince Weaver — Resolve the "conflicts" witht he libpfm4 merge
* 2011-05-19 Vince Weaver — Initial revision
* 2011-05-19 Vince Weaver — Pass the actual perf_attr structure around, rather than just a 64-bit event value.  This allows support for generalized events and eventual offcore/uncore support.
* 2011-05-19 Vince Weaver — Clean up some debugging #ifdefs
* 2011-05-19 Vince Weaver — The papi_events.csv file requires some additions for libpfm4 to work   + The CPU family names have changed from libpfm3 to libpfm4     It should be backward compatible to just add the libpfm4 ones     in addition to the libpfm3 ones   + libpfm4 does not provide a helper to get the instruction and cycle     event names.  So we have to add them for all supported CPUs
* 2011-05-19 Vince Weaver — New files needed for libpfm4 support
* 2011-05-16 Dan Terpstra — Add note to update from cvs before tagging. Thanks, Will Cohen :)
* 2011-05-11 Dan Terpstra — Last entries on POWER7 AIX
* 2011-05-11 Dan Terpstra — Final (?) updates for the 4.1.3 release.
* 2011-05-10 Vince Weaver — The --with-bitmode parameter was not being passed along to libpfm3,  so it was not possible to build perf_event PAPI on non-default bitmodes. This change passes along the $(BITFLAGS) value to the libpfm3 make invocation.
* 2011-05-10 Vince Weaver — The perf_events code was using __u64 instead of uint64_t and this was causing a warning when compiling for 64-bit Power.
* 2011-05-10 Dan Terpstra — Added Robert Richter's patch with a few new events for AMD Family 15h.
* 2011-05-06 sbk — Load the 'gcc' module not 'gnu' module for Cray.
* 2011-05-06 sbk — Update the install instructions for Cray XT and XE systems.
* 2011-05-06 Vince Weaver — Make the multiattach and multiattach2 failures into warnings.
* 2011-05-06 James Ralph — Band-aid for the leak debugging statement in papi_memory.c on NO_VARARG_MACRO systems. (aix currently)
* 2011-05-05 Vince Weaver — Had the division backwards on the validation.
* 2011-05-05 Vince Weaver — Update the multiattach test to fail if the results aren't in the proper ratio. This was failing on perf_event kernels but since the results weren't checked   it was never reported as an error.
* 2011-05-05 Dan Terpstra — delete cvs2cl.pl before release
* 2011-05-05 Dan Terpstra — First cut change log for the 4.1.3 release. Nothing's frozen yet...
* 2011-05-05 Dan Terpstra — Perl script to generate change logs. Keeping it with the project makes life easier.
* 2011-05-05 James Ralph — Change INSTALL to reflect that we support power7.
* 2011-05-05 Dan Terpstra — Modfy version number for pending release: 4.1.3.0
* 2011-05-03 Vince Weaver — Cleanup the _papi_hwi_cleanup_eventset() function in papi_internal.c
* 2011-04-28 James Ralph — Uncomment the actual signal passing functionality in _papi_hwi_broadcast_signal
* 2011-04-28 James Ralph — Include files added to papi_debug.h
* 2011-04-28 Heike Jagode — Added detailed instructions on how to build PAPI with the CUDA component
* 2011-04-27 James Ralph — Move an escape test to the outer loop in _papi_hwi_broadcast_signal.
* 2011-04-27 Vince Weaver — Clean up papi_internal.c so that functions not used outside are marked static.
* 2011-04-27 Vince Weaver — papi: Fix some memory leaks
* 2011-04-27 Vince Weaver — papi: Make functions and variables static in perf_events.c
* 2011-04-27 Vince Weaver — papi: Fix crash in error handler for pfm_get_event_code_counter()
* 2011-04-27 Vince Weaver — papi: Fix error check in native_avail.c
* 2011-04-26 Vince Weaver — AMD architectural PMU could not be detected for family 15h as there was a strict check for AMD family 10h. Enabling it now for all families from 10h.
* 2011-04-26 Vince Weaver — There is no kernel support for AMD family 15h northbridge events, disabling them in libpfm3 to not report them as available native events.
* 2011-04-26 Vince Weaver — Add some extra debug messages for better tracking of the   --with-assumed-kernel configure option.
* 2011-04-25 Vince Weaver — Add a new configure option:   --with-assumed-kernel=<ver> This allows you to specify a kernel revision to (instead of being   autodetected with uname) for perf_event workaround purposes.  With   this you can force PAPI to not use workarounds on kernels with   backported versions of perf_event features.
* 2011-04-19 Vince Weaver — Add debugging to sys_perf_event_open.c to show exactly what   values are being passed to the perf_event_open syscall.
* 2011-04-18 James Ralph — Fix for finding attach_target with execlp to search the path.
* 2011-04-14 Vince Weaver — Rename the linux-ia64-* files to be called perfmon-ia64-*
* 2011-04-14 Vince Weaver — Patch to have libpfm3 use 6 counters on Interlagos.
* 2011-04-14 Vince Weaver — Fix the POWER cache detection routines to work properly on POWER7.
* 2011-04-14 Vince Weaver — Have configure check for ifort if gfortran, etc, not found.
* 2011-04-14 Vince Weaver — Update the validation message on the ctests/johnmay2.c test to be   less confusing.  Also add some comments to the source code.
* 2011-04-13 Vince Weaver — Remove the accidentally added ctests/multiattach2 and add instead the proper ctests/multiattach2.c
* 2011-04-13 James Ralph — components_config.h is cleaned out with make clobber, not make clean this should fix the build bot issues.
* 2011-04-13 Philip Mucci — Minor typos in comments. Discovered another bug in attach code demonstrated by multiattach2. You cannot have an eventset running that is self counting as well as one that is attached. PAPI thinks that both are running and throws an error.
* 2011-04-13 Philip Mucci — We must update the control state after attaching for perf_events, zero_attach now passes
* 2011-04-13 Philip Mucci — This commit adds testing of attaching to fork/exec'd executables. zero_attach and multiattach just test forks. This also modifies do_loops.c to be able to generate a test driver when -DDUMMY_DRIVER is defined so we can use it to generate flops as a sub process.
* 2011-04-13 Philip Mucci — Make sure the two processes compute different numbers of flops to test attach
* 2011-04-05 James Ralph — Turns out Maynard Johnson answered my questions about the native_name enum back in December. ( this is a correct version of the events file )
* 2011-04-04 James Ralph — Clear out the components_config.h file on make clobber
* 2011-04-04 James Ralph — Initial support for power7 aix, the events file is a copy of power6_events.h with the number of groups changed. The native_name enum is unchanged, but unused?
* 2011-04-01 James Ralph — Commited wrong configure.in
* 2011-04-01 James Ralph — Clean up setting bitmode flags for non-gcc (xlc in this case) compilers.
* 2011-04-01 Vince Weaver — Change the Nehalem PAPI_FP_OPS event from   FP_COMP_OPS_EXE:SSE_SINGLE_PRECISION+FP_COMP_OPS_EXE:DOUBLE_PRECISION to   FP_COMP_OPS_EXE:SSE+FP_COMP_OPS_EXE:X87
* 2011-03-28 James Ralph — Turns out that getopt_long isn't as standard as I had hoped.
* 2011-03-25 James Ralph — Multiplex_cost utility.
* 2011-03-25 James Ralph — Split off the statistics functions from cost.
* 2011-03-22 Heike Jagode — Exclude some fork/thread tests from fulltest that won't run with CUDA (reason: cannot invoke same GPU from different threads)
* 2011-03-21 James Ralph — Add a test for DERIVED_[ADD | SUB ] events to papi_cost.
* 2011-03-18 Heike Jagode — all_native_events ctest failed when CUDA Component is used. Reason: removing cuda events from the eventset is currently not supported. According to the NVIDIA folks this is a bug in cuda 4.0rc and will be fixed in rc2. Note also, several fork and thread tests fail since it's illegal to invoke the same GPU device from different processes / threads. We need a mechanism that allows us to run tests for the CPU component only.
* 2011-03-15 James Ralph — Add a test case to cost util, look for a derived-postfix event and if found, give timing information for read calls to it.
* 2011-03-11 Heike Jagode — Added CUDA component, a hardware performance counter measurement technology for the NVIDIA CUDA platform which provides access to the hardware counters inside the GPU. PAPI CUDA is based on CUPTI support - shipped with CUDA 4.0rc - in the NVIDIA driver library. In any environment where the CUPTI-enabled driver is installed, the PAPI CUDA component can provide detailed performance counter information regarding the execution of GPU kernels.
* 2011-03-11 James Ralph — Add some missing includes to components.
* 2011-03-11 Vince Weaver — The SYNC_READ workaround in perf_events.c was being handled at compile time, rather than at run-time like all of our other workarounds.
* 2011-03-09 Vince Weaver — Between 4.0.0 and 4.1.0 a pthread_exit() call was added to ctest/multiplex1_pthreads.c that caused the test to exit partway through the test and without doing a proper PASS/FAIL result.
* 2011-03-09 Vince Weaver — Add missing header needed by --with-virtualtimer=times build.
* 2011-03-01 Vince Weaver — Fix broken Linux/PPC build caused by my pfm_events code movement changes.
* 2011-02-25 Vince Weaver — My changes yesterday broke the perfctr build.  This should fix it.
* 2011-02-24 Vince Weaver — Make the inherit test respect TESTS_QUIET so that it does not print extra output during a run_tests.sh run
* 2011-02-24 Vince Weaver — Fix missing newline in the overflow output.
* 2011-02-24 Vince Weaver — Move the libpfm3 specific functions from perf_events.c into papi_pfm_events.c
* 2011-02-24 Vince Weaver — Separate the libpfm3-specific code from _papi_pe_init_substrate() and _papi_pe_update_control_state() into their own functions.  This will allow eventual code sharing and also make the libpfm4 merge easier.
* 2011-02-24 Vince Weaver — Some minor cleanups I found after reviewing the inherit merge.   + Add missing "static inline" to the new kernel-version codes   + Remove duplicated test for Pentium 4   + Fix a warning only seen if --with-debug is enabled
* 2011-02-24 Dan Terpstra — Merging Gary Mohr's re-implementation of inherit into the code base. Thanks, Gary!
* 2011-02-23 Vince Weaver — Move some more duplicated OS common code (in this case the locking code and the context accessing code) out of the various substrate include files and into a common location.
* 2011-02-22 Vince Weaver — Separate out the kernel-version dependent checks and group them together near the beginning of the code.  This not only allows us to easily see which routines are kernel-version dependent, but it makes it easier to disable the checks one-by-one when debugging kernel-version related issues like those found with the inherit patches.
* 2011-02-21 James Ralph — Extend _papi_hwi_cleanup_eventset to free memory and better cleanup after us.
* 2011-02-18 James Ralph — PAPI_assign_eventset_component changed; refuses to reassign components.
* 2011-02-17 Vince Weaver — Add support for AMD Family 15h processors. Also adds suport for Family 10h RevE
* 2011-02-17 Vince Weaver — Modify papi_native_avail to properly handle event names with libpfm4-style  "::" separators in them.
* 2011-02-15 James Ralph — make install-doxyman will build/install the doxygen version of the manpages.
* 2011-02-15 James Ralph — Add install target for doxygen generated man pages.
* 2011-02-11 Vince Weaver — perfctr-2.6.42 introduced PERFCTR_X86_INTEL_WSTMR PAPI added support for PERFCTR_X86_INTEL_WSMR notice the missing T
* 2011-02-09 Heike Jagode — Added function pointer destroy_eventset to the PAPI vector table. Needed for the CUDA Component to disable CUDA eventGroups, to destroy floating CUDA context, and to free perfmon hardware on the GPU. (Note: the CUDA Component cannot be released yet since we are still under NDA with NVIDIA. Stay tuned.)
* 2011-02-07 Vince Weaver — The cpuid leaf2 code was printing a message to stderr if leaf4 was needed (only happens on Westmere currently).  Change this to be a MEMDBG() debug message instead.
* 2011-02-03 Vince Weaver — perfctr-x86 was reporting "Core i7" instead of "Nehalem".  i7 can mean Westmere or Sandy Bridge too, so change the code to properly report Nehalem.
* 2011-01-27 Harald Servat — Fix this ctest. It failed when the package was built with several components because the eventset was reused and failed to add events that were not from the first component.
* 2011-01-26 Vince Weaver — Fix Cray CLE build.
* 2011-01-26 James Ralph — Putting -Wall in cflags now requires CC = gcc
* 2011-01-26 Vince Weaver — Change the paramaters passed to update_shlib_info() to match better with those passed to get_system_info().  This only affects the substrates, outside users of PAPI will not notice this change.
* 2011-01-25 James Ralph — Make sure that aix gets -g.
* 2011-01-25 James Ralph — Give everyone else -g when configuring with debug.
* 2011-01-25 James Ralph — First run at supporting power7. NOTE: this code is only good for getting event listings eg papi_native_avail,
* 2011-01-25 Vince Weaver — Accidentally converted a function to _perfctr_ that should have stayed _linux_.
* 2011-01-25 Vince Weaver — Rename the various perfctr functions to be _perfctr_ rather than _linux_. This way _linux_ is reserved for the common functions used by all.
* 2011-01-25 Vince Weaver — Split the WIN32 specific code out from the new linux common code.
* 2011-01-24 Vince Weaver — Fix a compile error that only shows up on PPC.
* 2011-01-24 Vince Weaver — Fix compile warning if mmtimer is enabled.
* 2011-01-24 Vince Weaver — Missing comma in the perfctr code.
* 2011-01-24 Vince Weaver — One last batch of consolidation changes.
* 2011-01-24 Vince Weaver — Move the various Linux update_shlib_info() functions into a common place.
* 2011-01-24 Vince Weaver — Move the various timer-related functions to linux-timer.c This gets rid of the duplicated code spread throughout the substrates.
* 2011-01-21 Vince Weaver — Updated the release docs with what I learned when making the 4.1.2.1 release.
* 2011-01-21 Vince Weaver — Currently there are at least 3 identical copies of the linux memory detection code spread throughout the PAPI source code.
* 2011-01-21 Vince Weaver — Add minimal changelog.
* 2011-01-21 Vince Weaver — Changes required for a 4.1.2.1 release
* 2011-01-20 Vince Weaver — The PAPI_HW_INT/HW_INT:RCV event should have been Nehalem only, not Westmere.
* 2011-01-20 Harald Servat — I have rebirth the installation instructions for the FreeBSD substrate. They are the same instructions as the 3.x release.
* 2011-01-19 Dan Terpstra — Add files for the 4.1.2 release.
* 2011-01-17 Vince Weaver — Ran autoconf to generate updated configure file.
* 2011-01-16 Harald Servat — Adding a component for the FreeBSD OS that reports the value of the thermal sensors available in the Intel Core processors. There are as many counters as cores, and the value reported by each counter is in Kelvin degrees.
* 2011-01-16 Harald Servat — Implemented missing _papi_freebsd_ntv_name_to_code.
* 2011-01-16 Harald Servat — Fix dependency on -ldl
* 2011-01-16 Harald Servat — Fix to compile in FreeBSD.
* 2011-01-16 Harald Servat — Code cleanup.
* 2011-01-15 Vince Weaver — [PATCH 18/18] papi: make _perfmon2_pfm_pmu_type variable static
* 2011-01-15 Vince Weaver — [PATCH 17/18] papi: remove inline_static macro in Linux only code
* 2011-01-15 Vince Weaver — [PATCH 16/18] papi: remove static inline function declaration
* 2011-01-15 Vince Weaver — [PATCH 15/18] papi: remove unused linux.h header file
* 2011-01-15 Vince Weaver — [PATCH 14/18] papi: fix array out of bounds access
* 2011-01-15 Vince Weaver — [PATCH 13/18] papi: remove unnecassary checks in configure.in
* 2011-01-15 Vince Weaver — [PATCH 12/18] papi: include perfmon header files only where necessary
* 2011-01-15 Vince Weaver — [PATCH 11/18] papi: make some functions in papi_pfm_events.c static
* 2011-01-15 Vince Weaver — [PATCH 10/18] papi: rename pfmwrap.h -> linux-ia64-pfm.h
* 2011-01-15 Vince Weaver — [PATCH 09/18] papi, linux-ia64: make inline functions static
* 2011-01-15 Vince Weaver — [PATCH 08/18] papi: fix _papi_pfm_ntv_name_to_code() function interface
* 2011-01-15 Vince Weaver — [PATCH 07/18] papi: fix spelling modifer -> modifier
* 2011-01-15 Vince Weaver — [PATCH 06/18] papi: define function interface in papi_pfm_events.h
* 2011-01-15 Vince Weaver — [PATCH 05/18] papi: rename linux.c -> perfctr.c
* 2011-01-15 Vince Weaver — [PATCH 04/18] papi: make _papi_pfm_init() static by moving it to perfctr-x86.c
* 2011-01-15 Vince Weaver — [PATCH 03/18] papi: make some functions static in perfmon.c
* 2011-01-15 Vince Weaver — [PATCH 02/18] papi: do not compile libpfm examples to support cross compilation
* 2011-01-15 Vince Weaver — To cross compile papi we need to pass the architecture to libpfm. Otherwise it will be confused and tries to build the host's make targets with the cross compiler ending up in the following error:
* 2011-01-14 Vince Weaver — Temporarily back out the FreeBSD makefile change that breaks the build so that I can properly test some other changes.
* 2011-01-14 Vince Weaver — Change the Core2 L1_TCM preset to be LLC_REFERENCES
* 2011-01-14 Dan Terpstra — Update to match current configure.in
* 2011-01-14 Dan Terpstra — Fix the if / fi syntax of the last change.
* 2011-01-13 Dan Terpstra — Changes from Harald Servat for freebsd support. Note that configure has not been regenerated from this version of configure.in.
* 2011-01-13 Dan Terpstra — Change version numbers to 4.1.2 in preparation for a release.
* 2011-01-12 Vince Weaver — The code2name test was assuming that the native events start right at PAPI_NATIVE_MASK.  We specifically document elsewhere this might not be the case, and indeed for the libpfm4 code this fails.
* 2011-01-06 Vince Weaver — Fix a long-standing bug where we were walking off the end of the EventInfoArray in remap_event_position().
* 2010-12-20 Heike Jagode — Problem on POWER6 with AIX: pm_initialize() cannot be called multiple times with PM_CURRENT. Instead, use the actual proc type - here PM_POWER6 - and multiple invocations are no longer a problem. Ctests/multiplex1.c passes now.
* 2010-12-15 James Ralph — If we don't run any tests, get buildbot's attention.
* 2010-12-14 Heike Jagode — number_of_nodes var was set to zero in _aix_get_system_info. This caused the papi utilities to report that the number of total CPUs is zero. This also caused ctests/hwinfo to fail on POWER6 with AIX.
* 2010-12-13 James Ralph — Slight re-ordering of the no_vararg_macro debug statements. (I actually tested the changes with --with-debug and without on aix)
* 2010-12-10 James Ralph — Change the syntax on our find command to be more posix compliant.
* 2010-12-10 Vince Weaver — Update configure file to be aware of the existence of AIX-Power7.
* 2010-12-09 James Ralph — Make our grep invocation posix compliant. (--invert-match == -v & --regex == -e )
* 2010-12-09 Heike Jagode — Separate 'indent' check-in so that the previous modifications are comprehensible :)
* 2010-12-09 Heike Jagode — The overflow_allcounters test failed on Power6 with AIX (pmapi) but passes on Power6 with linux (perf_events | perfctr). Therefore detect if we're running on AIX, print a warning, but still pass the test.
* 2010-12-09 James Ralph — Move away from echo -n to the shell builtin printf (echo -n is not portable)
* 2010-12-09 James Ralph — Skip the non-test ctests/burn executable.
* 2010-12-09 James Ralph — Change documentation for matlab integration to reflect the need to link to the libpapi.so library and not the static one.
* 2010-12-08 James Ralph — Clean up (purge) references to libpfm-2.x in configure and run_tests.sh
* 2010-12-08 James Ralph — MATLAB fixups: Calls to PAPI('stop') now stop counting even if we ignore the return values.
* 2010-12-08 James Ralph — Fixup for papi matlab integration.
* 2010-12-08 James Ralph — mex does not like c++ style comments (double-backslash)
* 2010-12-06 Dan Terpstra — Resolved a couple type cast warnings. Also initialized a variable and enabled GET_OVERFLOW_ADDRESS code in two places. The overflow test suite still has a number of failures and is disabled in configure.
* 2010-11-24 James Ralph — That last commit was lacking in creativity... By having the debug function names still a macro, we get all the goodness of __FILE__ etc bing in the right place and still not using variadic macros.
* 2010-11-23 James Ralph — Turns out that when DEBUG and NO_VARARG_MACRO are true, we didn't correctly implement component-level debug functions. This change uses variable argument lists ( man stdarg) to correctly handle this case. ( papi_internal.h defines these)
* 2010-11-23 Vince Weaver — Enable the PAPI_HW_INT event on Nehalem, as tests show the   HW_INT:RCV event is the proper one to use here.
* 2010-11-22 Vince Weaver — Update the preset events for Nehalem, as contributed by    Michel Brown.
* 2010-11-19 Dan Terpstra — Address problem with overflow handler continuing to count events. Add overflow status field to determine if an event set has any events enabled for overflow. Use IOC_REFRESH instead of IOC_ENABLE when overflowing. Implement IOC_REFRESH at end of overflow handler. None of this worked. Also implemented an IOC_DISABLE at top of overflow handler. That worked, even though it's suboptimal.
* 2010-11-17 Dan Terpstra — test_fail_exit() substituted for test_fail(). This became necessary because PAPI_event_name_to_code now returns a PAPI_EATTR error if the base name matches but attribute names don't. This utility was producing an error message and then running the test. Perfctr implementations will happily add a base name with no umasks and then generate 0 counts. This fix prevents that behavior.
* 2010-11-17 Dan Terpstra — Rewrite of test_fail_exit() to call test_fail(). It should be noted that test_fail_exit() behaves the way test_fail() used to behave, i.e. it exits after printing the fail message. However, test_fail no longer exits as that was causing problems with multi-threaded tests not freeing memory. In those cases where an exit is desired, calls to test_fail_exit() should be substituted for calls to test_fail().
* 2010-11-17 Dan Terpstra — Added 3 new error codes: PAPI_EATTR, PAPI_ECOUNT, and PAPI_ECOMBO. These map onto equivalent errors in libpfm and are provided to give more detail on failures in libpfm calls. A new error mapping function has been added to papi_pfm_events.c to map libpfm errors to PAPI errors, and this function is employed in the compute_kernel_args function in perfmon.c. It could also be deployed elsewhere, but so far is not.
* 2010-11-09 Vince Weaver — The cpuid change yesterday broke compilation on a 32-bit Pentium 3. Fix the inline assembly to compile properly there too.
* 2010-11-08 Vince Weaver — Fix configure script to properly detect Pentium M machines.
* 2010-11-08 Vince Weaver — Add cpuid leaf4 cache detection support.
* 2010-11-08 Vince Weaver — Add perfctr Westmere support.
* 2010-11-06 Vince Weaver — Replace KERNEL_CHECKS_SCHEDUABILITY_UPON_OPEN with the proper dynamic kernel version number checking.  This should be the last place in our perf_events code that was using a hard-coded rather than dynamic check for a kernel-version related bugfix.
* 2010-11-06 Vince Weaver — This patch allows PAPI to read multiple events at a time out of the kernel when the kernel is new enough (2.6.34 or newer).  The previous code required setting a #define by hand to get this behavior, this new code picks the proper way to do things based on the kernel version number.
* 2010-11-04 Vince Weaver — Replace occurrances of PERFCTR_X86_INTEL_COREI7 with PERFCTR_X86_INTEL_NHLM as the former has been documented as being deprecated as of perfctr 2.6.41.
* 2010-11-03 sbk — Change "unicos" to "CLE" since "unicos" no longer exists.
* 2010-10-26 James Ralph — Add a call to PAPI_thread_init(), Thanks to Martin Schindewolf for pointing this out.
* 2010-10-21 James Ralph — Fixup url's that checkbot was finding in error.
* 2010-10-05 Vince Weaver — The zero_attach and multiattach were forking before off children   before testing that PAPI in fact is available.  Then when PAPI_init()   failed the children weren't being cleaned up properly.  This was   confusing build bot.  This changeset moves the fork to after the   check plus do a fail_exit() on failure.
* 2010-10-05 Vince Weaver — Solaris build will fail if /usr/ccs/bin isn't in the path. Have it check there for "ar" on Solaris systems if it can't be found   by normal methods.
* 2010-10-05 Vince Weaver — Only run the EAR tests on itanium systems.
* 2010-10-05 Vince Weaver — Pentium4-perfctr was skipping most of the CTESTS.  Make sure they are all run.
* 2010-10-01 Dan Terpstra — MInor change in how to upload a tarball to the website.
* 2010-10-01 Vince Weaver — Fix the build on linux-pfm-itanium2 that was broken due to some of the configure changes yesterday.
* 2010-10-01 Dan Terpstra — Add new change log for this release. Generated with the cool cvs2cl.pl perl script.
* 2010-10-01 Dan Terpstra — Update RELEASENOTES to reflect changes in 4.1.1 release. Tweak release_procedure to reflect alternate ChangeLog creation.
* 2010-10-01 James Ralph — Bump version numbering in doxygen config files for impending release. note to future release-wizards to do so.
* 2010-09-30 Vince Weaver — When --with-OS=CLE is enabled, check the kernel version and use perfmon2 for old kernels and perf_events for new kernels.
* 2010-09-30 Vince Weaver — If no sources of perf counters are available, then use the generic_platform substrate instead.
* 2010-09-30 Vince Weaver — If you specify --with-perf-events or --with-pe-include but the required perf_event.h header is not available, then have configure fail with an error.
* 2010-09-30 Dan Terpstra — Bump version number to 4.1.1 in affected files. Also bump requirement for kernel from 2.6.31 to 2.6.32. This in prep for the pending release.
* 2010-09-30 Dan Terpstra — Bump version number to 4.1.1 in affected files. This in prep for the pending release.
* 2010-09-30 Vince Weaver — Hope this late commit doesn't interfere with anything.  This updates the INSTALL.txt to reflect all of the improvements we've made to perf_event support since the last release.
* 2010-09-29 Vince Weaver — The -Werror problem was still occurring on ia64/perfmon compiles, as I hadn't updated Rules.pfm
* 2010-09-29 Dan Terpstra — Remove support for the perf_counter interface in kernel 2.6.31. Now supports only the perf_event interface in kernel 2.6.32 and above.
* 2010-09-22 Vince Weaver — Attempt to add mmtimer support to perf_events substrate.
* 2010-09-22 Vince Weaver — The multiplex code currently does not make a final adjustment at the time of MPX_read().  This is to avoid the case where counts could be decreasing if you have multiple reads returning estimated values before the next actual counter read.
* 2010-09-22 Vince Weaver — This is our only test that checks to see if multiplexed values are non-decreasing or not.  Unfortunately the test currently doesn't fail if values do go backward.
* 2010-09-17 Vince Weaver — Fix conflicts from merge.
* 2010-09-15 Vince Weaver — Finally fix the -WExtra problem.
* 2010-09-13 Vince Weaver — Fix the missing files from the import (CVS claims this as a "conflict")
* 2010-09-08 James Ralph — Fixed the recipies for [c|f]tests and utils. $(LIBRARY) => $(papiLIBS) (this way we don't build libpapi.a if we won't want it)
* 2010-09-03 Vince Weaver — Had a "%d" instead of "%lld" in that last commit.
* 2010-09-03 Vince Weaver — Give a more detailed error message on the sdsc-mpx test.
* 2010-09-02 Vince Weaver — Remove code that reported ENOSUPP if HW multiplexing is not available.
* 2010-09-01 Vince Weaver — Explicitly set the disabled flag to zero in perf_events for new events.
* 2010-08-31 James Ralph — Initial stab at a coretemp component.
* 2010-08-30 Vince Weaver — F_SETOWN_EX is not available until 2.6.32, so don't use it unless we are running on a recent enough kernel.
* 2010-08-30 Vince Weaver — Pentium 4 was not supported by perf_events until version 2.6.35. Print an error if we attempt to use it on an older kernel.
* 2010-08-27 Vince Weaver — The "overflow_allcounters" test failed on perfmon2 kernels   because the behavior of a counter on overflow differs between   the various substrates.
* 2010-08-27 Dan Terpstra — updating
* 2010-08-27 Dan Terpstra — removing westmere documentation
* 2010-08-27 Vince Weaver — Fix warning in compile due to missing parameter in a debug statement.
* 2010-08-27 Vince Weaver — In the ctests, test_skip() was attempting a PAPI_shutdown() before exiting.   On multithreaded tests (that had already spawned threads before the   decision to skip) this really causes the programs to end up confused   and reports spurious memory errors.
* 2010-08-26 Vince Weaver — byte_profile was failing on systems where fp_ops is a derived event.
* 2010-08-26 Vince Weaver — At PAPI_stop() time a counter with overflow enabled is being adjusted by a   value equal to the sampling period.
* 2010-08-26 Vince Weaver — Add validation check to overflow_allcounters
* 2010-08-26 Vince Weaver — On Power5 and Power6, hardware counters 5 and 6 cannot generate interrupts.
* 2010-08-26 Vince Weaver — Change some debug messages to be warnings instead of errors.
* 2010-08-26 Vince Weaver — Fix ctests/second on bluegrass (POWER6)
* 2010-08-25 Vince Weaver — Add support for including the OS version in the component_info_t struct.
* 2010-08-25 Vince Weaver — Update all_native_events ctest to print warning in the case where we skip events because they aren't implemented yet (offcore and uncore mostly).
* 2010-08-24 Vince Weaver — Adds a new "test_warn()" function for the ctests.
* 2010-08-24 Vince Weaver — From what I can tell, on perf_events the overflow PAPI_OVERFLOW_FORCE_SW case was improperly falling through in _papi_pe_dispatch_timer() to also run the HARDWARE code.
* 2010-08-24 Vince Weaver — Some minor changes to the ctests.
* 2010-08-20 Vince Weaver — Disable CFLAGS += $(EXTRA_CFLAGS) (-Wextra) for now.  This will get buildbot running again, and if I can manage to figure out exactly what the Makefiles are doing I'll re-enable it again.
* 2010-08-20 Vince Weaver — Add support for Pentium 4 under perf events.  This requires a 2.6.35 kernel. On p4 perf events requires a special format for the raw event, so we modify   the results from libpfm3 to conform to what the kernel expects.
* 2010-08-20 James Ralph — release_procedure updated to reflect files to keep under /doc
* 2010-08-18 Vince Weaver — Patch from Gary Mohr that allows PAPI on perf events to catch permissions   problems at the time of configuration, rather than only appearing   once papi_start() is called.
* 2010-08-05 Vince Weaver — Use F_SETOWN_EX instead of F_SETOWN in tune_up_fd()
* 2010-08-04 Vince Weaver — This is the PAPI_CPU_ATTACH patch from Gary Mohr that also fixes a  problem with multiple event sets on perf events.
* 2010-08-03 Heike Jagode — The option --with-no-cpu-counters was not supported on AIX. This has been fixed and works now. Also the get_{real|virt}_{cycles|usec} implementations for AIX (checked in Jul 29) have now been tested and work correctly.
* 2010-07-29 Heike Jagode — Added AIX support for the get_{real|virt}_{cycles|usec} functions +++ Fortran tests are now compiling on AIX. Wrong compiler flags were used for the AIX compilers.
* 2010-07-27 Vince Weaver — add PAPI_L1_DCM for atom
* 2010-07-27 Vince Weaver — Update the x86 cache_info table.
* 2010-07-16 Vince Weaver — Perf Events now support attach and detach.
* 2010-07-16 Vince Weaver — Add a few missing events to Nehalem, based on reading Intel Volume 3b.
* 2010-07-16 Vince Weaver — Fix Westmere to not use L1D_ALL_REF:ANY
* 2010-07-16 Vince Weaver — Enable support for having more than one CPU block with the same name in the .csv file. This allows easier support for sharing events between similar architectures.
* 2010-07-03 Brian Sheely — Added remaining low-level api tests
* 2010-06-21 Dan Terpstra — Updated for PAPI version 4.1.
* 2010-06-21 Dan Terpstra — Add edited change log for 4.1 release.
* 2010-06-21 Dan Terpstra — Minor syntax changes and amplifications. I'm picky.
* 2010-06-21 Dan Terpstra — Change version numbers in anticipation of the impending 4.1 release.
* 2010-06-21 Dan Terpstra — Change version numbers in anticipation of the impending 4.1 release.
* 2010-06-18 James Ralph — Friday afternoon typo... the command given for generating all documentation was wrong
* 2010-06-18 Vince Weaver — Correct a comment.
* 2010-06-18 James Ralph — Updated INTSALL.txt to mention doxygen.
* 2010-06-18 James Ralph — Fixed some of the comments to get doxygen's attention /* -> /**
* 2010-06-18 James Ralph — Added a small section about components on the main doxygen generated page.
* 2010-06-18 James Ralph — Upped the version number in doxygen config files for upcoming release.
* 2010-06-17 Heike Jagode — Added documentation (Doxygen) for InfiniBand component.
* 2010-06-17 Heike Jagode — Added documentation (Doxygen) for InfiniBand (and lustre) component.
* 2010-06-17 Heike Jagode — Added new component for infiniband devices. Major changes for lustre component.
* 2010-06-15 James Ralph — Added documentation for the several components. Doxygen will now search recursivly under the components directory for documented *.[c|h] files ( /** @file */ somewhere in it).
* 2010-06-15 Vince Weaver — Update INSTALL.txt with information on using PAPI with Perf Events.
* 2010-06-14 Dan Terpstra — Minor tweak to make sure libpfm builds without warnings.
* 2010-06-11 Brian Sheely — Added first few api test cases
* 2010-06-11 Heike Jagode — removed compiler warnings for lm-sensors component; switched to stderr so that papi_xml_event_info creates a clean output.
* 2010-06-10 Brian Sheely — Added test_fail_exit for use in single threaded tests
* 2010-06-09 Vince Weaver — Fix conflicts from import.
* 2010-06-09 Vince Weaver — Initial revision
* 2010-06-09 Vince Weaver — Properly attribute the example component code.
* 2010-06-08 Dan Terpstra — Bump versioning to 4.1
* 2010-06-08 Dan Terpstra — Bump version number in preparation for a 4.1 release.
* 2010-06-07 Brian Sheely — ctests/api (not yet implemented) added to default ctests
* 2010-06-07 Brian Sheely — Added freq.c to build
* 2010-06-07 Brian Sheely — Moved timer impl from any-null.c into papi_vector.c and added generic functionality to compute frequency if unable to determine based on platform
* 2010-06-07 Brian Sheely — pmapi is required for AIX even without cpu counters in order to set frequency for timer functions
* 2010-06-07 Brian Sheely — Added new error code
* 2010-06-03 Brian Sheely — Initial commit for ctests/api which is not yet implemented
* 2010-06-03 Brian Sheely — Updated to correspond to currently supported platforms, configuration, etc.
* 2010-06-03 Brian Sheely — Added test to allow AIX to be built without cpu counters
* 2010-06-02 Brian Sheely — Fixed for BG/P
* 2010-06-02 Brian Sheely — BG/P fix
* 2010-06-02 Brian Sheely — Fixed BG/P compile issues
* 2010-06-02 Brian Sheely — Reverted to previous CC and F77 settings for BG/P
* 2010-06-02 Brian Sheely — Regenerated for current configure.in (1.216) using autoconf v2.63
* 2010-06-01 Brian Sheely — Rolled back previous changes
* 2010-06-01 James Ralph — Initial support for OS X.
* 2010-06-01 Brian Sheely — Added code to define _rtc when Cray is compiled with gcc
* 2010-06-01 Vince Weaver — Fix typo in README
* 2010-06-01 Brian Sheely — Fixed issue with malloc called with size 0
* 2010-05-28 Brian Sheely — Removed all compiler warning flags for xlc
* 2010-05-27 Brian Sheely — AIX uses its specific set of ctests as before any recent changes
* 2010-05-27 Vince Weaver — Add example component.
* 2010-05-27 Brian Sheely — frequency initialized to -1 to prevent division by zero
* 2010-05-27 Brian Sheely — Regenerated due to additions in configure.in related to time stamp counters
* 2010-05-27 Brian Sheely — --with-no-cpu-component renamed --with-no-cpu-counters
* 2010-05-27 Brian Sheely — Removed papi_mem_info from --with-no-cpu-component configuration since that info is still initialized by the substrate
* 2010-05-27 Brian Sheely — Fixed bug to allow papi_native_avail to pass without cpu component
* 2010-05-27 Brian Sheely — Rollback last change
* 2010-05-27 Brian Sheely — Attempt to fix xlc compile errors
* 2010-05-26 Brian Sheely — xlc given precedence over gcc
* 2010-05-26 Brian Sheely — Implemented TSC code (cycles.h). NOTE: Not tested on BGP or AIX an WIN32 incomplete.
* 2010-05-25 Brian Sheely — Added papi_native_avail to utils available with no cpu component
* 2010-05-21 Dan Terpstra — Remove some obsolete patch commands. Per Will Cohen.
* 2010-05-21 Brian Sheely — Added cycle.h to --with-no-cpu-component build. Fortran compiler search looks for gfortran.
* 2010-05-21 Brian Sheely — Use MISCHDRS from configure
* 2010-05-20 Brian Sheely — CLAGS and FFLAGS now retain any initial settings
* 2010-05-20 Brian Sheely — Fixed compile error and warnings. Added option to configure
* 2010-05-19 Dan Terpstra — Hard-code an exception for Nehalem OFFCORE_RESPONSE_0. This event can't be counted because it uses a shared chip-level register.
* 2010-05-19 Brian Sheely — Fixed compile warnings
* 2010-05-19 Brian Sheely — Fixed debug compile error and resolved warnings
* 2010-05-19 Brian Sheely — Fixed warning in ia64
* 2010-05-19 Dan Terpstra — Latest changes from Will Cohen to bring the spec file current with cvs.
* 2010-05-19 Brian Sheely — Extra compiler warning flags are not added until after the libpfm build
* 2010-05-18 Brian Sheely — Added AIX and BGP code. NOTE: Not tested
* 2010-05-18 Brian Sheely — Corrected for powerpc
* 2010-05-18 Brian Sheely — Added model numbers for P3. No performance interface results in generic platform (no cpu component)
* 2010-05-17 Brian Sheely — Fixed itanium build
* 2010-05-14 Vince Weaver — Temporary fix to emulate cycles HW counter on BlueGeneP using the get_cycles() call.
* 2010-05-13 Brian Sheely — Replaced missing MEMSUBSTR macro in configure. AC_ARG_ENABLE macros replaced with AC_ARG_WITH macros. Continued changes for --with-no-cpu-component
* 2010-05-13 Brian Sheely — added missing C library headers
* 2010-05-13 Brian Sheely — fixed compile errors on torc0 by including missing C library headers
* 2010-05-11 Brian Sheely — Solaris builds without cpu component
* 2010-05-11 Brian Sheely — FFLAGS set to null for CLE
* 2010-05-11 Brian Sheely — Changes to support --with-no-cpu-component
* 2010-05-10 Brian Sheely — Restored --with-perfmon=<x.y> option
* 2010-05-07 Brian Sheely — Added --with-no-cpu-component option which has only been tested on x86
* 2010-05-07 James Ralph — Added makefile in doc to generate user and developer documentation.
* 2010-05-07 Heike Jagode — papi_xml_event_info generated some invalid xml output. This bug was introduced in Revision 1.10
* 2010-05-06 Brian Sheely — removed omp tests
* 2010-05-05 Brian Sheely — Removed hard coded disable_shared and disable_static values for CLE builds
* 2010-05-05 Brian Sheely — rolling back last change which included some onging development that is not finished
* 2010-05-04 Brian Sheely — Removed hard coded disable_shared and disable_static values for CLE builds
* 2010-05-04 Brian Sheely — Resolved configure bug with --with-perfmon and added default include macro for non-gcc compiles
* 2010-05-03 Brian Sheely — Removed obsolete file
* 2010-05-03 James Ralph — Updated Harald Servat's freebsd work to Component Papi.
* 2010-05-03 James Ralph — Removed a holdout from catamount support, are there any platforms where we don't get malloc from stdlib?
* 2010-05-03 Brian Sheely — Added README which contains basic instructions on how to add a new component
* 2010-04-30 Brian Sheely — Adding new components no longer requires modification of Papi code
* 2010-04-30 Dan Terpstra — Add a few more steps on testing a patch.
* 2010-04-30 Dan Terpstra — Add note about cvs date string version incompatibilities.
* 2010-04-29 Brian Sheely — Fixed compile issue with freebsd build
* 2010-04-29 Brian Sheely — Created new build environment for components
* 2010-04-29 Dan Terpstra — Bump version number to 4.0.0.3 to match the latest (forthcoming) patch.
* 2010-04-29 Dan Terpstra — Modify arguments for patching to ignore white space and blank lines. This can dramatically reduce diff file sizes, especially when indent has been applied :)
* 2010-04-28 Heike Jagode — Bug-fixings: Number of lustre counter in _init; _read and _stop didn't work correctly due to incorrect number of counters.
* 2010-04-22 Vince Weaver — Fix papi_native_avail to return properly when using the -e option. Before, an error condition was always returned even if the event was reported properly. This was most notable on machines using a batch system, such as BlueGeneP.
* 2010-04-21 Brian Sheely — removed code that was commented out (accidentally uncommented out on last commit
* 2010-04-20 Brian Sheely — Removed code for obsolete platforms
* 2010-04-20 Brian Sheely — Updated on 3.7 branch
* 2010-04-20 Brian Sheely — Modified configure.in to make to easier to maintain. NOTE: most of the code was touched so extensive testing is recommended
* 2010-04-16 Heike Jagode — Fixed compilation errors for AIX which were due to missing inclusion of new header file papi_defines.h.
* 2010-04-16 Heike Jagode — After further investigations of the stack corruption issue on BGP, the real problem has been nailed down. The size of the PAPI_event_info_t struct is different on BGP systems which is due to a bigger PAPI_MAX_INFO_TERMS value. A _BGP was defined at configure time to differentiate between BGP and other systems. However, the problem is that a user program does not know this macro. When PAPI_event_info_t is initialized to zero, the beginning of the user program's stack frame is zeroed out --> BAD. It was fun, though.
* 2010-04-15 Brian Sheely — Added files
* 2010-04-12 Brian Sheely — Added Lustre component to build
* 2010-04-12 Brian Sheely — Fixed compile warnings
* 2010-04-09 Brian Sheely — Removed support for ppc32 architectures. Removed support for perfmon versions older than 2.5 except for Itanium. Removed all code related to POWER3 and POWER4.
* 2010-04-09 Haihang You — add lustre component
* 2010-04-09 Haihang You — add lustre host code contributed by Michael Kluge
* 2010-04-09 Brian Sheely — Simplified Rules files by moving code to configure.in
* 2010-04-08 Brian Sheely — Removed recently added include file since that file is now included in the header which is included here
* 2010-04-08 Brian Sheely — Added new include file
* 2010-04-06 Heike Jagode — A stack corruption on BGP was caused after returning from PAPI_get_event_info(); this was due to setting all bits to zero (using memset) in _papi_hwi_get_native_event_info() and _papi_hwi_get_event_info()
* 2010-04-06 Heike Jagode — Missing declaration of PAPI_MAX_LOCK (fixed for linux-bgp only)
* 2010-04-06 Brian Sheely — Removed references to libpfm-2.x
* 2010-04-06 Brian Sheely — Removed unused dir
* 2010-04-06 Brian Sheely — Removed unused dir
* 2010-04-05 Brian Sheely — Removed references to perfctr versions older than 2.6
* 2010-04-05 Brian Sheely — Resolved compile warning
* 2010-04-05 Brian Sheely — Modified code to exit properly on test failure
* 2010-04-05 Brian Sheely — Included new header file
* 2010-04-01 Vince Weaver — Enable L1D:REPL as PAPI_L1_DCM on Nehalem.
* 2010-04-01 Brian Sheely — Prevent output after test failure
* 2010-04-01 Brian Sheely — Modified code so that a test failure within a thread does not prevent other threads from freeing memory
* 2010-03-31 Brian Sheely — Code change to resolve memory leak should be limited to Itanium builds but may need to be applied to BG/P builds as well
* 2010-03-31 Brian Sheely — Rolled back last change which resolved memory leak on one machine but caused seg faults on other machines
* 2010-03-31 Brian Sheely — Fixed memory leaks
* 2010-03-31 Brian Sheely — Fixed memory leak
* 2010-03-31 Brian Sheely — Fixed memory leak
* 2010-03-30 Brian Sheely — Fixed memory leaks
* 2010-03-30 Brian Sheely — Eliminated potential bug with locks
* 2010-03-30 Vince Weaver — Fix conflict from merge.
* 2010-03-29 Brian Sheely — Fixed last remaining logic error related to overflow
* 2010-03-29 Brian Sheely — Fixed buffer overflow debug output related to threads.c. Rolled back change to pthrtough.c
* 2010-03-29 Brian Sheely — Added  to ctests make line. Note that the CFLAGS macro in ctests/Makefile is overwritten by Makefile.inc
* 2010-03-25 Brian Sheely — Fixed buffer overflow debug warnings
* 2010-03-25 Brian Sheely — Removed unregister_pthreads which was a duplicate of zero_pthreads
* 2010-03-23 James Ralph — The rest of the low-level api is doxygenated, save PAPI_read_ts() PAPI_add_pevent PAPI_save PAPI_restore
* 2010-03-23 Brian Sheely — rolling back last change
* 2010-03-23 Brian Sheely — fixed the cause of false buffer overflow debug messages
* 2010-03-23 Brian Sheely — Eliminated inconsistencies in determining size of EventInfoArray
* 2010-03-19 Brian Sheely — Add new include for remaining substrates
* 2010-03-18 Brian Sheely — Removed change that did not exist on branch
* 2010-03-18 Brian Sheely — cvs merge error
* 2010-03-18 Brian Sheely — cvs merge error
* 2010-03-18 Brian Sheely — trying to sync head and branch
* 2010-03-18 Brian Sheely — trying to sync head and branch
* 2010-03-18 Brian Sheely — trying to sync head and branch
* 2010-03-18 Brian Sheely — temp removal
* 2010-03-18 Brian Sheely — continue trying to sync head with branch manually
* 2010-03-18 Brian Sheely — continue trying to sync
* 2010-03-18 Brian Sheely — continued cvs issues
* 2010-03-18 Brian Sheely — Merge bsheely-temp branch by hand
* 2010-03-18 Brian Sheely — Merged configure.in from branch
* 2010-03-18 Brian Sheely — Merge bsheely-temp branch by hand
* 2010-03-18 Brian Sheely — replace branch with head
* 2010-03-18 Brian Sheely — merge branch by hand
* 2010-03-18 Brian Sheely — Unable to resolve conflicts or merge using CVS. Adding bsheely-temp branch code by hand.
* 2010-03-18 Brian Sheely — cvs reporting conflict that does not appear to exit
* 2010-03-16 Heike Jagode — Bug-fixing: when configuring with --with-pmapi, PM_INITIALIZE did not get defined as it should be.
* 2010-03-12 Vince Weaver — Fix PAPI support for solaris-ultra. This code had not worked for some time.
* 2010-03-12 James Ralph — Commented more of the low level api
* 2010-03-09 Dan Terpstra — Minor typo in the spec file.
* 2010-03-08 Dan Terpstra — Bump the 4th digit of the version number to indicate the patch level: 4.0.0.2
* 2010-03-05 Brian Sheely — Test now passes while testing the same functionality without memory leaks
* 2010-03-05 James Ralph — doc/doxygen_procedure.txt provides a quick overview of how to use doxygen 	for commenting the PAPI code.
* 2010-03-04 Vince Weaver — Fix conflicts from the libpfm import.
* 2010-03-04 Vince Weaver — Initial revision
* 2010-03-04 Dan Terpstra — Second fix for PAPI_set_overflow. The first fix was in the wrong place: before events were potentially remapped. This one works for three events in all cases. Tested on Intel Core2, but should work everywhere, since there are minimal changes confined to the framework layer. Copied from HEAD.
* 2010-03-04 Brian Sheely — Fixed memory leaks
* 2010-03-04 Brian Sheely — Fixed memory leaks
* 2010-03-04 Brian Sheely — Fixed memory leaks
* 2010-03-04 Brian Sheely — Fixed memory leaks
* 2010-03-04 Brian Sheely — Fixed memory leaks
* 2010-03-04 Brian Sheely — Fixed memory leaks
* 2010-03-04 Brian Sheely — Fixed memory leaks
* 2010-03-03 Vince Weaver — Fix conflicts.
* 2010-03-03 Brian Sheely — Fixed memory leaks
* 2010-03-03 Vince Weaver — Initial revision
* 2010-03-03 Vince Weaver — Now that Athlon and Pentium II events use libpfm, remove the old hard coded event table files.
* 2010-03-03 Brian Sheely — Fixed memory leaks which causes test to fail. Redesign of test required.
* 2010-03-03 Brian Sheely — Fixed memory leaks
* 2010-03-03 Brian Sheely — Fixed memory leaks
* 2010-03-02 Vince Weaver — Move Athlon and Pentium II event support to use libpfm.
* 2010-03-02 Brian Sheely — Last checkin for Wextra changes
* 2010-03-02 Brian Sheely — Added output to configure
* 2010-03-02 Brian Sheely — corrected logic errors
* 2010-03-01 Brian Sheely — corrected logic error
* 2010-03-01 Brian Sheely — Maybe this time the right code is getting checked in
* 2010-03-01 Brian Sheely — Wrong code got checked in on last commit
* 2010-03-01 Brian Sheely — Wextra is not supported on gcc 3.3
* 2010-03-01 Brian Sheely — Adding -Wextra to itanium build causes compile error in libpfm
* 2010-02-26 Brian Sheely — Fixed (debug) compile error in P3/Athlon
* 2010-02-26 Brian Sheely — Fixed (POWER) compile warnings
* 2010-02-26 Brian Sheely — Fixed (P4) compile warnings
* 2010-02-25 Brian Sheely — Fixed (perfmon) compile warnings which don't show up when building via ssh
* 2010-02-25 Brian Sheely — Fixed (perfmon) compile warnings
* 2010-02-25 Brian Sheely — Fixed (perf_event) compile warnings
* 2010-02-24 Brian Sheely — Removed Wconversion option
* 2010-02-24 Brian Sheely — Removed hack to compile without warnings using Wconversion
* 2010-02-23 Brian Sheely — Fixed (debug) compile warnings
* 2010-02-23 James Ralph — In merging conflicts from heike work, I deleted a line in papi.h
* 2010-02-23 Brian Sheely — Formatted using indent
* 2010-02-23 James Ralph — Added Doxygen tags to the following
* 2010-02-23 Brian Sheely — Fixed (debug) compile warnings
* 2010-02-22 Heike Jagode — Added missing comment closer */ This misindented the rest of the source code in windows.c
* 2010-02-22 Heike Jagode — Added and applied new PAPI-coding-style profile file
* 2010-02-22 Brian Sheely — Fixed compile warnings
* 2010-02-19 Brian Sheely — Fixed compile warnings.
* 2010-02-19 James Ralph — Added the papi library as a dependency for ctests/utils/ftests
* 2010-02-19 Brian Sheely — Fixed compile warnings.
* 2010-02-19 Brian Sheely — Fixed compile warnings.
* 2010-02-19 Brian Sheely — Fixed compile warnings.
* 2010-02-18 Brian Sheely — Fixed compile warnings.
* 2010-02-18 Brian Sheely — Fixed compile warnings.
* 2010-02-18 Brian Sheely — Fixed compile warnings (by adding implementation of strspn).
* 2010-02-18 Brian Sheely — Use cleaner workaround for unused parameters
* 2010-02-18 Brian Sheely — Restored unused parameters to resolve seg faults in ftests
* 2010-02-17 Brian Sheely — Fixed (new) compile warnings
* 2010-02-17 Dan Terpstra — Redefine event_code in PAPI_event_info_t from unsigned int to int because that is what gets exposed to the user in the public API. This will likely trigger other warnings in the framework layer.
* 2010-02-17 Dan Terpstra — Get rid of a bunch of unused parameter warnings. Thanks to Corey Ashford for the tip.
* 2010-02-17 Brian Sheely — Fixed compile warnings
* 2010-02-17 Brian Sheely — Fixed compile warnings
* 2010-02-16 Brian Sheely — Fixed (new) compile warnings
* 2010-02-16 Dan Terpstra — Cleaned up a bunch of implicit type conversions.
* 2010-02-16 Dan Terpstra — PAPI PRESET events are defined in the API as int. Somehow, they were coming out of papiStdEventDefs.h as unsigned. By casting a #define explicitly to int, they now appear as signed values. This matches the API at the user level, but will inevitably throw warnings elsewhere.
* 2010-02-16 Brian Sheely — Fixed compile warnings
* 2010-02-16 Brian Sheely — Fixed compile warnings
* 2010-02-16 Brian Sheely — Fixed compile warnings
* 2010-02-16 Brian Sheely — Fixed compile warnings
* 2010-02-16 Brian Sheely — Fixed compile warnings most of which were implicit type casting
* 2010-02-15 Dan Terpstra — Resolve event code type inconsistencies.
* 2010-02-15 Dan Terpstra — Clean up type casting warnings on event codes in papi_memory.c Don't know how to get rid of warnings on passed parameters that are only used on debug...
* 2010-02-15 Dan Terpstra — Clean up type casting warnings on event codes in papi.c
* 2010-02-15 Dan Terpstra — Remove the encode and encode2 tests that exercise PAPI_set_event_info and PAPI_encode_event API calls, since they were never supported, and generally come to be thought of as a bad idea.
* 2010-02-15 Dan Terpstra — Remove the PAPI_set_event_info and PAPI_encode_event API calls, since they were never supported, and generally come to be thought of as a bad idea.
* 2010-02-12 Brian Sheely — Fixed compile error on x86 builds when using --with-CPU
* 2010-02-12 Brian Sheely — Added -Wextra and -Wconversion switches which generate hundreds of new warnings to be cleaned up later
* 2010-02-12 Dan Terpstra — Removing all files from the perfctr-2.4.x directory. I've been wanting to do that for a long time...
* 2010-02-12 Brian Sheely — Modified code to resolve memory leaks from _papi_hwi_assign_eventset
* 2010-02-11 Brian Sheely — Fixed memory leak (no issues this time)
* 2010-02-11 Brian Sheely — Commented out recently added code to free memory
* 2010-02-10 Brian Sheely — Modified to support additional Nehalem model numbers
* 2010-02-10 Brian Sheely — Added model numbers 30, 37, 44, 46 to Nehalem configuration
* 2010-02-10 Brian Sheely — Commented out code to free memory as it causes several tests to fail
* 2010-02-10 Brian Sheely — Moved code to free memory from MPX_cleanup to MPX_shutdown to prevent seg fault in kufrin and multiplex1_pthreads
* 2010-02-09 Brian Sheely — Fixed memory leaks from test sdsc2-mpx
* 2010-02-09 Dan Terpstra — Remove an unused variable to eliminate a warning message.
* 2010-02-08 Dan Terpstra — Expanded functionality to test and demonstrate both batch and interleaved setting of overflow. See the concurrent commit of papi_internal for more details.
* 2010-02-08 Dan Terpstra — Fix for loss of state on PAPI_set_overflow. This fixes the bug reported by Rick Kufrin and Rui Liu of NCSA where add, add, overflow, overflow worked, but add, overflow, add, overflow did not. Tested on Intel Core2, but should work everywhere, since all changes are in the framework layer.
* 2010-02-04 Brian Sheely — Using any of the --with-perfctr, --with-perfmon, or --with-pfm options will allow configure to complete if no performance interface is installed.
* 2010-01-29 Dan Terpstra — Add instructions for the creation of a patch file for a PAPI release directory.
* 2010-01-27 Heike Jagode — The unit mask problem was due to two issues: (1) function pointer ntv_name_to_code was not set for perf_events and perfmon; (2) exit condition in papi was one loop iteration too late.
* 2010-01-27 Heike Jagode — Deleted unused variable.
* 2010-01-27 Heike Jagode — Got rid of unused code; it's just commented out for now. Let's see what builtbot spits out.
* 2010-01-26 Heike Jagode — Bug fixing: unit masks were left out when converting names into native event codes.
* 2010-01-26 Brian Sheely — Configuration of em64t has been removed and all Intel family 15 processors will be configured as P4.
* 2010-01-26 James Ralph — The test now opens the math library to test PAPI_get_shared_lib_info() functionality.
* 2010-01-25 Brian Sheely — Fixed remaining compile warnings
* 2010-01-25 Brian Sheely — Fixed compile warnings
* 2010-01-20 Dan Terpstra — Return failure from PAPI_set_multiplex if cidx isn't set. Previously this function passed (failed silently) if cidx wasn't set and the eventset was empty. This may trigger other errors in test cases.
* 2010-01-19 Dan Terpstra — Update ChangeLog and Release Notes in preparation for the 4.0.0 release.
* 2010-01-18 Dan Terpstra — Set SHLIB = libpapi.so.$(PAPIVER) instead of libpapi.so.3 to prevent future obsolescence.
* 2010-01-15 Heike Jagode — Correction of preset PAPI_FP_OPS on i7. Unit masks for FP_COMP_OPS_EXE cannot be combined any longer; using two counters instead
* 2010-01-15 Brian Sheely — Modified logic based on the assumption that the number of files in /sys/devices/system/cpu gives the total number of CPUs instead of the number of CPUs per node
* 2010-01-14 Dan Terpstra — Current snapshot of the FAQ on the website. This badly needs updating.
* 2010-01-14 Dan Terpstra — Change copyright years to include 2010.
* 2010-01-14 Dan Terpstra — Remove outdated Change Logs from the repository.
* 2010-01-14 Dan Terpstra — More tweaks from Corey for event rescheduling problem. Also a syntax fix for POWER platforms.
* 2010-01-13 Dan Terpstra — Final changes from Will Cohen.
* 2010-01-13 Dan Terpstra — Bump the date.
* 2010-01-13 Dan Terpstra — Fix for rescheduling events after a failed add. This addresses the NULL pointer issue found in overflow_allcounters on i7. Thanks to Corey Ashford of IBM for the fix.
* 2010-01-13 Heike Jagode — Avoid printing conditional 'if' statements while compiling (but they are performed).
* 2010-01-13 Dan Terpstra — Update per Will Cohen for simpler build instructions.
* 2010-01-13 Dan Terpstra — Change test for version number to differentiate between PAPI-C and Classic PAPI. We were testing for versions >=3 && >= .9. This was missing versions >= 4.
* 2010-01-13 Heike Jagode — Seg fault on i7 with perf_events. This was fixed a while ago for perfmon and perfctr but perf-events was left behind.
* 2010-01-13 Brian Sheely — Generated configure to correspond to ost recent change (Cray XT) to configure.in
* 2010-01-13 sbk — Enable the static perf events static table to be created and compiled in again for Cray XT CLE.
* 2010-01-13 Dan Terpstra — Update version numbers for impending release of PAPI 4.0.0.
* 2010-01-13 Dan Terpstra — Updates for impending release of PAPI 4.0.0.
* 2010-01-13 Dan Terpstra — *** empty log message ***
* 2010-01-12 Heike Jagode — Avoid creating a symbolic link of a file while the reference to this file has the same name (Power, BG, Solaris)
* 2010-01-12 Dan Terpstra — Update description for BGP.
* 2010-01-12 Dan Terpstra — Modifications to build test files for BGP.
* 2010-01-12 Dan Terpstra — Modifications to build test files.
* 2010-01-12 Dan Terpstra — Restore prior native naming convention: PNE_BGP_... Needed to avoid conflict with system level naming conventions.
* 2010-01-10 Dan Terpstra — Misplaced terminator(s) when eliminating the --with-makefile clause. This was tricky. The --with-OS and other checks were done *inside* --with-makefile. When that clause was removed, scope nesting got screwed up for the next 250 lines. BG/P uses --with-OS, so the problem showed up here.
* 2010-01-08 Dan Terpstra — Eliminate duplicate definitions of environment variable for the compile line. These are now defined in configure.
* 2010-01-08 Dan Terpstra — Minor tweak to get this file to compile with DEBUG turned on.
* 2010-01-08 Dan Terpstra — Minor tweak to print native event codes in hex instead of decimal -- far more useful that way.
* 2010-01-07 sbk — The libpfm flag CONFIG_PFMLIB_OLD_PFMV2 was correctly set for when compiling and building libpfm, but it also needs to be set for installing also. The header file libpfm-3.y/include/perfmon/perfmon.h uses this flag to determine if a macro is prepended to perfmon.h when installing it.
* 2010-01-07 Heike Jagode — Renamed identifier 'native_name' for net, mx, and acpi components because of conflicts on POWER machines. This variable has also been defined in powerX_events.h.
* 2010-01-07 Brian Sheely — Moved check for debug build below check for programs since it needs CC to be set
* 2010-01-07 Heike Jagode — Brought back multiple variables into the code so that papi-c compiles and runs again on POWER/AIX. Brian, the following variables (CPU_MODEL, cpu_option, FLAGS, PMAPI, PMINIT) are needed to get the Makefile correct.
* 2010-01-07 Brian Sheely — Added DEBUGFLAGS to OPTFLAGS since only OPTFLAGS gets used in Makefile.inc
* 2010-01-07 Brian Sheely — rolling back last change
* 2010-01-07 Brian Sheely — Restored MSUBSTR variable for AIX builds
* 2010-01-06 Brian Sheely — Removed --with-makefile option and added comments to help resolve confusion with when to use --with-pfm-root
* 2010-01-06 Heike Jagode — Brought the component variables back to the code. Brian, you cleaned up a little bit too much. We need the component variables in order to use more than just the CPU component. Not sure about MEMSUBSTRC for the MX component yet. I cannot test this one.
* 2010-01-06 Brian Sheely — Fixed logic error when testingfor valid PEPATH
* 2010-01-05 Brian Sheely — Modified code to use macro instead of static int and eliminated unnecessary static int. Unable to test
* 2010-01-05 Brian Sheely — Modified code to that SYNC_READ is now defined for all kernels older than 2.6.33 and is defined using a compiler flag instead of a preprocessor directive
* 2010-01-05 Brian Sheely — Removed unused variables from the build. Note: Untested on several platforms (BG/P, AIX-POWER, Niagara).
* 2010-01-05 Dan Terpstra — Modified license language for John May's LLNL portion of this code to conform with BSD as provided by LLNL. Thanks, Bronis, for bird-dogging this.
* 2010-01-04 Heike Jagode — Updated conf option for adding lm-sensors headers.
* 2010-01-04 Brian Sheely — added compiler check when setting debug level with --with-debug
* 2009-12-22 Brian Sheely — added code to prevent segfaults in overflow_allcounters test
* 2009-12-22 Brian Sheely — added code to prevent segfaults in overflow_force_software test. Errors still exist so some functionality probably needs to be rewritten
* 2009-12-21 Brian Sheely — modified configure to support changes recommended by Will Cohen at Redhat (--with-pcl-incdir has precedence and kernel version determined by which perf header is found)
* 2009-12-20 Dan Terpstra — Changes to fix overflow/profile issues in niagara2. Thanks to Fabian Gorsler.
* 2009-12-18 Dan Terpstra — Committing changes for BG/P. Utilities and basic counting works; Not fully tested.
* 2009-12-18 Brian Sheely — modified changes made in revision 1.10 to correctly resolve 'cast to pointer from int of different size' compile warnings
* 2009-12-17 Brian Sheely — #define SYNC_READ is not done for 2.6.32 and later kernels
* 2009-12-16 Heike Jagode — Added missing LDFLAGS for lm_sensors configuration +++ Added modifications for Niagara2 support
* 2009-12-16 Dan Terpstra — Change definition of CFLAGS for debug from -g3 to -g. This in response to the fact that Sun Studio doesn't recognize -g3. It isn't as bad as it seems, because in GCC the default definition of -g is -g2. It would be nice to condition this on which compiler is in use.
* 2009-12-16 Dan Terpstra — Commit initial changes for Niagara2 support for PAPI-C. Thanks to Fabian Gorsler. Basic counting works; some unresolved issues remain for overflow and profile.
* 2009-12-16 Dan Terpstra — Minor tweaks on the header of the license text.
* 2009-12-11 Dan Terpstra — Add a synonym for Pentium M.
* 2009-12-11 Brian Sheely — resolved compile warnings on bluegrass
* 2009-12-09 Brian Sheely — make clean now removes library and shared object files and when the shared object is created a symbolic link is also created with the generic name libpapi.so
* 2009-12-09 Brian Sheely — Blue Gene modifications
* 2009-12-08 Brian Sheely — Fixed memory issue seen in testing on certain platforms
* 2009-12-03 Brian Sheely — Corrected --help output
* 2009-12-02 Heike Jagode — Adjusted function argument assignment between wrong types (void and int pointer)
* 2009-12-02 Brian Sheely — Set correct path variable for BGP
* 2009-12-02 Dan Terpstra — Slightly cleaner syntax for redefinition of perf_event_attr in KERNEL31.
* 2009-12-02 Heike Jagode — The 'added configuration for BGP' modifications cause a 'make install' failure on other architectures due to overwriting the prefix path.
* 2009-12-01 Dan Terpstra — Fix from Will Cohen to avoid round-off errors in computing small differences between large numbers, which occasionally resulted in sqrt of negative numbers. Originally applied to sdsc2; modified and applied to sdsc2.
* 2009-12-01 Brian Sheely — Added configuration for BGP (Untested)
* 2009-11-30 Dan Terpstra — Fix from Will Cohen to avoid round-off errors in computing small differences between large numbers, which occasionally resulted in sqrt of negative numbers. Thanks Will
* 2009-11-30 Dan Terpstra — Strip the Windows version of cpuid out to make this version compatible with the 3.7.x branch.
* 2009-11-30 Dan Terpstra — A fix and an update. The computation for AMD L3 cache was incorrect. I was assuming 2^18 was 512K and it really should be 2^19. The Intel cache descriptor table was from Nov 2008. I updated it to Aug 2009. This includes 3 fixes and 3 new entries for L3 cache descriptors. Tested for compilation/execution only; not for correctness.
* 2009-11-30 Dan Terpstra — Standardization of logic to test for valid component index. Several instances of (cidx > papi_num_components) were found by Gary Mohr of Bull. The correct logic should have been (cidx >= papi_num_components). All instances were replaced with an inline function mapped to the correct logic.
* 2009-11-25 Brian Sheely — resolved compile warning
* 2009-11-25 Dan Terpstra — PAPI_stop_counters was returning PAPI_OK even if PAPI_stop returned something other than PAPI_OK. Uncovered as part of the BG/P merge.
* 2009-11-25 Brian Sheely — added test for topology/thread_siblings and topology/core_siblings
* 2009-11-24 Brian Sheely — Removed invalid code (zero can be a valid value for nnodes)
* 2009-11-24 Dan Terpstra — Fix a bug in assigning signals for overflow.
* 2009-11-23 Brian Sheely — resolved compile error
* 2009-11-23 Brian Sheely — Applied patch papi_vector.c.patch. Thanks Fabian
* 2009-11-23 Brian Sheely — valgrind code merged into run_tests.sh and commented out by default
* 2009-11-20 Brian Sheely — Added script to run test with valgrind. Thanks Will
* 2009-11-20 Brian Sheely — applied patch papi-3.9.0-run_tests.patch
* 2009-11-20 Brian Sheely — when using --with-perf-events search in /usr/include/linux/ before searching in /lib/modules//source/include/linux
* 2009-11-20 Brian Sheely — Applied patch from Steve Kaufmann at Cray. Removes the remaining Unicos, Catamount, T3E, X1 and X2 references. Only explicit support for XT4+/CLE remains.
* 2009-11-19 Brian Sheely — Updated to include new hardware info
* 2009-11-19 Brian Sheely — --with-pe-incdir now works with either a path to the perf event header file without the header included in the path or a path with the header included as part of the path
* 2009-11-19 Brian Sheely — Fixed bug with incomplete PEPATH
* 2009-11-18 Brian Sheely — Restored TOPTFLAGS so that the PAPI source code has a different level of optimization than the test code
* 2009-11-18 Brian Sheely — The file extension should be .csv. Thanks Gary.
* 2009-11-18 Brian Sheely — Changed perfmon_events.cvs to papi_events.cvs. Thanks to Phil for catching that
* 2009-11-18 Philip Mucci — Renamed shutdown_global to shutdown_substrate to make it more obvious that this is per substrate. This callback will be important for freeing some memory up and making sure locks are reset. Looks like a big patch, but only a few lines.
* 2009-11-18 Philip Mucci — Add support for detecting gettid and syscall(gettid) which results in HAVE_GETTID and HAVE_SYSCALL_GETTID being defined in config.h
* 2009-11-18 Philip Mucci — Beginnings of a single function with all PAPI/Linux locking functions.
* 2009-11-18 Philip Mucci — Final commit for --disable-static and --disable-shared support.
* 2009-11-18 Philip Mucci — Support for --disable-static and --disable-shared for building
* 2009-11-17 Brian Sheely — fixed bugs related to configuration issues with linux perf event system when patch is installed
* 2009-11-13 Heike Jagode — Ensure that perf_events stuff is only used for kernel versions 2.6.31. and higher.
* 2009-11-12 Brian Sheely — renamed perfmon_events.csv perfmon_events_table.h perfmon_events_table.sh to papi_events.csv papi_events_table.h papi_events_table.sh and made code changes required by the renaming
* 2009-11-11 Heike Jagode — It appears that Ubuntu/perf_events cannot find the perf_events include files where they should be. Added additional workaround for this problem.
* 2009-11-11 Brian Sheely — removed code for obsolete cray builds
* 2009-11-11 Dan Terpstra — Remove OP_TYPE expansion of packed operations from AMD Family 10h definition of FP_INS per suggestion from John McCalpin.
* 2009-11-11 Brian Sheely — removed Catamount code
* 2009-11-11 Dan Terpstra — Fix overly restrictive verification of results. In verifying that FP_INS/FP_OPS/TOT_INS was non-zero, we were requiring it to be near theoretical FP_OPS which caused false verification failures in some edge cases. Now we just require count >= iterations.
* 2009-11-11 Dan Terpstra — Initialize the inp and outp structures to 0 in the update_control_state routine. This is overkill but should eliminate the complaints valgrind is generating about an uninitialized structure.
* 2009-11-10 Brian Sheely — Modified code so that there aren't multiple debug and optimization levels. Using --with-debug=yes results in -g3 and -O0. Removed TOPTFLAGS and FTOPTFLAGS to simplify the build
* 2009-11-10 Brian Sheely — Modified configure so that x86_cache_info.c cannot be included more than once. Added hwinfo_linux.c to CLE build.
* 2009-11-10 Philip Mucci — Patch to enable
* 2009-11-09 Brian Sheely — removed crayx2 code and fixed CFLAGS for crayxt
* 2009-11-09 Brian Sheely — created hwinfo_linux.c to encapsulate code to set _papi_hw_info struct on Linux platforms
* 2009-11-09 Brian Sheely — removed obsolete file
* 2009-11-06 Dan Terpstra — Fix for including unit masks in event codes for perf_events.
* 2009-11-05 Brian Sheely — removed code related to obsolete builds
* 2009-11-05 Brian Sheely — removed files related to obsolete builds
* 2009-11-03 Dan Terpstra — Initial revision
* 2009-11-02 Brian Sheely — removed or replaced all occurences of 'pcl'
* 2009-11-02 Brian Sheely — resolved compile warnings in kernel 2.6.31 when using --with-perf-events
* 2009-11-02 Dan Terpstra — Fixes to eliminate strcpy on overlapping strings The offending calls were replaced with memmoves and encapsulated in a single function for better maintenance.
* 2009-10-30 Brian Sheely — modified code to use types defined in perf_event.h
* 2009-10-30 Dan Terpstra — Mods to convert to perf_event style syntax. This will only compile on 2.6.31 because the perf_event syntax is converted back to perf_counter syntax in a #define block in perf_events.h. That block needs to be conditioned by the kernel version to make it work in either context.
* 2009-10-30 Dan Terpstra — Optimizations submitted by Corey Ashford to improve read times for multiple counters. It looks like this change provides about a 6% improvement for 2 counters, but that should improve for larger event sets.
* 2009-10-29 Brian Sheely — resolved compile errors on solaris
* 2009-10-28 Brian Sheely — Modified configure to look for and include perf_event.h instead of perf_counter.h when using 2.6.32 and subsequent versions of the linux kernel. NOTE: Our code does not currently compile with perf_event.h
* 2009-10-28 Heike Jagode — List events only that are supported by host CPU. (Problems on AMD family 10 processors)
* 2009-10-27 Brian Sheely — roll back to previous version
* 2009-10-27 Brian Sheely — resolved a few of many compile errors and warnings
* 2009-10-27 Brian Sheely — removed defines for __NR_perf_counter_open
* 2009-10-23 Brian Sheely — Resolved issue with __NR_perf_counter_open already defined in kernel 2.6.32
* 2009-10-23 Brian Sheely — Naming convention change from PCL to Perf Events: renamed pcl.h and pcl.c to perf_events.h and perf_events.c, renamed Rules.pfm_pcl to Rules.pfm_pe, configure option --with-pcl changed to --with-perf-events
* 2009-10-23 Dan Terpstra — Fixes to long standing bug in remove_native_event compaction logic. This only affects PAPI-C, but caused subtle destabilization and seg faults on tests like sdsc4-mpx. Thanks to Corey Ashford for some tremendous detective work here.
* 2009-10-22 Brian Sheely — resolved warning initializing const with non-const
* 2009-10-21 Dan Terpstra — Apply Phil's fix to initialize strings in _update_shlib_info. Thanks to Will Cohen for first identifying this. This code is poorly factored and badly needs a refactoring...
* 2009-10-20 Dan Terpstra — Fixed a problem where single native events were scanning across all components when they should have just looked at a single component.
* 2009-10-20 Brian Sheely — corrected possible logic error in setting end point of profile buffer
* 2009-10-20 Heike Jagode — Improved configuration of perf_events substrate. Thanks to Corey Ashford and Anton Blanchard.
* 2009-10-20 Dan Terpstra — Changes in pcl reset from Corey Ashford.
* 2009-10-15 Brian Sheely — corrected possible init error
* 2009-10-15 Brian Sheely — fixed warnings in solaris
* 2009-10-14 Heike Jagode — Incorrect path composition causes failure of 'make install' on Power6 with AIX.
* 2009-10-14 Dan Terpstra — Change libpapi.so to libpapi.so.3 per Will Cohen of Redhat.
* 2009-10-14 Dan Terpstra — Convert an exit() into an abort() per Will Cohen of Redhat.
* 2009-10-14 Brian Sheely — set BITS to correct value for AIX
* 2009-10-14 Dan Terpstra — Beef up error checking to report undercounts of flops or instructions. Zero shouldn't be a valid count!
* 2009-10-14 Dan Terpstra — Error checking was missing undercount conditions.
* 2009-10-13 Dan Terpstra — Conversion of AIX to PAPI-C. Most tests pass, except for some overflow related stuff. Haven't examined things closely yet, but thought I should check this stuff in.
* 2009-10-13 Dan Terpstra — This file never existed on the PAPI-C branch.
* 2009-10-13 Brian Sheely — modified for ifort compiler
* 2009-10-13 Brian Sheely — corrected icc error
* 2009-10-13 Brian Sheely — resolved input file not found in AIX build
* 2009-10-12 Brian Sheely — declare types explicitly
* 2009-10-12 Brian Sheely — declare types explicitly
* 2009-10-12 Brian Sheely — added openmp compile flag for icc
* 2009-10-12 Brian Sheely — corrected logic error with pid type
* 2009-10-12 Brian Sheely — corrected logic error with pid type
* 2009-10-09 Brian Sheely — ignore icc warning #188
* 2009-10-09 Brian Sheely — icc warnings
* 2009-10-09 Brian Sheely — testing icc warnings
* 2009-10-09 Brian Sheely — corrected build for cray XT/CLE
* 2009-10-09 Brian Sheely — fixed icc warning #10120
* 2009-10-09 Brian Sheely — testing icc
* 2009-10-09 Dan Terpstra — Somehow these got removed from the repository.
* 2009-10-08 Brian Sheely — *** empty log message ***
* 2009-10-08 Brian Sheely — eliminate icc warning #10120
* 2009-10-07 Brian Sheely — removed c99 related code which was recently added
* 2009-10-07 Brian Sheely — Changes for AIX which have been tested
* 2009-10-06 Brian Sheely — modifications for AIX
* 2009-10-06 Brian Sheely — updated to match configure.in
* 2009-10-06 Brian Sheely — replaced strong quotes with weak quotes to expand macros in order to compile on AIX
* 2009-10-06 Brian Sheely — modified include statement to compile on AIX
* 2009-10-06 Brian Sheely — modified for c99 build
* 2009-10-05 Brian Sheely — changes need to help build c99
* 2009-10-05 Brian Sheely — clean up of compile warnings
* 2009-10-02 Brian Sheely — removed duplicate target for bgl_tests
* 2009-10-02 Brian Sheely — removed ifeq conditionals to build on AIX
* 2009-10-02 Brian Sheely — reverting back to version 1.135 to undo last change
* 2009-10-01 Brian Sheely — removed ifeq conditional to compile on AIX
* 2009-10-01 James Ralph — Typo? if we want to check for PFMLIB_MIPS_ICE9B_PMU aswell, #if a && b breaks vc++'s feeble preprocessor, so use two ifs
* 2009-10-01 Heike Jagode — Configure mod: Use perfctr by default if available; otherwise pcl. Also, use pcl if manually specified during configure time (independently if perfctr is available or not).
* 2009-09-30 Brian Sheely — updated to reflect recent changes
* 2009-09-30 Brian Sheely — removed deprecated files
* 2009-09-30 Brian Sheely — x86_cache_info code moved from Rules files to configure.in and Makefile.inc
* 2009-09-28 Brian Sheely — added flag to define C99 for c99 compilers
* 2009-09-28 Brian Sheely — Deprecated all platform specific makefiles
* 2009-09-25 Haihang You — bug fix from Tushar:
* 2009-09-23 Dan Terpstra — Oops. It's _papi_pcl_reset, not _papi_hwd_reset.
* 2009-09-23 Dan Terpstra — Remove a #if 0 from _papi_pcl_start. This was preventing counters from being reset.
* 2009-09-22 Haihang You — use num_mpx_cntrs when kernel_multiplex; otherwise use num_cntrs.
* 2009-09-22 Haihang You — fixed PAPI_add_event for multiplexing.
* 2009-09-21 Heike Jagode — Added definition for 2 of the 4 new presets (SP_OPS, DP_OPS) for Opteron
* 2009-09-17 Heike Jagode — Eliminated assignment warnings
* 2009-09-17 Heike Jagode — Added workaround for missing perf_counter header files.
* 2009-09-15 Heike Jagode — Merge from papi-3-7-0 to head
* 2009-09-10 Dan Terpstra — replacing HEAD with papi-c-exp
* 2009-09-08 James Ralph — Fixing a typo
* 2009-09-08 James Ralph — Updates for Pentium M tables
* 2009-09-08 James Ralph — Windows compat. mods, will be sent upstream when they are in better shape, but they are needed for the release we're doing now.
* 2009-09-08 James Ralph — Windows lacks a real scripting environment, so we statically generate perfmon_events_table for it
* 2009-09-08 James Ralph — Updates to Windows read-me file.
* 2009-09-08 Dan Terpstra — Updates for the impending release.
* 2009-09-08 Dan Terpstra — Add Change Log to the repository.
* 2009-09-08 Heike Jagode — Added definition for the 4 new presets (SP_OPS, DP_OPS, VEC_SP, VEC_DP) for i7.
* 2009-09-08 Dan Terpstra — Synchronize with configure.in
* 2009-09-08 Haihang You — call PAPI_stop instead of PAPI_Shutdown
* 2009-09-08 Dan Terpstra — Updates for the impending release.
* 2009-09-08 James Ralph — Updated Windows install information
* 2009-09-07 Haihang You — call PAPI_shutdown when each thread finishes.
* 2009-09-06 Heike Jagode — minor change
* 2009-09-06 Heike Jagode — Added 4 new preset events to count the correct # of floating point operations for optimized libraries that use SIMD (single and double precision); SIMD instructions (single and double precision).
* 2009-09-06 Heike Jagode — No L3 preset definitions on Opterons as long as L3 events end up in shadow registers that are not associated with a specific core.
* 2009-09-04 Dan Terpstra — Changes to eliminate the installation of outdated man pages. Better no pages than outdated pages. Current man page content is now online at the PAPI documentation site.
* 2009-09-04 Haihang You — remove the compile errors
* 2009-09-03 Dan Terpstra — Fixes submitted by Corey Ashford for the POWER7 PRESET table.
* 2009-09-03 James Ralph — Revert to version 1.1.1.9 (Dan's latest import in the log)
* 2009-09-03 Dan Terpstra — Added a note on performance anomalies for Niagara submitted by Fabian Gorsler.
* 2009-09-03 James Ralph — Removing, guess we will have to push this upstream.
* 2009-09-03 Haihang You — set itimer_ns = 10000000; modify round_requested_ns to make ns multiple of itimer_res_ns
* 2009-09-03 Haihang You — add wraper functions for pfm_read_pmds, pfm_write_pmds and pfm_write_pmcs. set itimer_ns = itimer_res_ns
* 2009-09-03 James Ralph — Fixed line-endings in windows only headers
* 2009-09-03 James Ralph — 'Implements' some perfmon syscalls for windows.
* 2009-09-03 James Ralph — Switching from PERFCTR_PFM_EVENTS to SUBSTRATE_USES_LIBPFM #define
* 2009-09-02 James Ralph — Adding header files for use in windows
* 2009-09-02 James Ralph — Updating winextras for gettimeofday definition
* 2009-09-02 James Ralph — Exporting gettimeofday in the winpapi dll
* 2009-09-02 James Ralph — TODO: Find a good solution for variable arguments in vc++
* 2009-09-02 James Ralph — Adding include files for Windows
* 2009-09-02 James Ralph — moving variable, windows side fix
* 2009-09-02 James Ralph — gettimeofday routine for windows
* 2009-09-02 Dan Terpstra — Check for counters == 2 instead of cpu == Pentium III. Now it passes for CoreDuo.
* 2009-09-01 Heike Jagode — Update support for XT4/5 as well as INSTALL.txt.
* 2009-08-31 sbk — "perfmon", not "perfmon.h". Duh.
* 2009-08-31 sbk — Apparantly need to set SUBSTR to perfmon so it is known in the Rules file what the substrate is.
* 2009-08-31 Heike Jagode — Eliminate unused err header file.
* 2009-08-31 Dan Terpstra — Update reference to Rules.pfm2 to Rules.pfm_pcl.
* 2009-08-31 Dan Terpstra — Bump version numbers to 3.7.0.0 in prep for the upcoming release.
* 2009-08-31 Dan Terpstra — Change warning about wrong fd in the overflow handler from a PAPIERROR to a SUBDBG so it doesn't show up constantly in output. This appears to be related to a pending kernel fix that allows signals to be tied to specific tids.
* 2009-08-29 Heike Jagode — Adjust argument assignment between types for PAPI_thread_init() function (issue in 64-bit mode).
* 2009-08-28 Heike Jagode — Allow pre-processing source code using CPPFLAGS (because of issues on Power6 (AIX) in 64-bit mode.
* 2009-08-28 Haihang You — define PAPI_L1_DCA(atom) as derived add with LD and ST, due to NCOMP in libpfm table.
* 2009-08-28 Dan Terpstra — Add PRESET event definitions for CoreDuo processors.
* 2009-08-27 Dan Terpstra — Comment in Core,34 and Core,36 tables for perfmon style event table identification.
* 2009-08-27 Dan Terpstra — Enable a couple debug statements to make it easier to find cpu tables in perfmon_events.csv
* 2009-08-27 James Ralph — Unbroke my moving around of variable definitions.
* 2009-08-27 James Ralph — Fixed Windows only code #ifdefs
* 2009-08-27 James Ralph — Fixed misplaced variable definition.
* 2009-08-27 Harald Servat — Add some PAPI preset counters for Atom/Core processors
* 2009-08-27 Harald Servat — Missing start of enumeration value for native counter
* 2009-08-27 Dan Terpstra — Tweaks to make pcl compile and link for x86. Don't know if it's right, because it doesn't work yet, but at least it builds.
* 2009-08-27 Dan Terpstra — Heike was right in the first place. All that was needed was to remove the cast on the return value for papi_return() in PAPI_thread_id(). After much ado about nothing, we are finally back to where she said we should be all along.
* 2009-08-26 Heike Jagode — Disable shared build on Cray XT4/5 by default because it is currently not supported.
* 2009-08-26 James Ralph — *** empty log message ***
* 2009-08-26 James Ralph — Windows outreach work.
* 2009-08-26 James Ralph — Windows outreach work.
* 2009-08-26 James Ralph — Windows outreach work was done.
* 2009-08-26 James Ralph — Updates to Windows Driver
* 2009-08-26 James Ralph — Making perfmon.h more windows friendly.
* 2009-08-26 James Ralph — Updating _papi_hwi_using_signal to an array in the Windows portion of code.
* 2009-08-26 James Ralph — Wrong version of the file, think before you type and all..
* 2009-08-26 James Ralph — Windows version of this file is going to be compiled with gcc, so there is only one cpuid to rule them all, I screwed up, redo.
* 2009-08-26 James Ralph — Windows version of this file is going to be compiled with gcc, so there is only one cpuid to rule them all.
* 2009-08-26 James Ralph — Update to support Windows.
* 2009-08-26 James Ralph — Added a definition to support Windows
* 2009-08-26 Dan Terpstra — Add instructions for Solaris 10 / Niagara2.
* 2009-08-26 Dan Terpstra — Oops. Left a debug printf in the code :(
* 2009-08-25 Heike Jagode — Replace papi_return by return to avoid overflow issues when in debugging-mode.
* 2009-08-25 Dan Terpstra — Fix ID of Intel Nehalem on perfctr by checking all Intel native events for those beginning with "UNC_". It's a hack, but it works.
* 2009-08-25 James Ralph — *** empty log message ***
* 2009-08-25 Dan Terpstra — Updated for Solaris Niagara2 support. Thanks to Fabian Gorsler of Aachen University, Germany.
* 2009-08-25 Dan Terpstra — First commit of Solaris Niagara2 support. Thanks to Fabian Gorsler of Aachen University, Germany.
* 2009-08-24 Heike Jagode — Eliminate overflow warning
* 2009-08-24 Heike Jagode — Add pgi compiler support to accept 132-column source code
* 2009-08-24 Heike Jagode — Eliminate pgi compiler warnings on Cray XT4/5
* 2009-08-24 Dan Terpstra — Initial revision
* 2009-08-21 Dan Terpstra — Initial revision
* 2009-08-21 Haihang You — set soft_max
* 2009-08-20 Haihang You — set overflow threshold value
* 2009-08-20 Haihang You — set overflow threshold value
* 2009-08-20 Haihang You — set overflow threshold value
* 2009-08-12 Haihang You — minor fix for passing compilation on itanium and power
* 2009-08-11 Dan Terpstra — Changes in init_multiplex order submitted by Maynard Johnson to fix test cases for power6 & elsewhere.
* 2009-08-11 Haihang You — minor change
* 2009-08-11 Haihang You — count 2 events for p3
* 2009-08-05 Haihang You — for perfctr-2.6.x, when vperfctr_open() return error, call vperfctr_open_mode(0)
* 2009-08-03 Haihang You — zero count is ok.
* 2009-08-03 Haihang You — change pass condition from all non-zero to any non-zero.
* 2009-08-01 Dan Terpstra — Patches to perfmon.c and pcl.c to add support for Power7. Thanks to Corey Ashford.
* 2009-07-31 Dan Terpstra — Bump version number to 3.6.2.3 for a Cray intermediate release to support Istanbul. This will bump again prior to the official release.
* 2009-07-30 Dan Terpstra — Merging Corey's patch from 7/29 into papi. This fixes a long-standing bug in ppc_get_memory_info()
* 2009-07-28 Haihang You — to generate non-zero count, use do_stuff() instead of do_read()
* 2009-07-28 Haihang You — pentium4, bypass native event: REPLAY_EVENT:BR_MSP
* 2009-07-28 Haihang You — lower the number of iterations to make buildbot pass, otherwise running time exceeds the time limit
* 2009-07-28 Haihang You — won't fail if i<=20
* 2009-07-22 Haihang You — Corey's patch. see commited comments for detail.
* 2009-07-22 Heike Jagode — Fixed definition for preset FP_OPS for core2
* 2009-07-20 Dan Terpstra — Tweak to allow cross-compilation without testing for pcl.
* 2009-07-17 Haihang You — check for CPU string
* 2009-07-16 Haihang You — add itanium2 preset table
* 2009-07-14 Dan Terpstra — Remove SUBSTR=pcl from Rules. This is now defined in the calling Makefile.
* 2009-07-13 Dan Terpstra — First cut PRESET event table for Intel Atom.
* 2009-07-13 Dan Terpstra — Modified files to support Corey Ashford's pcl contribution.
* 2009-07-13 Dan Terpstra — New files to support Corey Ashford's pcl contribution.
* 2009-07-10 Dan Terpstra — Revert back to old identification for athlon and p4.
* 2009-07-09 Haihang You — modify varification condition for passing the test
* 2009-07-09 Dan Terpstra — This patch changes some Fortran testcases to set the domain to PAPI_DOM_ALL when processor type is "POWER6". There doesn't seem to be a means of determining the substrate type using the Fortran PAPI calls, so the patch is a bit of overkill, but should be OK. Submitted by Maynard Johnson @ IBM
* 2009-07-09 Dan Terpstra — This patch changes some C testcases to set the domain to PAPI_DOM_ALL when required (POWER6 with perfctr substrate). Submitted by Maynard Johnson @ IBM
* 2009-07-09 Harald Servat — Changed contact information.
* 2009-07-09 Harald Servat — George Neville-Neil extended the list of PAPI counters. Also reported that the L2_IFETCH does not work appropriately.
* 2009-07-09 Harald Servat — Initial support for Core / Atom processors.
* 2009-07-09 Harald Servat — Small upgrade of the documentation
* 2009-07-09 Harald Servat — Small fix on the code and parsing script.
* 2009-07-09 Harald Servat — This is a small utility I've created to parse rapidly the description of native performance counters obtained from (3) pmc.{atom|core|core2} manual pages.
* 2009-07-08 Dan Terpstra — This patch changes the papi library to return a new error code, PAPI_EINVAL_DOM, when using PAPI multiplexing on the POWER6/perfctr platform if the domain of the event set does not include user+kernel+supervisor. Submitted by Maynard Johnson @ IBM
* 2009-07-08 Dan Terpstra — More tweaks.
* 2009-07-08 Dan Terpstra — Oops. Fix a syntax error with nested if statements.
* 2009-07-08 Dan Terpstra — More completely identify Intel Core, Core2, Atom and i7 processors; Map all of these to Makefile.perfctr-p3 intermediate.
* 2009-07-08 Dan Terpstra — Fix for overflow indexing problem identified by Gary Mohr @ Bull. PAPI assumes that the overflow vector contains the register index of the overflowing native event. That is generally true, but Stephane used some tricks in perfmon2 to offset the fixed counters on Core2 (Core? i7?) by 16. This hack corrects for that hack in a (hopefully) transparent manner. Tested only on a Core2 machine. Needs further testing elsewhere.
* 2009-07-08 Dan Terpstra — Clean up commented lines.
* 2009-07-07 Haihang You — by default, thread_id = getpid(), and it causes confusion for perfctr. Add PAPI_init_thread(pthread_self) which substitute getpid with pthread_self.
* 2009-07-07 Harald Servat — Updated installation documentation for FreeBSD
* 2009-07-07 Harald Servat — Initial support fore Core2 / Core2Extreme processors.
* 2009-07-07 Harald Servat — Initial support fore Core2 / Core2Extreme processors.
* 2009-07-02 Harald Servat — Modified comments
* 2009-07-02 Harald Servat — Update the HOWTO
* 2009-06-30 Harald Servat — This document depicts how to add new substrates using the FreeBSD libpmc
* 2009-06-24 Dan Terpstra — Removing files that no longer exist in sourceforge.
* 2009-06-23 Dan Terpstra — More tweaks on output formatting.
* 2009-06-23 Dan Terpstra — Initial revision
* 2009-06-22 Dan Terpstra — Clean up output format; change event FAIL conditions to SKIP; relax low software overflow error FAIL condition.
* 2009-06-19 Dan Terpstra — Add FLOPS and FINS events for Intel Core; change decode for Core processor.
* 2009-06-19 Dan Terpstra — Initial revision
* 2009-06-19 Dan Terpstra — merging changes for perfctr 2.6.39 CVg: Committing in papi/src/perfctr-2.6.x/linux/drivers/perfctr
* 2009-06-19 Dan Terpstra — Initial revision
* 2009-06-10 Dan Terpstra — Remove unneeded '&' from GET_OVERFLOW_ADDRESS macro definition. This was returning the *address of* the instruction pointer instead of the *value of* the instruction pointer, and causing all profiling tests to fail.
* 2009-06-06 Heike Jagode — Fix of PAPI_library_init failure on AIX-Power6 systems when the name of the executable is longer than 32 characters. Problem: /proc/xxxx/map contains only the first 32 characters for each entry.
* 2009-06-04 Dan Terpstra — Iterate argv from 1 to argc instead of 0, since 0 is the executable name, which may inadvertently contains a match.
* 2009-06-03 Heike Jagode — Testing 1 - 2 - 3 ...
* 2009-05-20 Dan Terpstra — Loop termination change; minor syntax change.
* 2009-05-20 Dan Terpstra — Don't include x86_cache_info.c in the build for POWER/Linux.
* 2009-05-18 Dan Terpstra — Restructure this test to add more multiplexed events and relax failure conditions. Zeros and duplicates are now treated as cautions rather than failures.
* 2009-05-18 Dan Terpstra — Redefine some commonly used format strings for more uniform presentation.
* 2009-05-18 Dan Terpstra — Migrate #define MAX_TO_ADDD to the (few) tests that actually use it.
* 2009-05-13 Dan Terpstra — Remove some dead code.
* 2009-05-11 Dan Terpstra — Remove an unused variable that was triggereing a warning.
* 2009-05-08 Dan Terpstra — Replace z'80000000' with PAPI_L1_DCM in recognition that z'80000000' is undefined for 32-bit integers by strict interpretation of the Fortran spec, and PAPI_L1_DCM is the first event, which is what is intended by this construct anyway. This eliminates a compiler crash that occurs in some versions of gfortran.
* 2009-05-04 Maynard Johnson — Fix build error involving native_name_map on ppc64
* 2009-04-24 sbk — Add the correct -DPFMLIB_OLD_PFMV2 to CFLAGS to build for an older perfmon2. Tidy up refs to the static event table file.
* 2009-04-24 Dan Terpstra — Rebuilt with autoconf 2.61.
* 2009-04-24 Dan Terpstra — Add -DPFM_OLD_PFMV2 to CFLAGS when appropriate so PAPI will access the proper structures from libpfm-3.y/include/perfmon/perfmon.h.
* 2009-04-24 sbk — No longer add -DPFMLIB_OLD_PFMV2 to CFLAGS for CLE as configure does that for us now.
* 2009-04-22 Dan Terpstra — Changes to correctly detect and build for old perfmon interface. Fixes problem reported by Rui Liu @ NCSA.
* 2009-04-21 Dan Terpstra — #if 0 out another unused routine
* 2009-04-20 Dan Terpstra — #if 0 out an unused routine; comment out a #warning pragma
* 2009-04-20 Dan Terpstra — Fix bad syntax on two print statements.
* 2009-04-20 Dan Terpstra — Fix to eliminate warning message for unused return value from a read.
* 2009-04-20 Dan Terpstra — Casting fix to eliminate warning messages at compile on 32-bit address machines Thanks to Piotr Luczek, the high priest of C.
* 2009-04-16 Dan Terpstra — Remove type casting warnings. Also commented out a #warning message...
* 2009-04-16 Dan Terpstra — Rework GET_OVERFLOW_ADDRESS to eliminate "dereferencing type-punned pointer " warning message.
* 2009-04-15 Dan Terpstra — Fixes build on torc14 (athlon 32)
* 2009-04-13 Haihang You — set itimer_ns = 1000000; (perfmon.c) set us has to be > 0  (extra.c)
* 2009-04-09 Dan Terpstra — Remove x86_cache_info from build for Itanium; it isn't needed. Anaka now builds again and passes most tests.
* 2009-04-09 Dan Terpstra — Modify native event handling to deal with modifiers and perfmon. This fixes a bug where events would not be recorded if they had modifiers.
* 2009-04-07 sbk — Update pmu (cpu) names for AMD reflecting their definition in libpfm/lib/pfmlib_amd64_priv.h. Note that comma's have been removed, as they will be for the libpfm definition in perfmon.c so as to facilitate proper matching.
* 2009-04-07 Dan Terpstra — Modified cpu name compare to strip possible commas from source names. Names to match in the perfmon_events.csv file should *never* have commas.
* 2009-04-03 Dan Terpstra — Didn't mean to commit these debug changes...
* 2009-04-03 Dan Terpstra — Relaxed perfmon version dependencies per Steve Kaufmann's recommendations. You can still specify a perfmon version from the configure command line, but now it serves only determine which makefile to use and which ABI to specify. A version < 2.5 will define PFMLIB_OLD_PFMV2 for CFLAGS.
* 2009-03-23 Dan Terpstra — Fixed a data type warning identified by Corey Ashford. Unfortunately, the test it's embedded in doesn't work. We need a more robust way to report family and model information to userspace.
* 2009-03-12 Dan Terpstra — Convert error checks to information reporting. This acknowledges that the MHz value reported in /proc/cpuinfo no longer tracks the actual clock rate, at least for several of our Intel multicore cpus. We might be better off computing this value instead of relying on cpuinfo. Then we run into speedstep issues.
* 2009-03-11 Dan Terpstra — Initial revision
* 2009-03-02 Haihang You — fixed typo
* 2009-03-02 Harald Servat — Fixed:
* 2009-02-25 sbk — Protect native_avail from sending NULL to strcpy which results in a segfault. A mask for an event may not apply to the CPU and therefore strchr(name,':') may return NULL and be the second argument to strcpy. This happened for the AMD K8 event PROBE and its umask UPSTREAM_WRITES which only applies to AMD Rev D and later.
* 2009-02-25 Haihang You — fix init_papi()
* 2009-02-24 Haihang You — forgot remove printf statment
* 2009-02-24 Haihang You — change events for itanium2. Old events had conflict.
* 2009-02-13 Dan Terpstra — Oops. Typo.
* 2009-02-13 Dan Terpstra — Added test for PAPI_reset. Looks like reset is the difference between read and accum, at least on Nehalem with Perfmon.
* 2009-02-13 Dan Terpstra — Added tests for PAPI_accum and PAPI_read_ts. Refactored code to reuse duplicates; cleaned up the reporting to be a bit more meaningful.
* 2009-02-12 Dan Terpstra — Fix argument passing inconsistencies in local papi_init routine.
* 2009-02-09 Dan Terpstra — Rearrange flags for avail to match other dependencies and try to figure out why gfortran doesn't like this file. No luck so far.
* 2009-02-09 Dan Terpstra — Removed unused variables to keep compiler from complaining.
* 2009-02-09 Dan Terpstra — Fixed a typo in an event name string.
* 2009-02-09 Dan Terpstra — Fix native event reporting for Opteron/perfmon. Events with unit masks were not being handled properly, causig dispatch_events errors in libpfm.
* 2009-01-26 Dan Terpstra — Alias Intel Nehalem event table.
* 2009-01-23 sbk — Use the "-D PFMLIB_OLD_PFMV2" flag for XT and X2 CLE so that a libpfm is built that executes on perfmon2 releases v2.2 - v2.4. Only perfmon2 v2.2 (CLE 2.0) and v2.3 (CLE 2.1+) is presently supported.
* 2009-01-23 Dan Terpstra — Bump the version to 3.6.2.2 to indicate development support for Nehalem.
* 2009-01-22 Dan Terpstra — Modify some debug reporting in _hwd_stop.
* 2009-01-22 Dan Terpstra — Exclude encode and encode2 since they aren't implemented anywhere.
* 2009-01-22 Dan Terpstra — Working (and identical) definitions for PAPI_FP_OPS and FP_INS on i7.
* 2009-01-22 Dan Terpstra — Add Atom and i7 to xlate_cpu_type_to_vendor(); clean up some debug reporting.
* 2009-01-22 Dan Terpstra — Don't Fail if events don't exist; just Skip instead.
* 2009-01-22 Dan Terpstra — Added a little exception processing to keep from failing on Nehalem Uncore events.
* 2009-01-21 Dan Terpstra — Added cases for Intel i7 and Atom to switch to initialize counter enable and user space selection bits. Without these bits set, PAPI_start fails and all tests fail.
* 2009-01-20 Dan Terpstra — These files no longer in the sourceforge repository.
* 2009-01-17 Dan Terpstra — Tweaks on events for Intel i7 (Nehalem).
* 2009-01-17 Dan Terpstra — Add a first cut set of events for Intel i7 (Nehalem). This still needs work. And testing.
* 2009-01-16 sbk — Do not include x86_cache_info.c source in builds for the Cray-X2 platform. This might actually make sense for other platforms as well.
* 2009-01-16 Dan Terpstra — Initial revision
* 2009-01-16 Dan Terpstra — Segregated the cpuid-based cache and tlb info collection out of linux-memory.c and deleted it from perfmon.c. Now both make systems include x86_cache_info.c and the former files call a routine there to collect this information. Note that x86_cache_info should be usable directly in a Windows implementation. Tested on Intel Nehalem/perfctr and Core2/perfmon; Opteron/perfctr
* 2009-01-16 seymour — -modifying the JNI wrappers to have package name edu.utk.cs.icl.papi. keith
* 2009-01-16 Dan Terpstra — Massive rewrite to bring AMD and Intel info up-to-date (Apr 08 for AMD: Barcelona; Nov 08 for Intel: Nehalem) Also restructured to remove perfctr dependencies and make the Intel portion table-driven for easier future updates. Finally, added more depth to TLB descriptions to support Nehalem's dynamic TLB partitioning. This code is not linux specific. It's duplicated in perfmon.c It will be useful in Windows. It needs to be redeployed in a different file and make configuration so it isn't duplicated. I haven't quite figured out how to do that yet...
* 2009-01-14 Dan Terpstra — Output cleanup and changes to support more features.
* 2009-01-14 Dan Terpstra — Minor changes in mem hierarchy data structures and sizes to accomodate newer architectures like Nehalem and Barcelona.
* 2009-01-14 Dan Terpstra — Remove an #ifdef 0 / #endif pair from the start/stop test. This crept in between PAPI 3.6.0 and 3.6.1 and has been producing erroneously low results in 3.6.1 and 3.6.2.
* 2009-01-09 Dan Terpstra — Bump the version # to 3.6.2.1, using the last digit to indicate development status. Reintroduce #define long_long for backward compatibility. Add a couple definitions to the memory heirarchy descriptors.
* 2009-01-07 Dan Terpstra — Minor change in an error message.
* 2009-01-07 Dan Terpstra — Add perfctr definitions of Intel Atom and Core i7 processors as found in perfctr 2.6.37. This allows PAPI to properly execute basic operations on these processors, but as libpfm does not yet have event tables for i7, this is not very useful.
* 2008-12-12 sbk — "overflow-tests" should have been "overflow_tests". Need empty targets in the make file for Fortran tests to avoid "don't know how to make" errors.
* 2008-12-12 Dan Terpstra — Beef up the reset test, which really tests start, stop, accum, reset. Now there's nine different sequences that exercise a wide variety of combinations. If something isn't behaving right, it should show up here.
* 2008-12-11 Dan Terpstra — Change the names of some of the new test targets to avoid namespace collision. Don't know if it was necessary, but it seemed prudent.
* 2008-12-11 Dan Terpstra — Syntax error in the TARGET definition; search and replace dropped a space. Missed two more. :(
* 2008-12-10 Dan Terpstra — Missed one...
* 2008-12-10 Dan Terpstra — Syntax error in the TARGET definition; search and replace dropped a space.
* 2008-12-10 Dan Terpstra — Split the SERIAL tests target into SERIAL, FORKEXEC, OVERFLOW and PROFILE This provides a bit more control over test compilation for platforms like BG/P that don't support fork/exec and may not support overflow and profiling.
* 2008-12-10 Dan Terpstra — merging changes
* 2008-12-10 Dan Terpstra — Initial revision
* 2008-12-10 Dan Terpstra — Translate system error codes to strings from the pfm system calls. These were being incorrectly translated into pfm error strings instead of system error strings. Identified by Steve Kaufman of Cray.
* 2008-12-08 Haihang You — set PAPI_DATADIR for installed library to find the events file.
* 2008-12-08 Haihang You — set PAPI_DATADIR for installed library to find the events file.
* 2008-12-05 Dan Terpstra — Fixes from Corey Ashford to several return values in PAPI_{get,set}_opt.
* 2008-12-04 Dan Terpstra — Fixes from Corey Ashford to bring Fortran version into line with C version and eliminate the compile time check for POWER6.
* 2008-12-04 sbk — Fix compilation error by providing empty array and #events of zero for power6.
* 2008-12-03 Dan Terpstra — Fixes from Corey Ashford to eliminate the compile time check for POWER6. Also a fix for a nasty bug in Fortran strings.
* 2008-12-03 Dan Terpstra — Fixes from Corey Ashford to eliminate the compile time check for POWER6.
* 2008-12-01 Haihang You — fix compilation errors on power6 linux
* 2008-11-26 Dan Terpstra — Minor syntax fix.
* 2008-11-26 Dan Terpstra — Fix return value for error return of PAPI_stop_counters.
* 2008-11-24 Dan Terpstra — Big commit to remove all instances of long_long and u_long_long. These constructs were introduced years ago to accomodate the Microsoft compiler, which didn't understand (long long) and (unsigned long long). That restriction has since been removed. And besides, we're using the Intel compiler now anyway... This change has been tested clean on Linux, and should only matter for Windows anyway. Please test on other platforms as well. Any code *not* in cvs that uses long_long will also need to be modified, as these definitions no longer exist in papi.h.
* 2008-11-24 Dan Terpstra — Add further tests for Intel Core architectures. Syntax error correction.
* 2008-11-24 Dan Terpstra — Add further tests for Intel Core architectures.
* 2008-11-13 sbk — Further updates for Cray CNL to CLE references.
* 2008-11-12 sbk — Rename Cray "CNL" to the more techically correct "CLE" Cray Linux Environment.
* 2008-11-12 Dan Terpstra — Add PAPI_L3_TCH to Barcelona per Bill Homer @ Cray. Thanks, Bill
* 2008-11-12 Dan Terpstra — Mods from Chris Arges @ IBM to support ppc970mp.
* 2008-11-03 Haihang You — add --with-shlib=<yes|no>, by default it is 'no', and all test cases and utilities are linked with static library, otherwise link with dynamic library.
* 2008-10-24 Haihang You — check FP_INS and FP_OPS
* 2008-10-24 Haihang You — add checking for PAPI_FP_OPS and PAPI_FP_INS.
* 2008-10-23 Haihang You — always build libpapi.so during compilation stage, and put version number when install the library.
* 2008-10-15 sbk — Ensure if help messages were issued that exit value is zero. Ensure that if there was an error or any type to exit with a non-zero value.
* 2008-10-14 Dan Terpstra — Change return value for PAPI utility functions from exit(1) to exit(0). Don't know how this crept in, but it's been there for years, and just got propagated from one tool to another. Same is true for many of our tests. Thanks to Steve Kaufmann of Cray for catching this.
* 2008-10-09 Dan Terpstra — Add a utility to report the PAPI version number. Currently this is a simple one line output of the 4 digit PAPI_VERSION value from papi.h. It may be useful to add enhancements in the future to also report which substrate library and version (perfctr, perfmon, etc.) is linked in as well.
* 2008-10-09 Dan Terpstra — Add a line in the utility header block that reports the PAPI version number.
* 2008-10-03 Dan Terpstra — Missed a test loop in PAPI_shutdown that showed up with this change.
* 2008-10-03 Dan Terpstra — Change 3.6.1 reference at the top of the file to 3.6.2 as pointed out by Steve K. No, I'm not re-releasing the tarball.
* 2008-10-03 Dan Terpstra — Final updates for the PAPI 3.6.2 release.
* 2008-10-03 Dan Terpstra — Oops. One more dereferencing syntax fix. Warnings are your friends. Pay attention to them!
* 2008-10-02 Haihang You — add Makefile for 64bit power6
* 2008-10-02 Dan Terpstra — Ooops. Forgot a line.
* 2008-10-02 Dan Terpstra — Revert to implementation from 3.6.0 and earlier where EventSetInfo structures were independently malloc'd and maintained through a pointer list, rather than maintained directly in an array of structures.This may result in slowdowns due to false cache line sharing on some platforms. It may be useful to introduce a platform-specific modulus in the pointer list to minimize the false sharing where it is a problem.
* 2008-10-02 Dan Terpstra — Add a 'volatile' qualify to a variable to get rid of a casting warning in AIX.
* 2008-10-02 Dan Terpstra — Add an explanatory printf and correct a mistaken event name on final report.
* 2008-10-01 Haihang You — remove pfm_events_table.h when make clean
* 2008-10-01 Haihang You — let configure generate pfm_events_table.h, and add -DPFM_EVENTS to CFLAGS etc
* 2008-10-01 Dan Terpstra — Added support for static event table. This is hard-coded rather than driven by configure, because I couldn't figure out how to handle conditionals with aix make. Needed for POWER5 and 6. I don't know how this affects POWER4, where this file is also used.
* 2008-10-01 Dan Terpstra — Redefinition of PAPI_FP_OPS for POWER5, 5+, 6. Each has different constraints and increasing complexity. Results should be much better than with previous definitions. POWER5+ not fully validated.
* 2008-09-23 Dan Terpstra — Modify init routine to return error code instead of calling test_fail. Low level library routines should never call error processing functions; they should just pass the errors back up the chain. This change affects POWER6 only.
* 2008-09-22 Dan Terpstra — Version bump to 3.6.2.
* 2008-09-22 Dan Terpstra — Exception handling for case when kernel is perfmon 2.8 and libpfm is 2.81.
* 2008-09-19 Dan Terpstra — Initial revision
* 2008-09-18 Haihang You — new formular of PAPI_FP_OPS for power5 and power6
* 2008-09-18 Dan Terpstra — Redefine PAPI_FP_OPS for Core2 Duo to X87_OPS_RETIRED:ANY. This produces 0 error with calibrate.
* 2008-09-15 Haihang You — power6 support. most tests passed.
* 2008-09-05 Dan Terpstra — Remove initialization of a sub_info.reserved field that no longer exists. This probably did no harm, since it's a bit-field that gets initialized again in the following code, but it was flagged by xlc.
* 2008-09-04 Dan Terpstra — Now reports total events available and derived event counts.
* 2008-09-04 Dan Terpstra — Add _POWER6 to some condifitonal code compilations; trim line endings from description strings for better formatting in native_avail. Now supports group identifications and finds events, but still doesn't count.
* 2008-08-28 Dan Terpstra — Propagate extlang setting into common file; pick up debug settings from configure file.
* 2008-08-21 sbk — Update build instructions for Cray XT CNL and Catamount and X2.
* 2008-08-20 Haihang You — fix for power6
* 2008-08-20 Dan Terpstra — Fix to compile on POWER6 AIX
* 2008-08-20 Haihang You — add PPC970
* 2008-08-12 Dan Terpstra — Eliminate unused variable warning.
* 2008-08-08 Haihang You — add -D_AIX
* 2008-08-07 Philip Mucci — Small typo in good timer detection on SiCortex. The fast timer really only works on the 3.0 release, coming real soon...
* 2008-08-04 Dan Terpstra — Final commit for the 3.6.1 release.
* 2008-08-01 Philip Mucci — Fixed up sicortex docs
* 2008-07-31 Dan Terpstra — Updated html files to match man pages.
* 2008-07-31 Dan Terpstra — Tweaks to better document new get_ns functions.
* 2008-07-30 Haihang You — minor fix
* 2008-07-30 Haihang You — set PMAPI for power6
* 2008-07-30 Dan Terpstra — Remove tab characters that threw warnings for gfortran 4.3 Rework evaluation of the 0x80000000 value and the description of the problem. This may throw a warning for some compilers, but there are ways to turn the warning off.
* 2008-07-30 Dan Terpstra — Remove tab characters that threw warnings for gfortran 4.3
* 2008-07-29 sbk — Spelling error corrections.
* 2008-07-29 Dan Terpstra — Corrected faulty reference to PAPI_init_library instead of PAPI_library_init.
* 2008-07-28 Haihang You — add fix for aix-power6
* 2008-07-26 Philip Mucci — Regenerated with 2.61 of autoconf to fix DOCDIR
* 2008-07-24 Haihang You — add power6 support
* 2008-07-17 Dan Terpstra — Tweaked a MACRO definition that caused a segfault due to an uninitialized variable, but only for PAPI versions < 3.9. Fixes problem reported by Wyatt Spear.
* 2008-07-17 Haihang You — remove a printf message
* 2008-07-16 sbk — Get rid of compilation message by removing decl of unused variable.
* 2008-07-16 Philip Mucci — Fixup for recent commit for AIX systems that set ANY_THREAD_GETS_SIGNAL
* 2008-07-14 sbk — The length of the device in the maps file can be longer than just the five bytes that are used by the sscanf() to fetch from the character buffer. Increase the size of the array to hold the device name to 16 and read it from the buffer as a "%s". Also initialize the integral values to zero before sscanf() reads them out of the buffer to better identify invalid acquistion of data.
* 2008-07-14 Philip Mucci — PAPI*ns function info
* 2008-07-11 Philip Mucci — emoved duplicate CLK_TCK line
* 2008-07-11 Philip Mucci — Minor fixup in type
* 2008-07-11 Philip Mucci — Correct comment
* 2008-07-11 Philip Mucci — More support for setting ITIMER_NS in switching
* 2008-07-11 Philip Mucci — Hot path analysis revealed:
* 2008-07-11 Philip Mucci — This commit adds:
* 2008-07-11 Philip Mucci — Part 2 of the previous commit for standalone test building support.
* 2008-07-11 Philip Mucci — Updates to Makefiles to support standalone building of tests. i.e. If you have an installed papi in the standard places, you should be able to build the tests against it. Now you can.
* 2008-07-08 Dan Terpstra — Added text for Cell, SiCortex, and IBM POWER/Linux series with Perfmon2.
* 2008-07-02 Dan Terpstra — Change size of calloc in _papi_hwd_update_shlib_info as identified by a customer of Gary Mohr at Bull. Thanks, Gary
* 2008-07-02 Haihang You — add proc type detection, and init preset table from csv file. support power4 power5 power5+ power6. only tested on power5
* 2008-07-02 Haihang You — generating native_table without using event mapping table. use csv file for preset definition. only tested on power5.
* 2008-07-02 Dan Terpstra — Condition assignment of pfm_libdir and pfm_incdir to avoid clobbering command-line settings. Thanks to Chris Arges of IBM.
* 2008-07-02 Dan Terpstra — Merge of 2.6.35
* 2008-07-02 Dan Terpstra — Import of perfctr 2.6.35
* 2008-07-02 Dan Terpstra — Initial revision
* 2008-06-27 sbk — Use GNU gfortran for CNL builds on XT.
* 2008-06-26 Philip Mucci — Fixed up clock for SiCortex systems, old fast trap known to be broken. Also, added detection of that into configure. Added --disable-papi-vector to configure to be able to compile systems with -DPAPI_NO_VECTOR. Currently, something in the code is still preventing this, but we should be able to do it for systems where it is a benefit.
* 2008-06-26 Philip Mucci — Install instructions for SiCortex, native and cross as well as MIPS64/MIPS Linux
* 2008-06-24 Dan Terpstra — Changes to better support DESTDIR during install. Thanks to Steve Blackburn.
* 2008-06-24 Dan Terpstra — Changes to support the new VPERFCTR_CONTROL_CLOEXEC flag in perfctr. Needs testing.
* 2008-06-23 Dan Terpstra — Fix OVERFLOWADDRESS macro for powerpc64 builds. Thanks to Chris Arges of IBM.
* 2008-06-23 Philip Mucci — Fixed up handling of datadir and datarootdir, which allows us to handle these in a standard way and remove hacks from the configure file.
* 2008-06-18 Dan Terpstra — Bump version number to 3.6.1 in prep for the next release.
* 2008-06-13 Dan Terpstra — Added some initial event definitions for Cell.
* 2008-06-13 Dan Terpstra — Modify csv event loader to optionally load CYCLES and TOT_INS from either the perfmon built-in routines or from the table. Previously assumed they always came from the built-ins.
* 2008-06-12 Dan Terpstra — Re-Corrected verification output. Although columns appear to be added together, the verification is in terms of multipliers.
* 2008-06-11 Dan Terpstra — Added single and double quotes while I was at it.
* 2008-06-11 Dan Terpstra — Substitute character entities for illegal characters in strings. This includes <>& for now. Might add others later.
* 2008-06-11 Dan Terpstra — Add a place holder for a Cell event table.
* 2008-06-11 Dan Terpstra — Format tweaks for some debug and error messages.
* 2008-06-11 Dan Terpstra — load_preset_table previously assumed that the cycles and instructions events always existed. This is not true for Cell. This change relaxes this assumption and checks for the existence of these events before automatically adding them.
* 2008-06-11 Dan Terpstra — Modification to always represent the maximum negative number symbolically rather than numerically. Originally identified as a problem for the Cray Fortran compiler, Jim Rosinski demonstrated that it now exists on gcc Fortran as well. This fix (a hack, really) appears to work everywhere.
* 2008-06-11 Dan Terpstra — Clarification of return values.
* 2008-06-11 Dan Terpstra — Initial revision
* 2008-06-10 sbk — When writing a counter that has been set up for overflow, add to the desired value the long reset value (overflow frequency). This assumes (and defines) the counter value being passed in as the actual number of counts (zero-based).  This adds symmetry to the _hwd_read() function which already accounts for the long reset value, subtracting it off from the returned pfm_read_pmds() call.
* 2008-06-05 Philip Mucci — Small commit to avoid a redundant space.
* 2008-06-05 Dan Terpstra — Oops. Leftover chevrons from cvs conflict.
* 2008-06-04 Dan Terpstra — Rework the -e option for native events to display unit mask information for events that have unit masks defined but not specified. Mirrors new functionality in native_avail.
* 2008-06-04 Dan Terpstra — Rework the -e option to display unit mask information for events that have unit masks defined but not specified.
* 2008-06-04 Dan Terpstra — Add a debug statement.
* 2008-06-04 Dan Terpstra — Rework _papi_pfm_ntv_name_to_code to return a valid base event code even for events with unspecified unit masks. Also some random format cleanup.
* 2008-06-04 Dan Terpstra — Modify argument parsing to prevent false error message on event name for -e option.
* 2008-06-04 Philip Mucci — Removed redundant space ahead of Unit Mask qualifier
* 2008-06-03 sbk — Pass the PFM_VERSION_FLAG down even on perfctr (Catamount) builds to fully qualify the installed include/perfmon/perfmon.h file.
* 2008-06-02 Dan Terpstra — merge of 2.6.34
* 2008-06-02 Dan Terpstra — Initial revision
* 2008-05-30 Dan Terpstra — One line change in the conditional execution of PAPI_overflow to make profiling work on Intel Core 2 processors. Thanks to Rick Kufrin for pointing out this problem. See papi.c 1.315 and 1.316 for the context in which this  bug was introduced.
* 2008-05-30 Dan Terpstra — Remove a block of duplicate code in _papi_pfm_ntv_bits_to_info() that was introduced in version 1.13
* 2008-05-30 Philip Mucci — Add CFLAGS back in
* 2008-05-29 Dan Terpstra — Eliminate spurious warning in _papi_hwd_shutdown
* 2008-05-29 Philip Mucci — SiCortex has umasks and a fast timer.
* 2008-05-29 Philip Mucci — Regenerated with autoconf 2.61
* 2008-05-29 Philip Mucci — Ok, this fixes the --with-perfmon argument to be consistent.
* 2008-05-29 Philip Mucci — export TESTS_QUIET as env variable also
* 2008-05-29 Philip Mucci — TEST_QUIET fixes. We really should have made this an environment variable, not an argument.
* 2008-05-28 Philip Mucci — Regenerated with autoconf 2.61
* 2008-05-28 Philip Mucci — ha. Finally got the PFM_MSG_TYPE right
* 2008-05-28 Philip Mucci — Fixes to allow SiCortex to compile natively. Save Dan some headaches. Still needs pfm_msg_t fixup. But now chooses the right cycle timer if a SC machine is detected. But cross compiling is so much more fun...
* 2008-05-28 Dan Terpstra — Eliminate unused variable warning message.
* 2008-05-28 Dan Terpstra — Stomp out some annoying warning messages.
* 2008-05-28 Philip Mucci — Fix clock logic #ifdefs.
* 2008-05-28 Philip Mucci — Move back pfarg_msg_t.
* 2008-05-28 Dan Terpstra — Move the static perfmon_events_table.h file to MISCHDRS; Remove LIBS parameter from Rules.perfctr-libpfm; Standardize on sh instead of ksh in both files. This fixes dependency on generated event header for shared library in both cases.
* 2008-05-28 Philip Mucci — Little fudge in the clock to get it right.
* 2008-05-28 Philip Mucci — Don't hardcode clockrate for sicortex to 500.
* 2008-05-28 Philip Mucci — Added support for changing the multiplexing interval for Perfmon2 platforms, both default and for individual eventsets. Uses the reserved_ints[1] in the substrate structure to store the minimal kernel timeout. This will also prevent failures of PAPI on newer systems with dynamic ticks. Also, code to check/adjust the default multiplexing interval at initialization time. Found a failure on my 2.6.25 core2 due to this. Also, regenerated configure with 2.61 autoconf.
* 2008-05-24 Philip Mucci — More explicit directory creation
* 2008-05-23 Dan Terpstra — merge of changes to perfctr 2.6.33
* 2008-05-23 Dan Terpstra — Initial revision
* 2008-05-23 Dan Terpstra — Initial revision
* 2008-05-23 Dan Terpstra — Restructured event search logic: If the PAPI_PERFMON_EVENT_FILE environment variable is set, it looks for that file with no massaging and fails if not found. else if the static table is included it uses it. else it parses for various combinations of the default file and data directory.
* 2008-05-23 sbk — Accommodate the new/upcoming changes to libpfm 3.4. PFM_VERSION_FLAG is defined as PFMLIB_VERSION_22 or PFMLIB_VERSION_23, w/o the -D compilation flag. The Cray make files that use it as a compilation macro now require the -D preceeding it. Configure issues it with no -D in the generated Makefile.
* 2008-05-22 Dan Terpstra — Change default for with-pfm-events from 'file' to 'static'. NOTE: This version of configure was built with autoconf 2.59.
* 2008-05-22 Dan Terpstra — Removed duplicate definition of PERFMON_EVENT_FILE which is preferentially defined in papi_pfm_events.h. While I was at it I also deleted some other deprecated definitions which had been moved to papi_pfm_events.h a long time ago.
* 2008-05-22 Philip Mucci — Added system() tests while overflowing, including a non-papi cycle burner.
* 2008-05-22 Philip Mucci — Added stop before exec, allows perfctr to pass
* 2008-05-21 Philip Mucci — adjust threshold for error detection...
* 2008-05-21 Haihang You — remove creation of fullname. only use libpapi.so and libpapi64.so. always assume library is in LD_LIBRARY_PATH.
* 2008-05-21 Philip Mucci — Ported Mark Krentels most excellent fork/exec/overflow test to the PAPI test structure. Note that this will fail on unpatched, vanilla, IA64 kernels as that kernel has the (very naughty) bug meaning self sampling is really boned for codes that fork there.. Up-to-date Perfmon2 kernels now have been fixed. Awaiting testing on Perfmon2.
* 2008-05-20 Philip Mucci — Correct path of file when looking for events
* 2008-05-20 Philip Mucci — Removed redundant definition for PAPI_DATADIR that broke the non-static file build
* 2008-05-20 Philip Mucci — Add PID and Thread ID to debug output display
* 2008-05-13 Philip Mucci — Docs should be installed in prefix/share/doc/papi by default, not directly in prefix/share/doc
* 2008-05-13 Philip Mucci — We were changing permissions of wrong directory Spotted on SiCortex
* 2008-05-09 Philip Mucci — Add PAPI_ENUM_ALL #define for backwards compatibility.
* 2008-05-08 Philip Mucci — *** empty log message ***
* 2008-05-08 Philip Mucci — papi_xml_event_info is actually called papi_event_info, otherwise the Makefile will keep rebuildng
* 2008-05-08 Philip Mucci — Move hwd_shutdown to linux.c as with other perfctrs. So much duplicated code!
* 2008-05-07 Haihang You — fix for recognizing intel Pentium4 model 2, 3
* 2008-05-07 Philip Mucci — Removed basic fork/exec tests from this. Overflow/running counters still broken across fork exec.
* 2008-05-07 Philip Mucci — Always call dummy. Solves fail on mips/linux.
* 2008-05-07 Philip Mucci — Threshold env variable for testing
* 2008-05-07 Philip Mucci — Proper ordering for includes and flags. Don't compile dummy and do_loops with any flags.
* 2008-05-07 Philip Mucci — $(INCLUDE) always comes before $(CFLAGS) unless you want to pick up stale headers.
* 2008-05-05 Philip Mucci — 1) Add new call to vperfctr_open_mode so that we can still open our context after forking 2) Remove errors from vperfctr_unlink, allow shutdown to always succeed
* 2008-05-02 Haihang You — comment out #ifdef HAVE_PFM_MSG_TYPE     pfm_msg_t msg; #else     pfarg_msg_t msg; #endif it breaks on brutus.
* 2008-05-02 Dan Terpstra — Last minute changes for perfmon2 support of Core2.
* 2008-05-02 Philip Mucci — Ok, various consistency fixes for the three. Please remember that when you fix one of these, you often need to fix the other three as they work identically. Added fix to detect when a preinstalled perfctr or pfm is in the default path /usr. For this case it is not correct to specify -I/usr/include. This can break various systems with a different -sysroot.
* 2008-05-02 Dan Terpstra — Documentation updates for PAPI 3.6
* 2008-05-02 Philip Mucci — Fix for older libpfm SPARC and pfm_msg_t
* 2008-05-02 Dan Terpstra — This appears to fix the differential build problem identified by Rick Kufrin yesterday. This commit is tentative, and for testing purposes, pending a potentially cleaner solution from Phil.
* 2008-05-02 Dan Terpstra — Add a step to run autoconf if configure.in changes.
* 2008-05-02 Dan Terpstra — Tweak on FreeBSD stuff; substitute an error message for a warning if the HWPMC driver isn't present.
* 2008-05-02 Dan Terpstra — Document where version numbers must be changed.
* 2008-05-02 Dan Terpstra — Version number changes.
* 2008-05-01 Dan Terpstra — Final tweaks before PAPI 3.6.0.
* 2008-05-01 Dan Terpstra — Commit Notes for PAPI 3.6
* 2008-05-01 Dan Terpstra — Initial revision
* 2008-05-01 sbk — Cray-specific code that enables the re-establishment of the perfmon2 context by performing a pfm_create_context upon starting the counters. This is required because a BLCR closes the PMU device files and does not save these file's state. While the state of PAPI and its internal tables are valid, when the ctx_fd is used in a pfm* system call after a restart the system call fails because the file descriptor has not been restored.
* 2008-05-01 Haihang You — fix a comment.
* 2008-05-01 Dan Terpstra — Remove reference to papi mailing list from footer, since this is now a private list. Add PAPI_read_ts to the html build macro.
* 2008-05-01 Dan Terpstra — Remove reference to papi mailing list from footer, since this is now a private list.
* 2008-04-30 Haihang You — change back to the previous version
* 2008-04-30 Dan Terpstra — Updates for the impending 3.6.0 release.
* 2008-04-30 Haihang You — minor fix
* 2008-04-30 Dan Terpstra — Remove reference to NO_DLFCN. This file is now included by configure if it exists.
* 2008-04-30 Dan Terpstra — Added documentation for xml_event_info; Updated related files.
* 2008-04-30 Dan Terpstra — Added documentation for xml_event_info
* 2008-04-30 Dan Terpstra — Minor updates in list of other utilities.
* 2008-04-30 Dan Terpstra — Removed unused variable from papi_init routine.
* 2008-04-28 Haihang You — minor name fix for intel core
* 2008-04-28 Karl Fuerlinger — Added papi_xml_event_info from PAPI-C
* 2008-04-28 Haihang You — add new changes for FreeBSD from Harald.
* 2008-04-26 Harald Servat — Improved FreeBSD installation instructions.
* 2008-04-26 Harald Servat — PAPI modifications to support FreeBSD (6 or higher) using its HWPMC kernel driver.
* 2008-04-25 Dan Terpstra — Skip on Cray X1
* 2008-04-25 Dan Terpstra — general update
* 2008-04-25 Dan Terpstra — make now does a make install instead of a make clean by default
* 2008-04-25 Dan Terpstra — Add a short description of the files found in this directory.
* 2008-04-25 Dan Terpstra — Add DOCDOR to the showconf target.
* 2008-04-25 sbk — Use "long_long" instead of "long long" for "from" array of event counts.
* 2008-04-25 sbk — Add perfmon2 support for PAPI_write(). Tested with AMD it works while the counters are running (after PAPI_start() since PAPI_start() resets the counters to zero).
* 2008-04-24 Haihang You — another minor fix
* 2008-04-24 Haihang You — put commented out command back in.
* 2008-04-24 Dan Terpstra — Tweak on comment syntax to only recognize # at the beginning of lines.
* 2008-04-23 Dan Terpstra — This version supports comment lines beginning with # which also allows individual tests to be commented in and out.
* 2008-04-23 Dan Terpstra — Add a feature to run_tests.sh to support an 'exclusions' list of test files to exclude from execution. This allows temporary exclusion of test cases while debugging, or exclusion of problem cases at release to reduce the noise and avoid generating unneccessary angst among users during acceptance testing. Future enhancements: - support comments in the text file to make it self documenting - support multiple exclusion files on a platform-by-platform basis
* 2008-04-23 Dan Terpstra — Initial revision
* 2008-04-21 Dan Terpstra — merging changes to perfctr-2-6-32
* 2008-04-21 Dan Terpstra — Initial revision
* 2008-04-18 Dan Terpstra — Updated man pages for these utilities.
* 2008-04-18 Dan Terpstra — Cast the parameter for PAPI_thread_init to avoid a type warning.
* 2008-04-17 Dan Terpstra — Tweak script to correct for Microsoft backslashes in path names. Thanks to Don Fike.
* 2008-04-17 Dan Terpstra — Update html versions of man pages.
* 2008-04-17 Dan Terpstra — Update man pages.
* 2008-04-17 Dan Terpstra — Minor tweaks in help text to match the man page.
* 2008-04-16 Dan Terpstra — Remove native.F because it is a pain to maintain and doesn't add any new coverage. This also mirrors the removal of native.c, since that functionality is covered by all_native_events.c, a version of which might arguably be useful for Fortran.
* 2008-04-16 Dan Terpstra — Fix warning message; Don't run pthrtough2 on CrayX1; it destabilizes the system.
* 2008-04-16 Dan Terpstra — Modify to suppress output when running TESTS_QUIET.
* 2008-04-16 Dan Terpstra — Oops. I removed this from the wrong branch... Remove native.F because it is a pain to maintain and doesn't add any new coverage. This also mirrors the removal of native.c, since that functionality is covered by all_native_events.c, a version of which might arguably be useful for Fortran.
* 2008-04-16 Dan Terpstra — Initial revision
* 2008-04-16 Dan Terpstra — Change version # to 3.5.9 in preparation for the 3.6.0 release...
* 2008-04-11 Dan Terpstra — cast parameter for PAPI_thread_init to avoid a type check warning. Eliminate ref to NPROCESSORS by pulling from mdi structure.
* 2008-04-10 Dan Terpstra — add $CTESTS to compilation of do_loops.c. This is needed to pass compile step on Cray X1.
* 2008-04-10 Dan Terpstra — Add a case for ths sig handler for Cray X1. Still some problems with overflow/profile on this platform.
* 2008-04-10 Dan Terpstra — Clean up overflow code for Cray X1. Still some problems with overflow/profile on this platform.
* 2008-04-10 Dan Terpstra — add $CTESTS to compilation of do_loops.c. This is needed to pass compile step on Cray X1.
* 2008-04-09 Haihang You — fix _papi_hwi_native_name_to_code
* 2008-04-04 Haihang You — call pfm_initialize() before other pfm calls.
* 2008-04-02 Philip Mucci — Failing overflow tests from Mark Krentel. To be integrated in the higher level
* 2008-04-02 Philip Mucci — Added Mark Krentels tests showing failures of fork/exec while eventsets are running. THESE NEED TO BE ADDRESSED and rolled into the ctests directory
* 2008-04-02 Philip Mucci — Added Mark Krentels thread tester
* 2008-04-02 Philip Mucci — Committed time limit for this test. Should run for about TIME_LIMIT_IN_US as defined in papi_test.h. May need some tweaking for big machines.
* 2008-04-02 Philip Mucci — Allow avail.F build to fail due to broken GNU fortran on certain releases, other tests cover this one anyways.
* 2008-04-02 Philip Mucci — Removed MAKEFLAGS as suggested by Mark Krentel.
* 2008-04-01 Dan Terpstra — patch to aliases file
* 2008-04-01 Dan Terpstra — merge of changes in perfctr 2.6.31 merge of changes in perfctr 2.6.31
* 2008-04-01 Dan Terpstra — merge of changes in perfctr 2.6.31
* 2008-04-01 Dan Terpstra — Initial revision
* 2008-04-01 Haihang You — add event which can have counts for the testing run.
* 2008-03-31 Dan Terpstra — Move the perfmon versioning checks in _papi_hwd_init_substrate() above all calls to libpfm. Per Steve K. @ Cray.
* 2008-03-28 Dan Terpstra — Correction in the description of how error values are returned.
* 2008-03-28 Dan Terpstra — Cast error return from PAPI_thread_id to unsigned long to avoid warning message. This may not be the best solution, since it requires the calling function to cast back to signed to detect errors, but it preserves current API syntax.
* 2008-03-28 Dan Terpstra — add missing else branch to enum_add_native_events()
* 2008-03-28 Dan Terpstra — replace #ifdef _Power4 with test for cntr_groups flag.
* 2008-03-28 Haihang You — fix for enumerate on event with mask bit
* 2008-03-26 Haihang You — minor fix to get rid of some warnings
* 2008-03-26 Haihang You — fixes for monteceto
* 2008-03-13 Philip Mucci — Added new configure flags to handle static, shared libs and static building of tests: --disable/enable-static --disable/enable-shared --enable-static-tests
* 2008-03-07 Haihang You — add Makefile.linux-pfm-itanium3, add -DITANIUM3 for montecito, fixes for montecito support
* 2008-03-06 Dan Terpstra — Modifications to support data ranging and other special event types for Montecito using old perfmon interface.
* 2008-03-05 Philip Mucci — Always fill in context, not just SW.
* 2008-03-05 Dan Terpstra — Fix to differentiate between Intel Core Duo (family 6 model 14) and Core2Duo (family 6 model 15) processors. Implementation of a minimal (5 event) preset table, pending more complete native event table in libpfm.
* 2008-03-04 Dan Terpstra — Modifications to support unit masks for Montecito using old perfmon interface.
* 2008-03-04 Philip Mucci — Fix for overflow_force_software in perfmon platforms where we weren't settng the context correctly.
* 2008-03-03 Philip Mucci — Fixed error message
* 2008-03-03 Philip Mucci — More defensive read/pfm_restart semantics
* 2008-03-03 sbk — Support hardware counters in the exception (other) domain on Cray systems.
* 2008-02-29 Dan Terpstra — Minor syntax tweaks.
* 2008-02-29 Philip Mucci — Missed these commits...
* 2008-02-29 sbk — Remove 'exec2' from the build list until such time the source is supplied. This allows the make to succeed since it was failing on all Cray platforms.
* 2008-02-28 Philip Mucci — PAPI_read_ts and Fortran version
* 2008-02-28 Philip Mucci — *** empty log message ***
* 2008-02-28 Philip Mucci — Add PAPI_read_ts man page
* 2008-02-28 Philip Mucci — Docs get installed to prefix/share/doc.
* 2008-02-28 Philip Mucci — CHeck for papi initialization before ever calling lookup thread.
* 2008-02-28 Philip Mucci — Finally a full complement of fork and exec tests. This shows perfctr failures with EEXIST that should be fixed soon.
* 2008-02-28 Philip Mucci — iCleaner test cases. exec fails on perfctr systems currently. Working to fix it. Test case is good. PAPI code is bad.
* 2008-02-21 Dan Terpstra — Updated Barcelona event table to match current event names in libpfm-3.y
* 2008-02-19 Philip Mucci — Test case from Mark Krental for threads and OV_F_SW
* 2008-02-19 Philip Mucci — Defensive checks for thread, flags and FD in place. CVi: ----------------------------------------------------------------------
* 2008-02-18 Dan Terpstra — Fixed a dereferencing problem.
* 2008-02-18 Dan Terpstra — This test isn't working. I don't think it ever worked. It formerly PASSed, but reported negative profile values. I added a SKIP if running TESTS_QUIET. It still runs (and fails) from the command line.
* 2008-02-18 Philip Mucci — More defensive checking in interrupt handler
* 2008-02-16 Dan Terpstra — Modify table of pebs_enable values for replay_event and fix a potential bug in masking tag bits for the umask values.
* 2008-02-16 Dan Terpstra — Got rid of a memory leak.
* 2008-02-16 Dan Terpstra — Provided more information on create_context errors; Eliminated a cast warning.
* 2008-02-16 Dan Terpstra — Removed error return if event is added successfully but not started successfully. The fixes the cascading failure problems on Pentium4 replay_event. Also beefed up error reporting a bit.
* 2008-02-14 Dan Terpstra — Refactor several utilities to move hwinfo print block to a commonly accessible subroutine. For clarity and maintenance; no functionality change.
* 2008-02-14 Dan Terpstra — Refactor several tests to move hwinfo print block to a commonly accessible subroutine. For clarity and maintenance; no functionality change.
* 2008-02-14 Dan Terpstra — Added prototype for PAPI_read_fast_ts() introduced by Phil for Paraver, TAU, Kojak. This still needs a man page and (possibly?) a Fortran interface.
* 2008-02-12 Dan Terpstra — Fixed an infinite loop in event_chooser. This showed up as a result of the rework of PAPI_enum_events. Thanks to Wyatt Spear. We really should make a file of shared output routines for avail, native_avail and event_chooser. That way common formats would live in one place and actually *look* the same...
* 2008-02-11 Dan Terpstra — Added another check for event file in parent directory. This makes it possible to successfully run utils and tests from their own directory. I.E.: > cd utils > papi_avail In addition to: > utils/papi_avail
* 2008-02-11 Dan Terpstra — Eliminate redundant -DNO_MEMORY_MANAGEMENT flag. CAUTION: This may *not* be redundant in some cases; further testing needed.
* 2008-02-11 Dan Terpstra — Minor syntax correction.
* 2008-02-11 Dan Terpstra — Fix for memory limited cases; proceed with smaller thread allocation.
* 2008-02-11 Haihang You — montecito port.
* 2008-02-08 sbk — Must add the other incarnations of AMD Opteron and one more for Barcelona so the PAPI presets for those revisions are set. This is based on the enumeration of said AMD revisions in libpfm/lib.
* 2008-02-08 sbk — Could not get Cray XT tests to bulid statically because building libpapi.so shared failed and I couldn't find a way around it. Oh well.
* 2008-02-08 sbk — Always build Cray-XT CNL tests statically.
* 2008-02-07 Dan Terpstra — Patches from Corey Ashford to fix compile and lock problems for ppc/perfmon.
* 2008-02-06 sbk — When the modules are properly set for Catamount, use the top-level cc and f77 compiler drivers.
* 2008-02-05 Dan Terpstra — New definitions for Barcelona FP_OPS and FP_INS, as well as implementations of FML_INS, FAD_INS, FSQ_INS, and FDV_INS. All these thanks to observation by Bill Homer of Cray re: new native event for Barcelona.
* 2008-02-04 Dan Terpstra — Implemented L1_LDM and L2_LDM for Pentium4 based on work by Kenneth Hoste and newly implemented replay_event logic in perfmon2.
* 2008-02-04 Dan Terpstra — Add a kernel version check to insure a match between the kernel ABI and the libpfm ABI. From a suggestion by Steve Kaufmann @ Cray.
* 2008-01-31 Dan Terpstra — Mods to support recent changes in libpfm to handle 'virtual masks' on replay_event. This provides limited support for cache events on Pentium 4. The perfmon_events.csv file must still be modified to support cache events.
* 2008-01-28 Dan Terpstra — Clean up formatting in papi_avail and add support for event list filtering. Add support for the -e EVENTNAME option to papi_native_avail for symmetry with papi_avail.
* 2008-01-26 Dan Terpstra — Update Opteron Barcelona table so it matches K8 table but with new names; Add a couple L3 cache events. There may be more L3 events, but these were the obvious ones.
* 2008-01-24 Dan Terpstra — Fixed a bug in name string length.
* 2008-01-23 Dan Terpstra — Fixes to properly load Opteron Barcelona floating point events. Now I need to flesh out the event table...
* 2008-01-22 sbk — Add support in configure for --with-perfmon accepting versions "22" and "23". This is for (mostly) Cray XT and X2 backward-compatability support for the perfmon2 v2.2 and v2.3 ABI interfaced.
* 2008-01-18 Dan Terpstra — Modify papi_avail to classify events by type. See papi_avail -h for details.
* 2008-01-18 Dan Terpstra — Implement a shadow data structure to classify PRESET events by a variety of types as defined in papi.h Modify PAPI_get_event_info to provide user access to these types.
* 2008-01-17 sbk — Ooops. Back out changes that should have never occurred.
* 2008-01-17 sbk — Remove -D PFMLIB_VERSION_22 from CNL and Catamount make files. This switch is set in the subsequent libpfm configuration.
* 2008-01-16 Dan Terpstra — Mods to support Opteron Barcelona under perfctr, and a first cut PAPI PRESET table for Barcelona. Thanks to Steve K @ Cray.
* 2008-01-16 Haihang You — use cntr_groups
* 2008-01-15 Dan Terpstra — Modify coding for enum groups to eliminate #ifdefs and make it run-time decodable. Tested on opteron for compile and link; not yet tested on POWER.
* 2008-01-14 Dan Terpstra — Modify coding for enum groups to eliminate #defines and make it run-time decodable. Tested on opteron for compile and link; not yet tested on POWER.
* 2008-01-14 Dan Terpstra — Modify POWER4/5/6 support for enum groups to make it less platform specific and run-time decodable. This allows us to get rid of more of those pesky #defines in, e.g.,  native_avail.
* 2008-01-11 Dan Terpstra — Enable a SUBDBG output to display the name of the CPU that was matched for loading events.
* 2008-01-11 Dan Terpstra — Restore 80 char line lengths modified by sbk. Fix to fail gracefully on mask names longer than can be formatted to fit 80 char lines. Only two occurences for one event on Opteron currently identified. SOME_OF_THESE_MASK_NAMES_ARE_GRAMMATICALLY_COMPLETE_FULL_SENTENCES!
* 2008-01-11 Dan Terpstra — Limit perfmon from providing more mask bit definitions than can be supported by papi. This is currently restricted to 16 per native event, where perfmon can support 48. Only 1 known event exceeds that limit for Opteron, and many of the mask definitions are arguably udefined.
* 2008-01-10 Dan Terpstra — Point to libpfm-3.y directory instead of libpfm-3.x directory. And *never, ever* commit changes to libpfm in this directory! Pass them along to Stephane!
* 2008-01-10 Dan Terpstra — Initial revision
* 2008-01-10 Haihang You — for AMD, this test does't check the difference with the threshold.
* 2008-01-10 Haihang You — use PAPI_FP_OPS if it exists
* 2008-01-10 sbk — Increase EVT_LINE from 80 to 120 to accommodate very long subevent names in the new AMD Opteron event tables in libpfm.
* 2008-01-10 Haihang You — add type casting from caddr_t to unsined long for new changes made to profile
* 2008-01-10 Haihang You — minor fix
* 2008-01-10 Haihang You — fix comments for aix
* 2008-01-08 Dan Terpstra — Big commit that introduces a rework of PAPI_enum_event to remove a bunch of platform dependencies, including the #defines for x1 and a bunch of #defines for Pentium4. This also incorporates changes to support the Itanium DARR and IARR stuff in a platform independent way. Yet to do: Power 4/5 grouped event enumeration. Some of this stuff isn't fully tested; we'll see how Tinderbox likes it...
* 2008-01-08 sbk — Added another alias for AMD (Revision E).
* 2008-01-05 Philip Mucci — Fix for signal status array length
* 2008-01-03 sbk — Perform integer calculations to retain as many bits as possible in the presence of division.
* 2007-12-22 Dan Terpstra — Addition of (K8 RevC) string for Opteron event table. Needed for perfmon. Thanks to Steve Kaufmann for identifying and Rick Kufrin for fixing this one.
* 2007-12-21 Philip Mucci — Lowered memory locking limit for perfmon2 sampling. Added C99 caddr_t def.
* 2007-12-21 Philip Mucci — Forward patches from SiCortex and perfmon.c. Improvements in overflow handling and address passing to/from sample handles. Move to unsigned long internally instead of caddr_t.
* 2007-12-21 Philip Mucci — Allow unknown processors in the preset map to still initialize and count native events.
* 2007-12-21 Philip Mucci — IA64: Now use kernel profiling buffers. Fixes for software overflow force case.
* 2007-12-21 Philip Mucci — Changes for recent 2.6.x IA64 kernels. Fix spurious signal issue originally reported and fixed on Altix
* 2007-12-13 Philip Mucci — Spooky copyright notice removed. Now part of PAPI's LGPL...
* 2007-12-13 Philip Mucci — Add proper PWD setting
* 2007-12-13 Philip Mucci — - Build do_loops with just -g -O - Sparc64/Linux/Perfmon2 support from David Miller
* 2007-12-13 Philip Mucci — - Build do_loops with just -g -O
* 2007-12-13 Philip Mucci — - Sparc64/Linux/Perfmon2 support from David Miller - Set TESTOPT to -O -g - Remove libpapi.so when clobbering
* 2007-12-07 Dan Terpstra — This file is no longer used for native events. libpfm is used instead.
* 2007-12-07 Dan Terpstra — Cleanup of definitions of PAPI_TOT_IIS and PAPI_TOT_INS. TOT_INS was fixed inside libpfm to select the proper event based on model # TOT_IIS was improperly qualified by model # but didn't rely on a model dependent event.
* 2007-12-07 Dan Terpstra — Qualification of definition of _get_instr_retired(). Now checks model # before selecting either instr_completed or instr_retired. We really need to stop checking changes into this directory tree and just import them from Stephane.
* 2007-12-06 Dan Terpstra — Condition definition of PAPI_TOT_INS on model >= 3. This code hasn't been tested, but it's a pretty simple change. Famous last words.
* 2007-12-05 Haihang You — rearrage the test case.
* 2007-12-05 Haihang You — fix derived preset and multi native events counting problem on opteron, maybe other linux platform as well.
* 2007-12-04 Dan Terpstra — Change definition of cpuid (again). Protect ebx with a bit-width independent push and pop. Seems to work everywhere tested, and may solve an esoteric problem in 64-bit systems.
* 2007-11-30 mkasam — *** empty log message ***
* 2007-11-29 Dan Terpstra — Minor fix to identify Opteron Barcelona (family = 0x10) Thanks to Jeff Larkin @ CRAY/ORNL
* 2007-11-29 Philip Mucci — Merge up to Sourceforge CVS
* 2007-11-29 Philip Mucci — Initial revision
* 2007-11-28 Dan Terpstra — Add PAPI_TOT_INS to Pentium4 based on input from Kenneth Hoste. This requires the latest perfmon files to work properly.
* 2007-11-28 Haihang You — minor fix for aix-power3
* 2007-11-27 Haihang You — fold in Corey Ashford's patch for power4 and power6 on perfmon.
* 2007-11-20 Haihang You — remove native test, as adding native events are tested by all_native_events
* 2007-11-20 Haihang You — minor fixes
* 2007-11-19 sbk — Fixed bug introduced in previous commit in regards to Cray-X2. Cray-X2 counters function more like other counters and do not need any special enum logic. See previous commit RE: files all_native_events.c and native_avail.c.
* 2007-11-19 Haihang You — using PAPI_enum_event to iterate native events
* 2007-11-19 Haihang You — set num_native_events & num_preset_events
* 2007-11-15 Haihang You — make the previous changes a special case for core2
* 2007-11-10 sbk — Minor tweaks to M chip names to make undefined names more consistent with named events. Added comments to make it easier to navigate the table.
* 2007-11-09 Dan Terpstra — Synchronize with the latest import. I wish I knew why...
* 2007-11-08 Dan Terpstra — update to latest sourceforge
* 2007-11-08 Dan Terpstra — Remove files in papi but no longer in sourceforge.
* 2007-11-08 Dan Terpstra — These files didn't get updated in the last import.
* 2007-11-08 Dan Terpstra — Remove files in papi but no longer in sourceforge.
* 2007-11-08 sbk — Changes to accommodate the new method of specifying Cray X2 event counter names. No need to make special arrangements to handle the unit masks which were not implemented as unit masks. No unit masks are used to represent these updated events.
* 2007-11-08 sbk — Redefine the Cray X2 counter events structure. Mostly deals with the way M chip events are represented. Previously the libpfm unit masks were used to idenfify which memory chip the event was activated upon. Using unit masks in this way was knowingly incorrect, and tools such as PAPI assume that unit masks can be bit-wise OR'd.
* 2007-11-07 Dan Terpstra — Fix make clean so it removes libpfm and properly triggers a rebuild.
* 2007-11-06 Dan Terpstra — merge of imported files with what's already there
* 2007-11-06 Dan Terpstra — Initial revision
* 2007-11-06 Philip Mucci — Unify threshold management for these 4 tests
* 2007-11-06 Philip Mucci — Fix for multiplexing wen removing events. Reported by Corey Ashford of IBM. Fix for forcing of software user level propfiling  VS: ----------------------------------------------------------------------
* 2007-11-05 Dan Terpstra — Fix Opteron event name typo to match fixed typo in libpfm
* 2007-11-05 Dan Terpstra — Update libpfm3 to latest sourceforge snapshot.
* 2007-11-02 Dan Terpstra — Mod to add support for a single OR'd mask value to the last round of changes.
* 2007-11-02 Haihang You — fix the the path to libpfm-2.x. thanks to Don.
* 2007-11-01 Haihang You — get rid of a printout message
* 2007-11-01 Haihang You — minor fix to get rid of warnings
* 2007-11-01 Haihang You — add new overflow test to test availability of overflow on all counters. It will create a eventset with native events occupying all counters, and iterate the overflowing on each one of them.
* 2007-11-01 Haihang You — add 5 counters support for core2
* 2007-11-01 Philip Mucci — Test for profile_force_sw
* 2007-10-31 Haihang You — modify LD_LIBRARY_PATH to libpfm-2.x
* 2007-10-31 Philip Mucci — Proper threshold for perfmon
* 2007-10-30 Dan Terpstra — Mod to accept valid colon-separated hex unit mask codes in addition to names for native event name strings. Requested by Rob Fowler to reduce the length qualified native event names.
* 2007-10-30 sbk — In v2.2 perfmon PFM_DFL_SMPL_UUID must be defined an used when sampling using the counters. It is not needed after v2.2 but is needed here for backward compatability.
* 2007-10-27 sbk — The *standalone* examples failed because the standalone.h file that contains the same pfm* wrappers as in lib/pfmlib_os.c did not have the version 22 macro defined for the XT.
* 2007-10-25 Philip Mucci — Last fix for the Altix! Cst fix VS: ----------------------------------------------------------------------
* 2007-10-25 Haihang You — add libpfm-2.x/lib to LD_LIBRARY_PATH. It is needed on itanium and libpfm-2.x combo.
* 2007-10-25 Haihang You — fix comments for aix. Don's script is handy.
* 2007-10-24 Philip Mucci — Added testing code for overflow_pthreads that will show the bug on the Altix. Modified realtime pass criteria. Removed printf from sdsc test.
* 2007-10-24 Philip Mucci — Fixes for seriously broken Altix kernel substrates. Also support for reset during overflow on IA64 systems. Working and tested on 2.6.16 Altix, 2.6.9 and 2.4.21. Tested on Madison hardware.
* 2007-10-22 Haihang You — replace add_two_event with add_two_nonderived_event for overflow and profile tests
* 2007-10-17 Philip Mucci — Updated MMTIMER for latest Altix releases. Working and tested on a 4700.
* 2007-10-16 Philip Mucci — Added MAX_THREADS definition, which should always be used. NUM_THREADS should be removed. MAX_THREADS should also be checked against ncpu.
* 2007-10-16 Philip Mucci — Fix for libpfm-2.x semantics of get_event_name
* 2007-10-16 Philip Mucci — Support for USE_SEMAPHORES which are now disabled. Also, proper cleanup of semaphores in a destructor if used. Use improved IA64 locking with store semantics.
* 2007-10-16 Philip Mucci — Updated IA64 locking. We needed a store with release semantics.
* 2007-10-16 Philip Mucci — Added --with-semaphores option for broken IA64 installations. Also passed flags to libpfm nicely when debugging. Fixed up PAPI_DATADIR handling.
* 2007-10-16 Philip Mucci — Improve return codes of PAPI_enum_event
* 2007-10-15 Haihang You — correct return local variable in pfmw_get_event_name()
* 2007-10-13 Philip Mucci — Improved test case and fix for multiplexing/non-multiplexing
* 2007-10-12 Haihang You — use nonderived events for profile test ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ "/tmp/cvszUaaiU" 9 lines, 350 characters Checking in ctests/overflow_twoevents.
* 2007-10-12 Haihang You — use nonderived events for overflow test
* 2007-10-11 Dan Terpstra — Minor changes to support CPU name synonyms. This addresses a difference in naming schemes between what perfmon was reporting and what was hard-coded into our perfctr substrates for Pentium4. Pentium4/perfmon is still not working, but at least it now finds the event table.
* 2007-10-10 Haihang You — fix profile bugs
* 2007-10-10 Dan Terpstra — Initial revision
* 2007-10-10 Dan Terpstra — commiting merged changes of perfctr-2.6.29
* 2007-10-10 Dan Terpstra — Initial revision
* 2007-10-10 Philip Mucci — Fix for when multiplexing is used and then the eventset is deleted.
* 2007-10-08 sbk — Do not configure Cray CNL OS to link statically by default.
* 2007-10-08 Philip Mucci — Fix for domain and vendor code detection from Corey Ashford, IBM
* 2007-10-05 mkasam — Fixed the export variable in run_tests.sh
* 2007-10-05 Philip Mucci — Revert previous change until we sanitize our IA64 build environment
* 2007-10-05 Philip Mucci — Skeleton code to check for PAPI_reset working with PAPI_overflow
* 2007-10-05 Philip Mucci — Seriously broken on IA64 for perfmon1 platforms. This likely affects virtually all IA64's out there. Configure was enabling features for libpfm-3.x on platforms that require 2.x.
* 2007-10-05 Philip Mucci — Fix for perfmon2, when using oveflow, read and reset
* 2007-10-05 Philip Mucci — Fix for perfmon2, when using oveflow, read and reset
* 2007-10-04 Dan Terpstra — Added "--with-linkstatic" to force static linking by adding the -static argument to LDFLAGS.
* 2007-10-03 Dan Terpstra — modifications on validation tests to allow for wider range of variance on software overflows. For perfmon/opteron they were coming in at about 20% of hardware overflows, which was just under the accepted limit.
* 2007-10-03 Dan Terpstra — rework _papi_hwd_dispatch_timer to properly handle forced software (timer based) overflows in addition to hardware overflows.
* 2007-10-02 Dan Terpstra — rolled back element count on a calloc call in _papi_hwd_update_shlib_info. This got inadvertently changed during a recent merge. Should fix problem identified on CNL/X2.
* 2007-10-02 Philip Mucci — Fixed up definitions for Intel Core ICache metrics
* 2007-10-01 Haihang You — as bgl_tests moved from src to src/ctests, Makefile needs tobe modified.
* 2007-10-01 Haihang You — replace add_two_events with add_two_nonderived_events
* 2007-09-28 Haihang You — put _papi_hwd_shutdown() back, as it is needed by _papi_hwi_shutdown_thread()
* 2007-09-28 Haihang You — restructure the test with quiet mode, put _papi_hwd_shutdown back to solaris substr
* 2007-09-27 Haihang You — add add_two_nonderived_events(), it is needed for tests are only valid for non-derived events like overflow
* 2007-09-26 Haihang You — _papi_hwd_ntv_code_to_name() return PAPI_ENOEVNT when event does not exist
* 2007-09-26 Haihang You — set _papi_hwi_system_info.sub_info.num_native_events
* 2007-09-26 Haihang You — add address into _papi_hwi_dispatch_overflow_signal(&ctx, address, NULL, 0, 0, &t);
* 2007-09-25 Haihang You — fix code2name program on ia64. in pfmw_get_event_name(idx), idx has to be less than total number of events pfm supports.
* 2007-09-14 Haihang You — fold in more changes in test files
* 2007-09-14 Haihang You — fixes for solaris and itanium
* 2007-09-14 Haihang You — roll back previous changes
* 2007-09-12 Haihang You — fold in phil's changes into perfmon.c, and change arguments' list of _papi_hwi_dispatch_overflow_signal in linux.c
* 2007-09-11 Dan Terpstra — Changes from Phil to modify the way overflow addresses are handled. Non-perfmon substrates will need similar modifications.
* 2007-09-11 Dan Terpstra — Changes from Phil to modify the way overflow addresses are handled.
* 2007-09-10 Dan Terpstra — Changes from Phil. These will probably break the build until the rest gets checked in.
* 2007-09-10 Dan Terpstra — New pthreads test added by Phil.
* 2007-09-10 Dan Terpstra — Minor changes in string lengths and in the MIPS ICE-9 event table.
* 2007-09-06 Dan Terpstra — Commit a local copy of the resolution independent version of cpuid pending stabilization of the sourceforge version of libpfm.
* 2007-09-06 Haihang You — before link libpapi.so, remove it.
* 2007-09-06 Dan Terpstra — Redefine the cpuid function shared by these two files as inline to work around an apparent bug in gcc 4.1.2 for Intel Core. With -O3, the function is inlined and works; with -O2 or less, the function is standalone and causes a segfault. By declaring it as inline it works regardless of optimization level.
* 2007-09-04 Dan Terpstra — Remove selector massaging based on CORE2 identification; It's apparently no longer needed.
* 2007-08-31 sbk — Fix the label of clock ticks to match that in ctests.
* 2007-08-30 sbk — Print out clock tick value where appropriate as it was in the ctests.
* 2007-08-30 Dan Terpstra — Updated both files with a universal (I hope) version of cpuid. There's way too much duplicate code in these files (and in linux.c and perfmon-memory.c) We need to consolidate this stuff in one file...
* 2007-08-30 Haihang You — call papi_init after exec
* 2007-08-30 Haihang You — create libpapi.so, setenv LD_lIBRARY_PATH to make shlib pass.
* 2007-08-29 sbk — Save sysconf(_SC_CLK_TCK) in a hw_info member when global stuff is initialized. Use this member in timing calculations in place of sysconf(_SC_CLK_TCK). Those apps that call thse timing routines should get a performance boost since now they'll avoid a system/library call with each call.
* 2007-08-28 sbk — For the "shell" commands in make files, use a macro if it exists. When checking for the GNU C compiler version for OpenMp, compare against "4.2" since this is the first version that OpenMP is supported by GNU.
* 2007-08-23 sbk — Forgot to update configure.
* 2007-08-23 sbk — Set the compilers for Catamount in its own Makefile rather than having configure do it.
* 2007-08-20 sbk — For XT/Catamount set the default for the SIGPROF and SIGALRM signals to ignore so when profiling or multipexing terminate, the state returns to this ignore state preventing stray interrupts from appearing. This changes allows the ctests for multiplexing, profile, and overflow to complete exection, although some do FAIL.
* 2007-08-20 sbk — mistyped SIGPROF
* 2007-08-20 sbk — define multiplexing signal separate from itimer signal
* 2007-08-17 Dan Terpstra — Initialize clock_mhz value that was added to this structure for perfmon.c There's still a lot of redundant code here that needs to be cleaned up.
* 2007-08-17 sbk — update Cray-x2 papi presets
* 2007-08-17 Haihang You — fix segfault
* 2007-08-16 sbk — use '.' instead of  to libpfm-3.x
* 2007-08-16 Dan Terpstra — Modify the family and model logic from cpuid to properly include the extended family and model info.
* 2007-08-15 sbk — check for too many input events for x2 dispatch
* 2007-08-15 Dan Terpstra — Changed type of event code from int to unsigned int to eliminate a warning.
* 2007-08-15 Dan Terpstra — Bump the size of event names in PAPI_event_info_t to HUGE to accomodate the occasionally *very* large native names produced by perfom2:opteron. Fixes buffer overflow error reported by Steve Kaufmann.
* 2007-08-14 Haihang You — expand build of fork exec forkexec forkexec2
* 2007-08-14 Dan Terpstra — Delete extra return line in _papi_hwd_ntv_code_to_descr to reflect updated calling sequence.
* 2007-08-14 Dan Terpstra — Change return value for _papi_hwd_ntv_code_to_descr from char * to int to reflect updated calling sequence.
* 2007-08-14 Dan Terpstra — Define $TESTS as ctests only for Cray X2.
* 2007-08-14 Dan Terpstra — Round 2 implementation of a $TESTS macro generated by configure. Added support for --with-tests in configure, and support for a $TESTS  macro in Makefile.inc.
* 2007-08-14 Dan Terpstra — Eliminate some dead code.
* 2007-08-14 Haihang You — set tests
* 2007-08-14 Haihang You — let configure to set tests by default, tests=ctests ftests on bgl, tests=bgl_tests on crayx2, tests=ctests
* 2007-08-14 Haihang You — change fork exec forkexec forkexec2: %: %.c $(UTILOBJS) $(PAPILIB) to be fork exec forkexec forkexec2: $(UTILOBJS) $(PAPILIB)
* 2007-08-13 Dan Terpstra — Syntax error: extra paren. Dang!
* 2007-08-13 Dan Terpstra — Purge some stray // comment lines. The AIX compiler doesn't like // comment lines.
* 2007-08-13 Dan Terpstra — Change virtual time calculations from (utime+stime)*((long_long)(1000000/sysconf(_SC_CLK_TCK))) to (long_long)(utime+stime)*1000000/sysconf(_SC_CLK_TCK) This postpones the divide and allows for greater computed resolution. Thanks to Steve Kaufmann @ Cray.
* 2007-08-10 sbk — remove unused make file for Cray X2
* 2007-08-10 sbk — update configure via autoconf
* 2007-08-10 sbk — update CNL Makfile, add -DPFMLIB_VERSION_22 for catamount, don't install .so's for X2 and XT/Cat
* 2007-08-10 Dan Terpstra — New combined Makefile for CNL-x2 and CNL-xt.
* 2007-08-10 Dan Terpstra — Ooops. I hadn't saved all the changes...
* 2007-08-10 Dan Terpstra — Change f77 to qk-g77 for catamount and target a single MAKEVER for CNL.
* 2007-08-09 Haihang You — set docdir
* 2007-08-09 Dan Terpstra — Updates for catamount with pfmlib events and first cut at Cray X2 CNL support.
* 2007-08-09 Dan Terpstra — Only build the library for libpfm. Make the install of shared libraries conditioned on !catamount. Thanks to Steve K @ Cray.
* 2007-08-09 Dan Terpstra — Make shared libraries dependent on !qk-gcc. Catamount doesn't do shared libraries. Thanks to Steve K @ Cray.
* 2007-08-09 Dan Terpstra — Rewrite _amd64_detect to rely on an inline asm version of cpuid instead of /proc/cpuinfo. This is primarily because catamount doesn't support /proc/cpuinfo, but also results in something much lighter weight. Pending Stephane's approval into libpfm...
* 2007-08-08 sbk — /tmp/sbk/msg
* 2007-08-08 Dan Terpstra — String initialization to 0 length in _papi_hwd_updae_shlib_info per Steve Kaufmann.
* 2007-08-07 Dan Terpstra — String length and allocation fixes by Steve Kaufmann to prevent crashes on Cray X2.
* 2007-07-31 Dan Terpstra — Change pfm_msg_t to pfarg_msg_t
* 2007-07-27 Dan Terpstra — Updates to Stephane's latest release.
* 2007-07-26 Dan Terpstra — Makefile for Cray X2.
* 2007-07-26 Dan Terpstra — First round of changes for CrayX2. Untested.
* 2007-07-26 Dan Terpstra — Preliminary changes to support crayx2. Specify --with-OS=CNL and --with-CPU=crayx2 on the configure command line. This will select Makefile.CNL-perfmon2-crayx2. More work needs to be done...
* 2007-07-26 Dan Terpstra — Mod to support perfmon2 native event names. *Not tested*
* 2007-07-26 Dan Terpstra — Corrected syntax error.
* 2007-07-24 Dan Terpstra — Changes to the make sequence to handle shared library dependencies. Thanks to Todd Gamblin of UNC.
* 2007-07-23 Dan Terpstra — Fixed a call to strncpy, thanks to Tinderbox and Don Fike; Fixed a pointer dereferencing problem in native and preset tables.
* 2007-07-18 Dan Terpstra — Fix for POWER6 definition of TOT_CYC. Submitted by Corey Ashford.
* 2007-07-18 Dan Terpstra — Fix for POWER6 to set domain to ALL. Submitted by Corey Ashford.
* 2007-07-18 Dan Terpstra — Fix to second to enable all supported domains instead of all possible domains (except SUPERVISOR).
* 2007-07-18 Dan Terpstra — Add two Makefiles that were overlooked when committing Corey Ashford's POWER6 updates.
* 2007-07-05 Dan Terpstra — Changes in both framework layer and component layers to accomodate new calling sequence for code_to_{name,descr} functions. This eliminates the return of potentially malloc'd strings to the framework layer which removes a potential memory leak and a thread-safety problem. Tested on most x86 architectures; Please test on your favorite architecture of choice.
* 2007-07-05 Dan Terpstra — Changes by Stephane to support Opteropn revision differences.
* 2007-06-26 Dan Terpstra — Fix for extra long native event name problems. CAUTION: This returns a strdup of a possibly long name, which in some cases may not be free()d. That sets up a potentially significant memory leak...
* 2007-06-20 Dan Terpstra — Corey Ashford's changes to support IBM POWER6/Linux. Here's a couple files I missed...
* 2007-06-06 Dan Terpstra — Changes to multiplex to allow mpx event sets to inherit domain and granularity from parent event sets rather than from defaults. Thanks to Corey Ashford and Maynard Johnson of IBM.
* 2007-06-05 Dan Terpstra — Updates to perfmon-only bits_to_info. Tested on opteron only.
* 2007-06-04 Dan Terpstra — Corey Ashford's changes to support IBM POWER6/Linux.
* 2007-06-04 Dan Terpstra — Fixed typo in line 871 identified by Don Fike.
* 2007-05-25 Philip Mucci — Missed one
* 2007-05-25 Philip Mucci — Make sure we install the GIF
* 2007-05-25 Philip Mucci — Exported to standard formats using OpenOffice. PDFs and GIFS checked in with -kb
* 2007-05-24 Philip Mucci — Make sure local include paths come before system include paths. This will prevent version skew with an installed PAPI.
* 2007-05-24 Philip Mucci — Full prototype:
* 2007-05-24 Philip Mucci — Prototypes for < extern int _papi_hwi_error_level; < extern hwi_describe_t _papi_hwi_err[];
* 2007-05-24 Philip Mucci — String overrwrite bug caused by new string length introduction. Caught on SiCortex.
* 2007-05-22 Dan Terpstra — Removed bogus references to deprecated papi_data.h file.
* 2007-05-22 Philip Mucci — Install docs in $docdir, including HTML man pages, license, .doc files. Modify configure to install man pages in LSB standard /usr/share/man Modify configure to install doc pages in /usr/share/doc/papi
* 2007-05-22 Philip Mucci — Regenerate with newer autoconf, which sets mandir to datarootdir/man. This allows Linux man pages to be installed in the LSB standard place of /usr/share/man.
* 2007-05-21 Dan Terpstra — Merged  lost changes in _bits_to_info from Phil's last commit to the papi-3-5-0 branch.
* 2007-05-18 Dan Terpstra — Move unused GNU Makefile to the attic.
* 2007-05-18 Dan Terpstra — Move outdated documentation files to the attic.
* 2007-05-18 Philip Mucci — This needs to use _papi_hwi_locks...
* 2007-05-18 Philip Mucci — Pointers to static data structures should not be incremented. When forks() happen allhell breaks loose. Now if we have built-in events, use a tmp variable.
* 2007-05-18 Philip Mucci — ksh is not standard anywhere
* 2007-05-18 Philip Mucci — ksh is not standard anywhere really...but sh is.
* 2007-05-18 Dan Terpstra — Fixed double reporting of Mem Peak Size.
* 2007-05-18 Philip Mucci — Add the important AR extract function for libpfm.a Comment out HW cycle counter for SiCortex, it's just a tmp fix. MIPS should use gettimeofday().
* 2007-05-15 Dan Terpstra — Merged changes from Phil's commit to 3.5 branch.
* 2007-05-15 Dan Terpstra — Merged changes from Phil's commit to 3.5 branch.
* 2007-05-15 Dan Terpstra — Updated CPUID cache info for Intel x86 cpus.
* 2007-05-15 Dan Terpstra — Updated table for CPU-IO_REQUESTS_TO_MEMORY-IO event.
* 2007-05-10 Dan Terpstra — Add Harald Servat's overflow_values test to the project. This test verifies Maynard Johnson's fix to the overflow read that provides correct counter values inside an overflow handler. A version of this test was verified on ppc64; this test verified on Opteron, Athlon, P4, PIII, and Core. It may still choke on other systems.
* 2007-05-10 Dan Terpstra — Added PAPI_TOT_CYC event to Pentium4 table. How did that get overlooked?
* 2007-05-08 Dan Terpstra — Changes to properly sample all counters during overflow when using perfctr. Calls vperfctr_read_state instead of vperfctr_read_pmc in the overflow handler.
* 2007-05-07 Maynard Johnson — Remove unnecessary makefile
* 2007-05-07 Maynard Johnson — Add POWER6 support to perfctr2.7.x
* 2007-05-01 Dan Terpstra — Fix initialization of domain and granularity when an eventset is created. Thanks to Corey Ashford of IBM.
* 2007-04-27 Dan Terpstra — Merged changes from papi-pfm branch to HEAD. Also merged Steve Kaufmann's code to allow the perfmon_events.csv file to be incorporated directly as a header file. See the --with-pfm-events=<static,file> switch in configure. Tested on Pentium4.
* 2007-04-10 Haihang You — minor fixes
* 2007-04-10 Haihang You — allow using different compilers and CFLAGS FFLAGS for building on BG/L e.g. ./configure --with-OS=bgl CC=blrts_xlc F77=blrts_xlf CFLAGS="-D_BGL -qarch=440 -qmaxmem=64000" FFLAGS=-Dlinux
* 2007-04-09 Dan Terpstra — Merge specialized BG/L tests from 3.5.0 branch, where they were first introduced.
* 2007-04-07 Dan Terpstra — Correction to error tests for _papi_hwd_ntv_code_to_name and _papi_hwd_ntv_code_to_bits
* 2007-04-05 Haihang You — fix reported bug if test "x$AR" = "x"; then
* 2007-04-05 Dan Terpstra — Changes from Maynard and Corey @ IBM to better support POWER5+.
* 2007-03-29 Haihang You — remove semophore when shutdown the substrate
* 2007-03-06 Dan Terpstra — Fix for edge conditions on the distribution array. Identified by Dong Ahn.
* 2007-03-06 Dan Terpstra — Remove comment refering to PAPI 3.4.9 pre-release. Thanks to Celso Mendes.
* 2007-02-20 Dan Terpstra — Mods to support external event tables in files such as p3_core_event_tables.h, etc. Also now supports generalized umask bits, at least for opteron. This is a poor man's emulation of perfmon2 native event functionality.
* 2007-02-16 Dan Terpstra — Restructuring of p3_events file into a base code file and several event table files. This provides for easier maintenance. It may never make production, because libpfm may be a better way to support this. But it's easier to commit it and delete it than to lose it and need to reconstruct it.
* 2007-02-15 Dan Terpstra — Changes from Phil re: new fields in dmem_info; Fix typo in previous merge.
* 2007-02-12 Dan Terpstra — Changes from Phil re: new fields in dmem_info.
* 2007-02-12 Philip Mucci — When adding an error code, you need to add the string as well as bump the number of error codes
* 2007-02-09 Dan Terpstra — New make file for Intel Core processors. Supports either straight perfctr or perfctr/libpfm for native events.
* 2007-02-06 Dan Terpstra — Patches from Maynard Johnson for Power5+/Linux
* 2007-02-05 Dan Terpstra — Changed PAPI_EINIT to PAPI_ENOINIT per Phil's request.
* 2007-02-04 Dan Terpstra — Added explicit support for Intel Core; relaxed id conditions for Opteron.
* 2007-02-04 Dan Terpstra — Update to latest sourceforge commits.
* 2007-01-31 Dan Terpstra — Add a check for library init to PAPI_event_name_to_code() and a PAPI_EINIT error to papi.h. This check should probably be added to *every* exposed API entry point.
* 2007-01-26 Haihang You — check for core 2
* 2007-01-19 Dan Terpstra — Add files that existed in 3.5 branch and sourceforge but not in HEAD.
* 2007-01-18 Dan Terpstra — Update to latest sourceforge commits.
* 2007-01-10 Dan Terpstra — Add SuSE info to the discussion of the perfctr permissions fix for systems running udev.
* 2007-01-09 Dan Terpstra — Incorporate changes made to 3.5.0 branch since tag papi-3-5-0-m1 into HEAD. This includes all changes up to and including the tag papi-3-5-0-m2. Primarily support for POWER5+ and updated perfmon files.
* 2007-01-09 Dan Terpstra — Add discussion of the perfctr permissions fix for systems running udev.
* 2006-12-04 Dan Terpstra — Incorporate changes made to 3.5.0 branch into HEAD. This includes all changes up to and including the tag papi-3-5-0-m1.
* 2006-11-17 Dan Terpstra — We deprecated this file in PAPI 3.5.
* 2006-11-17 Dan Terpstra — Where did this directory come from anyway? Another extraneous copy of perfctr bites the dust.
* 2006-11-17 Dan Terpstra — Remove extraneous Alpha files leftover in HEAD.
* 2006-11-17 Dan Terpstra — Remove Kevin's private copy pf perfctr leftover in HEAD.
* 2006-11-17 Dan Terpstra — Remove extraneous T3E files leftover in HEAD.
* 2006-11-17 Dan Terpstra — Remove extraneous Visual Studio 6 files leftover in HEAD.
* 2006-11-17 Dan Terpstra — Copying all old file(s) from PAPI 3.5 branch to HEAD.
* 2006-11-17 Dan Terpstra — Adding new file(s) from PAPI 3.5 branch to HEAD.
* 2006-11-16 Dan Terpstra — Adding new file(s) from PAPI 3.5 branch to HEAD.
* 2006-11-16 Dan Terpstra — Adding new file(s) from PAPI 3.5 branch to HEAD.
* 2006-11-16 Dan Terpstra — Adding new file(s) from PAPI 3.5 branch to HEAD.
* 2006-10-16 Dan Terpstra — Merging changes from perfctr 2.6.25 into sources
* 2006-10-16 Dan Terpstra — Initial revision
* 2006-09-18 Dan Terpstra — merging changes in Makefile to perfctr-2-6-24
* 2006-09-18 Dan Terpstra — Initial revision
* 2006-08-23 Dan Terpstra — Merging changes
* 2006-08-23 Dan Terpstra — Initial revision
* 2006-07-01 london — Fix to return a value if using the papi_m* calls.
* 2006-06-05 Dan Terpstra — merging changes and conflicts
* 2006-06-05 Dan Terpstra — Initial revision
* 2006-04-27 Dan Terpstra — Add a note indicating that our configure script lives in /src, not papi.
* 2006-04-25 Dan Terpstra — resolving conflict in Makefile
* 2006-04-25 Dan Terpstra — Initial revision
* 2006-04-10 Dan Terpstra — Updates to support AMD64 and restructured build.
* 2006-04-10 Dan Terpstra — Updates to support AMD64 and restructured build.
* 2006-04-10 Dan Terpstra — New files to build a command line test harness for the winPMC.sys kernel driver. This allows unit testing of the driver without requiring a complete GUI and PAPI library.
* 2006-04-10 Dan Terpstra — Pure assembly level rdpmc routine to support lack of inline assembly in Microsoft's AMD64 compiler. This is really tacky, because it requires a subroutine call to execute a single assembly instruction. But so far, I haven't figured out a better way to do it.
* 2006-04-10 Dan Terpstra — Updates to support AMD64 are restructured build.
* 2006-04-10 Dan Terpstra — Pure assembly level cpuid routine to support lack of inline assembly in Microsoft's AMD64 compiler.
* 2006-04-07 Dan Terpstra — Added new opteron events identified by Sarah Anderson of Cray. There are more new events available. This table should reviewed against current AMD docs.
* 2006-03-16 Dan Terpstra — Maynard's fix for building PPC64-bit
* 2006-03-15 Haihang You — data range pfm30 support
* 2006-03-09 Dan Terpstra — Maynard's domain propagation changes for ppc64 linux
* 2006-03-09 Dan Terpstra — Attempted to implement pfmw_get_event_description. It works for libpfm2/Itanium2. It doesn't work anywhere else. The underlying routines were deprecated for libpfm3; I don't know why. The data is still in the event info structure :(
* 2006-03-08 Dan Terpstra — Naming and casting changes for consistency between pfmlib 2 and 3
* 2006-03-08 Dan Terpstra — This one is generated by autoconf; the previous copy was edited in Windows and not executable.
* 2006-03-07 Dan Terpstra — Add html documentation for data range restriction feature.
* 2006-03-07 Haihang You — put in test_quiet
* 2006-03-06 Dan Terpstra — Added support to enumerate Itanium native events filtered by qualifiers including - data event address register - instruction event address register - data address range restriction - instruction address range restriction - opcode matching
* 2006-03-04 Haihang You — add Dan's data_range test case.
* 2006-03-04 Haihang You — fixes for instruction and data range support. Now everything is done by PAPI_set_opt. A
* 2006-03-03 Dan Terpstra — Rip out the PAPI_get_opt support stuff for data and instruction range. There's a better way; we can just pass the offset info back in the option structure.
* 2006-03-03 Dan Terpstra — Copy instruction and data range offsets into context for get_opt.
* 2006-03-03 Dan Terpstra — Changed detection string for newer Opterons per input from gwh@allinea.com
* 2006-03-02 Dan Terpstra — Modifications to get range addresses and offsets
* 2006-03-02 Dan Terpstra — Modifications to get range addresses and offsets
* 2006-03-02 Haihang You — fix for rr support
* 2006-02-28 Dan Terpstra — Preliminary functionality to support data address range and instruction address range restrictions.
* 2006-02-28 Dan Terpstra — Formatting changes.
* 2006-02-28 Dan Terpstra — Minor bug fix in PAPI_set_opt for DATA_ADDRESS case.
* 2006-02-28 Dan Terpstra — Minor format correction.
* 2006-02-25 Haihang You — fix for rr.
* 2006-02-24 Haihang You — notice the difference of pfm2 and pfm3. we only have RR stuff for pfm20.
* 2006-02-24 Dan Terpstra — Modified address_option structure to bind addresses to a specific eventset and pass the thread context to the substrate.
* 2006-02-24 Haihang You — first cut of rrange and drange support. add start and stop in the context structure.
* 2006-02-24 Dan Terpstra — Added support to PAPI_get_opt and below for data and address range restrictions. This will currently only be available on Itanium, but may appear elsewhere later. The code compiles and links and doesn't appear to break anything. Now a test case must be developed to see if it actually works. The dummy routines set_drange and set_irange in the linux_ia64.c substrate must also be replaced by active code as well.
* 2006-02-24 Dan Terpstra — Minor bug fix for substrate versioning.
* 2006-02-24 Dan Terpstra — Eliminate unused variable in the PFM30 branch.
* 2006-02-08 Haihang You — delete wrong cpu info update in mx
* 2006-01-20 Philip Mucci — This file always gets broken and I don't know why.
* 2006-01-20 Philip Mucci — Initial revision
* 2006-01-19 Haihang You — mx support for multiple substrate
* 2006-01-17 Dan Terpstra — Found and fixed the MX / perfctr-p3 collision. sidx must be declared static int inside substrates to avoid symbol table collisions. I never can keep those scoping rules straight... This fix must be applied to all other substrates as well.
* 2006-01-11 Dan Terpstra — Hard-coded MX_MAX_COUNTERS to 16. This value was previously 100. If it is set to greater than 18, substrate 0 fails in vperfctr_control. That shouldn't happen. There's still a problem here, but at least the standard tests now pass.
* 2006-01-09 Dan Terpstra — Replaced reference to PAPI_allocate_eventset with PAPI_create_sbstr_eventset.
* 2006-01-09 Dan Terpstra — There was a bug in PAPI_get_opt. In the course of fixing it, I normalized the naming of substrate related entry points. They're uglier now, but at least they're consistent.
* 2006-01-08 london — Added two functions: PAPI_get_substrate_opt which is just like PAPI_get_opt, but takes a substrate as an argument to determine which substrate you are talking about.
* 2006-01-06 Dan Terpstra — Fixed a naming problem when PAPI_DEBUG_MEMORY is true.
* 2006-01-06 Dan Terpstra — Added support for the myrinet mx substrate.
* 2006-01-06 Dan Terpstra — Added an optional MYRINET_MX keyword to trigger inclusion of the mx substrate. You must edit the make to turn this flag on if you want the mx substrate.
* 2006-01-06 Dan Terpstra — Major changes and code deletions to make this substrate conform to the multi-substrate model.
* 2006-01-06 Dan Terpstra — Minor changes to hide a variable and make this substrate play nice with other substrates.
* 2005-12-16 Dan Terpstra — Changes to support CATAMOUNT.
* 2005-12-16 Dan Terpstra — Added a commented out ACPI variable to trigger inclusion of the ACPI substrate. Now, this variable shoudl be commented in to include ACPI. At a later date this may be further automated by inclusion in the configure script.
* 2005-12-16 Dan Terpstra — Added conditional inclusion of ACPI substrate based on definition of ACPI variable in the high level Makefile.
* 2005-12-16 Dan Terpstra — - Fix bug where x86_64 ARCH was getting clobbered by ppc64 ARCH; - Set TOPTFLAGS to -O instead of -O0 for floating point tests; - Modified inclusion of ACPI substrate to be conditioned on definition of ACPI variable - Modified Opteron case to *not* include P4 code; - P3 and P4 include each other and generate a library that executes cross-platform on P3, P4, Athlon and Opteron
* 2005-12-16 Dan Terpstra — Modified to *not* include p4 code when compiling for Opteron. Both P3 and P4 code is included when building on either of those systems.
* 2005-12-15 Yuanlei Zhang — *** empty log message ***
* 2005-12-14 Dan Terpstra — Restructured GET_OVERFLOW_ADDRESS for PAPI 4
* 2005-12-14 Dan Terpstra — Commented back *in* a vperfctr_unlink that had been commented out. Now _papi_hwd_shutdown matches ppc and pentium4.
* 2005-12-09 Dan Terpstra — Fixed a nasty bug in overflow structure allocation. Enough memory was being allocated, but pointers were initiallized incorrectly, causing array elements to stomp on each other when multiple overflows were invoked. See, e.g. overflow_twoevents.c
* 2005-12-06 Dan Terpstra — Regularize the initialization of the hwi_search_t structure arrays. The only platform on which this actually caused a bug was Opteron, but it was a good time to clean things up everywhere.
* 2005-12-02 Dan Terpstra — Condition inclusion of expat.h on both its existence and whether or not we want it.
* 2005-12-02 Dan Terpstra — Cast a void * to avoid a warning message; rework overflow handler for perfmon 2.
* 2005-12-02 Dan Terpstra — Reconfigure these files *not* to be dependent on papi_sys_headers.h, but only on the small subset of headers they need. For some reason, this was causing grief in the definition of ffsll.
* 2005-12-02 Dan Terpstra — Fix a return value in papi_valid_free
* 2005-11-23 Dan Terpstra — Update to build on P4
* 2005-11-23 Dan Terpstra — Merge changes from PAPI 3.1.0
* 2005-11-23 Dan Terpstra — Merge changes from PAPI 3.2.1
* 2005-11-23 Dan Terpstra — Merge changes from PAPI 3.1.0
* 2005-11-23 Dan Terpstra — Merge new files from PAPI 3.1.0
* 2005-11-23 Dan Terpstra — Initial revision
* 2005-11-22 Dan Terpstra — Merge changes from PAPI 3.1.0 This is the merge I'm least certain of. It may contain functions duplicated elsewhere. The proof will be in the build.
* 2005-11-22 Dan Terpstra — Merge changes from PAPI 3.1.0
* 2005-11-22 Dan Terpstra — Merge changes from PAPI 3.1.0
* 2005-11-22 Dan Terpstra — Temporary support for linux-acpi substrate.
* 2005-11-22 Dan Terpstra — Merge changes from PAPI 3.1.0
* 2005-11-22 Dan Terpstra — Merge changes from PAPI 3.1.0
* 2005-11-22 Dan Terpstra — Merge changes from PAPI 3.1.0
* 2005-11-22 Dan Terpstra — Merge Power5 support from PAPI 3.1.0
* 2005-11-17 Dan Terpstra — Merging changes from 3.1.0 branch
* 2005-11-15 Yuanlei Zhang — updates of including the common header file "papi_sys_headers.h"
* 2005-11-15 Dan Terpstra — Modified for compatibility with PAPI 4
* 2005-11-15 Dan Terpstra — Corrections and simplifications: - replaced hwd_allocate_registers with update_control_state; - re-indexed events to 0,1 instead of 1,2 It now appears to work, but I'm still concerned that load is always 0.
* 2005-11-15 Dan Terpstra — Minor format correction.
* 2005-11-14 Dan Terpstra — Mods for multiple substrates. Still failing on ACPI add_native_event.
* 2005-11-11 Dan Terpstra — Changed execution flag from 'ACPI' to 'HAS_ACPI' for consistency with substrate.
* 2005-11-11 Dan Terpstra — Changes to compile ACPI into Itanium.
* 2005-11-10 Dan Terpstra — Revert prototype of _papi_hwd_get_system_info(). It needs to be non-static for p3, p4, itanium.
* 2005-11-10 Dan Terpstra — Removed _papi_hwd_get_system_info(). It now lives *only* in linux.c
* 2005-11-10 Dan Terpstra — Added a reference to papi_protos.h
* 2005-11-10 Dan Terpstra — General cleanup: - Modified event tables for 4 events rather than 8; - added VECTOR_STATIC where needed; - added another function to the vector table; - removed some dead code.
* 2005-11-10 Dan Terpstra — Defined MAX_COUNTER_TERMS in terms of MAX_COUNTERS and redefined the itanium_preset_search struct in terms of MAX_COUNTER_TERMS
* 2005-11-10 Dan Terpstra — Added VECTOR_STATIC to a few more routines.
* 2005-11-10 Dan Terpstra — Suppress warning messages for unimplemented vector table functions.
* 2005-11-08 Dan Terpstra — Merged changes from 3.1.0 for Catamount and POWER5/AIX.
* 2005-11-03 Dan Terpstra — Tweaks to get the gcc branch working. Removed some dead code.
* 2005-11-03 Dan Terpstra — Tweaks per Maynard's comments; POWER5 isn't in the HEAD branch yet.
* 2005-11-03 Dan Terpstra — Added Maynard's description of Linux/POWER installation and updated description of AIX support.
* 2005-11-01 Dan Terpstra — Modified run script for Catamount.
* 2005-10-31 Dan Terpstra — Redefinition of PAPI_ITIMER for Catamount
* 2005-10-27 Dan Terpstra — Replace references to substrate_info[0] with references to substrate_info[sidx]. Shouldn't matter for cpu counters, but it's more portable and consistent.
* 2005-10-26 Dan Terpstra — Minor tweaks in debug messages.
* 2005-10-26 london — Fix for overflow on p4
* 2005-10-20 Dan Terpstra — Plug a leak in the #ifdef logic for POWER3 and linux.
* 2005-10-19 Dan Terpstra — Test file for use by configure to determine if the OS is catamount.
* 2005-10-19 Dan Terpstra — Eliminate datatype warning in PAPI_set_event_info
* 2005-10-19 Dan Terpstra — Fix mis-assignment in vector table that caused real time counts to fail; modified Dl_info structure reference per Sameer's suggestion.
* 2005-10-19 Dan Terpstra — Force NOTLS = -DNO_TLS for Catamount, since threads aren't supported.
* 2005-10-11 london — Print help message if tests are not quiet and not enough args were supplied
* 2005-10-11 london — Initial revision
* 2005-10-06 Philip Mucci — This file got edited manually somewhere along the line, reimporting
* 2005-10-06 Philip Mucci — Initial revision
* 2005-09-26 Dan Terpstra — Added OS=irix line to fix 64-bit build.
* 2005-09-23 Dan Terpstra — Modifications to papi_memory.c to support 8-byte data alignment on irix. Also did significant code rearrangement, cleanup, and standardization of names, mainly to get it to where I could understand it. No offense, Kevin. My problem, not yours.
* 2005-09-23 Philip Mucci — Forward changes from 3.0.8.1
* 2005-09-22 Philip Mucci — Initial revision
* 2005-09-20 london — Fixes so the locking mechanisms work in X1 and byte_profile compiles
* 2005-09-19 london — Setting items before all declarations is not c90 compliant.  Breaks on the X1.
* 2005-09-19 london — Working port to multiple substrates, need to fix the hwd_lock/unlock functions before this substrate is finished
* 2005-09-18 london — Start of xl port to multiple substrates, checking in for the fix for overflow on P4/p3's
* 2005-09-18 london — Irix changes to support multiple substrates
* 2005-09-17 london — Ooops forgot to submit these files
* 2005-09-15 london — Solaris port to the multiple substrates.  Still needs to be extensively tested.  The solaris machine I had access to, was taking 1 minute for a pwd, so NFS or something was messed up.   Also, AIX thread test will fail now, because I had to remove the AIX_THREAD export symbol, because it prevented run_tests.sh from running at all. Finally, there was a small cleanup in perfctr-p3.c which if xml was turned on, would cause a failed compile
* 2005-09-02 Dan Terpstra — Rearranged the elements in the NativeInfo_t structure for better alignment on 64-bit systems.
* 2005-09-02 Dan Terpstra — Fixed a data structure cast in initialize_NativeInfoArray so the correct size of the structure could be computed.
* 2005-09-01 Dan Terpstra — Hide native_event table references behind a static to avoid collisions.
* 2005-09-01 Dan Terpstra — Make native_event table references substrate specific.
* 2005-09-01 Dan Terpstra — More syntax tweaks to build for Pentium 4
* 2005-08-30 Dan Terpstra — Merging 3.1.0 changes
* 2005-08-29 Dan Terpstra — Fix by Maynard to prevent infinite loops.
* 2005-08-26 Dan Terpstra — Commiting changes in perfctr import
* 2005-08-26 Dan Terpstra — Initial revision
* 2005-08-25 Dan Terpstra — Removed a couple unused variables
* 2005-08-25 Dan Terpstra — Moved some function definitions from here to perfctr-p3.c where they were actually called.
* 2005-08-25 Dan Terpstra — Added papi_protos.h
* 2005-08-25 Dan Terpstra — Minor cleanups
* 2005-08-25 Dan Terpstra — Moved and commented papi_sizeof
* 2005-08-25 Dan Terpstra — Removed an unused variable
* 2005-08-25 Dan Terpstra — Prototyped papi_sizeof; Converted a bunch of routines to VECTOR_STATIC
* 2005-08-25 Dan Terpstra — Various initialization rearrangements.
* 2005-08-25 Dan Terpstra — Comment out debugging printf
* 2005-08-25 Dan Terpstra — Added -Wno-unused-function to CFLAGS; Modified syntax on test for misc sources; still doesn't work right.
* 2005-08-25 Dan Terpstra — Added papi_protos.h
* 2005-08-25 Dan Terpstra — Commented out an unused variable. This utility needs to be rolled back to previous functionality.
* 2005-08-24 Dan Terpstra — Add two new files needed for multi-substrate support.
* 2005-08-24 Dan Terpstra — Always include libperfctr.h
* 2005-08-24 Dan Terpstra — Correct typo on papi_table.o rule.
* 2005-08-19 london — Multiple substrate suppot.  This is pre-alpha release at the moment.  Only p4, itanium II, p3, opteron platforms are supported.  Everything else will return bogus numbers or segfault.  I will be porting the rest of the substrates over the next couple of weeks.  Then we will get rid of the warnings and polish everything up.  Till then, I would strongly urge you to use the papi-3-1 branch.
* 2005-08-19 Dan Terpstra — Bumped version number to PAPI 3.1.0.0. This will trigger a recompile, because the first 2 digits are checked in PAPI_library_init It reflects the addition of PPC/Linux support as well as a number of bug fixes.
* 2005-08-19 Dan Terpstra — Updated mechanism for getting perftr info in the init_substrate stuff. Allows compatibility with perfctr 2.6.15 without breaking backward compatibility. Tested against opteron, PIII, P4.
* 2005-08-19 Haihang You — add check for pm_initialize in configure and Bernd Kallies's modification on power4 for using pm_initialize.
* 2005-08-17 Haihang You — skip acpi test when it is not supported.
* 2005-08-17 Haihang You — minor changes. now it works on power4.
* 2005-08-16 Dan Terpstra — Initial revision
* 2005-08-16 Dan Terpstra — Bracketted sig handler changes with #ifdef PPC64 to isolate them from other platforms. Per Phil's suggestion.
* 2005-08-16 Dan Terpstra — Updates for Linux/PPC code.
* 2005-08-16 Dan Terpstra — Modified add_two_events() to do_the_right_thing (TM). Submitted by Maynard Johnson. Thank you Maynard.
* 2005-08-16 Dan Terpstra — signal handling fixes submitted by Maynard Johnson
* 2005-08-16 Dan Terpstra — New event mappings to support POWER4, POWER5, and PowerPC970 on linux with perfctr. These were added and then removed due to copyright issues. Now they're here to stay (we hope!)
* 2005-08-16 Dan Terpstra — Modified source files to support POWER4, POWER5, and PowerPC970 on linux with perfctr.
* 2005-08-13 Joseph Thomas — A first crack at the central header file.
* 2005-08-10 Dan Terpstra — Changes to eliminate the correction of accumulated flops on data conversion. This was always squirrelly to begin with, and is apparently version dependent. Code for Matlab 7.0.4 running on Pentium M is cleaner without it.
* 2005-08-10 Haihang You — add support of mem_info
* 2005-08-09 Joseph Thomas — Updates of the configure script, and the *.in files.  I want to make sure nothing breaks before I start editing #include lines.
* 2005-08-03 Dan Terpstra — These Visual C project files were never stored commited to cvs.
* 2005-08-03 Dan Terpstra — Updated to support Pentium M SSE instructions.
* 2005-08-03 Haihang You — minor fixes. use correct PAPI_VER_CURRENT.
* 2005-07-22 Philip Mucci — Removed all this stuff that should have never been here.
* 2005-07-06 Dan Terpstra — Another test of email notification.
* 2005-07-05 Philip Mucci — test log message
* 2005-07-01 Dan Terpstra — Another test of email notification.
* 2005-07-01 london — Testing pserver mail bounce
* 2005-06-30 Dan Terpstra — Test checkin using earth instead of icl.
* 2005-06-30 Haihang You — myrinet mx support and acpi modification
* 2005-06-29 Dan Terpstra — Removed these files. We don't yet have permission from IBM legal to distribute them.
* 2005-06-29 Philip Mucci — Test pserver commit
* 2005-06-29 london — Testing mail reflector log messages without pserver
* 2005-06-29 london — Testing to see if log information is correctly mailed to lists when going through pserver
* 2005-06-28 london — Oops forgot to check this in.
* 2005-06-28 Dan Terpstra — Backed out a change in get_cycles.
* 2005-06-28 Dan Terpstra — Modified c test files to support POWER4, POWER5, and PowerPC970 on linux with perfctr.
* 2005-06-28 Dan Terpstra — New and modified source files to support POWER4, POWER5, and PowerPC970 on linux with perfctr.
* 2005-06-28 Dan Terpstra — New event mappings to support POWER4, POWER5, and PowerPC970 on linux with perfctr.
* 2005-06-28 Dan Terpstra — Event and group info for PowerPC970 Caution: these versions contain copyright disclaimers by IBM.
* 2005-06-28 Dan Terpstra — Event and group info for POWER5. Caution: these versions contain copyright disclaimers by IBM.
* 2005-06-28 Dan Terpstra — Event and group info for POWER4. Caution: these versions contain copyright disclaimers by IBM.
* 2005-06-28 Dan Terpstra — New MakeFiles and changes in configure and rules to support POWER4, POWER5, and PowerPC970 on linux with perfctr.
* 2005-06-28 Haihang You — mod to get rid of warnings on AIX
* 2005-06-24 Haihang You — acpi substrate checkin
* 2005-06-22 Dan Terpstra — Changes that never got committed for the encode stuff.
* 2005-06-17 london — Stop using // as comments in the PAPI Library!  Not all compilers support the C++ style comments (Like AIX)
* 2005-06-13 london — Remove papi_cleanup_memory whenever PAPI_NO_MEMORY_MANAGEMENT is defined.
* 2005-06-13 london — Typo fix
* 2005-06-13 london — Fixed a typo, realloc should have been calloc
* 2005-06-02 Dan Terpstra — Makefile for Catamount.
* 2005-06-02 Dan Terpstra — Changes to support Catamount/XT3. Added Catamount compiler section, suppressed build of libpapi.so, forced build of perfctr with $(CC)
* 2005-06-02 Dan Terpstra — Code changes to support Catamount/XT3.
* 2005-05-26 Dan Terpstra — More modifications to make genpapifdef independent of libpapi. Moved initialization of some data structures to a new header file. This makes it possible to include them in both papi and genpapifdef without creating compile conflicts. I forgot this one yesterday.
* 2005-05-25 Dan Terpstra — Modify such that clobber doesn't remove the fortran header files. That way, they only get rebuilt if their dependencies are triggered. This means they will be built on a cvs checkout, or on a papi.h change, but can be distributed prebuilt with our tarballs. This will simplify distributions on platforms such as RedStorm.
* 2005-05-25 Dan Terpstra — Remove dependence of genpapifdef on libpapi and explicitly specify the headers on which it depends Make the 3 fpapi.h files dependent only on papi.h instead of genpapifdef. That way if current copies already exist, they don't need to be rebuilt every time the library is.
* 2005-05-25 Dan Terpstra — Modifications to make genpapifdef independent of libpapi. This should make it easier to implement on platforms like RedStorm, where the compute node is different from the compile node.
* 2005-05-19 Dan Terpstra — Missed one.
* 2005-05-19 Dan Terpstra — Updated to reflect addition of a new utility; and addition of 2 new APIs
* 2005-05-19 Dan Terpstra — Updated to reflect name changes in utilities; addition of a new utility; and addition of 2 new APIs
* 2005-05-19 Dan Terpstra — Changed the names of the papi utility functions to be prepended with papi_ This triggered a change in the names of the man pages, too.
* 2005-05-19 Dan Terpstra — Modifications to make these files more TESTS_QUIET friendly and provide better error handling on argument parsing; incorporate these files into the make.
* 2005-05-19 Dan Terpstra — Modifications to name all utilities as papi_xxxx. This way they could be moved to a common directory and not risk name collisions with other files.
* 2005-05-19 Dan Terpstra — Tweaks to get rid of warning messages.
* 2005-05-18 Dan Terpstra — Utility that uses PAPI_get_event_info() to create csv formatted output suitable for use by PAPI_encode_events(). Such output can be viewed and edited in a csv-compatible spreadsheet, such as Excel, an can be used as input to the encode and encode2 test programs.
* 2005-05-18 Dan Terpstra — Two new tests to exercise the new APIs introduced to PAPI. encode.c exercises PAPI_set_event_info encode2.c exercises PAPI_encode_events Both require properly formatted csv files to function. See utils/decode to create such files.
* 2005-05-18 Dan Terpstra — Added two new entry points to the API: - PAPI_set_event_info() is symmetric with PAPI_get_event_info().   It allows a user to add or modify the definition of a preset event for a given platform.   The scope of the modification is only for the duration of that invokation of PAPI. - PAPI_encode_events() reads a csv (comma separated values) file containing   event definition information and loads it into the preset table.   In conjunction with a decode utility, this provides the user (or toolmaker) with   the ability to support custom event definitions or overrides on specific platforms.
* 2005-05-18 Dan Terpstra — Migrated optional XML code from perfctr-p3 to papi_preset. Also restored data structures to pointers-to-strings rather than pre-allocated fixed length string space. Reworked arrays to use Kevin's new memory management stuff and added support routines to properly allocate and clean things up. Some of this was done to better support xml, but it was just good code cleanup anyway. The optional XML stuff still works only on pentium III. We may or may not ever go further with it.
* 2005-05-18 Dan Terpstra — Tiny tweak in a debug printf for better viewing of strings in native name_to_code
* 2005-05-18 Dan Terpstra — Some cleanup odds and ends: - fixed definition of PAPI_NATIVE_AND_MASK from 0x3F... to 0xBF... - added terminators to the enum list and #define event list No change in current functionality.
* 2005-05-10 london — Setup p3&p4 vector tables before the presets
* 2005-05-10 london — Remove an inline for solaris until I can figure out why solaris thinks it doesn't have the symbol.
* 2005-05-10 london — Fixed a typo
* 2005-05-01 london — New papi_strdup call
* 2005-04-29 london — Addition of papi memory calls.  This allows papi to track memory and free up all memory in a shutdown call.  All calls should now be papi_free, papi_malloc, papi_realloc and papi_calloc
* 2005-04-28 Dan Terpstra — Modifications to allow prototype checking as static in the substrates and as extern in the independent layer.
* 2005-04-28 Philip Mucci — All strings now use PAPI definitions that match their declarations in papi.h, no more PATH_MAX
* 2005-04-28 Philip Mucci — Propagated new update shlib function from 3.0.8.1 BSS is now deprecated!
* 2005-04-28 Dan Terpstra — Convert the PAPI license to BSD wording.
* 2005-04-26 Philip Mucci — More fixes from Stefane Eranian
* 2005-04-26 Philip Mucci — Prefer PAPI_FP_OPS over PAPI_FP_INS, this helps EM64T platforms and gcc 3.4 pass cleanup
* 2005-04-25 Dan Terpstra — Fixed a few typos.
* 2005-04-25 Philip Mucci — The fix for fopen which someone hacked in didn't even have the right variable name. Fixed. and PAPI_OK is retval even if update_shlib fails.
* 2005-04-25 Philip Mucci — Removed not 1, but 2, calls to exit in this code.
* 2005-04-20 Dan Terpstra — Tweaks to get rid of warning messages. I don't like warning messages.
* 2005-04-19 Joseph Thomas — This is the XML file containing preset events and their mappings given to us a year or so ago.  The substrate should read this file when building preset tables if it supports XML.
* 2005-04-19 Joseph Thomas — Added XML support for the Pentium 3.
* 2005-04-19 Joseph Thomas — Added support for XML on the penitum III.
* 2005-04-19 Dan Terpstra — Add 4th digit to the version number stuff; set the current version to 3.0.8.2.
* 2005-04-18 Philip Mucci — Two patches from Stefane covering multiplexing and print_info
* 2005-04-07 london — Removed papi_redefine.h which should ONLY be included in the papi.c, papi_internal.c and other Non-substrate files (and not papi_vector.c). Fixed the problem in papi_vector.c that was causing things not to compile as well.
* 2005-04-07 Haihang You — Pentium M should not be considered as p4. remove the case from check_p4(int cputype)
* 2005-04-06 Haihang You — add #include "papi_vector_redefine.h", this will fix the compilation error.
* 2005-04-05 london — Complete rewrite of any-null, now the code is completely seperated from perfctr and will work on any platform.  If you link with this then your program will compile and run and all PAPI routines will return succesfully.  However, results will of course be incorrect.
* 2005-04-05 london — Fix for P3-M
* 2005-03-31 london — Better error reporting for dlopen
* 2005-03-31 london — Check for NULL in fopen
* 2005-03-24 Joseph Thomas — Checked in Jack Perdue's suggestions.  They work on version 3.0.8.1.
* 2005-03-18 london — PAPI vectorized functions, more changes to come and this is just a first rough cut and doesn't include version info and other functionality that will be added.
* 2005-03-16 Dan Terpstra — Initial round of changes to support Cray RedStorm/Catamount. Folded forward from Sandia's implementation in PAPI 2.3.4.
* 2005-03-15 london — Update the man page to list PAPI_LIB_VERSION and PAPI_SUBSTRATE_SUPPORT
* 2005-03-15 london — PAPI shouldn't fail building just because fortran tests failed. This makes PAPI ignore non library failures.
* 2005-03-15 london — clobber didn't have clean as a dependency and so *.o were left around
* 2005-03-09 london — Fixes for copying the man files over
* 2005-03-08 Philip Mucci — Added native_clobber to all targets. This is now called by make clobber. It's a NOOP on platforms with builtin support.
* 2005-03-04 Dan Terpstra — Final tweaks.
* 2005-03-04 Dan Terpstra — Change log for PAPI 3.0.8 release.
* 2005-03-03 Philip Mucci — I'm a FAQer. Yes indeed. New import of entries reflecting AIX need for AIXTHREAD_SCOPE and other mods made today.
* 2005-03-03 Philip Mucci — Added AIXTHREAD_SCOPE=S
* 2005-03-03 Philip Mucci — Removed AIX entry! Hooray! It works. I wasn't setting AIXTHREAD_SCOPE=S.
* 2005-03-03 Philip Mucci — Removed redundant delete_program_mythread
* 2005-03-03 Dan Terpstra — Modified the Athlon event table based on input from Anoop Iyer of AMD; Removed the need for the previously implemented DERIVED_SUB underflow fix -- at least for Athlon.
* 2005-03-03 Philip Mucci — Corrected wrong error message
* 2005-03-03 Dan Terpstra — Added FARGS to Rules and __athlon__ to Makefile so that native.F can PASS instead of SKIP. This test really needs a rewrite, but this'll work for now.
* 2005-03-03 Haihang You — change #define CACHE_FLUSH_BUFFER_SIZE_INTS 32*1024*1024 to #define CACHE_FLUSH_BUFFER_SIZE_INTS 16*1024*1024 this will solve byte_profile limit memory problem on power.
* 2005-03-03 Philip Mucci — Added notes about the IA64 bugs on Redhat kernels (interrupt on overflows stop!) and about the as yet, somewhat unverified bug on Power 4/AIX .50 BOS and .40 PM kernel where PMAPI seems to lose thread context information when we have lots of threads. It happens in the kufrin test case. it doesn't happen when we have 4 threads, enable PAPI debugging or run the case under strace. But with 8 threads, we're hosed. Can NCSA try this on their power 4?
* 2005-03-03 Philip Mucci — Changed to less restrictive redistribution clause which brings IBM, Cray, Sun, Pacific Sierra, Etnus, myself, Nils Smeds and others in compliance.
* 2005-03-03 Dan Terpstra — Updated for PAPI 3.0.8
* 2005-03-02 Haihang You — use higher threshold defined by mhz for linux with software overflow.
* 2005-03-02 Haihang You — use higher threshold defined by mhz for linux with software overflow.
* 2005-03-02 Dan Terpstra — Updated for PAPI 3.0.8
* 2005-03-02 Dan Terpstra — Added six new undocumented native events to Opteron event table per Phil's request. These measure NUMA HyperTransport memory and IO transfers. Run utils/native_avail on Opteron and look at the last six entries.
* 2005-03-02 Dan Terpstra — Tweaked on Kevin's fix for DERIVED_SUB errors on Athlon and PIII. Lowered correction threshold to -3. Added compile switch to Athlon and PIII make files.
* 2005-03-02 Haihang You — As Phil mentioned, On all Linux the timer is maxed at 1/100 of a second, to prevent owerflow threshold is too small, use mythreshold = hw_info->mhz*10000*2 on linux system.
* 2005-03-02 Philip Mucci — When PAPI is run as SUID, often links in /proc are inaccessible. This was reported by the guys at CMU. Thanks guys!
* 2005-03-02 Dan Terpstra — Added html versions of man pages for each of the utility functions.
* 2005-03-02 Dan Terpstra — Modified base PAPI man page to point to the utility functions.
* 2005-03-02 Dan Terpstra — Added (minimal) man pages for each of the utility functions.
* 2005-03-01 Philip Mucci — Added 32 bit library support for 64 bit platforms. This has been tested on an Opteron. All tests pass. Configure script works also.
* 2005-03-01 Philip Mucci — Added message about using configure and added 32 bit makefiles to list.
* 2005-03-01 Philip Mucci — Used and && instead of cd man. This would cause an infinite loop in the build if you didn't have the man directory.
* 2005-03-01 Philip Mucci — Added LD_FLAGS necessary for compiling a 32bit version on a 64 bit system
* 2005-03-01 london — In some cases a DERIVED_SUB is negative, this checks for this case.
* 2005-03-01 london — A few fixes to prevent buffer overruns.  This still doesn't fix the occasional error we are getting though.
* 2005-03-01 Philip Mucci — Restructured TLS test for Debian/SuSE 9/IA64 compiler bug
* 2005-03-01 Dan Terpstra — Added PAPI_L2_TCH to Opteron per Brian Wylie's suggestion.
* 2005-02-28 Dan Terpstra — Mods to eliminate warning messages.
* 2005-02-28 london — Added man1 for install
* 2005-02-28 Philip Mucci — Added pm_error calls if not quiet. Fix until hwd_error is implemented fully.
* 2005-02-28 Philip Mucci — Made using signal volatile
* 2005-02-28 Philip Mucci — Removed definition of using signal
* 2005-02-28 Philip Mucci — Removed error string that was wrong when we had an unknown error code
* 2005-02-28 Dan Terpstra — Cleaned up Opteron events per Brian Wylie's suggestions:
* 2005-02-28 Dan Terpstra — Added a SUBDBG message on the si structure for overflows.
* 2005-02-28 london — Fix for segfaults on software overflow.  Also, may have found an OS bug that you can't count events after setting hardware overflow, as the counters get reset once the threshold is set, even if overflow has been turned off.  Creating a sample that demonstrates this and sending to Cray.
* 2005-02-28 Philip Mucci — Added clobber phase to utils
* 2005-02-28 Philip Mucci — Added clobber and proper TARGET specification
* 2005-02-24 Dan Terpstra — Modified fwrappers to support Cray X1 string length at end convention.
* 2005-02-24 london — Fix to check for compound derived events which CAN be used to overflow on in hardware (Currently only p4 has them).  This allows P4 to use FP_INS instead of TOT_INS
* 2005-02-24 london — Changes to check for derived events, and to get rid of the need for strcmp on os names.
* 2005-02-23 Philip Mucci — Removed some papi_return macros. papi_return only belongs in papi.c
* 2005-02-22 london — Fix for software overflow on irix
* 2005-02-22 london — Fix for software overflowing using PFM 3.0
* 2005-02-22 Philip Mucci — Recommit of Makefile and event_chooser written by Haihang and Dan. This is 1.1
* 2005-02-22 Philip Mucci — Last fix for new dir
* 2005-02-22 Philip Mucci — New rules for libpfm-2.x and 3.x directories.
* 2005-02-22 Philip Mucci — Updates from latest libpfm 3.1. We should adopt a 3.x and 2.x naming scheme.
* 2005-02-22 Dan Terpstra — Changes to support utils directory
* 2005-02-22 Dan Terpstra — Added native events for Cray X1. Test no longer FAILS on X1. Now it SKIPs. Something's still not right...
* 2005-02-22 Dan Terpstra — Moved cost.c, clockres.c, and mem_info.c from ctests to the newly created utils directory. Makefile contains appropriate mods to remove these files.
* 2005-02-21 Dan Terpstra — Moved avail.c, command_line.c, and native_avail.c from ctests to the newly created utils directory. This is the first step in creating a useful set of utilities apart from our usual tests. Makefiles will also need to be modified.
* 2005-02-21 Dan Terpstra — Modified ftest_fail to match test_fail. Now skips on PAPI_EPERM so that second.F will skip the same as second.c BTW, second.F now bears little resemblance to second.c... Someday these should be reconciled.
* 2005-02-21 Philip Mucci — Removed leftover abort and moved to test fail
* 2005-02-21 Philip Mucci — Added MMTIMER support on Altix for good global timing.
* 2005-02-21 london — Fix for not compiling using libpfm 3.0
* 2005-02-21 Philip Mucci — More fixes for EM64T confgure.
* 2005-02-21 Philip Mucci — Fixed build for ALTIX. This was building with PFM in our directory, but there should be always building with the pfm in /usr. Also allowed configure to detect the altix for when we add the MM timer in the future.
* 2005-02-19 Haihang You — fix the failures on enterprise. in function _papi_hwd_update_shlib_info(), flags are r w x instead of being read write and exec on enterprise.
* 2005-02-18 london — Perfctr 2.6.13
* 2005-02-18 london — Initial revision
* 2005-02-18 london — Fix for _papi_hwi_using_signal, we bumped it in _papi_hwi_start_signal and then checked if _papi_hwi_using_signal > 0 and then if it was didn't install the timer, but since _papi_hwi_start_signal called before _papi_hwi_start_timer systems with ANY_THREAD_GETS_SIGNAL won't ever have a timer setup.  This basically stopped any overflowing on systems like Power.   Also, there are all kinds of race conditions as to if the timer gets installed, I know _papi_hwi_using_signal is to make us feel all warm and fuzzy, but I am not sure it fixes the problems it is meant to address.
* 2005-02-18 london — Added linux check for TLS
* 2005-02-18 london — Changed the verification to check overflows and removed the printing of the event when hardware overflowing is enabled as reading an event that is on hardware overflow doesn't mean anything. We should probably change the event from PAPI_FP_INS/PAPI_FP_OPS to PAPI_TOT_INS as this test will skip if PAPI_FP_INS or PAPI_FP_OPS is derived as it is on some platforms.
* 2005-02-18 london — Fixes for forced overflow, first we had no default for a sigaction so in some cases a sigaction wasn't getting setup, and ia64 didn't have dispatch_timer routine implemented at all. Added better debugging messages.
* 2005-02-18 Dan Terpstra — Bumpe version number to 3.0.8
* 2005-02-16 Dan Terpstra — Fixed event assignment. PAPI_FP_OPS was being assigned when it should have been PAPI_FP_INS, and vice versa.
* 2005-02-16 Dan Terpstra — Fixed indexing problem in output. A 'j' should have been an 'i'.
* 2005-02-16 Dan Terpstra — Deprecated PAPI_TOT_IIS for X1. Previous definition was giving random results from 0 to very large.
* 2005-02-15 Dan Terpstra — Add 20 cache and branch events contributed by Brian Wylie. This nearly doubles the number of events available on POWER4. Thanks, Brian!
* 2005-02-14 Haihang You — add configure switch --with-tls=<yes|no>. By default, it is 'yes' and running the checking code. When it is 'no', -DNO_TLS passed to gcc.
* 2005-02-09 Dan Terpstra — Clean up of Cray X1 exception processing. Thanks to Kevin for pointing out the __crayx1 compiler flag.
* 2005-02-09 Philip Mucci — Modifications to the Power 4 PAPI Presets...Surely these still aren't correct. Upon checkin on preset maps from IBM on the Linxu/PPC64, we will calibrate the two.
* 2005-02-09 Philip Mucci — If you set PAPI_DEBUG to ALL or THREADS and compile with -DDEBUG, now the internal eventset lookup routine will return NULL if you lookup another threads eventset. This should help debug possible problems on architectures where signals may be delivered to any threads. Under normal operation, this is not turned on for performance reasons.
* 2005-02-09 Philip Mucci — Removed timer_ms definition from hwd_control_state. It doesn't need to be there.
* 2005-02-09 Philip Mucci — This seems to be working for me again.
* 2005-02-09 Philip Mucci — Anynull build fixes
* 2005-02-09 Philip Mucci — The last fix for Brian Wylie's problem. I done fixed it good dis time.
* 2005-02-09 Philip Mucci — Added pm_data_t to hwd_control_state_t. This contains per thread space for the counters!
* 2005-02-09 Philip Mucci — kufrin: changed type to long long, as they should be. overflow_force_software: removed C99 like declaration to the front.
* 2005-02-07 Dan Terpstra — Modifications to work around Cray Fortran bug with maximum negative integer values. This fix requires editing the file to #define a tag to direct preprocessing. Not an elegant solution. Does anyone know a predefined flag to ID the X1?
* 2005-02-07 Philip Mucci — Minor formatting changes for clarity
* 2005-02-06 Haihang You — modified with suggestions from Maynard.
* 2005-02-04 london — Fix for install_tests
* 2005-01-28 Philip Mucci — Fixed the bug that showed up on the Nocona. A string was being used as HUGE but declared as MAX. Craig T of HPTI reported coredumps on Nocona that caught this one.
* 2005-01-27 Philip Mucci — Quick fix from Maynard J of IBM.
* 2005-01-26 Philip Mucci — Bug fixes from Maynard Johnson of IBM maynardj@us.ibm.com
* 2005-01-20 Philip Mucci — Removed -R argument to shared link, which was putting the wrong path in to the run-time loader. Removed the -h flag to the shared link, which was (in the 64 bit case) setting the wrong name of the library. Neither is required.
* 2005-01-20 Philip Mucci — Ooops. Missed a little bug on line 961. Thanks to Shirley for catching this.
* 2005-01-13 Dan Terpstra — Implemented PAPI_L1_ICA and PAPI_L1_ICM per suggestions from Brinkley Sprunt. Don't know how to validate whether the counts are reasonable. That's left as an exercise for the user.
* 2005-01-13 Dan Terpstra — Added some comment spacers to clarify event numbering.
* 2005-01-10 Dan Terpstra — Modifications to native event tables for Pentium II, III, Athlon and Opteron to dynamically generate all combinations of events that support MESI (Intel) or MOESI (AMD) bits. Similar to the way that Pentium 4 supports groups and modifiers, but MUCH simpler. Tested on Pentium III and Opteron. Not tested on Pentium II and Athlon. This is in response to Luiz DeRose's request for more flexibility in specifying native events on Opteron. You're welcome, Luiz.
* 2005-01-10 Dan Terpstra — Changes to address the thread-unsafe behavior of _papi_hwd_code_to_{name,descr}(). Rather than change the calling sequence of these routines in every substrate, I changed the way the routines are called from extras.c, wrapping them in PAPI_lock/unlock pairs. Pentium 4 was the only substrate that posed a thread risk. That hole has now been plugged. Also, other substrates can now engage in the same shenanigans if desired. NOTE: This required changes in the calling sequences of two _hwi_ routines. These changes are not exposed to the user.
* 2005-01-07 Philip Mucci — Fixes for SGI Propack 3 on Altix...
* 2005-01-06 london — Import fixes
* 2005-01-06 london — Initial revision
* 2004-12-10 Dan Terpstra — Windows doesn't support %lld formatting. Tweak on output format so Windows reports stuff correctly.
* 2004-12-10 Dan Terpstra — Minor change in scope of TESTS_QUIET variable so that tests would run quiet on Windows. Don't know how/why this ever worked before...
* 2004-12-08 Dan Terpstra — Fixed the remaining Windows format string problems on output.
* 2004-12-08 Dan Terpstra — Fixed format string problems on output. There's still some output issues I need to look at...
* 2004-12-08 Dan Terpstra — Windows was complaining about implicit casts. long_long -> int and float -> double. These changes make them explicit.
* 2004-12-08 Dan Terpstra — Minor syntax changes for Windows compatibility. Removed Windows version of _papi_hwd_set_overflow() from perfctr-p3.c, because it was essentially identical to linux version. Windows version is now up-to-date with PAPI 3.0.7.
* 2004-12-08 Dan Terpstra — Rearranged for signal and timer handling on Windows
* 2004-12-03 Philip Mucci — Added little ditty about Perfctr 2.6.11 and the fact that you SHOULD NEVER USE PERFCTR 2.4.x UNLESS YOU HAVE TO.
* 2004-12-02 Dan Terpstra — Add most recent ChangeLog items.
* 2004-12-01 Dan Terpstra — Change the PAPI version number to 3.0.7
* 2004-12-01 Philip Mucci — Resolve conflicts from import
* 2004-12-01 Philip Mucci — Import of PerfCtr 2.6.11
* 2004-12-01 Philip Mucci — Initial revision
* 2004-12-01 Dan Terpstra — Updated for PAPI 3.0.7. Actually only changes PAPI-get_hardware_info.
* 2004-12-01 Dan Terpstra — Updated to match Phil's recent change.
* 2004-11-30 Dan Terpstra — Created for PAPI 3.0.7
* 2004-11-30 Dan Terpstra — Updated for PAPI 3.0.7
* 2004-11-30 Dan Terpstra — Changed name of clear_control_state to clear_cs_events to more accurately reflect the functionality. Removed unneeded call to init_control_state from update_control_state. Modified p3 clear routine to preserve state of ENABLE bit in event register.
* 2004-11-30 Philip Mucci — Marked ADD_PIPE,MULT_PIPE and ADD_MULT_PIPE for Opteron as Speculative
* 2004-11-30 Philip Mucci — Updated note about Linux/Alpha being stale.
* 2004-11-30 Dan Terpstra — Modified to match p3 substrate re: update_control_state.
* 2004-11-30 Dan Terpstra — Removed unneccessary setting of CPL(1) in ESCR for definition of all native events. This bit set the USR domain bit for every native event, which was then OR'd into the event set control state whether you wanted it or not. This fix takes care of Rick Kufrin's PAPI_set_domain problem from last week.
* 2004-11-30 Dan Terpstra — More informative descriptive messages of what's happening; rearrangement of outputs to match descriptions and validation tests; rearrangements of variable declarations so it would compile. Muchly improved, thanks to Phil's recent revisions. Next time it would be even better if it compiled :)
* 2004-11-29 Philip Mucci — Removed misleading comment.
* 2004-11-29 Philip Mucci — Fix for new definitions and more rigorous testing... Output on Opteron....
* 2004-11-29 Philip Mucci — Minor fixes for the Opteron and Pentium cache information. Pentium series cache attributes may be incorrect.
* 2004-11-29 Philip Mucci — Changed the definitions of WT and WB caches so they are exclusive. By default, all caches now have the LRU and Write Through attribute. Please check your processor! linux-memory.c and memory.c need to be updated to set and test for the correct bits. Everyone grab a processor...I'll take the AMD's...
* 2004-11-25 Philip Mucci — Brian's update
* 2004-11-25 Philip Mucci — Much improved test case that demonstrates domain setting bug on Linux/x86 and x86_64 systems.
* 2004-11-25 Philip Mucci — Added val_omp.c test to the makefile
* 2004-11-25 Philip Mucci — I sure thought I fixed this. My bad. Added correct PAPI_L1_TCM and PAPI_L2_TCM events to Opteron preset map.
* 2004-11-24 Haihang You — remove defines of PAPI_FLOPS PAPI_IPS
* 2004-11-23 Philip Mucci — Test case that caught the thread bug on AIX from Brian Wylie
* 2004-11-23 Dan Terpstra — Fixed bug in p4 where _papi_hwd_init_control_state wasn't being called inside _papi_update_control_state. This should make control_states properly inherit default domains as set by PAPI_set_opt, but will still cause local (non-default) domains set by PAPI_set_opt(PAPI_DOMAIN) to get trashed.
* 2004-11-23 Philip Mucci — This is a fix for Brian Wylie's bug in AIX/Power.
* 2004-11-18 Haihang You — modify EventSet class definition add num_events() function. fix create_eventset(), make it set eventset=PAPI_NULL
* 2004-11-18 Philip Mucci — Added better L2_TCM metric. Removed INVALID cache specifier from L2 events. According to AMD a refill to L1 from L2 or SYS cannot be in Invalid state. Which makes sense of course....
* 2004-11-17 Joseph Thomas — Updated a few events and grammatical errors that Office found.
* 2004-11-15 Philip Mucci — Added a better placed dlerror call to print out the library loading failure.
* 2004-11-15 Philip Mucci — Added NO_TLS definition at the head of threads.h. This will allow us to turn off TLS storage.
* 2004-11-15 Philip Mucci — Updated lots of Opteron cache metrics and branch metrics. The only remaining questions are PAPI_L2_TCH and PAPI_L2_TCM. Thanks to AMD and Anoop Iyer for the preset mappings. VENDORS TAKE NOTE. IF YOU HAVE NOT HELPED US GET YOUR PRESET MAPS RIGHT, THEY MAY NOT BE CORRECT!
* 2004-11-15 Philip Mucci — Added test for lib64 installation of PerfCtr on x86_64.
* 2004-11-10 Joseph Thomas — Added Bryan Wylie's fixes for some event definitions.
* 2004-11-05 Dan Terpstra — Finally fixed that &*%! integer too large warning message.
* 2004-11-01 Joseph Thomas — Typo for one of the Opteron events #defines.  BAD!!
* 2004-10-28 Joseph Thomas — A better compile string for mex.
* 2004-10-28 Joseph Thomas — A better compile string for our mex compile.
* 2004-10-28 Joseph Thomas — We were using the // comment format instead of the /* */ format.
* 2004-10-28 london — Fix for an assert that was reported by Sameer
* 2004-10-20 Dan Terpstra — Ooops. I never intnded to check in that last version.
* 2004-10-20 london — Removed check for 0 counts until we change the events to be added, because right now we have no idea which events will be added and it is possible that 0 counts IS a valid result.
* 2004-10-20 Dan Terpstra — Updated Change Log for PAPI 3.0.6 release.
* 2004-10-20 Dan Terpstra — Updated FAQ for PAPI 3.0.6 release.
* 2004-10-20 london — Fix to compile
* 2004-10-20 london — Fixed another memory leak with shlib
* 2004-10-20 Haihang You — fix a memory leak in _papi_hwd_update_shlib_info()
* 2004-10-20 Dan Terpstra — Reformetted Users Guide for PAPI 3.0.6.
* 2004-10-20 Dan Terpstra — Updated documentation procedure for use with Adobe 6.
* 2004-10-20 Haihang You — potential memory leak. Before the pinter to be NULL, free it.
* 2004-10-20 Haihang You — replace fread with fscanf, still read byte by byte. This fix the multiplex1_pthread problem.
* 2004-10-19 london — The install never called the native_install stubs and so libs like libperfctr.so never got installed.
* 2004-10-19 london — Fix conflicts
* 2004-10-19 london — Import of perfctr 2.6.10.2
* 2004-10-19 london — Initial revision
* 2004-10-19 Haihang You — add do_misses to ensure PAPI_L2_DCM have counts on power4.
* 2004-10-18 Haihang You — set default pmapi path
* 2004-10-15 Dan Terpstra — Updated for compatibility with PAPI 3.0.6
* 2004-10-15 Dan Terpstra — Bump the version number up to 3.0.6
* 2004-10-12 Haihang You — add Pentium 2 use sun4u for ultra detection on solaris more lib check use 64 bit mode as default for platforms only support 64bit mode
* 2004-10-12 Dan Terpstra — Major restructuring of the way we handle READMEs and FAQs. Thanks to Phil for taking the lead on this. All content for README and platform specific READMEs have been merged into a single FAQ. That FAQ is maintained EXCLUSIVELY in the PAPI website database. If you need to ADD or EDIT information to the FAQ **DO IT ON THE WEBSITE**
* 2004-10-12 Dan Terpstra — Rewrite content to point to ChangeLog file.
* 2004-10-12 Dan Terpstra — Removed reference to the (fixed) Windows Athlon bug.
* 2004-10-12 london — New test file to make sure we can read counters from a overflow handler
* 2004-10-12 Philip Mucci — Removed these two files. TODO is outdated. CVS-HOWTO now in the FAQ.
* 2004-10-12 Philip Mucci — Simply points elsewhere. Following GNU convention, this file should be here.
* 2004-10-12 Philip Mucci — Removed implicit thread barrier from papi.c PAPI_shutdown(). This violates UNIX-like semantics and now only gets compiled in with -DDEBUG. This doesn't affect normal code. Added a magic environment variable PAPI_ALLOW_STOLEN that will enable tools to detect if the code they are running has used PAPI from underneath them. Only functions properly when linked with the .so. This is a harmless commit as it merely tests for the existance of an environment variable on non-Windows platforms.
* 2004-10-12 Philip Mucci — Missed this commit on the virtual time fix.
* 2004-10-08 london — Obviously we don't compile with -DDEBUG much, as this platform wouldn't even compile with it.  This is fixed now.
* 2004-10-08 london — Fixes to actually compile in 64 bit mode :)
* 2004-10-08 Philip Mucci — WHOA! Long standing bug on the computation of virtual time. This could affect the IA64 by a factor of 978. (1000000/1024). Other systems have been changed accordingly. Please test x1, unicos, and aix.
* 2004-10-08 london — This fixes the problem with not being able to read the counters inside a handler. The only "real" changes are in perfctr-p3.c and perfctr-p4.c.
* 2004-10-08 Philip Mucci — Update from before...
* 2004-10-08 Philip Mucci — Added a note to indicate that the user CAN call this before PAPI_library_init().
* 2004-10-08 Philip Mucci — Updated our old crufty top level makefile to be consistent with the makefiles available and the options to make.
* 2004-10-08 Philip Mucci — Added file for OLD pentiums, pentium2s etc...
* 2004-10-07 Philip Mucci — Bug fix for when PAPI is used in an LD_PRELOAD environment and the process calls exec. The LOAD_CONTEXT syscall returns EBUSY when we have already initialized our PID. This happens when one process EXEC's another and papi is preloaded...the subsequent process doesn't need to load the context.
* 2004-10-04 london — Update
* 2004-10-04 london — Update for the release
* 2004-10-04 Dan Terpstra — Updates for generating PAPI 3 documentation.
* 2004-10-04 Dan Terpstra — Updates for generating PAPI 3 documentation.
* 2004-10-04 Dan Terpstra — HTML Man Pages updated for PAPI 3.
* 2004-10-04 Joseph Thomas — Forgot another .LP
* 2004-10-04 Joseph Thomas — Got rid of some white space in the example.
* 2004-10-04 Joseph Thomas — Missed a dreaded .LP
* 2004-10-04 Joseph Thomas — PAPI_start/stop tweak.
* 2004-10-04 Joseph Thomas — Man page updates; brace yourself for error check updates.
* 2004-10-02 Dan Terpstra — Minor tweak
* 2004-10-02 Dan Terpstra — More man pages.
* 2004-10-02 Dan Terpstra — Looks like Haihang and I were both working on the same file at (about) the same time!
* 2004-10-02 Dan Terpstra — Another man page...
* 2004-10-02 Dan Terpstra — Tweak a print statement for case 4.
* 2004-10-01 Haihang You — man page update
* 2004-10-01 Haihang You — man page update
* 2004-10-01 Dan Terpstra — More man pages.
* 2004-10-01 Haihang You — man page update
* 2004-10-01 Haihang You — man page update
* 2004-10-01 london — Man page update
* 2004-10-01 london — Set all eventsets to PAPI_NULL before create_eventset
* 2004-10-01 Haihang You — man page update
* 2004-10-01 Haihang You — man page update
* 2004-10-01 Haihang You — manpage update
* 2004-10-01 Haihang You — manpage update
* 2004-09-30 Dan Terpstra — Another man page...
* 2004-09-30 Dan Terpstra — Added interface for PAPIF_get_multiplex.
* 2004-09-30 london — We need to support --with-bitmode=  whenever we really do, It was only allowing 32 bit configures on linux
* 2004-09-30 london — Man Page update
* 2004-09-30 london — Man page update
* 2004-09-30 london — Man page update
* 2004-09-30 london — Changed PAPI_get_thr_specific and PAPI_set_thr_specific to return an error if the thread can't be found
* 2004-09-30 london — oops missed one
* 2004-09-30 london — Eventsets must == PAPI_NULL before sending to PAPI_create_eventset
* 2004-09-30 london — All EventSets must be == to PAPI_NULL before being sent to PAPI_create_eventset as specified in the spec/man pages.
* 2004-09-29 Dan Terpstra — More man page changes.
* 2004-09-29 Dan Terpstra — More format tweaks after actually *viewing* the html version of the page.
* 2004-09-29 london — More man page updates
* 2004-09-29 london — Man Page update
* 2004-09-29 Dan Terpstra — Format tweaks after actually *viewing* the html version of the page.
* 2004-09-29 Dan Terpstra — Updates to man pages.
* 2004-09-29 Haihang You — fix for t3e
* 2004-09-29 Philip Mucci — Updates for my recent changes. Much more descriptive now, including output format.
* 2004-09-29 Philip Mucci — Add support for PAPI_QUIET to the PAPIERROR handler. Setting this makes no messages send to stderr, just return codes like a good API should.
* 2004-09-28 london — Updated man page
* 2004-09-28 london — Better error codes returned
* 2004-09-28 Philip Mucci — Removed another assert...
* 2004-09-28 london — Oops forgot to dereference the pointer
* 2004-09-28 Dan Terpstra — Update comment for profiling scale factor.
* 2004-09-28 london — Updated the manpage
* 2004-09-28 london — PAPI_create_eventset was not checking for EventSet != PAPI_NULL as the documentation states
* 2004-09-28 Philip Mucci — Changes to PAPI_shutdown. Better cleanup routine that won't leave dud event sets around.
* 2004-09-28 Haihang You — fix typos
* 2004-09-28 london — Updated Man page
* 2004-09-28 Haihang You — fix for CPU=opteron again
* 2004-09-28 Philip Mucci — BUG! You can pass NULL to PAPI_stop for the values array. MPX_stop didn't allow this. Dumb, dumb, dumb.
* 2004-09-27 london — Added a comment under bugs for the possible Memory leak
* 2004-09-27 london — Changed PAPI_cleanup_eventset to call PAPI_sprofil instead of PAPI_profil as this could cause User supplied memory to be freed.
* 2004-09-27 london — Fixed a memory leak, PAPI_profil was mallocing memory for the sprofil buffer and it was never being freed.  In addition, PAPI_overflow and PAPI_sprofil both added new buffers when an eventcode was added with a non-zero threshold and was never checking to see if that EventCode already exists, now it does and updates the values.
* 2004-09-27 london — First round changes on man pages
* 2004-09-27 Haihang You — check certain library on certain platform
* 2004-09-27 Haihang You — fix to check CPU=opteron
* 2004-09-27 Haihang You — comment out PMAPI, it will be set by configure
* 2004-09-27 Haihang You — add falg for pmapi path on aix
* 2004-09-27 london — First round of changes for 64 bit semantics, this basically just converted all long long to long_long for consistency.  All API's will use PAPI defined sizes as: papi_i64, papi_i32, papi_i16, papi_ui64, papi_ui32, papi_ui16
* 2004-09-27 london — Check to make sure PAPI_thread_init is not called more than once.  It also checks to make sure PAPI_library_init is called before PAPI_thread_init.
* 2004-09-27 london — kurfin test added back to the Makefile
* 2004-09-27 Philip Mucci — Removed redundant PAPI_library_init
* 2004-09-27 Philip Mucci — Missed a PAPI return statement!
* 2004-09-27 Philip Mucci — Additional minor fix for AIX
* 2004-09-27 Philip Mucci — This is a poor attempt at a lock in PAPI_library_init to prevent the kind of failures we saw when I checked in my broken multiplex1_pthreads test. This test (mistakenly) called PAPI_library_init multiple times causing confusion.
* 2004-09-27 Philip Mucci — Added check for setting thread ID function on AIX. On AIX, the set function is a NO-OP because the functions are dlsym'd dynamically at run-time. This is all because of the ANY_THREAD_GETS_SIGNAL behavior of the itimers.
* 2004-09-24 Haihang You — output error message when the configure can't figure out the right platform
* 2004-09-24 Haihang You — add information about first fail on aix5.2 & power4
* 2004-09-24 london — Bugs were introduced into the code, because case[x]() was calling init_papi_pthreads, but so was case[1]_pthreads which was bad as the init is initializing the library, etc....  This hopefully will fix all the platforms.
* 2004-09-24 Philip Mucci — Much better error checking on both tests. If a pthread_create called before, we wouldn't report this as a fail.
* 2004-09-24 Philip Mucci — Removed unreferenced variable from remove_event
* 2004-09-24 london — Updated for forcing software overflow, and added PAPI_overflow for more info in the profil man pages
* 2004-09-24 Haihang You — add comments for configure
* 2004-09-24 Haihang You — if bitmode is not supported, configure will print error message and fail
* 2004-09-23 Haihang You — fix for 3.0
* 2004-09-23 Haihang You — fix for supporting 3.0
* 2004-09-23 Haihang You — fixes for supporting papi3.0
* 2004-09-23 Philip Mucci — Slight fix to prevent rentrant signals and fix up error strings. Multiplexing is still horribly broken when run on a BUSY aix 4.3 box
* 2004-09-23 Philip Mucci — Make these 3 tests consistent in terms on way that they start threads. zero_pthreads had a bug in thread arguments that showed up on big machines
* 2004-09-23 Philip Mucci — Make these tests consistent with each other...finally. This may require some tweaking but looks ok at the moment.
* 2004-09-23 Philip Mucci — added proper return value check for PAPI_add_events
* 2004-09-23 Philip Mucci — Partial success for PAPI_add_events/remove_events...
* 2004-09-23 Philip Mucci — Both calls can now partially succeed as before...just better return values. If partial success, return the number of consecutive entries that failed.
* 2004-09-22 Dan Terpstra — Keep html pages current with man pages
* 2004-09-22 Dan Terpstra — Split profile pages into two instead of just linking to one; Massive rewrite to finally *explain* profiling and the differences between profil and sprofil; Expansion to describe recent changes to definition of scale factor.
* 2004-09-22 london — Removed kufrin from default build until, a lockup is fixed
* 2004-09-22 london — We were checking in PAPI_list_events if number <= 0, but number was a pointer that wasn't dereferenced ;)
* 2004-09-22 london — Resolved conflicts with the perfctr import
* 2004-09-22 london — Perfctr 2.6.10.1 import
* 2004-09-22 london — Initial revision
* 2004-09-22 london — Updated to test removing/adding events with eventsets that have overflow on some events.
* 2004-09-21 Dan Terpstra — Add byte_profile to demonstrate byte level address scaling and multi-event simultaneous profiling.
* 2004-09-21 Dan Terpstra — Propagated the fixes from the P4 substrates back to the P3
* 2004-09-21 Dan Terpstra — Fixed two nasty bugs: 1. the clear_control_state routine was not clearing the nrictrs field; 2. nracntrs was not initialized before being used in a counter swap call.
* 2004-09-21 london — Upped the Threshold when PAPI_event = PAPI_TOT_INS, because the hardware overflow would get the exact number, but the software overflow's granularity is so bad that I can only get ~20 overflows during the test run, which was way off since we were looking for 160. New threshold = threshold*10 when PAPI_event=PAPI_TOT_INS
* 2004-09-21 Philip Mucci — Return PAPI_ESYS when you get an error from pthreads.c
* 2004-09-21 Philip Mucci — In honor of Ricks ability to kill PAPI, he gets his own test case...
* 2004-09-21 Philip Mucci — Updates to reflect updated semanitcs
* 2004-09-21 Philip Mucci — Possible bug fix to Rick Kufrins observed threading problem with hundreds of eventsets.
* 2004-09-20 london — Changes for profil to work with forced software overflow, and allow profil to use derived events in that mode.  In addition, added automatic PAPI_profil calls when removing an event that is profiled.
* 2004-09-20 london — Change PAPI_remove_event to work without the user having to first call PAPI_overflow to remove overflow handeling on that event.
* 2004-09-20 Dan Terpstra — Tweaked the scale factor checking for a minor bug that caused the sprofile.c 'single bucket' case (scale = 2) to fail.
* 2004-09-20 london — Bug in software overflow version of profile, this bug, would cause weighted smaples, to always increment by 255 as it was - the threshold, instead of the deadline, so once a threshold was exceded it would always be exceded on each overflow after that.
* 2004-09-20 london — Changes PAPI_OVERFLOW_FORCE_SW from 0x30 to 0x40 (oops) In Multiplex, set default values for variables to stop a compiler warning
* 2004-09-20 Dan Terpstra — Added #ifdef DEBUG to a couple of print_control calls
* 2004-09-20 london — Fix for Profiling with the new force software overflow, a flag was being set inproperly
* 2004-09-20 london — Ooops left my debug print statements in the file
* 2004-09-20 london — Fixes for Force overflow when also trying to overflow in hardware. This should fix all the bugs, with the exception you currently can't add an event to a EventSet that has a event with overflow turned on.  I am investigating to see if this is a general PAPI thing, or something wrong with the p4 substrate.
* 2004-09-17 Dan Terpstra — Check for L3 cache before adding L3 events to the event table.
* 2004-09-17 Dan Terpstra — Fixed a minor output formatting problem.
* 2004-09-17 Dan Terpstra — Fixed a minor reporting bug in the utility routines for profiling.
* 2004-09-17 Dan Terpstra — Expanded the definition of the scale factor in PAPI_profile to allow for byte level resolution of the address buckets as requested by Nathan Tallent and the gang at Rice. Also moved scale validity checks from PAPI_profile to PAPI_sprofile to make sure they always get checked consistently.
* 2004-09-17 Dan Terpstra — Addition of prototype for _papi_hwi_get_granularity(). Not sure how the regression tests were compiling without this.
* 2004-09-17 Philip Mucci — Slightly better error handling and the removing of a few asserts...most are still necessary due to this code. Yes, I promise a rewrite for PAPI 3.1. Promise!
* 2004-09-17 Philip Mucci — Removed dead code....
* 2004-09-17 Philip Mucci — Removed debugging asserts...
* 2004-09-16 Philip Mucci — Bumped the revision number for 5. This is needed for code that depends on the PAPI_event_info_t structure, like papiex.
* 2004-09-16 Dan Terpstra — New events implemented based on input from Brinkley Sprunt: PAPI_LD_INS PAPI_SR_INS PAPI_LST_INS and a bunch of L2 and L3 cache events. They haven't been extensively tested, but at least in the case of sdsc-mpx the loads and stores generate numbers. Further testing would be beneficial.
* 2004-09-15 Dan Terpstra — Changes in the way event tables are handled on Pentium 4. Now, a base table is loaded for all p4s, and other tables are conditionally overloaded based on model number, #defines, and/or environment variables. Following Phil's model there is now compile time or run time control over the definition of PAPI_VEC_INS and PAPI_FP_OPS. To minimize overlap and maximize flexibility, PAPI_FP_INS counts ONLY events passing through the FP unit, but effective use of tagged native events can change that behavior one the fly. Tagging conventions have been defined as follows: Tag 1: PAPI_FP_INS Tag 2: PAPI_FP_OPS Tag 3: PAPI_VEC_INS Tag 4: undefined
* 2004-09-15 Haihang You — fix the segfault sameer reported
* 2004-09-15 london — Ugh, checking in the right version of Makefile
* 2004-09-15 london — *** empty log message ***
* 2004-09-15 Dan Terpstra — Minor changes to allow dense event tables to overload existing tables. This allows a base event table to be modified for processor or compiler differences. In this way, events can be added, deleted or modified, based (for instance) on processor model number. Implemented and tested for Pentium 4. Possibly also useful for Pentium III/Athlon, etc.
* 2004-09-14 london — Force software fix
* 2004-09-14 london — First round of changes for forcing software overflow.  The interface has been completely rewritten.  Now you pass in PAPI_OVERFLOW_FORCE_SW in the flags of the PAPI_overflow to force software overflow.  This will also allow users to overflow on Derived events which you can't do with hardware overflow.
* 2004-09-14 london — First round of changes for forcing software overflow.  The interface has been completely rewritten.  Now you pass in PAPI_OVERFLOW_FORCE_SW in the flags of the PAPI_overflow to force software overflow.  This will also allow users to overflow on Derived events which you can't do with hardware overflow.
* 2004-09-14 Joseph Thomas — Undid previous checkin
* 2004-09-14 Joseph Thomas — Enabled set_granularity to either perform or return the correct error.
* 2004-09-13 Haihang You — CC_SHR  = xlc -bnoentry -bE:libpapi.exp -bM:SHR still not working on our power3. rollback to the old one which works on eagle.
* 2004-09-13 Haihang You — changes to make the compiler on our power3 happy
* 2004-09-13 Philip Mucci — Added code to configure PAPI_VEC_INS for MMX or SSE. New default is to count packed SSE instructions. Also, dynamically update the descriptions according to the settings of FP stuff I checked in before.
* 2004-09-11 london — Changed to _rtc for a real time clock
* 2004-09-10 london — Fixes so fortran will compile on the X1, this implies no implicit none, so beware
* 2004-09-10 london — Added compile flag to support __FILE__ in fortran
* 2004-09-10 london — Need to prewarm the do_misses for L2 misses
* 2004-09-10 london — Updated the table for Intel, this was never setting the unified cache correctly, this has now been fixed.
* 2004-09-10 Haihang You — hope this can fix the problem on solaris. What happened is that gnu uname would not give the info 'Ultra'.
* 2004-09-10 Philip Mucci — Added code to put the thread ID as part of the debug label if threads are enabled.
* 2004-09-10 london — Added a 1% error range
* 2004-09-09 london — Fixes to make X1 work with Phil's latest changes
* 2004-09-09 Haihang You — add nocona support by detect family(15) and model(3).
* 2004-09-09 london — We only opened libpapi.so but on most 64 bit archs, it is libpapi64.so, I added a loop to try and open libpapi64.so if libpapi.so fails.
* 2004-09-09 Philip Mucci — Sure would help if I committed the working P4 patch to have configurable FP counts! ----------------------------------------------------------------------
* 2004-09-09 Haihang You — fix for solaris. tested on enterprise and hera.
* 2004-09-08 Philip Mucci — We missed setting retval on an error statement.
* 2004-09-08 Joseph Thomas — Fixed a typo of my own.
* 2004-09-08 london — ntv stuff for tru-alpha, only prints out the code in hex, should be a little more complete....
* 2004-09-08 Joseph Thomas — Tested and fixed the T3E substrate.  One typo and one function definition were the only problems.  The lock_init() had a compile error; I noticed it was completely empty, so I removed.  If we need it in the future, I'll be glad to put it back.
* 2004-09-08 Haihang You — change c++ comment style to c comment style, it will make the compiler happy on aix
* 2004-09-08 london — Added do_misses in addition to do_l1misses, it only does 1 iteration on a 4 MB size This ups the L2 misses being monitored on solaris, so there is not a large error margin.
* 2004-09-08 london — Skip PAPI_L1_ICM and PAPI_L2_ICM to make sure we have counts, as we don't always have an instruction cache miss and currently we don't have a loop to force them.
* 2004-09-08 Philip Mucci — Fixes for AIX from my massive update. Tests seem to pass on AIX 5
* 2004-09-08 london — Added check for 0 counts on multiplex was causing a bunch of failures that were not really failures because L2 DCM can be 0 on many platforms, added do_misses to take care of this, but I am still concerned PAPI_L2_ICM could come up as 0, but we will see.
* 2004-09-08 Dan Terpstra — Reworked this test to repeat the basic test 10 times and compute min, max, and sum. This gives better statistics and much smaller errors. It now passes every time on itanium.
* 2004-09-07 Philip Mucci — Added code for 2 things. First are #defines for types of counts PAPI_FP_INS and PAPI_FP_OPS should count.
* 2004-09-07 Haihang You — add _papi_hwd_ntv_bits_to_info function
* 2004-09-07 Dan Terpstra — Added a definition for PAPI_RES_STL that generates at least a few counts in command_line.
* 2004-09-07 Dan Terpstra — Forgot to check these in the other day when I converted max scale factor from 65535 to 65536.
* 2004-09-07 Philip Mucci — Added wrappers for PAPI_unregistr/register
* 2004-09-07 Philip Mucci — Added new information about OpenMP and dumb calls like omp_get_thread_num that don't reflect new LWP-IDs.
* 2004-09-07 Philip Mucci — Removed an exit found in the code and lots of unused variables.
* 2004-09-06 Philip Mucci — Moved around PAPIERROR one last time.
* 2004-09-06 Philip Mucci — Last round of debugging header fixups
* 2004-09-06 Philip Mucci — New linkage for broadcast call
* 2004-09-06 Philip Mucci — added static keyword to inline
* 2004-09-06 Philip Mucci — Papi_protos.h wasn't on the headers dependency
* 2004-09-06 Philip Mucci — Fixed to broadcast_signal on the platforms that send an itimer to any thread. (AIX). More discretion as to who we send the signal to!
* 2004-09-06 Philip Mucci — Continuation line needed.
* 2004-09-06 Philip Mucci — parallel end is not an openmp construct.
* 2004-09-06 Philip Mucci — Cleaned up debugging macros, made the right ones PRF, OVF and INTDBG
* 2004-09-06 Philip Mucci — New lock interface, papi_hwi_lock/unlock
* 2004-09-06 Philip Mucci — Moved debugging macros to be inline so the optimizer can get rid of them hopefully...unfortunately when we don't have VARARG macros these functions still get called. ARGH!
* 2004-09-06 Philip Mucci — Locking fixes, not needed on this platform.
* 2004-09-06 Philip Mucci — Renamed local lock_init
* 2004-09-06 Philip Mucci — Added errno.h, fixed header files to be conformant and changed locking functions o the new papi_hwi_locks which don't lock when threads are not enabled.
* 2004-09-06 Philip Mucci — Build fixes for Solaris, added errno.h always a good thing. Reordered debugging check for unknown thread.
* 2004-09-06 Philip Mucci — Minor fixes with build performance options and gcc flags.
* 2004-09-06 Philip Mucci — Added support for Nocona. Now works. Counts FP instructions via scalar-DP-uop and x87 meaning single precision won't count.
* 2004-09-06 Philip Mucci — Makefile and Makefile.inc: install target now installs man pages, headers and libs. install all does the above AND test programs.
* 2004-09-05 Philip Mucci — Removed all references to DBG to use appropriate DBG macros. All messages to stderr now go through PAPIERROR
* 2004-09-05 Philip Mucci — Entirely new thread handling library, required for unregister thread and other goods. Now uses __thread keyword with GCC 3 for superfast TLS lookups (no searching, constant time!)
* 2004-09-05 Philip Mucci — Restructured TLS and LOCK definitions so the user can't mess up PAPI's locks and TLS.
* 2004-09-05 Philip Mucci — removing more linux/x86isms from this code. Added lock static lock init which is no longer called from the high level.
* 2004-09-05 Philip Mucci — Added code for multiple compilers, COMPILER=INTEL,PGROUP,PATHSCALE default is GCC Added openmp target for INTEL Tested with INTEL, PGROUP, PATHSCALE
* 2004-09-05 Philip Mucci — Makefile.any-null: Slowly removing all linux dependance from any-null substrate. More to go. Makefile.inc: add threads.h Makefile.linux-perfctr-athlon: Removed sse flags to support OLD athlons Makefile.linux-*: Added support for different compilers selectable by COMPILER=INTEL,PGROUP,PATHSCALE default is GCC of course, tested with INTEL, PATHSCALE. PGROUP doesn't compile assembly yet...
* 2004-09-05 Philip Mucci — Makefile: Added unregister_pthreads test case. locks_pthreads.c: Changed test_fail to test skip if thread support not available. multiplex2: added check for zero counts multiplex3_pthreads: made it look like multiplex2, removed crufty special case code native.c: Added initializer to IA64 array, we were overwriting memory! profile_twoevents.c sprofile.c: removed comparison of subtraction of two unsigned > 0 that's always greater than zero because of the data type. test_utils.c: changed message to Error test_utils.h: changed MAX_TO_ADD to 5 to try and get some decent presets for multiplex cases zero_omp.c: Added tough test case submitted by portland group, now uses unregister_thread. zero_pthreads.c: Added unregister code and use 4 pthreads instead of 2
* 2004-09-01 Dan Terpstra — In one of my more anal-retentive moments, I decided the profil scale factor couldn't exceed 65535, or 0xFFFF This is because in the olden days, scale was implemented as a short (16-bit) int. These days, scale is an unsigned int (32-bits), which can easily hold more than 0xFFFF. AND 65535/65536 produces a rounding error for a nominal scale of 1. So, I broke with tradition and made maximum scale == 65536 for all our profile tests.
* 2004-08-31 london — Submitting the fix for Solaris for the 2nd time, be careful overwriting changes ;)
* 2004-08-31 Dan Terpstra — Cleanup to match the profiling code in ctests.
* 2004-08-31 Dan Terpstra — Cleanup to match the profiling code in ctests.
* 2004-08-31 Dan Terpstra — Stuff added to cost to elucidate the cost distribution problem identified by Phil. Check out the -d and -s command line options to display cost distribution and standard deviation distribution.
* 2004-08-31 Joseph Thomas — Updates for the new ntv functions.  Compiles AND works.
* 2004-08-31 london — Added _papi_hwd_ntv_bits_to_info  and _papi_hwd_ntv_code_to_bits.
* 2004-08-30 Haihang You — add t3e
* 2004-08-27 Haihang You — fix for irix
* 2004-08-27 Haihang You — add some fix for solaris-ultra. remove some redundant chekas Kevin suggeted
* 2004-08-27 Joseph Thomas — branches.c works.
* 2004-08-27 Joseph Thomas — Fixed some compile warnings.
* 2004-08-27 Haihang You — fix for x1
* 2004-08-27 Dan Terpstra — Fixed allocation problem with pebs conflict. Previously we were bailing out when we updated the control structure. This was leaving events in an indeterminate state and screwing things up. Now we trap for pebs conflicts during event resource allocation, which prevents them from ever making it to the event list. Thanks to Aleksandar Donev for finding this stinker.
* 2004-08-26 london — Add the ntv stuff for x1
* 2004-08-26 london — We were copying info.event_note which apparently does not exist anywhere and I assume it is suppose to be info.note instead.  The question is how was papi_fwrappers.c compiling anywhere?  Dan, can you check this to make sure I didn't do anything wrong just in case.  Line 361.
* 2004-08-26 london — Wouldn't detect Solaris correctly, this is now fixed.
* 2004-08-26 Dan Terpstra — This is a waay cool little utility. But it was segfaulting on PAPI_perror(). And it was failing to count if an event didn't add. I fixed it. Thanks, Kevin!
* 2004-08-26 Dan Terpstra — Rewrite of the profiling routines. They now share a great deal of common code, found in prof_utils.c. I don't know if this is any easier, but at least we're making the same mistakes the same way every time. Hopefully this will improve maintainability.
* 2004-08-26 london — New test that takes presets [Native or PAPI] from the command_line and attempts to add them in that order, starts them, does 1 do_flops and then stops and prints out values.  This will pass if no arguments are given or the tests_quiet arg is passed in.  Meant as an easy way to verify problems with our allocation scheme (IE can only add in this order, or can add if you add this event, etc....)
* 2004-08-26 london — Ooops forgot I need this too
* 2004-08-26 london — It should be tru64, not true64 for the Makefile on alpha not using DADD.
* 2004-08-24 Dan Terpstra — Implementation of NULL stubs for _papi_hwd_ntv_code_to_bits() and _papi_hwd_ntv_bits_to_info() routines. I'd rather implement real routines, but I'm not sure where the register info is stored in itanium.
* 2004-08-24 Dan Terpstra — Explicit initialization of retval in _papi_hwi_get_native_event_info() to avoid a compiler warning.
* 2004-08-24 Dan Terpstra — Added a comment to the _papi_hwd_ntv_code_to_bits() routine.
* 2004-08-24 Dan Terpstra — Modified _papi_hwd_ntv_code_to_bits() to hand back data instead of a pointer to a structure.
* 2004-08-24 Haihang You — add cray-x1
* 2004-08-23 Haihang You — still fix for power4 aix5
* 2004-08-23 Haihang You — little twist for aix5.2
* 2004-08-23 Haihang You — this file is needed by configure
* 2004-08-23 Haihang You — add configure, it would generate right Makefile for the platforms we currently support. configure --prefix=/... --with-bitmode=64 bitmode default is 32, and it won't be 64 if the platform does not support 64 bit mode. prefix default is /usr/local
* 2004-08-23 Joseph Thomas — Updated T3e with all major functionality working.
* 2004-08-20 Joseph Thomas — Added an extra definition of a function on my previous commit.
* 2004-08-20 Dan Terpstra — More support for DERIVED_CMPD. Basically, I had to allow overflow to work on DERIVED_CMPD events as well
* 2004-08-18 Dan Terpstra — Added a case for DERIVED_CMPD, a derived type that has existed forever, but was never implemented. It does nothing, but should be supported. I added it to the P4 event table when testing the avail changes. That broke papi_internal.
* 2004-08-18 Joseph Thomas — Updated new native event table function.
* 2004-08-18 Joseph Thomas — Added  _papi_hwd_ntv_bits_to_info().
* 2004-08-18 Joseph Thomas — profile.c was seg faulting on t3e because we hard- coded some values concerning data-type sizes.  Tested on the pentium3.  If I hurt another substrate, let me know and I'll implement another fix.
* 2004-08-18 Dan Terpstra — Ya gotta change the code, not just the help text. Doh!
* 2004-08-17 Dan Terpstra — Rearrangement of options.
* 2004-08-17 Dan Terpstra — Minor mods to make PAPIf_get_event_info work with the new event_info struct. Very little change was needed. Doesn't support all C functionality, but at least what it does support now works as advertised.
* 2004-08-17 Dan Terpstra — Beefed up avail.c to make it work more like a tool and less like a test. Try typing avail -h. New options to display in the old tabular format (-t), and the new full detail format (-f). As well as the event detail format (-e).
* 2004-08-17 Dan Terpstra — Changes to PAPI to implement reporting of information on native events. Adds a new _hwd_ call: _papi_hwd_ntv_bits_to_info() that converts a hwd_register_t structure into a series of names and values. See the bottom of p4_events.c for a reference implementation; See the bottom of p3_events.c for the minimum 'no-op' implementation to pass the linker.
* 2004-08-17 Joseph Thomas — PAPI's version of ffsll wasn't working properly in the case sizeof(int)==sizeof(long_long).
* 2004-08-16 Dan Terpstra — Oops. Added code to support the full info display of a named native event.
* 2004-08-16 Dan Terpstra — Changes to PAPI ctests to implement reporting of information on native events. avail now supports a new command line parameter: > avail -f(ull) PAPI_TOT_INS will present all information on one specific event, including all native event info for each term associated with a preset event.
* 2004-08-16 Zhou Min — return an error when the user tries to set multiple overflow on two and more events and these events happen to be counted by one hardware counter.
* 2004-08-16 Zhou Min — return an error when the user try to set the domain to PAPI_DOM_OTHER   in function set_domain
* 2004-08-14 Zhou Min — changed set_granularity function according to dan's suggestion
* 2004-08-13 Joseph Thomas — Fixes for the T3E.  Profiling tests are still in the works.
* 2004-08-13 Joseph Thomas — Removed maxmem option from set_opt and all _papi_hwd_setmaxmem() references.
* 2004-08-13 Zhou Min — added multiple overflow support in IRIX
* 2004-08-13 Philip Mucci — Common for x86_64 archtectures. If uname -m reports x86_64, then we build with -fPIC for the shared lib and append 64 to the library suffix. ----------------------------------------------------------------------
* 2004-08-11 Dan Terpstra — Clarification of the new EventInfo structure.
* 2004-08-11 Zhou Min — tweak on set_granularity function
* 2004-08-11 Dan Terpstra — Phil's recent addition of the following line:
* 2004-08-11 Zhou Min — minor change to compile memory.c
* 2004-08-11 Zhou Min — removed this program from ctests directory.
* 2004-08-10 Joseph Thomas — Added case for the Cray T3E.
* 2004-08-10 Zhou Min — Add mix/max/stddev information to 'cost' and 'clockres' test cases
* 2004-08-10 Zhou Min — change the output order
* 2004-08-10 Joseph Thomas — Cray T3e needs the same special case.
* 2004-08-10 Joseph Thomas — Fixed a bug with PAPI_get_event_info().  This escaped most substrates, but not the T3E or probably other 64-bit systems. An EventCode was where an i was supposed to be.  It's better now.
* 2004-08-09 Joseph Thomas — Some corrected presets.
* 2004-08-09 Joseph Thomas — T3E updates.  Event add order corrected.  Updated for Dan's changes. Also, do_read() looked at /dev/zero which doesn't exist on the T3E, so I made it look at another big file (p3_events.c).
* 2004-08-09 Dan Terpstra — Checking in changes to ctests that I should've committed *before* leaving on vacation. Sorry, guys...
* 2004-08-09 Philip Mucci — Fixes for Nocona/EMT64. Fairly simple changes. No test cases pass but that's due to other changes going on in the library. Retrofitting these changes on 3-0-4 seemed to work.
* 2004-08-02 Joseph Thomas — Huge error in _papi_hwd_read caused counts to be wacky at times.  35/77 tests pass now.
* 2004-08-02 Joseph Thomas — T3e updates - can count.
* 2004-07-30 Joseph Thomas — Mod to get native_avail to work.
* 2004-07-30 Dan Terpstra — Major rewrite (first pass) of pepi_event_info functionality. Data structure changes have been implemented in the independent layer and tested on Pentium 4 and POWER3. No other changes should be required in other substrates (for now).
* 2004-07-29 Dan Terpstra — Minor tweaks in preparation to rewrite _papi_hwi_get_native_event_info() to better support more comprehensive documentation of native events.
* 2004-07-29 Dan Terpstra — Changes to support the removal of the international strings files.
* 2004-07-29 Dan Terpstra — Deprecated the header files that provided internationalization support for event strings and error messages. This 'feature', introduced by me 3 years ago, was a misguided attempt to add multiple language functionality to a product that didn't need it. It ended up just getting in the way and complicating things. Now, strings are initialized directly in papi_data.c.
* 2004-07-29 Dan Terpstra — This substrate {perfctr-p4.c and p4_events.c} is the reference implementation for changes to _papi_hwi_setup_all_presets()  to add new developer notes functionality. This change basically just adds a parameter to the call. If the new parameter is NULL, nothing changes. If the new parameter is a pointer to a dense <notes>array, developer notes can be added in a space efficient way to any event.
* 2004-07-29 Dan Terpstra — Changed all substrates to support new event_info functionality. This change basically just adds a parameter to the _papi_hwi_setup_all_presets() call. If the new parameter is NULL,  nothing changes. If the new parameter is a pointer to a dense <notes> array, developer notes can be added in a space efficient way to any event. See the Pentium 4 implementation {perfctr-p4.c and p4_events.c} for more specifics. All other substrates are NULLed. NOTE: This tests clean on Pentium4 and POWER3. All other platforms beware...
* 2004-07-29 Dan Terpstra — Eliminate an unreferenced data structure.
* 2004-07-29 london — Updated the release number and added X1
* 2004-07-29 Zhou Min — tweak on papi_hwd_reset
* 2004-07-29 Joseph Thomas — The t3e's preset map was incorrect.
* 2004-07-28 london — *** empty log message ***
* 2004-07-28 london — Perfctr 2.6.9
* 2004-07-28 london — Initial revision
* 2004-07-28 london — A few flag changes for Fortran
* 2004-07-28 london — Some flag changes
* 2004-07-28 london — Initial revision
* 2004-07-28 Joseph Thomas — Removed a #define that is no longer needed.
* 2004-07-28 Joseph Thomas — Event table for the t3e.
* 2004-07-28 Joseph Thomas — Updated files for the t3e port.
* 2004-07-28 london — Ooops forgot to add this file
* 2004-07-28 Zhou Min — added special treatment in IRIX
* 2004-07-28 Zhou Min — changed the test events to PAPI_TOT_CYC and PAPI_TOT_INS
* 2004-07-28 Zhou Min — fixed the overflow but in UltraSparcIII
* 2004-07-27 Zhou Min — changed a local variable length from unsigned long to long, because the condition if (length > 0) would otherwise always be true.
* 2004-07-27 london — Turn off debugging and fix a variable that was never set before being used.  Luckily the compiler set it to 0, not it is explicit though ;)
* 2004-07-27 london — Added debugging info in papi.c for overflow.  Fixed bug where X1 used hardware and software overflow at the same time, new Makefiles for msp and ssp libraries.  Added __crayx1 defines to overflow so it shows flops at correct rate and shows that the 2nd reading of floating point instrcutions is inaccurate (in this case 0), because we used hardware overflow
* 2004-07-27 Zhou Min — fix the compile warning in itanium2
* 2004-07-27 Zhou Min — fix the compile warning message in tru64-alpha
* 2004-07-27 london — Definition for _papi_hwi_dummy_handler would not compile on the Cray X1, this is the fix.  Please test your platforms to make sure the fix doesn't screw up compiles on other platforms.
* 2004-07-27 Joseph Thomas — Removed a useless typedef of _papi_hwd_context_t.
* 2004-07-24 Zhou Min — deleted a duplicated compile option
* 2004-07-24 Zhou Min — fix a compile warning message
* 2004-07-24 Zhou Min — fix the compile warning message
* 2004-07-23 Dan Terpstra — Added MH_TYPE_WT and MH_TYPE_WB flag bits to the memory heirarchy stuff to allow encoding for write-through and write-back cache types. These bits are exclusive and not currently set anywhere. If neither is set, characteristic is 'not known' or 'not defined'.
* 2004-07-23 london — New setopt to override HW overflowing (Needed fo Cray X1) PAPI_FORCE_SW_OVERFLOW, setting this to 1 will force using software overflow.
* 2004-07-23 london — Added shlib to test targets, look at this for example.
* 2004-07-23 Zhou Min — 1. change the data type for pid to pid_t; 2. change the data type for tid to unsigned long int;
* 2004-07-23 Zhou Min — fixed a bug which caused itanium to include executable information of itself into the shared library array;
* 2004-07-23 Zhou Min — 1. added -D_GNU_SOURCE in the makefile; 2. replaced getpid with syscall(__NR_gettid); 3. other fixes to reflect Kevin's change;
* 2004-07-23 Zhou Min — added shared target
* 2004-07-23 Zhou Min — added shared targets
* 2004-07-23 Haihang You — add -DNEED_FFSLL
* 2004-07-23 Zhou Min — deleted -DDEBUG option
* 2004-07-23 Zhou Min — Updated _papi_hwd_update_control_state()'s arguments to reflect Kevin's changes.
* 2004-07-23 Haihang You — add -DNEED_FFSLL
* 2004-07-23 Haihang You — add -DNEED_FFSLL
* 2004-07-23 Haihang You — minor fix to reflect Kevin's changes
* 2004-07-23 Zhou Min — Updated _papi_hwd_update_control_state()'s arguments to reflect Kevin's changes.
* 2004-07-23 Zhou Min — Updated _papi_hwd_update_control_state()'s arguments to reflect Kevin's changes.
* 2004-07-23 Haihang You — add -DNEED_FFSLL
* 2004-07-23 Haihang You — minor fixes to reflect previous changes
* 2004-07-23 london — Added that overflow threshold for P-Chips is compared to the aggregate of the 4 SSP counters for software profiling, but the threshold is compared against each individual SSP counter for hardware overflow
* 2004-07-23 london — X1 Readme file
* 2004-07-22 Dan Terpstra — Updated _papi_hwd_update_control_state()'s arguments to reflect Kevin's changes.
* 2004-07-22 Dan Terpstra — Updated defines to match most recent Intel docs; added a new native event group for model 3.
* 2004-07-22 Zhou Min — Updated _papi_hwd_update_control_state()'s arguments to reflect Kevin's changes.
* 2004-07-22 Zhou Min — change the return type of function _papi_hwi_dummy_handler to PAPI_overflow_handler_t;
* 2004-07-22 Joseph Thomas — Updated _papi_hwd_update_control_state()'s arguments to reflect Kevin's changes.
* 2004-07-22 Dan Terpstra — Kevin's X1 changes went back to profiling the entire address space. This broke the recent fix I introduced for Itanium only.
* 2004-07-22 london — Several Check ins as follows: New error code: PAPI_EPERM for cases where you don't have sufficent permissions to execute.  For example running Kernel or Exception count mode on the X1 or SGI machines.  This will also cause test cases to skip instead of failing.
* 2004-07-21 Joseph Thomas — We had some errors in the case the user wanted to use the gcc compiler.
* 2004-07-19 Dan Terpstra — Minor modifications to the declarations of the event tables so that itanium 1 can be distinguished from itanium 2.
* 2004-07-15 Zhou Min — include  <libgen.h> which has the prototype for function basename
* 2004-07-15 Zhou Min — tweak to avoid compile warning message
* 2004-07-15 Zhou Min — tweak to avoid compile warning message
* 2004-07-15 Dan Terpstra — hwi_search_t structures were declared with PAPI_MAX_PRESET_EVENTS entries. This resulted in dead entries and an unnecessarily large footprint. I removed the fixed size constraint, renamed the tables for consistent naming convention,  and declared the structs as 'static const'.
* 2004-07-15 Zhou Min — tweak to avoid compilor warning message in Itanium
* 2004-07-15 Zhou Min — tweak to avoid compilor warning message in Solaris
* 2004-07-14 Zhou Min — revoke the change made by me
* 2004-07-14 Zhou Min — nothing is changed except a blank line is gone.
* 2004-07-14 Zhou Min — My bad, should not check in these files.
* 2004-07-14 Zhou Min — used another method to capture the overflow signal in Itanium
* 2004-07-14 Haihang You — remove old unnecessary comments
* 2004-07-14 Haihang You — as we discovered that _AIXVERSION_510 and _AIXVERSION_520 are defined in standards.h, changed defined( _AIX51) || defined(_AIX52) to defined( _AIXVERSION_510) || defined(_AIXVERSION_520)
* 2004-07-14 Zhou Min — changed the output order of the events
* 2004-07-14 Zhou Min — change the prototype for add_two_events
* 2004-07-13 Zhou Min — now these programs call add_two_events to add events to the eventset
* 2004-07-13 Zhou Min — add a function called add_two_events. This function always adds PAPI_TOT_CYC into the eventset. Depending on the platform and availability of the event, this function also adds PAPI_FP_INS or PAPI_FP_OPS or PAPI_TOT_INS into the eventset.
* 2004-07-12 Dan Terpstra — Cleaned up event checking for propagation to other profile tests.
* 2004-07-12 Dan Terpstra — Modify to properly support Itanium's function descriptors instead of function pointers; Also tweak output to better handle 64-bit addresses.
* 2004-07-09 london — Fixes so that the shlib test can find libperfctr.so.5 even if LD_LIBRARY_PATH or LIBPATH (AIX) is not set.  This should be considered a bandaid, and a better fix would be use autoconfig or some other measures.
* 2004-07-08 Haihang You — new preset definition  PAPI_L1_LDM  =  L1D_READ_MISSES_RETIRED  PAPI_L2_LDM  =  L3_READS_DATA_READS_ALL  PAPI_L3_LDM  =  L3_READS_DATA_READS_MISS
* 2004-07-02 Philip Mucci — Added changes from 3-0-3 branch....
* 2004-07-02 Dan Terpstra — New test to examine full PAPI version. Probably should just be incorporated into avail.
* 2004-07-02 Dan Terpstra — Refactor and restructure this test. Now incorporates profile calls for all three bucket sizes, allowing direct comparison. Displays additional info about profile settings. Properly explains and mallocs memory for bin buffers. Profiles only on do_flops rather than the entire text address space.
* 2004-07-02 Dan Terpstra — Expose prototype for fdo_flops to enable it to be used as an ending address for profile tests.
* 2004-07-02 Dan Terpstra — Tweak calling sequence to PAPI_profil to match new tighter prototype.
* 2004-07-02 Dan Terpstra — Deprecate profile_32 and profile_64 because they are now incorporated into profile.c.
* 2004-07-02 Dan Terpstra — Deprecate these tests because they are now incorporated into profile.c.
* 2004-07-02 Dan Terpstra — Restructure low level profile support routines to properly handle bucket sizes. Bucket sizes shouldn't affect address resolution. Resolution defaults to minimum 2 addresses per bucket, modified by scale. Results are now identical for 16, 32, and 64 bit bucket sizes, if bin buffers are allocated appropriately. Also, proper checks are in place to guarantee no buffer overwrites.
* 2004-07-02 Dan Terpstra — Set PAPI_profil bucket size to 16 as default if not set; Check for only one bucket size set; error if more; Tweak PAPI_profil parameters for greater consistency and tighter typing.
* 2004-07-02 Dan Terpstra — Remove deprecated structure fields for old mem_info descriptions; Expand descriptions of profile bucket and scaling info; Tweak PAPI_profil parameters for greater consistency and tighter typing
* 2004-07-01 Zhou Min — used a different way to reset the counter and decreased a little bit overhead on _papi_hwd_read
* 2004-06-29 Philip Mucci — Updated patch from Stephane Eranian for L2 Cache events
* 2004-06-28 Dan Terpstra — Add a new option to PAPI_get_opt() to report the complete papi version. Thanks to Rick Kufrin for the suggestion. See ctests/version.c for example usage.
* 2004-06-28 Zhou Min — added a shell script to test the example programs
* 2004-06-28 Zhou Min — rename papi_hwd_mdi_init to mdi_init and change it's type to static
* 2004-06-28 Zhou Min — example programs, tested in AIX, Linux, Solaris, IRIX
* 2004-06-22 Dan Terpstra — Convert EventSet > 100 sanity check into an assert.
* 2004-06-22 Zhou Min — removed two useless global variables
* 2004-06-22 Zhou Min — use a flexible way to define macro NUM_OF_PRESET_EVENTS
* 2004-06-18 Zhou Min — Now this program use the absolute path to find libpapi.so
* 2004-06-18 Zhou Min — moved the function from svr4.c to the substrate;
* 2004-06-18 Zhou Min — moved the function from svr4.c to the substrate
* 2004-06-18 Zhou Min — deprecated this file
* 2004-06-15 Zhou Min — added a test program for PAPI_get_overflow_event_index
* 2004-06-15 Zhou Min — added error check for empty eventset for PAPI_get_overflow_event_index
* 2004-06-15 Zhou Min — removed the static initialization for _papi_hwi_system_info; added necessary fields initialization for _papi_hwi_system_info in   function _papi_hwi_mdi_init() in papi_internal.c
* 2004-06-14 Philip Mucci — Fixed up the test cases to look like each other, since they test the same thing.
* 2004-06-14 Philip Mucci — More test fixes. cost now uses ITERS definition from test_utils.h multiplex1_pthreads now ises DO_BOTH call insteaf of braindead loops. Fixed typecast in overflow_twoevents.c
* 2004-06-14 Philip Mucci — Test files should only include papi_test.h, nothing else!
* 2004-06-14 Philip Mucci — Added a note how to easily remove directories and directory structures from CVS.
* 2004-06-14 Philip Mucci — Removed files from head fevision
* 2004-06-14 Philip Mucci — Removing files from head revision
* 2004-06-11 Dan Terpstra — For some reason, Windows doesn't like the fact that #include SUBSTRATE isn't in this file. Even though it isn't needed. It causes the next file in the compile line to fail. This change isn't needed for PAPI 3.0.3., but I didn't want to lose it.
* 2004-06-11 Dan Terpstra — A first cut at Release Notes for PAPI 3.0 beta 3. I'm sure there's more that I forgot than that I remembered, but it's a start.
* 2004-06-11 Dan Terpstra — Change log of all commits between PAPI 3.0.2 and 3.0.3
* 2004-06-10 Haihang You — missed this one too. change do_both to fdo_both
* 2004-06-10 Haihang You — missed this one. change do_flops to fdo_flops.
* 2004-06-10 Haihang You — in do_llops.c, add 'f' in front of function names of fortran wrapers. Since on aix for code is case sensitive, the new naming will differentiate C version and Fortran version.
* 2004-06-10 Haihang You — fix for aix. instead of using do_l1misses_ do_l1misses is used on aix, that caused probelm since we only pass int to do_l1misses in the C version.
* 2004-06-10 Dan Terpstra — Added code to compute cache[i].num_lines given cache[i].size and cache[i].line_size
* 2004-06-10 Dan Terpstra — Changed name of CPU_CLK_UNHALTED event for Opteron to match current documentation.
* 2004-06-10 Zhou Min — comment out the unreachable code.
* 2004-06-10 Zhou Min — removed an unused variable in PAPI_list_events function.
* 2004-06-10 Zhou Min — deprecate the shared library support until SUN fixes the bug in dladdr or we find a good way to replace dladdr.
* 2004-06-10 Zhou Min — skip the test in AIX if the program can't find the dynamic shared library.
* 2004-06-10 Dan Terpstra — Static variables in this file were examined for appropriate initialization and usage in threaded and forked situations. We have a number of such static and global variables throughout PAPI and the substrates. Each will need to be examined for correctness. When you're satisfied that a variable is initialized and used appropriately, add a comment similar to the following, so we all know it's been checked.
* 2004-06-09 Zhou Min — When the platform doesn't support multiple threads to operate the device driver, we didn't shutdown gracefully.
* 2004-06-09 Zhou Min — forgot to update the comment
* 2004-06-09 Zhou Min — skip the test in Alpha.
* 2004-06-09 Zhou Min — change the acceptable error rate from 0.1% to 0.15% so that alpha can pass the test.
* 2004-06-09 Haihang You — recently broken, minor fix to make it work on power3
* 2004-06-09 Haihang You — recently broken, minor fix to make it work on power3
* 2004-06-09 Philip Mucci — Fixes for UltraSparc. Lots of code still had #ifdefs which weren't working on the USIII.
* 2004-06-09 Philip Mucci — Bug fix  for PAPI_list_events. It was not returning the right number of events.
* 2004-06-09 Zhou Min — changed the return value for  _papi_hwd_get_real_usec so that this function will not overflow.
* 2004-06-08 Zhou Min — change the return value of _papi_hwd_get_real_usec so that it will not overflow
* 2004-06-08 Zhou Min — fix the bug caused the segfault in some test programs
* 2004-06-08 Haihang You — make it consistent with Makefile.aix5-power3
* 2004-06-08 Philip Mucci — This commit fixes the all elusive multiplexing bug. Rick Kufrin has been wrestling with this for a while, once he sent me a simple test case, boom, fixed.
* 2004-06-08 Philip Mucci — More debugging fixes. Unfortunately, I still can't find the error in overflow_SINGLE_event or overflow_two_events. We've got a memory leak somewhere that's trashing the heap I believe.
* 2004-06-08 Haihang You — initialize _papi_hwi_system_info.supports_multiple_threads
* 2004-06-08 Dan Terpstra — A couple fixes for Windows compatibility.
* 2004-06-08 Philip Mucci — Removed old references to the papi_debug variable, which has long died and could cause problems when building with -DDEBUG.
* 2004-06-08 Haihang You — add testing code to eliminate memory leak in library initialization.
* 2004-06-08 Haihang You — initialize _papi_hwi_system_info.pid in get_system_info in _papi_hwd_start, replace     if ((retval == 13) && (_papi_hwi_thread_id_fn)) with     if ((retval == 13) since in thread case, _papi_hwi_thread_id_fn should not be NULL; otherwise it is NULL and cause problem.
* 2004-06-08 Dan Terpstra — Commented out static cpuid routine, which is apparently no longer called.
* 2004-06-08 Zhou Min — man page for PAPI_get_overflow_event_index
* 2004-06-08 Zhou Min — deleted the printf statement added by me
* 2004-06-07 Zhou Min — added -xarch=v8plus option to OPTFLAGS
* 2004-06-07 Zhou Min — set _papi_hwi_system_info.supports_hw_overflow to 0 for UltraSparc 2
* 2004-06-07 Zhou Min — considered the case two counters overflow at the same time
* 2004-06-07 Zhou Min — set _papi_hwi_system_info.supports_hw_overflow to 0
* 2004-06-07 Dan Terpstra — Pentium 4 was failing about 15% of the time. I corrected it by applying an error bar of 0.1% to both computed microseconds and computed cycles. My only explanation is that the MHz value reported by the system has an accuracy no better than this.
* 2004-06-07 Zhou Min — added -DITANIUM$(CPU) to FFLAGS, now native.F can pass the test.
* 2004-06-07 Dan Terpstra — Removed reference to unused variable in the pfm 3.0 branch.
* 2004-06-07 Zhou Min — deleted the branchprofile object from the Makefile
* 2004-06-07 Zhou Min — removed this test program
* 2004-06-07 Zhou Min — add a type cast in posix_profil to avoid address overflowing
* 2004-06-07 Philip Mucci — Reverted some experimental changes that ended up in the substrate of the IA64. This broke libpfm3.
* 2004-06-05 Zhou Min — changes made to be compatible with Phil's update
* 2004-06-04 Dan Terpstra — Modifications in the version independent layer for compatibility with the new memory structure
* 2004-06-04 Zhou Min — Deleted -g option
* 2004-06-04 Zhou Min — deleted duplicated compile option for svr4.c, added -ldl to LDFLAG
* 2004-06-04 Zhou Min — forgot to delete -DDEBUG option
* 2004-06-04 Zhou Min — changed #define inline_static to static instead of __inline
* 2004-06-04 Zhou Min — added some headfiles
* 2004-06-04 Zhou Min — deleted duplicated compile option for svr4.c and added svr4.c to Makefile.irix-mips-64bit
* 2004-06-04 Haihang You — add SUBSTRATE header
* 2004-06-04 Philip Mucci — More build fixes...please make sure your header files have #ifndef _HEADER_H #define _HEADER_H ... #endif
* 2004-06-04 Philip Mucci — More build fixes brought on from the last commit. Mostly just adding recursive header file checks and proper include statements.
* 2004-06-04 Philip Mucci — svr4 target missing from numerous 64 bit target files.  (min?) inappropriate flags set for svr4, we should always build libpapi.a/so files with LIBCFLAGS and OPTFLAGS...please!
* 2004-06-04 Philip Mucci — Added standard use of NUM_ITERS in clockcore, fixed typing in tests in realtime.
* 2004-06-04 Philip Mucci — This commit makes all timers long_long, and fixes a few places where we were using u_long_long and shouldn't have. Please test your platforms. Specifically run ctests/realtime and ctests/clockres before and after the update.
* 2004-06-03 Zhou Min — Minor change to pass the compile in AIX4.3
* 2004-06-03 Zhou Min — change libm.a to libpapi.so in AIX to test our own shared library
* 2004-06-03 Zhou Min — Add this file to help to generate the shared library in AIX, the shared library tested with dlopen, fortran program and c program, works fine.
* 2004-06-03 Zhou Min — implemented _papi_hwd_update_shlib_info in AIX5 added -DNO_FUNCTION_MACRO and necessary options to generate shared library; add some headfiles in aix.h
* 2004-06-03 Zhou Min — revise the function PAPI_get_overflow_event_index based on Phil's suggestion. Tested in Itanium.
* 2004-06-03 Zhou Min — Deleted a useless include path
* 2004-06-03 Zhou Min — changed DBG to SUBDBG
* 2004-06-03 Zhou Min — delete -DHAS_NATIVE_MAP option
* 2004-06-02 Dan Terpstra — Changed a call to get_memory_info() into a call to _papi_get_memory_info() for better consistency.
* 2004-06-02 Haihang You — make power's Makefile consistent
* 2004-06-02 Zhou Min — fixed two compile warning.
* 2004-06-02 Dan Terpstra — Removed a trap for PENTIUM4 leftover from earlier development.
* 2004-06-02 Dan Terpstra — Recoded to eliminate need for PENTIUM4 define.
* 2004-06-02 Dan Terpstra — Added -DPENTIUM4 back to TOPTFLAGS
* 2004-06-02 Dan Terpstra — Changes for new static memory descriptors. Forgot to set the value in the mem_hierarchy.levels field.
* 2004-06-02 Dan Terpstra — Looks like irix needs the same __inline definition as AIX.
* 2004-06-02 Dan Terpstra — Changes for new static memory descriptors. Forgot to set the value in the mem_hierarchy.levels field.
* 2004-06-02 Dan Terpstra — Changes for new static memory descriptors. Forgot to set the value in the mem_hierarchy.levels field.
* 2004-06-02 Philip Mucci — Got it. I needed __USE_GNU as well as _GNU_SOURCE in this strange case.
* 2004-06-02 Philip Mucci — Better implementation of the ffsll GNu source handling function.
* 2004-06-02 Philip Mucci — Added -D__USE_GNU flag to get ffsll intrinsic prototype Added HAVE_FFSLL flag and ffsll inline def to papi_protos.h. Restructured and optimized PAPI_get_overflow_index function, it's almost there. Min's going to fix the rest I hope. ;-)
* 2004-06-02 Zhou Min — oops, forgot to check in this file.
* 2004-06-01 Zhou Min — change the macro value for TLB entry size
* 2004-06-01 Zhou Min — add a new function PAPI_get_overflow_event_index
* 2004-06-01 Zhou Min — add type cast to avoid compile warning information
* 2004-06-01 Dan Terpstra — Changes for new static memory descriptors. Preliminary ports for POWER, Irix, and Itanium. Successful compiles on POWER and Itanium. No verification of results. No attempt to compile on Irix. Please test and contact me with any questions.
* 2004-06-01 Dan Terpstra — Changes for new static memory descriptors. Oops. I forgot to committhese changes when I committed the new papi.h.
* 2004-06-01 Philip Mucci — Rename for Rules.pfm
* 2004-06-01 Philip Mucci — Updated the list of valid Makefiles.
* 2004-06-01 Philip Mucci — Minor fixes to the CVS-HOWTO to be clearer about imports.
* 2004-06-01 Philip Mucci — Import of perfctr 2.4.9pl2
* 2004-06-01 Philip Mucci — I don't know why this file always has conflicts on import. ARGH!
* 2004-06-01 Philip Mucci — Import of perfctr 2.6.8
* 2004-06-01 Philip Mucci — Initial revision
* 2004-06-01 Philip Mucci — Added -c99 flag to MIPSpro compiler line to support inline keyword.
* 2004-06-01 Philip Mucci — Added native_clobber target which is not used yet. All new nmakefiles should have this target. Better cleanup and install rules. Rules.perfctr and Rules.libpfm look almost the same1
* 2004-06-01 Philip Mucci — Fully updated Rules file to conform with Rules.perfctr. It works identically now as well as autodetects the kernel version and version of PFM.
* 2004-06-01 Philip Mucci — Minor fixes, deprecated old makefiles
* 2004-05-31 Philip Mucci — Added SA_RESTART to overflow signal handler flags.
* 2004-05-31 Dan Terpstra — Changes for new static memory descriptors. Implemented on Pentium III, 4, Athlon. Tested on Pentium 4. Porting to other platforms underway.
* 2004-05-28 Philip Mucci — Bumped minor version number.
* 2004-05-26 Joseph Thomas — The new/modified events in the Pentium M eventset changed the unit mask a hair and wasn't clear enough for success in the first round of updates.
* 2004-05-26 Joseph Thomas — Fixed a few typos and errors I spotted.
* 2004-05-26 Philip Mucci — -march=athlon-mp is the wrong instruction set for the k8. -march=k8 is the right one. gcc3 only.
* 2004-05-25 Joseph Thomas — Added pentium M support to the event table and gave the p3 substrate the ability to handle the new tables.  I haven't tested on a pentium M (I don't have access to one).  Haihang?
* 2004-05-25 Zhou Min — add an MDI variable supports_multiple_threads
* 2004-05-25 Zhou Min — add an MDI variable supports_multiple_threads and delete the ifdef for ALPHA/OSF  in papi.c
* 2004-05-25 Dan Terpstra — To further clarify the clock rate, I added a computed MHz report, based on the data we collect. For Pentium 4 (torc17) the clock precision between measurements is about 2 ppm, but the accuracy wrt reported MHz is about 200 ppm low.
* 2004-05-24 Dan Terpstra — Pentium 4 cycles (on torc17) are consistently low by about 4 parts per 10000. I added an error tolerance to the cycles test of 1 part per 1000 to accomodate this.
* 2004-05-24 Joseph Thomas — Added a SA_RESTART flag to the sigaction's flags in _papi_hwd_set_overflow() based on Bradley Broom's recommendation.
* 2004-05-24 Zhou Min — shift overflow_vector in the substrate rather than in extras.c
* 2004-05-21 Dan Terpstra — Modified inlining define to properly support AIX.
* 2004-05-21 Philip Mucci — Opteron install fix from Bryan O'Sullivan along with better make macros in Rules.perfctr
* 2004-05-20 Dan Terpstra — Deprecate PAPI_RES_STL until we can figure out a definition that properly counts resource stalls.
* 2004-05-20 Dan Terpstra — Remove #define for inline_static from the P4 substrate and promote it to papi_internal.h This #def is now needed in extras.c, so it has to be available above the substrate level. My bad for only testing on one platform.
* 2004-05-20 Dan Terpstra — Remove #define for inline_static from the P3 substrate and promote it to papi_internal.h This #def is now needed in extras.c, so it has to be available above the substrate level. My bad for only testing on one platform.
* 2004-05-20 Zhou Min — optimize _papi_hwi_dispatch_overflow_signal for Itanium
* 2004-05-20 Dan Terpstra — Ooops. That last commit left in a bunch of dead commented code. This version is also more completely commented.
* 2004-05-20 Dan Terpstra — Refactored profiling code to eliminate redundancies between 16, 32, and 64 bit versions. Created two inline subroutines to compute size dependent array index and increment values. Eliminated subroutine call to size dependent profiling routine. This should be easier to maintain, and (hopefully) easier to debug.
* 2004-05-19 Haihang You — use PM_DATA_FROM_L3 for L2 cache miss on power4
* 2004-05-17 Zhou Min — updated the comments
* 2004-05-17 Zhou Min — fix the profile_twoevnets bug in Itanium reported by Nathan Tallent
* 2004-05-17 Philip Mucci — Added better test case for overflow_twoevents.
* 2004-05-17 Philip Mucci — Much better test case for profile_twoevents.c
* 2004-05-14 Zhou Min — implemented _papi_hwd_update_shlib_info function in IRIX, the result was verified by dbx.
* 2004-05-14 Joseph Thomas — PERFCTR_X86_INTEL_P4M3 was not defined in perfctr-2.4.x, so I #ifdef'ed its usage in setup_presets().
* 2004-05-13 Dan Terpstra — Add stub routines to support all four namespace variations as found in papi_fwrappers and the perfometer api.
* 2004-05-13 Dan Terpstra — Rework Fortran project files to support replacement of dummy.F and do_loops.F with equivalent C functionality.
* 2004-05-13 Dan Terpstra — Typecast some parameters so VS.NET won't flag warnings about them.
* 2004-05-13 Dan Terpstra — Remove DESCRIPTION line (not supported in VS.NET); Deprecate dmem_info ref, since it's been deprecated in papi.c
* 2004-05-13 Dan Terpstra — Update directory tree for latest install of ddkbuild
* 2004-05-13 Dan Terpstra — Added support for Pentium M to two more switch statements.
* 2004-05-13 Dan Terpstra — Added support for Pentium M to Windows branch.
* 2004-05-13 Zhou Min — fix the bug reported by broom@rice.edu bug: s_profile maps all hits onto first section of     large profiling region
* 2004-05-11 Joseph Thomas — The duplicate preset event was actually an 8 month old typo with the incorrect preset label.  L1 store misses was mislabeled as a duplicate L1 load misses.
* 2004-05-11 Dan Terpstra — Removed duplicate definitions of PAPI_L1_LDM event.
* 2004-05-11 Dan Terpstra — Minor updates for PAPI 3 release.
* 2004-05-11 Zhou Min — fix a compile error(not introduced by me)
* 2004-05-11 Philip Mucci — Wow. This was an ugly bug. The return was in the wrong place for the error_return macros. The result? If we didn't have internal debugging set, the code would never return.
* 2004-05-10 Philip Mucci — Now skipped test case according to temporary deprecation of dmem info.
* 2004-05-10 Philip Mucci — Added sample structure definitions for memory heir. defs and for PAPI_event_info_t as suggested by Dan. These are guarded by
* 2004-05-07 Philip Mucci — These changes may be lost due to impending commits.
* 2004-05-06 Philip Mucci — If we are building from a preinstalled PerfCtr (via PERFCTR_PREFIX=<> on the make line) then we do not want to run install in the perfctr directory. That would overwrite the installed perfctr. Yikes.
* 2004-05-06 Philip Mucci — Hi,
* 2004-05-05 Joseph Thomas — Bug fixes in response to Phil's recent changes.  -fPIC appears to be necessary for the opteron to work and until I know otherwise, -fPIC needs to remain.
* 2004-05-05 Zhou Min — add -DNO_VARARG_MACRO to cflag
* 2004-05-04 Joseph Thomas — In the case of a clean checkout, perfctr soft link for some reason does not create itself, so our Makefile did the dirty work.  For some reason, this code was removed and not tested afterwards, unless I am misunderstanding something about the new make method.
* 2004-05-04 Dan Terpstra — Documentation no longer relevant. Go to the web for the latest.
* 2004-05-04 Dan Terpstra — Latest batch file for building kernel drivers from within Visual Studio.
* 2004-05-04 Dan Terpstra — Updated documentation for Visual Studio.NET and for the latest ddkbuild.bat file.
* 2004-05-04 Philip Mucci — Updated CVS HOWTO instructions and INSTALL.txt
* 2004-05-04 Philip Mucci — Restored deleted file
* 2004-05-04 Philip Mucci — Somehow this got locally modified.
* 2004-05-04 Philip Mucci — Imported version 2.6.7
* 2004-05-04 Philip Mucci — Initial revision
* 2004-05-03 Philip Mucci — Added corrections that reflect the addition of the PERFCTR_PREFIX flag
* 2004-05-03 Philip Mucci — Ok, now we have one Rules.perfctr that works for all versions of PerfCtr.
* 2004-05-01 Joseph Thomas — The high number of NUM_READS was causing the pentium 3 to fail on profiling tests.  Reduced it to 20000 instead of 2000000. *This was only a problem on the pentium3*
* 2004-04-30 Philip Mucci — Added realtime test case. My laptop religiously fails this test. I don't know if it's speedstep or what. But it passes on normal systems.
* 2004-04-30 Philip Mucci — Removed trailing period from native event definitions. Added comment to PAPI_event_info_t field in papi.h
* 2004-04-29 Philip Mucci — A big commit. This patch changes the old NATIVE_MASK and PRESET_MASK to PAPI_NATIVE_MASK and PAPI_PRESET_MASK etc... Unfortunately, these were used everywhere.
* 2004-04-28 Philip Mucci — This fixes a bug in the filling in of the vendor fields. It showed up when you forked a code that used the shared library and each called PAPI_get_event_info. Ah, papiex exposes yet another subtle bug.
* 2004-04-26 Zhou Min — add some example programs
* 2004-04-23 Philip Mucci — Count only PACKED SSE/SSE2 instructions for PAPI_VEC_INS on the Opteron. test case coming soon...
* 2004-04-23 Philip Mucci — Changed debugging statement when master thread is initialized to dump PID and old PID if there is one.
* 2004-04-23 Philip Mucci — Added fortran bindings do dummy and do_loops. Added MAX_TO_ADD variable in test_utils.h and updated that in the other tests.
* 2004-04-23 Philip Mucci — Now using the do_loops and dummy from the C tests for synchronicity. Removes test failures.
* 2004-04-20 Joseph Thomas — Update of _papi_hwd_read() to a better guess.  The t3e is still awaiting testing.
* 2004-04-19 Zhou Min — add some example programs
* 2004-04-14 Dan Terpstra — Added parentheses to #defines to guarantee proper precedence during preprocessing. This makes the weird errors noticed yesterday disappear. Thanks, Joe!
* 2004-04-13 Philip Mucci — More optimization safety.
* 2004-04-13 Philip Mucci — Added headers as dependencies
* 2004-04-13 Philip Mucci — Standardized tolerance of .2. Added prototype for dummy(void *)
* 2004-04-13 Philip Mucci — Added some debugging statements showing relative percentages of repeat measurements.
* 2004-04-13 Philip Mucci — Made the same tolerance as C version. += 20%
* 2004-04-13 Dan Terpstra — OK. So I'm stubborn and belligerent. I didn't want to give up the enum table of events, in spite of the fact that negative enums are not defined by ANSI. I converted the enum table into an index table of positive zero-based values. Then I mapped those values onto event definitions by or-ing in the PRESET_MASK bit. This way we can still maintain (and rearrange) events in the enum table, and the defines remain valid. Phil - didn't you want to rearrange the presets for PAPI_enum_events() to report events by category?
* 2004-04-12 Joseph Thomas — Very preliminary port of the t3e substrate.  Not tested whatsoever.  _papi_hwd_read, _papi_hwd_set_overflow _papi_hwd_get_system_info and _papi_hwd_get_memory_info still need attention.  The rest of the functions are merely good guesses until I can test.
* 2004-04-12 Zhou Min — add some example programs.
* 2004-04-12 london — Readding the Papi_add_env_event example, this one works with PAPI 3.0 Please be careful will removing files.
* 2004-04-12 Zhou Min — This can't be use with PAPI3.0
* 2004-04-12 Zhou Min — add some example programs to show how to use PAPI3.0 functions
* 2004-04-12 Zhou Min — minor adjustment
* 2004-04-12 Zhou Min — man page update
* 2004-04-10 Philip Mucci — Added library preloading information.
* 2004-04-10 Philip Mucci — Fixed problem with get_hardware_info call. It was called before PAPI_library_init. Joe?
* 2004-04-10 Philip Mucci — Fixed Opteron Branch preset. Inlined counter_read call and added a check for negative numbers from handle_derived
* 2004-04-08 Dan Terpstra — Changes to promote the modifiers for PAPI_enum_event to the user interface level (papi.h) for presets and substrates. I forgot to check these in earlier...
* 2004-04-08 Dan Terpstra — Updates for the PAPI 3 Matlab stuff.
* 2004-04-08 Dan Terpstra — Updates for the PAPI 3 installer. The papi_matlab page still needs a rewrite.
* 2004-04-07 Dan Terpstra — General refresh of all these files.
* 2004-04-07 Dan Terpstra — Documentation updates for PAPI 3 beta 2.
* 2004-04-07 Dan Terpstra — Comment out context switch hook. For some reason this causes the driver to fail for Win XP.
* 2004-04-07 Dan Terpstra — Changes to properly identify Pentium 4, so we can fail gracefully in Windows.
* 2004-04-07 Dan Terpstra — More robust display of versioning for PAPI and the WinPMC driver.
* 2004-04-06 Dan Terpstra — Changes to support Pentium 4
* 2004-04-06 Haihang You — add preset PAPI_L2_DCM implementation.
* 2004-03-31 Dan Terpstra — After much wailing and gnashing of teeth, the PAPI Users Guide has finally been updated for PAPI 3.
* 2004-03-31 Philip Mucci — New test case. I found bugs in PAPI/fork() with papiex on apps that fork. This test case I should have written a long time ago. This test does the following:
* 2004-03-31 Philip Mucci — New install rule, uses make install in perfctr directory.
* 2004-03-29 Zhou Min — change the return error check condition after dlsym() function call.
* 2004-03-29 Zhou Min — comment out the dlerror check in Solaris
* 2004-03-29 Zhou Min — comment out the printf statement
* 2004-03-26 Zhou Min — ease the check condition for data segment address
* 2004-03-26 Zhou Min — 1. added an running_eventset field in the thread structure, so that the    user will get an error message when he call PAPI_start another event    set without stop the current running eventset;
* 2004-03-26 Joseph Thomas — Replaced some more overwritten changes.
* 2004-03-26 Joseph Thomas — Fixed a seg fault due to an overwrite of an old fix - from version 1.220:
* 2004-03-23 Joseph Thomas — Fixed a boundary condition bug showing up in native_avail and probably other places for the x86 substrates.  While fixing the bug I removed several variables related to native table size.
* 2004-03-22 Philip Mucci — Windows ifdef
* 2004-03-22 Philip Mucci — Added getpid() code to initialization path to detect people that have forked() and want to reinitialize. Added extern statements to end of papi_internal.h.
* 2004-03-22 Dan Terpstra — Changes to promote the modifiers for PAPI_enum_event to the user interface level (papi.h) for presets and substrates.
* 2004-03-22 Dan Terpstra — Changes to promote the modifiers for PAPI_enum_event to the user interface level (papi.h) for presets and substrates. Preset modifiers aren't implemented yet. If you add modifier values to a substrate, add values to the enum in papi.h. Currently supported on Pentium4, POWER4; tested on Pentium4.
* 2004-03-17 london — Fix for another install problem on Solaris
* 2004-03-15 Zhou Min — man page update
* 2004-03-12 Zhou Min — man page update
* 2004-03-12 Dan Terpstra — Minor correction caught by Felix.
* 2004-03-11 Zhou Min — man page update
* 2004-03-11 london — Changes to the install directory structure to stop: installing to:  PREFIX/share/papi/share/papi/ctests
* 2004-03-11 london — Fixes so install works correctly
* 2004-03-11 london — Changed DESTDIR to PREFIX
* 2004-03-11 london — Breaks install, was DESTDIR, needed to be PREFIX
* 2004-03-11 Zhou Min — Now in tru64-alpha shlib skips the test and exeinfo can pass the test
* 2004-03-10 Zhou Min — fix the compile warning information
* 2004-03-10 Zhou Min — man page update
* 2004-03-10 london — Fix so Irix will compile with 64 bit and got rid of some warnings.
* 2004-03-10 Haihang You — fix the errors.
* 2004-03-10 Dan Terpstra — Extraneous imports.
* 2004-03-10 Dan Terpstra — Extraneous imports.
* 2004-03-10 Zhou Min — importing libpfm-3.0
* 2004-03-10 Zhou Min — Initial revision
* 2004-03-10 Dan Terpstra — Initial revision
* 2004-03-10 Dan Terpstra — At the last minute I had a conversion experience and decided to make the minor revision number track the beta release. This is now PAPI 3.0.2.
* 2004-03-10 Joseph Thomas — Replaced some lines I had removed in an earlier revision.
* 2004-03-09 Dan Terpstra — Added parsing of /proc/pal/cpu0/vm_info file to determine TLB characteristics.
* 2004-03-09 london — do_flops would crash alpha when quiet was set, changed a,b to not be commons and initialized all the variables to fix this.
* 2004-03-09 Joseph Thomas — The third test on the opteron was failing.  I bumped up (down?) the failure threshold (the absolute difference, not the percentage error) just a bit.
* 2004-03-09 Zhou Min — man page update
* 2004-03-09 Zhou Min — fix the compile error.
* 2004-03-09 Zhou Min — Specification document for PAPI3.0
* 2004-03-09 Dan Terpstra — Removing these files from the Windows directory. Cross-platform versions now exist in the src directory.
* 2004-03-09 Joseph Thomas — Left the hardcoded version in the include line instead of the VERSION variable.
* 2004-03-08 Joseph Thomas — User can now specify older perfctr version on the command line instead of being forced to change the makefile.
* 2004-03-08 Zhou Min — Deleted outdated information
* 2004-03-07 Joseph Thomas — Brought the p4 into the new makefile scheme.  Had to create a CPU make variable to identify which files compile.
* 2004-03-06 Zhou Min — forgot to remove the -DDEBUG option
* 2004-03-06 Zhou Min — 1. fix the compile error in tru64-alpha; 2. set data segment address for dadd-alpha; 3. return PAPI_ESBST for shlib in solaris;
* 2004-03-06 london — Ooops, forgot to pull my debugging statements
* 2004-03-05 Philip Mucci — Added 64bit solaris, renamed 64 bit MIPS, removed -g -DDEBUG, other fixes. Updated targets in Makefile. Linux makefiles now refer to Rules files.
* 2004-03-05 london — Thanks to Stephane we have L1,L2 and L3 memory information.  I will add the TLB stuff shortly.
* 2004-03-05 Haihang You — Makefile for 64bit library on aix5 and power3 combination
* 2004-03-05 Philip Mucci — Corrected handling of name field in exe info. No longer do we use getcwd(). That could be broken, now we rely exclusively on /proc and the behavior of the realpath() system call. Note that I have changed PATH definitions to use PAPI_HUGE_STR_LEN to fix the problems we've seen at LANL with long pathnames.
* 2004-03-05 Haihang You — add -qenum=4 flag
* 2004-03-05 Zhou Min — let shlib to skip rather than fail for non-linux platforms. It will be fixed once we know how to get the right name from  /proc/id/objects/
* 2004-03-05 Philip Mucci — Added better model checking and error messages. Suggested by Jack Purdue. tested on P3/P4.
* 2004-03-05 Philip Mucci — Correction from Jack Purdue. j-perdue@tamu.edu. We had hardcoded the number of events in the eventset...bad bad idea.
* 2004-03-05 Zhou Min — Restructure makefile for itanium/itanium2
* 2004-03-05 Zhou Min — restruture of Makefile for itanium/itanium2
* 2004-03-05 Joseph Thomas — New common makefiles and a makefile for the athlon.  We seem split on whether or not to add this, so we might want to remove it.
* 2004-03-05 Joseph Thomas — Removed common code which is now in Makefile.perfctr-2.6.x and Makefile.perfctr-2.4.x.
* 2004-03-04 Zhou Min — set value for exe_info.address_info.name
* 2004-03-04 Haihang You — add _text
* 2004-03-04 Haihang You — remove _P64 flag
* 2004-03-04 Haihang You — assign right value to shlib_info.
* 2004-03-04 london — Fixed type, fulltest is used to run all the tests, not test.
* 2004-03-04 Philip Mucci — Removed those UGLY ^M's from Windoze.
* 2004-03-03 Haihang You — minor fix to use new defined structure _papi_program_info
* 2004-03-03 Zhou Min — set value for exe_info.address_info.name, now exeinfo can pass the test in solaris
* 2004-03-03 Joseph Thomas — Changed a #ifdef(__ATHLON__) to #ifdef(__athlon__)
* 2004-03-03 Dan Terpstra — Not sure exactly what changed, but I don't want to lose it...
* 2004-03-03 Dan Terpstra — Changes to the Visual Studio projects to reflect Phil's changes in the way Fortran programs are built.
* 2004-03-03 Dan Terpstra — Removed /D PENTIUM3 tag (no longer needed).
* 2004-03-03 Dan Terpstra — Changes to abstract hardware overflow support, since linux supports it and Windows (currently) does not.
* 2004-03-03 Dan Terpstra — Removed the C-style comment at the top of this file. Since it's being used for both C and Fortran now, some Fortran preprocessors (e.g. Compaq on Windows) can't cope with C comment syntax.
* 2004-03-03 Dan Terpstra — Eliminated a casting warning in Windows.
* 2004-03-03 Dan Terpstra — Index fix found by Jack Perdue. Thanks!
* 2004-03-03 Nils Smeds — Joseph,
* 2004-03-02 Zhou Min — deleted outdated stuff
* 2004-03-02 Zhou Min — with Per Ekman's help, added five PAPI preset events in itanium2    {PAPI_L2_ICA, 0, {"L2_INST_DEMAND_READS", 0, 0, 0}},    {PAPI_L3_ICA, 0, {"L3_READS_INST_FETCH_ALL", 0, 0, 0}},    {PAPI_L1_TCR, DERIVED_ADD, {"L1D_READS_SET0", "L1I_READS", 0, 0}},    {PAPI_L1_TCA, DERIVED_ADD, {"L1D_READS_SET0", "L1I_READS", 0, 0}},    {PAPI_L2_TCW, 0, {"L2_DATA_REFERENCES_L2_DATA_WRITES", 0, 0, 0}}, changed the definition for PAPI_L2_DCM in itanium2; deleted PAPI_MEM_SCY from itanium2's preset table;
* 2004-03-02 london — First run on adding memory info to itanium.  Currently this is very limited, I have code to determine Model, Family, Stepping and Arch Revision, but not the cache info. This is being hardcoded, and so far all I have is L1 Cache size on Itanium I and II and the L2 cache size on the Itanium II.  Feel free to fill in the rest if you find documentation to support it.
* 2004-03-02 Philip Mucci — Changed definitions to be lower. This is due to no more replicated definitions all over the Fortran tests. do_loops.F will complete in less than a year now.
* 2004-03-02 Philip Mucci — Working do_reads now. Fortran doesn't like reading from /dev/zero so we make a temporary file.
* 2004-03-02 Dan Terpstra — Fixes to get rid of compiler warnings. Warnings just distract from real problems. They bug me almost as much as duplicate code bugs Phil. ;)
* 2004-03-02 Philip Mucci — Removed the ?= operator in the Makefile. Non-GNU makes choke on this.
* 2004-03-02 Dan Terpstra — Fixes in Windows for Phil's recent changes.
* 2004-03-02 Philip Mucci — Added -O back into TOPTFLAGS. Added proper PMTOOLKIT define for power3.c
* 2004-03-02 Philip Mucci — Fixed broken do_reads. Added TOPTFLAGS to do_loops compile.
* 2004-03-02 Philip Mucci — Oh how I love duplicated code! No more Fortran defs...they all come from test_utils.h
* 2004-03-01 Philip Mucci — Added SA_RESTART to multiplex.c. This MIGHT be the culprit of some of the problems on AIX and the installation at NCSA. Unfortunately, this flag does not help MPICH with shared memory. On Linux, semop()'s are never restarted by the OS.
* 2004-03-01 Dan Terpstra — Minor tweaks
* 2004-02-28 Philip Mucci — All output goes to stdout, not mixed stderr,stdout.
* 2004-02-28 Dan Terpstra — Project files for Windows Visual Studio, and source file for PAPI FLOPS function.
* 2004-02-28 Dan Terpstra — Updates to m file documentation and addition of a bunch of m file example code. Also some fixes to the PAPI_Matlab stuff to make it work with PAPI 3.
* 2004-02-27 Philip Mucci — Added much better install instructions. It's about time huh?
* 2004-02-27 Philip Mucci — Added new targets to Makefile, edited test targets in Makefile.inc
* 2004-02-27 Dan Terpstra — Fix for rate calculation in hl_rate_calls to properly handle both flips and flops
* 2004-02-27 Philip Mucci — Renamed DESTDIR to PREFIX, which is much more consistent to autoconf like configurations. bins go to PREFIX/bin, libs to PREFIX/lib, includes to PREFIX/include [cf]tests to PREFIX/share/papi/[cf]tests. Updated INSTALL.txt to reflect this.
* 2004-02-27 Philip Mucci — PAPI_TOT_CYC was wrong on Opteron. Fixed it. Someone had defined it as instructions.
* 2004-02-26 Philip Mucci — Added test target that I missed. Fixed use of abs in test case.
* 2004-02-26 Philip Mucci — Aha! gcc warned me about not having braces. This was the first time I've seen it affect code. Now prints events again.
* 2004-02-26 Philip Mucci — Removed old test targets from makefile.
* 2004-02-26 Zhou Min — added POSTFIX  support in Itanium/Itanium2
* 2004-02-26 Zhou Min — minor change due to the update of PAPI_exe_info_t
* 2004-02-26 Zhou Min — restructure Makefile for Itanium/Itanium2
* 2004-02-26 Zhou Min — 1. Based on Phil's update, now itanium also calls the functions in linux.c 2. delte preload stuff in  dadd-alpha.c
* 2004-02-26 Zhou Min — I have to disable the warning information in dadd-alpha because   the definition in papiStdEventDefs.h
* 2004-02-26 Philip Mucci — get_shlib info almost working...Min can you help? This also uses linux.c!
* 2004-02-26 Philip Mucci — Fixed broken memset statements. memset(where,what,size)
* 2004-02-26 Philip Mucci — Added proper targets for linux.o and miscellaneous objects.
* 2004-02-26 Philip Mucci — Renamed memory function to be like other substrates. Added ctype.h to header file
* 2004-02-26 Philip Mucci — More code...made functions look identical to perfctr-p4.c, moved ctl call to this substrate out of linux.c
* 2004-02-26 Philip Mucci — More shlib updates. Should work on itanium...working to fix it now. Also, moved _ctl() call to substrate. Not a linux issue...
* 2004-02-25 Philip Mucci — Removed define of NUM_FLOPS.
* 2004-02-25 Philip Mucci — Added a real do_loops function JUST LIKE ctests. Made a real include file, edited make targets.
* 2004-02-25 Philip Mucci — Please dont build dummy or do_loops with optimization!
* 2004-02-25 Philip Mucci — Removed referneces to preload.
* 2004-02-25 Philip Mucci — Added this to INSTALL file. Also a note about the need for rebuilding PAPI after you install a new perfctr. Why? Because PAPI depends on the objects in the .a file!
* 2004-02-25 Philip Mucci — Added a real PAPI_get_execuable_info test case.
* 2004-02-25 Philip Mucci — Fixed update_shlib on Linux. All libraries are reported properly.
* 2004-02-25 Philip Mucci — Removed cp of README files to share directory.
* 2004-02-23 Philip Mucci — Install target fixes.
* 2004-02-20 Philip Mucci — Fixed broken makefile.
* 2004-02-20 Philip Mucci — Changed order of print statements. Currently this test is bombing due to a horribly broken implementation of shared_lib_info. But hey, I just found that from the test case!
* 2004-02-20 Philip Mucci — New define in papi_test.h
* 2004-02-20 Philip Mucci — Edited the function name handling again. There is a better one than __FUNCTION__ which is the GNU standard. C99 defined __func__ as the CPP keyword of choice.
* 2004-02-20 Zhou Min — 1. change the papi event definition PAPI_L2_DCM in itanium2 from     {PAPI_L2_DCM, 0, {"L3_READS_DATA_READ_ALL", 0, 0, 0}}    to     {PAPI_L2_DCM, DERIVED_SUB, {"L2_MISSES", "L3_READS_INST_FETCH_ALL", 0, 0}}
* 2004-02-19 Zhou Min — fix the bug in profile(not sprofile) P3 and P4 introduced by me yesterday
* 2004-02-18 Zhou Min — fix a typo and the bug in PAPI_sprofil
* 2004-02-16 Dan Terpstra — Updates for PAPI 3 on Windows
* 2004-02-13 Zhou Min — minor change in profile support, so that if the user don't want to use hardware profile support in Itanium, then the profile based on hardware overflow support also works.
* 2004-02-13 Philip Mucci — Revised macros, added __FUNCTION__ back in where appropriate. use of __FUNCTION__ in non-supported platforms should return the label "unknown" now.
* 2004-02-11 Zhou Min — Now read the text start address and end address from /proc/processid/maps, profile should work now.
* 2004-02-11 Joseph Thomas — Changed some compiler options.  Profiling didn't work with the bad options.
* 2004-02-11 Joseph Thomas — Some perfctr25 flags remained to updated.  Fixed.
* 2004-02-10 Philip Mucci — Initial revision
* 2004-02-10 Dan Terpstra — Cleanup in an attempt to get it working in Windows. It doesn't.
* 2004-02-10 Dan Terpstra — Tweak for Windows
* 2004-02-10 Dan Terpstra — Fix to prevent overwriting of values in pebs_enable and pebs_matrix_vert. The unfortunate implication of this fix is that multiple unique replay_events cannot be counted in the same eventset. If you look at the event definitions, this includes (excludes) L1 and L2 cache events.
* 2004-02-09 Dan Terpstra — Minor tweaks: Windows needs all caps for FORTRAN; one of the APIs was misdefined.
* 2004-02-09 london — Fixed compilation problem
* 2004-02-09 Zhou Min — 1. update in user overflow handler upon request from Sun Corp, we add one    more parameter, the context structure pointer, to the handler interface;
* 2004-02-09 Zhou Min — 1. check in Larry Meadow's update in solaris-ultra.c, now PAPI3 support    UltraSparc 3+;
* 2004-02-06 Dan Terpstra — Fixes to both Opteron and PIII make files to build a clean perfctr from scratch
* 2004-02-06 Dan Terpstra — Adding a bunch of new Visual Studio projects for test cases for Windows/PAPI3
* 2004-02-06 Dan Terpstra — Forgot to add x86.o to the perfctr object file dependencies. And this revision DOES break on 2.6.{0,1,2,3}.
* 2004-02-06 Dan Terpstra — Fixed the MISCOBJS tag to include x86.o for perfctr-2.6.4+ Unfortunately, this may now break on 2.6.{0,1,2,3}
* 2004-02-06 Joseph Thomas — Changed a -DPERFCTR25 to a -DPERFCTR26.
* 2004-02-06 Joseph Thomas — Updated a #ifdef PERFCTR25 to #ifdef PERFCTR26
* 2004-02-05 Joseph Thomas — Forgot to remove the -fPIC flag.
* 2004-02-05 Joseph Thomas — A seperate makefile for the opteron.  This removes any reliance on the user adding and subtracting the -fPIC flag and -D__x86_64__ definition flag.
* 2004-02-05 Joseph Thomas — Removed opteron support from this file.  Users don't have to mess with flags and we will hopefully have to hold fewer hands. There is now a seperate opteron makefile with a -fPIC flag.
* 2004-02-05 Dan Terpstra — Minor tweaks for Linux.
* 2004-02-05 Dan Terpstra — Another round of changes for Windows. All Windows appropriate tests now work except multiplex1. This code has been tested on Linux PIII with perfctr 2.4.x.
* 2004-02-04 Dan Terpstra — Another round of changes for Windows. All Windows appropriate tests now work except multiplex1. This code should also still run on Linux and other platforms, but it hasn't been tested yet. Caveat Emptor. I'll be testing PIII Linux tomorrow.
* 2004-02-04 Dan Terpstra — Another round of changes for Windows. All Windows appropriate tests now work except multiplex1. This code should also still run on Linux and other platforms, but it hasn't been tested yet. Caveat Emptor. I'll be testing PIII Linux tomorrow.
* 2004-02-04 Zhou Min — Bug fix for domain error in itanium platform for libpfm-3.0
* 2004-02-02 Zhou Min — support for libpfm-3.0
* 2004-02-02 Zhou Min — 1. papi3.0 support DADD-alpha now; 2. added support for libpfm-3.0(not totally finished); 3. makefile change in Solaris, will support UltraSparc 3+ soon;
* 2004-01-20 Dan Terpstra — Added Walt Travis's boolean logic fixes for the allocation stuff. Removed __FUNCTION__ macro, which is only guaranteed under gcc.
* 2004-01-20 Dan Terpstra — First cut changes to compile under Windows; Resolved some minor data typing issues; Removed __FUNCTION__ macro, which is only guaranteed under gcc.
* 2004-01-16 Dan Terpstra — First cut changes to compile under Windows.
* 2004-01-16 Dan Terpstra — First cut changes to compile under Windows; Removal of __FUNCTION__ macro, which is only guaranteed under gcc.
* 2004-01-15 Joseph Thomas — Removed #ifdef __ATHLON__
* 2004-01-15 Joseph Thomas — Removed #ifdefs concerning machine type.
* 2004-01-15 Joseph Thomas — Removed #ifdef's.
* 2004-01-15 Joseph Thomas — Removed #ifdef MACHINE_TYPE.
* 2004-01-15 Joseph Thomas — Removed #ifdef __ATHLON__
* 2004-01-14 Joseph Thomas — Attempt at removing dependence on #ifdef PENTIUM3 and #ifdef __ATHLON__. I think it's a little ugly, but it's a first swipe.  Let me know if I trampled another substrate.  I will attempt to remove the #ifdef __x86_64__ dependence next.
* 2003-12-21 Philip Mucci — Bug fix for add events....number must be > 0
* 2003-12-18 Dan Terpstra — Minor changes to support perfctr 2.6.x on Pentium 4. Compiles and links, but hasn't been tested locally. Thanks to Ward Travis for submitting and testing these changes.
* 2003-12-18 Dan Terpstra — Updated procedures and bat files for producing the PAPI Programmer's Reference documents (man pages) for PAPI 3. These documents are now posted to the web page in html, doc, pdf, and ps formats.
* 2003-12-18 Dan Terpstra — Rearranged order of SERIAL test files. This order works better for PAPIvi.
* 2003-12-15 Dan Terpstra — PAPI Conversion Cookbook documents a stepwise conversion from PAPI 2 to PAPI 3. 6 pages on converting 2 to 3; 2 pages on converting to PAPI version independent code.
* 2003-12-15 Dan Terpstra — First version of a PAPI version independent header file. This replaces 'papi.h' in user code and allows mostly transparent linking to either PAPI 2 or PAPI 3 libraries. Requires initial conversion to PAPI 3, and then syntax changes to avoid name collisions. See the PAPI Conversion Cookbook in the doc directory for more details.
* 2003-12-11 london — Changes so hopefully you can also compile with a native libpfm that comes with the Altix.  It appears our Altix installation is not complete as it is missing pfmlib_compiler.h which is included by pfmlib.h but is not there.
* 2003-12-10 london — When a negative time is seen, then we abort but print out no message as to why.  Added a message.  Now the question would seem to be, why Altix occasionally has negative elapsed time.
* 2003-12-10 london — The lock/unlocks to the thread list has to be added even though we are just looking up on a circular linked-list, I believe these can still be safely removed, and will look at it closer, but for now I am reinserting the locking mechanisms since this was causing problems on Altix.
* 2003-12-09 Dan Terpstra — Fixed a nasty bug in _papi_hwd_bpt_map_preempt() that was causing counters to share ESCRs when they shouldn't. This fixes Chee Wai's bug with PAPI_L1_DCM and PAPI_FP_INS.
* 2003-12-09 Dan Terpstra — Commented out PAPI_L1_DCA from mge2 event table because it won't work on some (all?) Xeons. As reported by Jon Burgoyne, 12/05/03.
* 2003-12-05 Joseph Thomas — Removed the _papi_hwd_ctl() from the PAPI_DEFDOM case in PAPI_set_opt. This removes a bug that will either result in a seg fault or papi error when trying to set the default domain.  I'm not sure if this is the proper fix, but it does remove the bug.  The thinking is that if you want to change the default domain, then you don't want to change the current eventset's domain.  If you want to change the current eventset's domain, you would use PAPI_DOMAIN instead of PAPI_DEFDOM. So, _papi_hwd_ctl is not needed.
* 2003-12-05 Joseph Thomas — Removed #ifdefs dealing with substrates.
* 2003-12-04 Haihang You — add new preset entries for power4:   PAPI_LD_INS :  PM_LD_REF_L1   PAPI_LSR_INS :  PM_ST_REF_L1   PAPI_LST_INS :  PM_LD_REF_L1 + PM_ST_REF_L1
* 2003-12-03 Joseph Thomas — Removed #ifdefs concerning any substrates.
* 2003-12-03 Joseph Thomas — Added a case in _papi_hwd_ctl() to recognize PAPI_DEFDOM.
* 2003-12-02 Haihang You — on power3 hw_info->model_string is a string contains 'POWER3'. change !strcomp to strstr.
* 2003-12-02 Joseph Thomas — Removed #ifdefs concerned with substrates.
* 2003-12-02 Joseph Thomas — Removed #ifdefs concerning substrate.
* 2003-12-02 Haihang You — on power3 hw_info->model_string is a string contains 'POWER3'. change !strcomp to strstr.
* 2003-12-02 Zhou Min — change the parameters of _papi_hwi_dummy_handler
* 2003-12-02 Joseph Thomas — Removed #ifdefs concerning substrates.
* 2003-12-02 Joseph Thomas — Removed #ifdefs concerning substrates.
* 2003-12-02 Joseph Thomas — Removed #ifdefs concerning the substrate.
* 2003-12-01 Haihang You — change 'power4' to 'POWER4' in model comparison. This will fix the error Rick reported seen from multiplex1_pthreads.
* 2003-12-01 Haihang You — add -qenum=4
* 2003-12-01 Haihang You — get rid of an extra ','
* 2003-12-01 Haihang You — add -qenum=4 to fix enum conflict
* 2003-11-24 Philip Mucci — Removed __data_start declaration
* 2003-11-24 Zhou Min — Change the event name used in Solaris, now it can pass the test instead of skipping the test.
* 2003-11-24 Joseph Thomas — Removed a debugging printf statement and a redundant line of code.
* 2003-11-23 Joseph Thomas — Removed all #ifdefs that referred to a specific substrate.  I don't have access to a power4 so haihang should test on the power4.  Also, I wasn't satisfied with my results on sparc, so min should test too.  If no other problems are found, I'll start removing the #ifdefs elsewhere.
* 2003-11-23 Zhou Min — In Irix, when the user add or remove an event after he has already called PAPI_overflow, divide the user threshold by the number of events in count 0 or count 1, depends on which counter the overflow event is counted by.
* 2003-11-23 Dan Terpstra — Update the html files changed by Min.
* 2003-11-22 Zhou Min — commit the change made by Nils in papi-2-3-4
* 2003-11-22 Zhou Min — man page update
* 2003-11-22 Dan Terpstra — Update all the html files before copying to the website.
* 2003-11-22 Dan Terpstra — Minor tweak. Still conforms to the old definition. We need to decide what to do about the new debug interface.
* 2003-11-22 Dan Terpstra — Replaced the event #defines with an enum struct as suggested by Kevin. This should simplify maintenance of the table. Tested on Pentium 4
* 2003-11-22 Zhou Min — an syntax error made by me
* 2003-11-22 Zhou Min — change an return error in UltraSparc from PAPI_ESYS to PAPI_ESBSTR
* 2003-11-22 london — Changes to support new variables, and moved a couple of defines in papi.h so it didn't break-up the logic.
* 2003-11-21 Zhou Min — use PAPI_TOT_CYC instead of PAPI_FP_INS in UltraSparc
* 2003-11-21 Zhou Min — change the native event name in UltraSparc
* 2003-11-21 Zhou Min — add PAPI_TOT_CYC and PAPI_TOT_INS into the eventset instead of     PAPI_FP_INS  and PAPI_TOT_CYC into the eventset  when platform is     UltraSparc
* 2003-11-21 Zhou Min — 1. change first.c so that only PAPI_TOT_CYC and PAPI_TOT_INS are    added in Solaris;
* 2003-11-21 Zhou Min — 1. when platform is alpha, add _papi_hwd_shutdown in PAPI_shutdown function    to fix the error returned in PAPI_thread_init; 2. add PAPIf_name_to_code support in tru64-alpha
* 2003-11-21 london — Changed do_flops to call do_dummy and changed a few things around to make sure and trick the compiler
* 2003-11-21 Dan Terpstra — Updates for PAPI 3.
* 2003-11-21 Dan Terpstra — Removed an unused parameter (flag) from the PAPI_thread_init call. I did it to simplify things since now seemed to be the time. After I did, I noticed that the documentation said it was reserved for future use. Since it's been there since before 2.0 and hasn't been used, I figure this is bogus. But I'm probably wroing... No guts, no glory.
* 2003-11-21 Dan Terpstra — Removed an unused parameter (flag) from the PAPI_thread_init call. I did it to simplify things since now seemed to be the time. After I did, I noticed that the documentation said it was reserved for future use. Since it's been there since before 2.0 and hasn't been used, I figure this is bogus. But I'm probably wroing...
* 2003-11-21 Dan Terpstra — Updates for PAPI 3.
* 2003-11-21 Philip Mucci — _data_start causes a number of problems for people when PAPI is built as a shared library.
* 2003-11-21 Dan Terpstra — Updates for PAPI 3.
* 2003-11-21 Joseph Thomas — Fixed a variable name that caused a compile error.
* 2003-11-21 Dan Terpstra — Updates for PAPI 3.
* 2003-11-21 Dan Terpstra — Add support for PAPI_is_initialized.
* 2003-11-21 Dan Terpstra — New definition of PAPI_TOT_CYC based on a re-reading of the latest Intel documentation. Now we need to figure out what to do with hyperthreading...
* 2003-11-21 Dan Terpstra — Roll back Joe's changes to support the new definition of PAPI_TOT_CYC.
* 2003-11-20 Zhou Min — deleted some printf statements
* 2003-11-20 Zhou Min — fix the overflow bug in tru64-alpha
* 2003-11-20 Haihang You — update java implementation. tested on solaris. It has probelm on P3, because dlopen() would fail to load libpapi.so, and it says _data_start not defined.
* 2003-11-20 Joseph Thomas — Tweaked _papi_hwd_set_domain() to make sure it affects all counters.
* 2003-11-20 london — Added errno.h since it was failing to compile on some installations, fix provided by Steve Augart
* 2003-11-20 Joseph Thomas — The pentium4's PAPI_TOT_CYC is a special case and not a good event to test when it comes to domains.  We're using the PAPI_TOT_INS event instead.
* 2003-11-20 Joseph Thomas — PAPI_TOT_CYC is strange on the p4, so instead this test will use PAPI_TOT_INS.
* 2003-11-20 Joseph Thomas — Fix to make domain counting work and therefore make ctests/second work. Also removed some redundant code in _papi_hwd_update_control_state().
* 2003-11-20 Joseph Thomas — Added a debug statement that was removed for some reason.
* 2003-11-20 Dan Terpstra — Minor tweak to get rid of an annoying warning everywhere but POWER
* 2003-11-20 Dan Terpstra — Updates for PAPI 3.
* 2003-11-20 Dan Terpstra — Changes to support the mods to the calling sequence for PAPI_set_mutliplex. Tested on Pent4; should work everywhere. Caveat Emptor.
* 2003-11-20 Dan Terpstra — Changes to support the mods to the calling sequence for PAPI_set_mutliplex.
* 2003-11-20 Dan Terpstra — Changed the calling sequence for PAPI_set_mutliplex from passing a pointer to an eventset to passing the eventset. I know it's late in the game to be making changes like this, but one of the design goals of PAPI 3 was to get rid of that pesky unneeded dereferencing. Amazing what you can discover when you document things!
* 2003-11-20 Joseph Thomas — Altered the code that resulted in a seg fault every time an event was removed from a full event list.
* 2003-11-20 Joseph Thomas — Fixed PAPIF_NUM_EVENTS.  We were passing a pointer when PAPI_num_events() was looking for an int.
* 2003-11-20 Dan Terpstra — Implemented domain stuff in Pent4. Second now runs instead of skipping, but for some reason cycles don't seem to be affected by domain settings. So we've gone from a SKIP to a FAIL. This is progress?
* 2003-11-20 Dan Terpstra — Added Fortran support for PAPI_num_events
* 2003-11-19 Dan Terpstra — Stupid coder tricks. This one works now for Pentium4.
* 2003-11-19 Dan Terpstra — I've got this one working on Pentium4. Made the same change to the C version, but it STILL doesn't work. Go figure.
* 2003-11-19 london — Ooops forgot to check this in with papi.c
* 2003-11-19 london — Removing events could end up reordering the events if another event was added after the remove and the remove was not the last element just added.
* 2003-11-19 Zhou Min — Due to the multiplex feature in IRix, I forget to muliply the result by the number of events in that counter when hardware multiplexing occurs, now sdsc-mpx can pass the test in mips r10k
* 2003-11-19 Dan Terpstra — Updates for PAPI 3. Clarified examples.
* 2003-11-18 Haihang You — new power4-64bit Makefile
* 2003-11-18 Haihang You — move setup_native_table to init_global(). remove extra hwd_init()
* 2003-11-18 Dan Terpstra — Fixed a couple typos in comments.
* 2003-11-18 Zhou Min — changes made to let native.F to pass in Itanium2
* 2003-11-18 london — Changed PAPI_FP_INS to PAPI_TOT_INS so we didn't have to do checks for FP_INS and in addition it brings it inline with multiplex1.c
* 2003-11-18 london — Fix for Athlon, sometimes no PAPI_L2_DCM and PAPI_L2_ICM were no present which caused a failure for the test, this was OK, but changed the code a bit to force L2 DCM and ICM.
* 2003-11-18 Haihang You — use different events for power4 test
* 2003-11-18 london — This didn't check to see if 3 counters were possible, and would print an error string but pass, changed to not flag PAPI_ECNFLCT as a failure and made the events the same as case2.c
* 2003-11-18 Zhou Min — change the native event name for Irix
* 2003-11-18 Zhou Min — fix an syntex error in native.c
* 2003-11-18 Zhou Min — native event update
* 2003-11-18 Zhou Min — man pape update
* 2003-11-18 Dan Terpstra — A whole bunch of boilerplate changes for PAPI 3: - Changed title time stamp to November, 2003; - Changed AUTHOR(S) to the PAPI team and pointed to the website. This is an attempt to shield individuals from unneccessary emails and nudge people into posting emails to the lists rather than to individuals.
* 2003-11-18 Dan Terpstra — Updates for PAPI 3.
* 2003-11-17 Joseph Thomas — Left an unsigned long in where I should have replaced it with a unsigned int.
* 2003-11-17 london — EventInfo may not be dense, added check for PAPI_list_event for PAPI_NULL
* 2003-11-17 london — Multiplex was never removing the event from the EventInfo structure which was causing 2 problems, list_events wouldn't work and you couldn't add events to multiplex after removing due to hw conflicts.  The "fix" is to null out the eventinfo array and use the multiplex list of events in PAPI_list_events.  In the future we should really compact the structure to a dense array, but not this close to a release since this could have other ramifications...
* 2003-11-17 Dan Terpstra — And now a stupid logic error.
* 2003-11-17 Dan Terpstra — Another stupid syntax error.
* 2003-11-17 Dan Terpstra — Stupid syntax error.
* 2003-11-17 Dan Terpstra — Reworked to drive every platform from a list of events. Removes redundant code and simplifies maintenance. Also makes better example code. Rewritten for all platforms; tested only on Pentium 4. Please test on your substrate.
* 2003-11-17 Dan Terpstra — Added a pmtoolkit function to return the version of pmtoolkit. This is needed to support modifications to native.F.
* 2003-11-17 Dan Terpstra — Reworked to drive every platform from a list of events. Removes redundant code and simplifies maintenance. Also makes better example code. Rewritten for all platforms; tested only on Pentium 4. Please test on your substrate.
* 2003-11-17 london — Change PAPI_FP_INS to PAPI_TOT_INS for Athlon machines
* 2003-11-17 Joseph Thomas — Added a "fix" to make locking routines compatible from opteron to pentium3 and vice versa.  (Removed the ifdefs)
* 2003-11-17 Joseph Thomas — Made changes so that this makefile will work on: Pentium2/3, opteron and athlon. I say should because we are not yet able to test.
* 2003-11-17 Joseph Thomas — Multiplexing was hanging on the opteron as a result of a bug in _papi_hwd_lock().  Fixed.
* 2003-11-16 london — Changed hera to icl
* 2003-11-15 Joseph Thomas — Opteron fix for string length.  Fixes eventname and avail for fortran.
* 2003-11-15 Joseph Thomas — Added an opteron fix.
* 2003-11-14 Zhou Min — A quick fix for multiplex. We delete PAPI_FLOPS from the file, but didn't set the field "is_a_rate" to 0. Thus it caused the problem for sdsc-mpx. Now All the tests passed or skipped in Itanium2.
* 2003-11-14 Joseph Thomas — Altered tests on the p3 and athlon.
* 2003-11-14 Haihang You — fix for aix5-power3
* 2003-11-14 Haihang You — add some event support for AIX5-power3
* 2003-11-14 Haihang You — copy and revision of MAkefile.aix-power3
* 2003-11-14 Haihang You — take out allocate.o
* 2003-11-14 Joseph Thomas — Modified the tests for native.c.  The other tests were obscure and returned 0.
* 2003-11-14 Haihang You — extra ( found in power4  part
* 2003-11-14 Joseph Thomas — -fPIC removal undone. I'm not saying -fPIC has to stay, but if it is to be removed, it is essential that we have a working alternative.  Before making changes to code, please check to make sure those changes actually compile. This file, for the time-being, is only for compiling on the opteron. It is the only machine patched to work with perfctr-2.6. Later, we will have 2.6 working on more platforms; should we rename this file for now?  It gives no indication that it is only to be used for opteron compiling.
* 2003-11-14 Zhou Min — delete the printf statement added by me
* 2003-11-14 Zhou Min — better fix for FFLAGS
* 2003-11-14 Zhou Min — Format changes in Itaniu, Pentium4 and Mips platform. I add some continuation marks when the line is longer than 73 characters, because it will report an error in some platforms. Now this program also passed in Itanium
* 2003-11-14 Zhou Min — add some printf statements, will be deleted
* 2003-11-14 Zhou Min — forget to set FFLAGS when compile fortran programs in the Makefile
* 2003-11-14 london — -fPIC removed
* 2003-11-14 Haihang You — update for all platforms. only tested on sparc. you may want to test it onyour platform.
* 2003-11-14 Haihang You — add -WF, -DPOWER3  and -WF, -D_POWER4 flag for fortran compilation
* 2003-11-14 Joseph Thomas — Locks work on the opteron.
* 2003-11-13 Haihang You — no longer needed
* 2003-11-13 Joseph Thomas — Tweaked the optimization settings for the C compiler and the results are correct.
* 2003-11-13 Haihang You — update
* 2003-11-13 Dan Terpstra — This should fix the all_events and avail problems I introduced yesterday. When I deleted PAPI_FLOPS and PAPI_IPS, I didn't renumber the events in the rest of the table. This caused events to get misassigned, and tests to fail.
* 2003-11-13 Joseph Thomas — Removed -DPERFCTR20.  It is no longer used anywhere in 3.0.
* 2003-11-13 Joseph Thomas — It looks like the event PAPI_BR_NTK was incorrect on the Athlon and opteron.  They are found using a DERIVED_SUB.  I reversed the event order.  I assume it was only the order that was incorrect.
* 2003-11-13 Zhou Min — man page update
* 2003-11-13 Joseph Thomas — Domain counting works now.
* 2003-11-13 Joseph Thomas — Updated the opteron preset table. One more test passed, but FP_INS are still off by a factor of 2.
* 2003-11-13 Joseph Thomas — Added Athlon to the machines that can't count FP_INS so this test can work.
* 2003-11-12 Dan Terpstra — More changes to remove PAPI_FLOPS and PAPI_IPS. Nineth is really no longer valid. I pulled it from the Makefile. Not sure why I left it in the cvs tree... I modified all substrates, but tested only Pentium 4. Caveat Emptor.
* 2003-11-12 Dan Terpstra — More changes to remove PAPI_FLOPS and PAPI_IPS. Nineth is really no longer valid. I changed it, but then pulled it from the Makefile. Not sure why I left it in the cvs tree... I modified all substrates, but tested only Pentium 4. Caveat Emptor.
* 2003-11-12 Dan Terpstra — Finished adding PAPI_FP_OPS where needed; Also removed PAPI_FLOPS and PAPI_IPS, since rate events are deprecated in PAPI 3. That triggered a whole bunch of changes. Kevin - didn't you want to add some other events, like L2_TLB stuff? Guess that can wait... I modified all substrates, but tested only Pentium 4. Caveat Emptor.
* 2003-11-12 Haihang You — use PAPI_TOT_INS on power3
* 2003-11-12 Haihang You — update preset search table
* 2003-11-12 Haihang You — event name fix for power4
* 2003-11-12 Joseph Thomas — Corrected several errors in the opteron native table.  I was far off base in my implementation of the unit mask.  When the preset table is corrected, calibrate and other tests should be accurate.
* 2003-11-12 Dan Terpstra — Added a definition for PAPI_VEC_INS. Now we need a program to test it...
* 2003-11-12 Dan Terpstra — Realphabetized the prototypes to better match the documentation; Removed unsupported calls; Added a few comments.
* 2003-11-12 Dan Terpstra — Minor tweaks in declaration of PAPI_thread_id
* 2003-11-11 Dan Terpstra — Update the man to html converter script to match the new list of man pages.
* 2003-11-11 Dan Terpstra — Add a bunch of new man pages for new functionality in PAPI 3. Also update some pages for shared entries. NOTE: Most of these pages are preliminary and still need more work. Now they're at least in the repository where we can all get to them...
* 2003-11-11 Dan Terpstra — Remove a bunch of man pages that are either no longer needed or superceeded by others.
* 2003-11-10 Haihang You — change to use the old test pass message. Make it print out consistant message like other tests.
* 2003-11-10 Haihang You — modify to use the new native event adding function
* 2003-11-10 Zhou Min — comment update for papi_start_counters
* 2003-11-10 Zhou Min — man page update
* 2003-11-10 Dan Terpstra — More tweaks to convert PAPI_get_virt_{cyc, sec} from u_long_long return to long_long return.
* 2003-11-10 Dan Terpstra — More tweaks to convert PAPI_get_virt_{cyc, sec} from u_long_long return to long_long return.
* 2003-11-10 Dan Terpstra — Convert PAPI_get_virt_{cyc, sec} from u_long_long return to long_long return. I did this at the high level via  a cast. Substrates are inconsistent in how this is defined. Eventually this should propagate down, but for now this protects the API.
* 2003-11-10 Haihang You — use PAPI_FP_OPS
* 2003-11-10 Haihang You — add PAPI_FP_OPS support
* 2003-11-10 Haihang You — change PAPI_FP_INS to PAPI_FP_OPS
* 2003-11-10 Haihang You — add PAPI_FP_OPS support in MASK, add_test_event, and remove_test_event
* 2003-11-10 Haihang You — removed. use Makefile.aix-power3 for power4 AIX4.3.3
* 2003-11-10 Dan Terpstra — Removed several blocks of '#if 0' code; Added support for PAPI_enum_events and PAPI_flops
* 2003-11-10 Dan Terpstra — These tests exercise the old description routines, and only show up in Windows. We really don't need 'em for anything. They were preliminary test code for the early Windows port.
* 2003-11-09 Joseph Thomas — Modified the definition of GET_OVERFLOW_ADDRESS.  Profiling now works on the opteron.
* 2003-11-08 Joseph Thomas — Fixed a bug.  Compiles again.
* 2003-11-08 Zhou Min — Thanks for Per Ekman and Dan's help in ffs, I wrote a new function for ffsll, which also works in power3. /* find the first set bit in long long */ int ffsll(long long lli) {    int i, num, t, tmpint, len;
* 2003-11-08 Joseph Thomas — Added optional flags to identify system.
* 2003-11-08 Joseph Thomas — Since Athlon doesn't support flips or even flops, I added support for it via Haihang's PAPI_TOT_INS event instead.
* 2003-11-08 Joseph Thomas — Since Athlon doesn't support flips or even flops, I added support for it via Haihang's PAPI_TOT_INS event instead.
* 2003-11-08 Joseph Thomas — Added optional flags to identify system.
* 2003-11-07 Dan Terpstra — Removed PAPI_hw_counters and changed references to PAPI_hwctrs; Changed PAPI_initialized to PAPI_is_initialized in papi.h
* 2003-11-07 Zhou Min — 1. fix a minor bug in all_events.c 2. increase the overflow threshold when PAPI_event is PAPI_TOT_INS    in overflow.c , overflow2.c, overflow_single_event.c; 3. add PAPI_shutdown in test_skip and test_fail;
* 2003-11-07 Zhou Min — clear the overflow or profile flag in PAPI_cleanup_eventset keep the error report in PAPI_remove_event if the eventset state is overflow or profile;
* 2003-11-07 Dan Terpstra — Added PAPI_FP_OPS to P4 event list. Tweaked a comment in papi.h
* 2003-11-07 Dan Terpstra — Documentation tweaks. Added a PAPI_flops proto to papi.h and added some comments to papi_hl.c
* 2003-11-06 Haihang You — use PAPI_TOT_INS instead of PAPI_FP_INS on power3, since PAPI_FP_INS is derived event on power3
* 2003-11-06 Philip Mucci — Added thread fix for AIX...This fixes the inheritance problem we saw in PAPI 2.3.4...by the way, seems like we can get rid of the memcpy in hwd_start...
* 2003-11-06 Haihang You — roll back changes in dispatch_profile(), let each substrate to handle it. in aix.h, change #define GET_OVERFLOW_ADDRESS(ctx)  (void *)(((hwd_ucontext_t *)ctx)->sc_jmpbuf.jmp_context.iar) to #define GET_OVERFLOW_ADDRESS(ctx)  (void *)(((hwd_ucontext_t *)(ctx->ucontext))->sc_jmpbuf.jmp_context.iar) VERFLOW_ADDRESS(ctx)  (void *)(((hwd_ucontext_t *)(ctx->ucontext))->sc_jmpbuf.jmp_context.iar)
* 2003-11-06 Haihang You — here is another round of fix. use type int for overflow_vector on AIX.
* 2003-11-06 Haihang You — here are 2 fixes: 1. in _papi_hwi_dispath_overflow_signal()    change type of overflow_vector from long_long to int.    ffs(overflow_vector) tends to be 0 if declared as long_long, if size of int is not big enough, we need come    up another way to fix it. This is a real bad bug. 2. in  dispatch_profile() instead of being    caddr_t pc=(caddr_t)GET_OVERFLOW_ADDRESS(ctx),    it should be    caddr_t pc=(caddr_t)GET_OVERFLOW_ADDRESS(ctx->ucontext);    This is a bad bug too.
* 2003-11-05 Joseph Thomas — Added support for opteron revision C to make ctests/mem_info work.
* 2003-11-05 Zhou Min — reduce the buffer size allocted to profbuf to it's half, since in PAPI_profil(void * buf, int length, .........), length should be the total bytes in buf.
* 2003-11-05 Zhou Min — delete useless functions in these programs
* 2003-11-05 Zhou Min — man page update
* 2003-11-04 Joseph Thomas — Added opteron support.  75% or so tests pass with the notable exception of profiling.
* 2003-11-04 Joseph Thomas — Updated opteron presets.
* 2003-11-04 Zhou Min — delete useless statement added by me
* 2003-11-04 Zhou Min — add PAPI_FP_OPS preset event into preset event table
* 2003-11-04 Zhou Min — man page update
* 2003-11-03 Haihang You — remove PAPI_add_pevent
* 2003-11-03 Haihang You — change PAPI_rem to PAPI_remove, PAPI_rem_pevent removed
* 2003-11-03 Haihang You — copy and modified PAPI_rem_event.3
* 2003-11-03 Haihang You — change PAPI_rem to PAPI_remove
* 2003-11-03 Haihang You — modify some words. change PAPI_rem to PAPI_remove.
* 2003-11-03 Haihang You — modify PAPI_add_event() in the example. reformat some line.
* 2003-11-03 Haihang You — change it to new API. add info about PAPI_event_name_to_code for adding native event. modify example too.
* 2003-11-02 Zhou Min — Added one more PAPI_overflow or PAPI_profil function call before we remove the overflow event
* 2003-11-02 Zhou Min — Added PAPI_FP_OPS preset event
* 2003-11-01 Joseph Thomas — Added PAPI_FP_OPS to the event tables.
* 2003-11-01 Joseph Thomas — Removed -DPERFCTR24.  #ifdef PERFCTR24 is nowhere to be found
* 2003-11-01 Joseph Thomas — Fixed an error in opteron support.
* 2003-10-31 Haihang You — changes PAPI_flips() to PAPI_flops() since calibrate really count flops. each platform should have PAPI_FP_OPS defined.
* 2003-10-31 london — Really need to make sure > 0 events were added
* 2003-10-31 london — Need PRESET_MASK for get_info
* 2003-10-31 london — Fixes for PAPI_library_init working with shutdown and the high level
* 2003-10-31 london — Check to make sure cycles aren't 0 before dividing.
* 2003-10-31 Dan Terpstra — Modified the event table for Pentium 4. Someone had commented out case 1 in this test. I commented it back in and it passes on Pent4. Please test on your substrate(s).
* 2003-10-31 Haihang You — add -DPOWER3 in the Makefile. since PAPI_FP_INS on power3 is derived event, need change to be PAPI_TOT_INS for overflow tests
* 2003-10-31 Haihang You — add -DPOWER3 in the Makefile. since PAPI_FP_INS on power3 is derived event, need change to be PAPI_TOT_INS for overflow tests n power3 is derived event
* 2003-10-30 Haihang You — add function PAPI_flops(). It is the copy of PAPI_flips() except that PAPI_FP_OPS is counted in the new function. In order to use this function on one platform, PAPI_FP_OPS must be defined. It could mimic PAPI_FP_INS and modify it to get desired numbers.
* 2003-10-30 Haihang You — add entry PAPI_FP_OPS in preset search table
* 2003-10-29 Dan Terpstra — Fixed a nasty one line bug in _papi_hwi_remove_event() that was indexing outside the position array when removing an event. This could cause extra event info to get inintentionally deleted.The good news is it would probably only show up somewhere like Pentium 4 or X1 where numCounters > MAX_COUNTER_TERMS.
* 2003-10-28 Joseph Thomas — Added a -DPENTIUM3 to identify proper substrate.
* 2003-10-28 Joseph Thomas — Added a -D__x86_64__ to identify the proper substrate.
* 2003-10-28 Joseph Thomas — Added PIII, ATHLON and opteron codes.
* 2003-10-28 Dan Terpstra — Minor cleanups; no change in functionality. Calibrate should now work with Kevin's fixes in the hl code. When PAPI_FP_OPS is generally implemented, this code should be modified slightly.
* 2003-10-28 london — Changed the rate calculation to get rid of some overhead
* 2003-10-28 Dan Terpstra — Rewritten to support new PAPI HL model. Now produces spurious counts on Pentium 4. Haihang, Min -- please test on POWER and Itanium 2 and send me the output.
* 2003-10-28 london — Subtract out 1 flip that can't be avoided for the papi_flips call.
* 2003-10-28 Joseph Thomas — Two things:  PAPI v3.0 compiles and links on the opteron, but produces errors on test. Also, profiling works on the PIII after noting Dan's P4 changes.
* 2003-10-28 Haihang You — update power Makefiles
* 2003-10-28 Haihang You — update power3
* 2003-10-28 Dan Terpstra — Removed the HAS_NATIVE_MAP flag from all code and make files, since every substrate should now have a native map. Couldn't remember which power make files were still current, so I changed 'em all. We really should remove the outdated ones from cvs and rename appropriately.
* 2003-10-28 Dan Terpstra — native.c needs to be reworked for all platforms except Pentium 4, Itanium, and POWER. We no longer support native bit patterns, and much of the code can be recast using  a native event name list
* 2003-10-28 london — Ooops was relying on the user to pass in the array length for PAPI_stop_counters when they started it with flips or ipc, which is a bad thing.  Now they can pass in anything they want and it will still work.
* 2003-10-28 london — Fix for high_level, when I stopped the counters for flips or ipc I didn't have enough memory locations.
* 2003-10-27 Dan Terpstra — P4 can have non-derived events that contain more than one counter. E.G. PAPI_FP_INS. To handle these with profiling, you need to search more than just counter position 0.
* 2003-10-27 Dan Terpstra — P4 & perfctr requires that overflowing events be at the end of the list. swap_events was supposed to take care of that. It didn't. Classic example of 'stupid programmer tricks' And another reason to step through new code in a debugger -- even when you KNOW its right.
* 2003-10-27 Dan Terpstra — I was doing the second level of indirection in _papi_hwd_dispatch_timer when it should have been done in GET_OVERFLOW_ADDRESS. Also removed a bunch of x86_64 stuff for Opteron, since that's in the P3 substrate.
* 2003-10-27 Dan Terpstra — _papi_hwd_dispatch_timer now dereferences the overflow address properly. FINALLY! I was missing one level of indirection. That's what I get for coding blind.
* 2003-10-23 Zhou Min — 1. changes made in solaris such that when the eventset is not overflowing,    then papi_stop will not stop the physical counter. This is for    reducing the overhead for PAPI_stop;
* 2003-10-21 Haihang You — instead of using fixed event for limited platforms, I make it scan presets, and choose the first derived event to count.
* 2003-10-21 Joseph Thomas — First attempt at adding perfctr 2.6 support.
* 2003-10-20 Dan Terpstra — Fixes for the derived event problem on PIII. It had to do with the fact that this substrate supports hardware with either 2 or 4 counters. Initiialize_EventInfo was initializing 2 counters and derived_subtract was checking 4 counters.
* 2003-10-18 Haihang You — replace 0 with PAPI_NULL in preset search table. add PAPI_FP_OPS
* 2003-10-18 Haihang You — fix syntax error
* 2003-10-18 Zhou Min — Format change and native can pass the test in alpha.
* 2003-10-18 Zhou Min — 1. use PAPI_NULL in preset event table;
* 2003-10-17 Joseph Thomas — Updated to work with PAPI_NULL initialized in the preset structure. linux-memory.c updated - added memory entries.
* 2003-10-17 Dan Terpstra — Minor changes in derived events to support PAPI_NULL. Shouldn't change results, which, BTW, work on Pentium 4 for an artificial derived event.
* 2003-10-17 Dan Terpstra — Changes to convert the preset table native event lists to terminate with PAPI_NULL. These changes may break other substrates that were working before. Please check!
* 2003-10-16 Dan Terpstra — Preliminary changes for PAPI 3 that have been laying around for too long.
* 2003-10-15 Haihang You — here is the solution to make _papi_hwd_reset() working on power. It is simple and without affecting anyother functions. first is running right.
* 2003-10-15 Dan Terpstra — oops. Missed one.
* 2003-10-14 Dan Terpstra — reformatted everything using 'indent -kr -l90 -i3 -nut' to provide k&r format with 90 char line length, 3 char indents, and no tabs.
* 2003-10-14 Joseph Thomas — Accidentally left some debugging printf statements in this file.
* 2003-10-14 Joseph Thomas — Overflow works somewhat.  Fixed an error with enum events.
* 2003-10-13 Haihang You — fix typo
* 2003-10-13 Dan Terpstra — Changes to add DEBUG_OVF for overflow; Changes in Pentium 4 substrate for overflow. It executes now, but still give spurious results: usually nil PC and improper counts.
* 2003-10-11 Philip Mucci — Import of PerfCtr v. 2.4.91
* 2003-10-11 Philip Mucci — Initial revision
* 2003-10-10 london — Now that I have permission to checkin the X1 stuff, here is a work in progress for the X1 port to PAPI 3.0, I have a working copy of X1 for PAPI-2.3.4, but it is rough and since we will be releasing a 3.0 soon, I am just going to release the code for the X1.  This currently will not compile or run, but I should have everything working soon.  Some things to be aware of when the release is done, this port will overflow using hardware will only P-chip events are being overflowed on, but if any M or E chip events are overflowed on then overflow will use software instead of hardware.  In addition, when in MSP mode you recieve the sum of the SSP counters, and currently there is no way to get just one of them.  Finally, while there are "64" counters available on this platform, 32 of them can be p-chip events, 16 can be m-chip events and 16 can be e-chip events.
* 2003-10-08 Joseph Thomas — Removed a line telling the user not to use numeric codes to represent events; the user can now do this.
* 2003-10-08 Joseph Thomas — Updated the PAPI_Matlab readme file to address the high level changes to PAPI.
* 2003-10-08 Joseph Thomas — Found some bugs, but the important overflow remains a mystery.
* 2003-10-07 Haihang You — increase the array size of OPS
* 2003-10-07 Haihang You — redefine PAPI_FP_INS as PM_FPU0_FIN + PM_FPU1_FIN + PM_FPU_FMA - PM_FPU_STF, and it is geeting right flops now
* 2003-10-06 Haihang You — modify postfix function, now 1000000.0 does not need to be in the operation string in the preset search table
* 2003-10-06 Haihang You — make it not to print out group info when executed in quiet mode on power4
* 2003-10-06 Zhou Min — fix the bug in set_domain funciton in each substrate
* 2003-10-06 Dan Terpstra — Code cleanup: Remove ureferenced structures; Eliminate stuff for Opteron (moved to x86 substrate; modified for new overflow interface.
* 2003-10-06 Dan Terpstra — Add proto for _papi_get_native_event_info(); Add definition for OVF_DEBUG (overflow); Minor typo corrections.
* 2003-10-06 Dan Terpstra — VERY preliminary changes to port dadd-alpha to PAPI 3
* 2003-10-06 Dan Terpstra — Change PAPIf_flops to PAPIf_flips
* 2003-10-03 Zhou Min — minor bug fix when initiated by run_tests.sh
* 2003-10-03 Zhou Min — another lock solution in Itanium
* 2003-10-03 Zhou Min — delete the printf statement added by me.
* 2003-10-03 Zhou Min — comment out the check on the result of overflow event
* 2003-10-03 Zhou Min — 1. add different scale support in PAPI_profil;
* 2003-10-02 Haihang You — in _papi_hwi_add_event() add native code instead of adding index of the native code. this solve the problems with adding and removing native events.
* 2003-10-02 Haihang You — put native code into event_info_t structure in _papi_hwi_get_native_event_info()
* 2003-10-02 Haihang You — postfix is in place now. To use postfix, just use DERIVED_POSTFIX instead of (eg.) DERIVED_ADD in the preset search table. you need put a operation string following postfix rules in the preset search table as well. Here are the notations: N0, the first native event, N1, the second native event; | is the delimiter; +, -, *, /, %, are the operators;# is mhz; $ is 1000000.0; you also can use integers too. I tested a little bit on power4. It is not fully tested yet. Anything happens, let me know.
* 2003-10-02 Zhou Min — change the user overflow handler function
* 2003-10-02 Zhou Min — fix a bug in _papi_hwi_add_event, so that native.c can pass the test now
* 2003-10-01 Joseph Thomas — PAPI_Matlab stuff.  The readme still needs to be updated, but it looks like it works - at least on the pentium 3.
* 2003-10-01 Joseph Thomas — I just wanted to keep things up to date.
* 2003-09-30 Haihang You — add native event support in functionos: PAPI_get_event_info(), PAPI_query_event()
* 2003-09-29 Dan Terpstra — Replaced PAPI_encode_native with PAPI_event_name_to_code. Min, I made the code changes, but didn't test it. Please rebuild and test on Itanium and MIPS at your convenience.
* 2003-09-29 Dan Terpstra — Remove PAPI_encode_native definition. We need this function eventually, but not the way it was defined here.
* 2003-09-29 Dan Terpstra — Remove Opteron event table from this file; it now lives in the p3 substrate.
* 2003-09-29 Zhou Min — add two test files to test 32 and 64 bucket profile support;
* 2003-09-29 Zhou Min — add two test files, profile_32.c and profile_64.c
* 2003-09-29 Zhou Min — 1. changes made to use the new preset data structure;
* 2003-09-26 Haihang You — get rid of _papi_hwi_query_native_event_verbose(EventCode, info). Dan, you did remove it, but you did it in 2.3.4 branch.
* 2003-09-26 Haihang You — changed preset_search_t to new defined hwi_search_t
* 2003-09-26 Haihang You — modify _papi_hwi_native_name_to_code(char *, unsigned int *) to _papi_hwi_native_name_to_code(char *, int *)
* 2003-09-26 Haihang You — modify macro GET_OVERFLOW_ADDRESS
* 2003-09-26 Haihang You — changed hwi_preset_t to new defined hwi_preset_data_t
* 2003-09-26 Haihang You — changed _papi_hwd_set_profile() to new defined interface
* 2003-09-26 Joseph Thomas — Updated preset stuff and added support for the opteron.
* 2003-09-26 Haihang You — changed total_tlb_size, total_L1_size to L1_tlb_size and L1_size
* 2003-09-25 Haihang You — adding new overflow support. compile with new debug macros.
* 2003-09-25 Haihang You — this file is no longer needed
* 2003-09-25 Dan Terpstra — Somehow my previous commit screwed up a bunch of changes in this file. This commit should fix it...
* 2003-09-25 Dan Terpstra — Restored _papi_search_t structure due to unforseen incompatibilities higher up the chain. This will require minor formatting changes in the search tables of all substrates. Also reworked the PAPI event description interface. Removed:   const PAPI_preset_info_t *PAPI_query_all_events_verbose(void);   int PAPI_describe_event(char *name, int *EventCode, char *description);   int PAPI_label_event(int EventCode, char *label);   int PAPI_query_event_verbose(int EventCode, PAPI_preset_info_t *info); Added:   int PAPI_get_event_info(int EventCode, PAPI_event_info_t *info); Changed:   "PAPI_preset_info_t" to "PAPI_event_info_t" These changes should have no effect on substrates, but will affect current and future test code.
* 2003-09-25 Dan Terpstra — Reworked the PAPI event description interface for these tests. Removed:   const PAPI_preset_info_t *PAPI_query_all_events_verbose(void);   int PAPI_describe_event(char *name, int *EventCode, char *description);   int PAPI_label_event(int EventCode, char *label);   int PAPI_query_event_verbose(int EventCode, PAPI_preset_info_t *info); Added:   int PAPI_get_event_info(int EventCode, PAPI_event_info_t *info); Changed:   "PAPI_preset_info_t" to "PAPI_event_info_t"
* 2003-09-25 Dan Terpstra — Changed:   "PAPI_preset_info_t" to "PAPI_event_info_t"
* 2003-09-25 Dan Terpstra — Reworked the PAPI event description interface for these tests. Removed:   const PAPI_preset_info_t *PAPI_query_all_events_verbose(void);   int PAPI_describe_event(char *name, int *EventCode, char *description);   int PAPI_label_event(int EventCode, char *label);   int PAPI_query_event_verbose(int EventCode, PAPI_preset_info_t *info); Added:   int PAPI_get_event_info(int EventCode, PAPI_event_info_t *info); Changed:   "PAPI_preset_info_t" to "PAPI_event_info_t"
* 2003-09-25 Dan Terpstra — Restored _papi_search_t structure due to unforseen incompatibilities higher up the chain. This will require minor formatting changes in the search tables of all substrates. Also reworked the PAPI event description interface. Removed:   const PAPI_preset_info_t *PAPI_query_all_events_verbose(void);   int PAPI_describe_event(char *name, int *EventCode, char *description);   int PAPI_label_event(int EventCode, char *label);   int PAPI_query_event_verbose(int EventCode, PAPI_preset_info_t *info); Added:   int PAPI_get_event_info(int EventCode, PAPI_event_info_t *info); Changed:   "PAPI_preset_info_t" to "PAPI_event_info_t" These changes should have no effect on substrates, but will affect current and future test code.
* 2003-09-24 london — Convert int to unsigned int to keep consistency, on some platforms this returns an error on compile, this fixes it.
* 2003-09-23 Philip Mucci — Changed L1LDM definition, L2LDM definition, removed L2STM definition.
* 2003-09-23 london — Fixed type (missing ) ), and added prototypes to papi.h for flips and ipc
* 2003-09-23 london — Added a new ipc program to test PAPI_ipc
* 2003-09-23 london — Change tests to use PAPI_flops instead of flips
* 2003-09-23 london — Added PAPI_ipc and renamed PAPI_flops fortran wrapper macros
* 2003-09-23 london — Rename PAPI_flops to PAPI_flips
* 2003-09-23 london — Change test to test how flips/start_counters interact and what is allowed which has changed slightly.
* 2003-09-23 Zhou Min — let the program call the new user overflow handler
* 2003-09-23 Zhou Min — we don't support overlapped eventset any more, delete with the permission from Nils.
* 2003-09-23 Zhou Min — 1. add a test file for multiple event profile;
* 2003-09-23 Zhou Min — 1. add multiple hardware overflow support in UltraSparcIII;
* 2003-09-19 Zhou Min — add another test case in this file:  When the user call Papi_overflow to turn off the overflow,  test whether we can get the right result if we start the  eventset again
* 2003-09-19 Zhou Min — change the interface int _papi_hwd_set_overflow(EventSetInfo_t *ESI, EventSetOverflowInfo_t *overflow_option) to int _papi_hwd_set_overflow(EventSetInfo_t *ESI, int EventIndex, int threshold)
* 2003-09-19 london — New high level interface changes.
* 2003-09-19 Zhou Min — add support to _papi_hwd_enum_events; made changes to accomodate the updates in papi_preset.c; tune the interface to call _papi_hwi_dispatch_overflow_signal;
* 2003-09-19 Zhou Min — delete unuseful debug added by me; add support for _papi_hwd_ntv_enum_events
* 2003-09-19 Zhou Min — interface change for the new user_handler
* 2003-09-19 Zhou Min — 1. New implementation for mulitple overflow, the new interface of two    functions:
* 2003-09-18 Joseph Thomas — Made minor changes to accomodate Dan's preset changes.
* 2003-09-17 Haihang You — new implementation of _papi_hwd_ntv_enum_events(unsigned int *EventCode, int modifer) on power when modifer=0, it would return PAPI_OK, *EventCode=*EventCode+1      modifer=1, it would return PAPI_OK, *EventCode contains group number, which is encoded in      digits 16-23. *EventCode=*EventCode+1 when there is no more group, now *EventCode is pure native      event code.
* 2003-09-17 Dan Terpstra — Removed the papi_search structure from papi_preset and replaced it with the hwi_preset structure. This is the first step in cleaning up our preset structures before modiying the event description API. Also renamed the ni_index field in the NativeInfo structure to ni_event and changed its semantics. Previously, this field contained an index without the high order native bit set. Now it contains a native event code WITH the high bit set. This allows zero to act as a terminator or empty value. All supporting code changed and tested. All substrates have been changed, but only Pentium 4 has been tested.
* 2003-09-17 london — Changes so that Pentium 4 will compile with the new overflow code.  This has NOT been ported, just stubs have been put in and a few things changed to arrays.  When the overflow code interface has stabalized, look for XXX to find locations of the changes to make this platform compile and fix the code :)
* 2003-09-15 Dan Terpstra — Removed some dead code; first cut at overflow structures and macros.
* 2003-09-15 Dan Terpstra — Change initialization of EventSetOverflowInfo_t structure in PAPI_overflow to be compatible with more compilers.
* 2003-09-14 Zhou Min — Add error checks in _papi_hwi_add_event to prevent the user to add a derived papi event which consists of at least one native event which has been used as oveflow event
* 2003-09-13 Zhou Min — 1. Fix the bugs in Software multiple overflow in Solaris 2. Move papi_hwd_context_t to papi_internal.h and change it to typedef struct {   hwd_siginfo_t *si;   hwd_ucontext_t *ucontext;   int overflow_vector; /* for software overflow and some platforms                           I can't found how to get the overflow bits */ } _papi_hwi_context_t;
* 2003-09-12 london — Created functions for platforms that do not support var arg macros (IE Solaris) to use these, define: NO_VARARG_MACRO
* 2003-09-12 Zhou Min — This headfile will not be used now
* 2003-09-12 Zhou Min — 1. implement PAPI_get_overflow_ctrs(int EventSet, void *context, int *papi_event_indices) 2. change the overflow handler; 3. change the EventSetOverflowInfo_t struct to let it support multiple    hardware or software overflow function call; 4. add a new type in Itanium substrate, these new data type also must    be defined in each substrate(this is for the context parameter in     overflow handler);    typedef struct {   pfm_siginfo_t *si;   struct sigcontext *ucontext; } papi_hwd_context_t;
* 2003-09-12 london — More memory changes
* 2003-09-12 london — I will eventually get all the .h referenced to memory.
* 2003-09-12 london — Needed to remove memory.h dependency
* 2003-09-12 london — Remove linux-ia64-memory.h this file is no longer needed.
* 2003-09-11 london — Tweak to DBG
* 2003-09-11 Joseph Thomas — Tweaked to get the athlon to work with this substrate.
* 2003-09-11 london — New debug macros, all are defined in papi_internal.h The new macros are as follows: PAPIDEBUG(level, format, args.....) Valid levels are: DEBUG_ON, DEBUG_SUBSTRATE, DEBUG_API, DEBUG_INTERNAL, 	DEBUG_THREADS and DEBUG_MULTIPLEX.  These can be or'd together if 	wanted: PAPIDEBUG(DEBUG_INTERNAL|DEBUG_MULTIPLEX, "This is test # %s\n", x);
* 2003-09-11 london — Added enteries for new thread functionality
* 2003-09-11 london — Added PAPI_register_thread()
* 2003-09-11 london — Changed the semantics of PAPI_thread_set_specific and PAPI_thread_get_specific calls to match the semantics of the POSIX pthread_setspecific and pthread_getspecific calls.  This compiles but no testing has been done on this yet, this will be incorporated into the high level interface changes so the testing will be done then. (IE don't use it yet ;) )
* 2003-09-11 Dan Terpstra — Fixed a bug in one of the bipartite callback routines.
* 2003-09-10 Haihang You — make new lock stuff compile. don't which test would confirm it is running ok. add _papi_hwd_ntv_enum_events() function support on power platform. power is up and running again based on yesterday's checkout, might break now.
* 2003-09-10 london — Added a few things that have been added to PAPI 3.0 or is almost finished. As you finish things remember to update this file.  I believe I have most everything that is in progress or that is done, so please review the file to make sure everything is in here and as we work down the PAPI 3.0 feature list update this file.
* 2003-09-10 london — Changes to remove _GET_ and _SET_ to the PAPI_get_opt and PAPI_set_opt calls.  Only GETs still in the api is for the dynamic memory information which has not been changed yet.
* 2003-09-10 london — Updated to work with the new system
* 2003-09-10 london — Removed PAPI_get_memory_info and rolled it into PAPI_hw_get_info, the only changes users will have to make is change PAPI_mem_info_t to PAPI_hw_info_t, and change PAPI_get_mem_info to PAPI_get_hardware_info and then everything else should be the same since I got rid of the mem structure.
* 2003-09-10 Joseph Thomas — Can finally add events after finding a well-hidden bug.  One bug, that I am aware of, remains.  Tests not related to this bug or overflow all pass.
* 2003-09-09 london — First round of memory updates The data structure was changed to support Multiple TLB's, size is now I+D, when there is a unified cache the total size should be set, but I and D should be 0.
* 2003-09-09 london — Removed the _thread_list, and ThreadInfo_t from the various substrates and moved it to papi_internal.h, removed locking around insert and lookup functions as this "should" be safe now, locks/unlocks are commented out for now, till I test this heavily.
* 2003-09-09 london — PAPI_overflow now checks to make sure the event is not a derived event, returns PAPI_EINVAL if it is.
* 2003-09-08 london — First round of changes to threads, this one turns the list into a circular linked list, the thread information most likely will be moved from the substrates next.
* 2003-09-08 Haihang You — change PAPI_get_real_usec() to _papi_hwd_get_real_usec()
* 2003-09-08 london — New PAPI version system, implemented from an email that Nils sent out a while back, this implements: PAPI_VERSION_NUMBER, PAPI_VERSION_MAJOR, PAPI_VERSION_MINOR, PAPI_VERSION_REVISION, PAPI_VERSION and PAPI_VER_CURRENT. This now allows things such as: #if (PAPI_VERSION==PAPI_VERSION_NUMBER(3,1,3))
* 2003-09-08 Haihang You — files are not needed any more.
* 2003-09-08 Haihang You — files for allocate are not needed any more.
* 2003-09-08 Dan Terpstra — Tweaks for locks.
* 2003-09-05 Joseph Thomas — Added enum_events support.
* 2003-09-05 Zhou Min — add a test file to test two PAPI_overflow calls
* 2003-09-05 Zhou Min — 1. let lock/unlock macro works; 2. supports multiple PAPI_overflow calls
* 2003-09-05 Joseph Thomas — Made changes to get locks working.
* 2003-09-05 london — Checkin
* 2003-09-05 Dan Terpstra — Tweaks for locks.
* 2003-09-05 london — PAPI_is_initialized function, initial implementation may change
* 2003-09-05 london — Fixes for the locking mechanism.  We can't expose a macro to the end user or they would have to include the substrate.h files
* 2003-09-05 london — Typos fixed
* 2003-09-05 london — changes to the locking structure
* 2003-09-05 london — Reorganization of the locking macros
* 2003-09-05 london — Rearranged the locking macros
* 2003-09-04 Dan Terpstra — Added PAPI_enum_event call. Modified Pentium 4 substrate to handle native events effectively. Try running native_avail on Pentium4 -- its pretty cool. Did you know there's over 83,000 possible native event combinations on Pentium 4?
* 2003-09-04 Dan Terpstra — Modified avail and native_avail to use the new PAPI_enum call.
* 2003-09-03 london — New locking test, has not been compiled yet, so don't be surprised if it fails, but first I have to find a 3.0 platform that does compile .
* 2003-09-03 london — Fixed the lock macro in p4
* 2003-09-03 london — Fixed a typo in the lock macro
* 2003-09-03 london — Changed papi_hwd_lock/unlock prototypes to match the new definition of taking an int as a variable.
* 2003-09-02 Joseph Thomas — Moved lock code from linux.c to p3's substrate per Kevin's behest.
* 2003-08-29 Joseph Thomas — These files will not be included in PAPI 3.0.  The makefiles are being replaced with Makefile.linux-perfctr-p3 and Makefile.linux-perfctr-p4. The substrate files are now mainly in linux.c and perfctr-px.x. The event file is now px_events.x.
* 2003-08-29 london — I have added multiple locking mechanisms as macros, the new API is:
* 2003-08-29 Joseph Thomas — Files needed to run PAPI 3 on the perntium III and athlon.
* 2003-08-28 Dan Terpstra — Massive changes to the event table for Pentium 4. It turned into a bigger project than I thought. Now fully supports an opaque virtual table AND a custom table AND a user definable table. We've just gotta figure out how the user edits it... Still need to propagate _enum_events to the user level.
* 2003-08-28 Dan Terpstra — Removed ESIhead from EventInfo struct. We never used it, and don't need it with the current register allocation scheme. Also added -g to p4_events in the Makefile. I'm finally using gdb!
* 2003-08-27 Philip Mucci — Removed Level 1 and Level 2 Store misses, event not supported on P4
* 2003-08-22 Haihang You — power4 is running. native table is generated in run-time. Most tests passed
* 2003-08-22 Haihang You — add support for different cpu types. native table is generated in run time. most tests passed. It should be able to run on power3-aix5.
* 2003-08-20 Haihang You — changes in power substrate to comply with Dan's previous functions' name changes
* 2003-08-15 Dan Terpstra — Name changes (again) to make Kevin happy: _ntv_ changed to _hwd_ntv; _bpt_ changed to _hwd_bpt_ Also, commits for the reworked Pentium 4 native table. We can now generate a native event code for virtually any P4 native event. Unfortunately, all the tests segfault...
* 2003-08-15 Dan Terpstra — More code changes to accomodate changed names for the access functions for virtual native tables.
* 2003-08-14 Dan Terpstra — Somehow I checked in a copy with a 'G' as the first character. My bad... All better.
* 2003-08-14 Dan Terpstra — Cosmetic changes to naming schemes for the bipartite allocation code. Haihang - you'll need to recompile POWER to trap for these name changes. While I was at it, I also changed the names of the access functions for virtual native tables. Hate me if you like, but I think they make more sense.
* 2003-08-13 Haihang You — change do_counter_allocation to be bipartite_counter_allocation, and it has been moved to papi_internal.c.
* 2003-08-13 Zhou Min — change it back as in PAPI2-3-4, so that Itanium2 can get the right IP address of  do_reads and do_flops functions
* 2003-08-13 Zhou Min — 1. Add some comments in these file 2. Incorparate pfmwrap.h into linux-ia64.h 3. change run_tests.sh a little so that it can also be run in yogi successfully.
* 2003-08-12 Haihang You — PAPI3.0 power3 is updated. Now the native table is generated in runtime.
* 2003-08-05 Haihang You — PAPI3.0 power4 is up and 85% tests passed
* 2003-08-05 Zhou Min — changed it to support only one eventset be active
* 2003-08-05 Zhou Min — delete a debug printf statement added by me : ----------------------------------------------------------------------
* 2003-08-05 Zhou Min — fix a bug in handle_derived_add and handle_derived_subtract
* 2003-08-04 Zhou Min — 1. change the return type of  function   _papi_hwd_update_control_state() back to int;   based on current add_native_events and remove_native_events process   Itanium and UltraSparc may fail in this function, so we need to check   the return type of this function;
* 2003-08-02 Haihang You — forgot aix.c, part of power4 upgrading
* 2003-08-02 Haihang You — first cut of power4 papi-3.0 implementation. some tests pass, and still in debuging mode
* 2003-08-02 Haihang You — _papi_hwd_update_control_state() does not need return value, checking return value is not necessary. add print_state() for debug use
* 2003-07-31 Zhou Min — change the return type of function  _papi_hwd_update_control_state from void to int
* 2003-07-31 Haihang You — fix the bug which haunting around for a week. now allocation works all right, and power3 test is getting right numbers
* 2003-07-31 Zhou Min — Sorry I don't remember I changed multiplex1.c, maybe adjust some format.
* 2003-07-31 Zhou Min — In papi_hl.c
* 2003-07-30 Haihang You — adding fixes to backup eventInfo and nativeInfo value when add_events fail. rename counter_reorder() to be counter_read()
* 2003-07-30 Dan Terpstra — Errors in the event table were causing test failures. A macro was being expanded improperly. Now we have a significantly higher pass rate!
* 2003-07-30 Dan Terpstra — Pentium 4 is now counting again. A reasonable number of the tests now pass. Of course, an unreasonable number still fail... CAUTION: I capriciously changed some variable names. Recompile your substrates to see if they were affected...
* 2003-07-25 Dan Terpstra — I found that I was referencing the wrong structure in NativeInfoArray. It wasn't used in power3, but I need it in Pentium 4. Sorry.
* 2003-07-25 Dan Terpstra — Removed a couple unused variables.
* 2003-07-24 Haihang You — fixes to the allocation part. Now position and owners are getting right values.
* 2003-07-22 Dan Terpstra — Fixes to _papi_hwd_allocate_registers to copy selector state back into NativeInfo array.
* 2003-07-22 Dan Terpstra — Roll back removal of NativeGen stuff for Power3. We need it until we restructure the Power3 substrate.
* 2003-07-22 Dan Terpstra — Added code to _papi_hwi_remove_event() to compact the EventInfo array when an event is removed. CAVEAT: This code has NOT been tested. FAMOUS LAST WORDS: It should work. I'll be testing it later today on Pentium 4, but wanted to check it in anyway. This doesn't trigger any interface changes, so you can ignore it for now...
* 2003-07-21 Haihang You — fix some Macros in extras.c
* 2003-07-21 Zhou Min — change the calling sequences of  _papi_hwd_read back
* 2003-07-19 Zhou Min — remove hwd_regmap_t regs        int hwd_selector;        int counter_index;    from  EventInfo_t structure because In Power3 and Itanium we don't use regs now,   and hwd_selector is redundant with pos array,       counter_index is the same as pos[0];
* 2003-07-18 Dan Terpstra — Iteration #5. Restructured access to the hwd_control structure. Now, both add and delete are completed by updating the control structure. The structure has become effectively "write-only" for the substrate, acting as a repository for data requred by the counter driver to do its thing.
* 2003-07-17 Dan Terpstra — Iteration #4. Removed references to COUNT_NOTHING in the hwi layer.
* 2003-07-17 Dan Terpstra — Iteration #3. Removed mod, rank, and selector from NativeInfo_t. Eliminated direct access to native table from hwi. Everything still works!
* 2003-07-17 Dan Terpstra — Second cut at promoting add_event and remove_event functionality to the hwi layer. Getting closer, AND this version still works as well as the previous. There are still a few hardware dependencies to work out, but it's real progress.
* 2003-07-16 Dan Terpstra — First cut at promoting add_event and remove_event functionality to the hwi layer. Nowhere near done, but this version works as well as what's currently in cvs. And its a few steps closer than before.
* 2003-07-10 Dan Terpstra — Moved native event tables into a file that was already part of cvs and deprecated the old style preset table.
* 2003-07-10 Dan Terpstra — More changes to get Pentium4 working. Avail and native_avail now work on Pentium4, so the tables are getting built properly. Also some tweaks to native table access in extras. I'm not satisfied yet with how all this works, but I need to think about it some. There's bigger fish to fry. On to Pentium4 hwd_add_event...
* 2003-07-10 Dan Terpstra — Minor change to get this file to pass the compiler. Eliminated one of the high level calls for native events.
* 2003-07-10 Dan Terpstra — Ported Haihang's native event table stuff to Pentium 4. In the process, I also ironed out a bunch of platform dependencies that showed up when I moved to a new platform. I also returned the native table to an 'opaque' state, accessing it only through guard functions. That way we preserve the option of keeping the native events in a 'virtual table' structure if that makes more sense on a given platform. This stuff triggered changes in the power3 platform as well. Current status: Power3 works as well (I think) as it did before I broke it; Pentium4 compiles and links, but segfaults all tests. All (ALL?) I need to do now is write a new hwd_allocate, hwd_add, hwd_remove and I'm ready to rock...
* 2003-07-10 Dan Terpstra — Call me an old fuddy-duddy, but I really didn't think 'preset' was descriptive enough. These files are pretty empty right now, but will be a good place to put anything that deals with presets -- like the derived code stuff currently in papi_internal.
* 2003-06-27 Haihang You — changes to make power3 compile
* 2003-06-27 Haihang You — modifications to add and remove functions
* 2003-06-27 Haihang You — changes to power3 substrate. now the substrate only handles add_native, counter allocation,and define preset_search_t table.
* 2003-06-27 Haihang You — add and change some predefines
* 2003-06-27 Haihang You — add preset.h preset.c which contains functions to handle hwi_preset calls
* 2003-06-27 Dan Terpstra — Merged some changes from Phil's most recent 2.3.4 commit; added some defines in the .h file.
* 2003-06-23 Dan Terpstra — Moved #ifdefs for native interface stuff so it would link on platforms with HAS_NATIVE_MAP turned off.
* 2003-06-21 Philip Mucci — AMD K8 support for real time functions
* 2003-06-18 Haihang You — add macro HAS_NATIVE_MAP to avoid compilation error
* 2003-06-17 Haihang You — changes to avoid compile conflict between powers and other platforms
* 2003-06-12 Haihang You — Mod to work with modified native event interface
* 2003-06-12 Haihang You — changes native interface functions to make those work with new native event structure. Mod to Makefile.inc to compile nativegen.
* 2003-06-12 Haihang You — This file will get compiled and run at compile time. It will generate native.h and native.c files which contain native events info. Currently it only support power3 and power4.
* 2003-06-10 Dan Terpstra — Tweaks to support Pentium IV on perfctr 2.4.5 with Opteron stuff present. Also changes in calling sequence for a couple routines. BTW, zero now aborts. Gotta check that out...
* 2003-06-10 Dan Terpstra — POWER3 Makefile changes to move allocate.c and support AIX 5
* 2003-06-09 Dan Terpstra — Changes to get POWER platforms to run under PAPI3. This is a work in progress. Both POWER3 and 4 compile and link; POWER4 passes zero.c; POWER3 still needs some work. WARNING: These changes WILL BREAK other substrates. The calling sequence on some routines has changed...
* 2003-06-03 Nils Smeds — Fixed function prototype error in overflow.c, commented out incorrect event swapping in _papi_hwd_set_overflow. Overflowing works, but the test case is not quite PAPI3 ready.
* 2003-06-03 Nils Smeds — Fixed function prototype error in overflow.c, commented out incorrect event swapping in _papi_hwd_set_overflow. Overflowing works, but the test case is not quite PAPI3 ready.
* 2003-06-03 Nils Smeds — First cut AMD Opteron support added. This is based on the perfctr-p4 substrate as this currently was the most PAPI3-like perfctr substrate around.
* 2003-06-03 Nils Smeds — First cut AMD Opteron support added. This is based on the perfctr-p4 substrate as this currently was the most PAPI3-like perfctr substrate around.
* 2003-06-02 Zhou Min — In Itanium, since it supports hardware overflow and profile, now the default is to use hardware support to implement overflow and profile
* 2003-06-02 Zhou Min — upgrade from papi2 to papi3 in Itanium platform, now overflow and profile works, but still more works to do
* 2003-05-30 Dan Terpstra — One more time: Tweaks to get these files to run successfully on PAPI 2.3.4.x. Folded in code from PAPI3 for allocate.c and native event stuff.
* 2003-05-29 Dan Terpstra — Tweaks to get these files to run successfully on PAPI 2.3.4.x. Now it's time to morph them into PAPI 3.
* 2003-05-28 Dan Terpstra — Created and referenced aix.h, power3.h, power4.h
* 2003-05-28 Dan Terpstra — Split aix-power.c into aix.c, power3.c and power4.c in anticipation of port to PAPI3. Next step is to create aix.h and power{3,4}.h. Then begin morphing into PAPI3 calling conventions.
* 2003-05-28 Dan Terpstra — Minor tweaks.
* 2003-05-21 Zhou Min — change the first parameter of _papi_hwd_add_event from  hwd_register_map_t * to EventInfo_t *
* 2003-05-21 Zhou Min — change the first parameter of _papi_hwd_add_event from  hwd_register_map_t * to EventInfo_t *
* 2003-05-20 Zhou Min — add a function _papi_hwi_counter_reorder(EventSetInfo_t *ESI, u_long_long *hw_co unter, u_long_long *events);  which reorder the counters from hardware order to events order and if one  event is a derived event, this function will do the appropriate calculation.
* 2003-05-20 Zhou Min — add a function _papi_hwi_counter_reorder(EventSetInfo_t *ESI, u_long_long *hw_counter, u_long_long *events);  which reorder the counters from hardware order to events order and if one  event is a derived event, this function will do the appropriate calculation.
* 2003-05-20 Joseph Thomas — Updated substrate-specific structure names to generic ones.
* 2003-05-20 Dan Terpstra — More changes in EventInfo structure: hardware_index and operand_index were mutually exclusive, so they were replaced with a single value: counter_index.
* 2003-05-20 Dan Terpstra — More changes in EventInfo structure: hardware_index and operand_index were mutually exclusive, so they were replaced with a single value: counter_index.
* 2003-05-20 Dan Terpstra — Changes in EventInfo structure to support EventSet optimizations.
* 2003-05-20 Dan Terpstra — First cut implementation of _papi_hwd_reset()
* 2003-05-20 Dan Terpstra — Better error reporting on PAPI_reset.
* 2003-05-15 Dan Terpstra — Code cleanup & fixes for PAPI3. Time to move on from Pentium 4. It's by no means done, but the only stuff failing now is overflows and profiles. Some because of multi-event event sets, and some with vperfctr_control errors in papi_start. Still an awful lot of SKIPs though...
* 2003-05-15 Dan Terpstra — Fixes for PAPI3
* 2003-05-13 Dan Terpstra — Convert calls to PAPIf_rem_event() into PAPIf_remove_event()
* 2003-05-13 Dan Terpstra — A few more fixes. Zero actually counts events, now...
* 2003-05-12 Dan Terpstra — Added notes regarding warning about use of PAPI_accum() with rate-based derived events.
* 2003-05-11 Joseph Thomas — Updated the initialization process of the mdi structure.
* 2003-05-09 Joseph Thomas — Updated mdi initialization functions.
* 2003-05-09 Joseph Thomas — New initialization of mdi structure.
* 2003-05-08 Dan Terpstra — Fix for uninitialized mdi structure.
* 2003-05-08 Dan Terpstra — Fix for infinite loop allocation of eventsets. MULTIPLEX flag was being tested improperly.
* 2003-05-08 Dan Terpstra — More cleanup for PAPI3 / Pentium4
* 2003-05-07 Dan Terpstra — Changes to get P4 to build for PAPI3. Getting closer. hwi_presets need to not be declared const so the avail flag can be set. Many tests now pass; some still segfault.
* 2003-05-07 Dan Terpstra — Changes to get P4 to build for PAPI3. Not there yet: It compiles & links, but segfaults on every test...
* 2003-05-02 Dan Terpstra — First commit of hardware independent code for PAPI 3. Be forewarned: This code compiles and links ON WINDOWS (don't ask). It doesn't yet RUN anywhere. No warranties are expressed or implied for any platform. Your milage may vary. Next step: rebuild the Pentium 4 substrate...
* 2003-05-02 Dan Terpstra — First commit of hardware independent code for PAPI 3. Be forewarned: This code compiles and links ON WINDOWS (don't ask). It doesn't yet RUN anywhere. No warranties are expressed or implied for any platform. Your milage may vary. Next step: rebuild the Pentium 4 substrate...
* 2003-05-02 Haihang You — to generate libpapi64.a and libpapi64.so.
* 2003-05-02 Haihang You — small fix in _papi_hwi_llokup_thread_symbols(). tests in 64 bit mode run as well as 32 bit mode
* 2003-05-01 Haihang You — small fix of the value END_OF_TEXT and END_OF_DATA
* 2003-05-01 Haihang You — create Makefile.aix-power4-64bit for power4 64 bit mode compilation. remove flags for 64 bit compilation in Makefile.aix-power4 add an entry for Makefile.aix-power4-64bit in Makefile add defines of start and end of text and data in aix-power.c
* 2003-04-24 Dan Terpstra — Removed unused variable in do_both()
* 2003-04-24 Dan Terpstra — Fixed a declaration of unsigned long_long for Windows compatibility.
* 2003-04-24 london — Fixes for Windows substrate
* 2003-04-22 Philip Mucci — Added I/D/Total TLB Events for the Pentium 4
* 2003-04-21 Dan Terpstra — Adding html version of the PAPI 3 Cookbook to cvs.
* 2003-04-17 Dan Terpstra — Remerged 2.3.4
* 2003-04-17 Dan Terpstra — Remerged 2.3.4
* 2003-04-17 Dan Terpstra — Remerged 2.3.4
* 2003-04-17 london — Merging files, testing checkin
* 2003-04-17 Dan Terpstra — Remerged 2.3.4
* 2003-04-17 london — Changes from 2.3.4 merged back in
* 2003-04-16 london — Fixes so itanium compiles and runs.
* 2003-04-16 london — Fixes so P4 will compile in the main branch
* 2003-04-15 Dan Terpstra — Fixed some merge problems from yesterday.
* 2003-04-14 Dan Terpstra — Merged from 2.3.3 branch
* 2003-04-14 london — A few typos in the file.
* 2003-04-11 Haihang You — changes to make PAPI run in 64-bit mode on power4
* 2003-04-11 Shirley Moore — restored first line which had gotten deleted somehow
* 2003-04-11 Dan Terpstra — Split the Windows wait_exit routine into two routines: wait and wait_exit. wait comes in very handy for debugging when the system smokes!
* 2003-04-10 Dan Terpstra — Minor tweaks to the UI, including changing tests to ctests.
* 2003-04-10 Dan Terpstra — Various changes to make the driver work on AMD (finally!).
* 2003-04-10 Dan Terpstra — Various changes to make the driver work on AMD (finally!).
* 2003-04-10 Dan Terpstra — Various changes to make the driver work on AMD (finally!).
* 2003-04-08 Philip Mucci — Added patches for new redhat kernels. Normally, we never do a CVS add to an external distribution, we use CVS import. But this time, we're hacking it up a bit.
* 2003-04-08 Nils Smeds — Fix for hopefully correct functionality of multiplexing of rate events (PAPI_IPS and PAPI_flops). mpx_events->stop_values[] was incorrectly set for rated events.
* 2003-04-07 london — Setting tolerance by event 1 and then checking against event 2. Changed to check against event 1 and things work.
* 2003-04-05 Zhou Min — fix bugs for itanium with pfmon-1.1 remove earprofile.c since it is only used in version 3
* 2003-04-05 Zhou Min — fix bugs for itanium with pfmon-1.1
* 2003-04-04 Philip Mucci — Ok, from now on, anyone who checks in a #define into a test.c file will be flogged with Udon noodles. All test definitions have been moved to test_utils.h. No more #def NUM in these tests.
* 2003-04-04 Philip Mucci — First, fixed initializer for last element in hwd_structure. It's amazing what a lot of compilers don't catch. gcc -Wall did though.
* 2003-04-04 Philip Mucci — Unified all test definitions to test_utils.h, this includes
* 2003-04-03 Nils Smeds — Added a summary table in the verbose output as per the other sdsc* tests.
* 2003-04-02 Haihang You — fixes to make calls follow 3.0 API
* 2003-04-02 Dan Terpstra — Fixed a bogus assertion error on AMD. It failed if more than 2 counters...
* 2003-04-02 Dan Terpstra — Added functionality to the shell to test the winPMC driver and monitor driver version #
* 2003-04-02 Philip Mucci — Oops, when I fixed the total instructions/total cycles bug, I forgot to propagate it to Model 2 PIV's. (Sorry Nils. ;-)
* 2003-04-02 london — This was looping on MAXEVENTS and setting blah[i] = blah[i+1], but i+1 on the last element = MAXEVENTS which is invalid.  In this case it didn't matter because we use # of events, but went ahead and changed it to be correct.
* 2003-04-02 london — PAPI_cleanup_eventset calls remove_event, and loops from 0 to Array length, but remove_event compacts the eventset so if you have a 2 array element (1,2)  and you remove event 1, then remove_event compacts it to (2,0) and cleanup_eventset tries to remove event 0 which is invalid.
* 2003-04-02 Nils Smeds — Last(?) fix of bugs detected by the new set of SDSC* multiplexing tests. In order to not get the active events mixed up after a number of adds and removes, remove_event() now packs the EventSetInfo EventInfoArray after each remove.
* 2003-04-02 Nils Smeds — Still some more output. This test now expresses two bugs in PAPI_add/remove_event (I think).   1) After removing a multiplexed event PAPI_list_events return      incorrect list of event codes in the event set   2) In the case of R12K/R14K after the event set has shrunk down      to only one event, when a new event is added, this event is      put _FIRST_ in the event set. This could be platform specific      or it is just that the two intermixed events on other platforms      give more or less the same counts. It is likely that R10K is affected      although the current two events PAPI_TOT_INS and PAPI_TOT_IIS      are too similar to show this.
* 2003-04-02 Nils Smeds — More detailed table output to debug screwed up PAPI internal tables. Hopefully only SGIs are involved in this...
* 2003-04-01 Nils Smeds — The DESCR lines got mixed up between the two IRIX makefiles. The 64bit ABI makefile had the line for the n32 ABI and vice versa. To catch the case where the sysadmin has set the default ABI to 64bit in /etc/compiler.defaults we should perhaps consider to explicitly set -n32 in the FLAGS?
* 2003-04-01 Dan Terpstra — Changes to test files that I forgot to check back in when I merged the 2.3.3 branch last week.
* 2003-04-01 Dan Terpstra — Changes to test files that I forgot to check back in when I merged the 2.3.3 branch last week.
* 2003-04-01 Dan Terpstra — Modify shell app to display the driver version.
* 2003-04-01 Dan Terpstra — Minor variable declaration tweaks for consistency.
* 2003-04-01 Dan Terpstra — Add a version query function to the Windows driver.
* 2003-04-01 Philip Mucci — Removed the 'inline' definition for debugging with non-GNU compilers.
* 2003-03-31 Philip Mucci — Added error return check to the pthread_attr_setscope call. After all, no performance counter interface can measure user threads.
* 2003-03-31 Philip Mucci — Removed threads target from Makefiles. IRIX has never had a 1:1 pthreads library without adding special capabilities to the system. See the man page for pthread_attr_setscope and capabilities if you don't believe me.
* 2003-03-31 Dan Terpstra — Fix for long long overflow identified by the guys at Rice.
* 2003-03-31 Shirley Moore — updated dadd-alpha.README with new locations of DADD files
* 2003-03-31 Philip Mucci — Pentium 4 ifdefs added.
* 2003-03-31 Philip Mucci — You cannot overflow on something that takes up more than one physical counters. This means no overflow on PAPI_FP_INS. So what? Who counts FP_INS overflows anyways?
* 2003-03-31 london — Added a check for P4 and PAPI_EINVAL to skip instead of failing, this occured in overflow where more than 1 event was in the eventset.
* 2003-03-31 Dan Terpstra — This 'fixes' Per's reported problem, at least in the main trunk. Don't know what's happening in the 2.3.3 branch. I thought I introduced these problems when I merged from 2.3.3. That may or may not be true. My fixes make it compile; they may not fix the logic.
* 2003-03-30 london — Changed 128 to PAPI_MAX_STR_LEN
* 2003-03-30 london — Changed destination str from 128 to PAPI_MAX_STR_LEN There was a strncpy and since i came after the dest str everytime PAPI_label_event was called, i got reset to 0, so the program looped indef.
* 2003-03-30 Philip Mucci — Minor cosmetic changes to get rid of "\n" Added dump of uname -a
* 2003-03-30 Philip Mucci — Various build fixes. All sdsc tests now use the NUM_FLOPS variable. Upped the multiplex tolerance to 0.1 as busy systems with lots of events are prone to this. Edited test_skip to do better output.
* 2003-03-30 Philip Mucci — More fixes for the IRIX platform. Better native event handling and fixed the error in rem_event that was not removing the correct counter from the num_on_counter array.
* 2003-03-30 london — Somehow do_test was moved from the bottom of the file to the top of the file and it relied on a global array that was defined after.
* 2003-03-29 Dan Terpstra — Bunch of stuff I fixed earlier but forgot to check in. Adds memory stuff to Windows substrate.
* 2003-03-29 Philip Mucci — Lots of overflow threshold fixes. this code was ugly, ugly ugly.
* 2003-03-29 Philip Mucci — Added get_memory prototypes.
* 2003-03-28 Philip Mucci — Fixed the bug manifested by sdsc.c.
* 2003-03-28 Dan Terpstra — Fixed example of use of PAPI_num_counters. We were flagging error on retval != PAPI_OK. Should have been error on retval <= PAPI_OK.
* 2003-03-28 Dan Terpstra — Added Phil's discussion of import vs. add for third party modules.
* 2003-03-28 Philip Mucci — Multiplexing bugs fixed in pentium 4 when total cycles were used with total instructions.
* 2003-03-28 Philip Mucci — These fixes needed a variable initialized. Please initialize variables before you use them, especially floating point ones. Uninited FP vars can cause exceptions and all kinds of guff.
* 2003-03-28 Philip Mucci — Last IRIX bugs fixed. This bug turned out to be a major bug in PAPI.c. When we removed an event, we were setting the EventInfo.selector to 0, but the substrate checks for PAPI_NULL, which certainly is not 0. I'm amazed this hasn't broken other platforms of PAPI_rem_event, but then, who really uses PAPI_rem_event that often?
* 2003-03-28 Dan Terpstra — Added quick description of how to merge branches back to the main trunk. For more detail, search the web for "cvs merge branch"
* 2003-03-28 Dan Terpstra — Oops. I left a bunch of junk at the end of the file.
* 2003-03-28 Dan Terpstra — Updated HISTORY file with changes contributed by the team for PAPI 2.3.4. Please read this file and modify your contributions for correctness or clarity as needed.
* 2003-03-28 Dan Terpstra — Updated HISTORY file with changes contributed by the team for PAPI 2.3.4. Please read this file and modify your contributions for correctness or clarity as needed.
* 2003-03-28 Philip Mucci — This commit fixes the multiplexing bug on the IRIX platform. The only remaining bug is that of sdsc4-mpx, to be fixed tomorrow.
* 2003-03-25 Shirley Moore — updated dadd-alpha.README with new locations of DADD files
* 2003-03-22 Philip Mucci — One line change can make all the difference
* 2003-03-22 Philip Mucci — REAL Pentium IV register allocation. Fixes bugs reported by Frank Desano
* 2003-03-21 Zhou Min — merge changes from papi-2-3-4 to head branch
* 2003-03-21 Zhou Min — merge changes from papi-2-3-4 to head branch
* 2003-03-21 london — Fixes to support libpfm 1.1, this wouldn't even compile for libpfm 1.1 as it used 2.0 specific calls.
* 2003-03-21 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-21 Philip Mucci — Added Pers improved locks
* 2003-03-21 Philip Mucci — New and improved locks from Per
* 2003-03-21 Philip Mucci — Forgot to replace shared target
* 2003-03-21 Philip Mucci — Added the branch test instead of branches-mpx, try it on your Itaniums today!
* 2003-03-21 Philip Mucci — Finally, real working branch events for Itanium I and II. Plus bug fixes in the pfmwrap layer that was corrupting memory.
* 2003-03-20 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-20 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-20 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-20 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-20 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-20 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-20 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-20 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-20 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-20 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-20 Dan Terpstra — Merging changes from papi-2-3-3 branch back into main trunk
* 2003-03-19 Zhou Min — delete some useless code and fix some minor bug
* 2003-03-19 Haihang You — fix to itanium negtive number problem
* 2003-03-19 Dan Terpstra — Event name corrections for Power4
* 2003-03-19 Dan Terpstra — Minor tweaks in native event stuff. Power4 does not yet support native event mapping the way Power3 does.
* 2003-03-19 Haihang You — fix itanium negtive number problem
* 2003-03-19 Philip Mucci — New lock code from Per checked in, added PAPI_BR_INS for Itanium 2, deprecated it from Itanium 1. Users should be warned about events that use opcode matching.
* 2003-03-19 Philip Mucci — Added PAPI_BR_INS for itanium 2 and branch test case
* 2003-03-19 Dan Terpstra — Folded in some pathing changes that had been made on the 2-3-3 branch.
* 2003-03-19 Dan Terpstra — Changed comment syntax from C style (/* */) to make style (#)
* 2003-03-18 Haihang You — use addr_t instead of using (unsigned long) for do_reads and do_flops. It would fail on power3. addr_t seems safer.
* 2003-03-18 Haihang You — mask off native bit of EventCode in _papi_add_event
* 2003-03-18 Dan Terpstra — Fixes for POWER4 build: allocate.h should not be included for this architecture.
* 2003-03-18 Philip Mucci — Improved safety for P4 overflows. Only one counter per eventset is supported if you use this functionsality.
* 2003-03-18 Dan Terpstra — New and/or modified tests for use with self-describing native events. So far only implemented on Power3 and 4.
* 2003-03-18 Philip Mucci — Added interrupt support for Pentium IV. This should allow vprof to work in some scenarious.
* 2003-03-17 Dan Terpstra — Added support for self-describing native events. This platform is interesting, since all the data is stored in a pminfo structure and provided for free at run-time.
* 2003-03-17 Dan Terpstra — First cut support for platform independent native events. Substrates must be modified to support this functionality. Use -DHAS_NATIVE_MAP in the Makefile to enable this code. One new API has been added to papi.c to facilitate enumeration of native event tables. Otherwise the PAPI event description calls should work as expected.
* 2003-03-17 Nils Smeds — The tolerance of 3% as too tight on at least the IBM system I test against. 4-5% occurs not too infrequently so I increased the tolerance level to 8%
* 2003-03-17 Nils Smeds — Fixes to make adding multiplex events more robust. If adding events fail mpx_insert_events, the changes made are undone properly. Previously, a failing mpx_insert_events could result in incorrect usage counts and minor memory leakage.
* 2003-03-17 Nils Smeds — Fix a long_long overflow error in variance computations. Missed an explicit cast to (double) before squaring...
* 2003-03-15 Philip Mucci — Ok, more makefile fixes. All builds well now.
* 2003-03-15 Philip Mucci — Ok, last minute build fixes for these platforms. Guess what? MPX_NONDECR was not set in multiplex.c. Now all platforms should report good numbers for multiplexing, with exception of Pentium 4. Makefile.linux-perfctr and the other have been merged via an include.
* 2003-03-15 Philip Mucci — *** empty log message ***
* 2003-03-15 Philip Mucci — Fixed locking functions. using these could cause your program to hang. In fact, it caused clockres_pthreads to hang. Thanks to Rick for catching this one. The fix was to use different routines from /usr/include/asm/bitops instead of the other file.
* 2003-03-15 Philip Mucci — New locking functions. Per Eckman caught these bugs on the IA64 and they turned out to exist on IA32 as well. Portability is not always a great thing eh?
* 2003-03-14 Zhou Min —  papi-2-3-3 doesn't support native events in itanium&itanium2 with libpfm2.0
* 2003-03-12 Nils Smeds — Protect a call against NULL pointers in mpx_remove_event(). This occurred in case2 of ctests/multiplex1 (PAPI_cleanup_eventset) and case1 in ctests/multiplex2 (also in PAPI_cleanup_eventset).
* 2003-03-12 Nils Smeds — Multiplexing fix. Primarily fixes the problem reported by Timothy Kaiser, SDSC. Together with today's updates to papi.c this commit also enables proper functionality of PAPI_rem_event of multiplexed event sets.
* 2003-03-12 Nils Smeds — Multiplexing fix. Primarily fixes the problem reported by Timothy Kaiser, SDSC. Together with today's updates to papi.c this commit also enables proper functionality of PAPI_rem_event of multiplexed event sets.
* 2003-03-12 Nils Smeds — Missed to update the EventInfoArray in my previous change. Still not quite confident it's done the right way.
* 2003-03-12 Nils Smeds — To make PAPI_destroy_eventset work also for multiplexed event set the event counter must be adjusted in papi.c accordingly. Also, to reduce the amount of memory leakage in the multiplex case the multiplex structure is now free'd by free_EventSet()
* 2003-03-12 Nils Smeds — Missing include of <errno.h> when compiled with -DDEBUG
* 2003-03-10 london — Backed out -qnostdinc
* 2003-03-08 london — OO should be O0 (yeah I know they look the same ;) But last should be zero, not an O)
* 2003-03-07 Philip Mucci — Build fixes to improve optimization on the recent IA64.
* 2003-03-07 Philip Mucci — Minor note to remind people to link /usr/src/linux to /usr/src/linux-2.4
* 2003-03-07 Philip Mucci — Added proper include path for these two files. /usr/include/dcpi
* 2003-03-07 Philip Mucci — Added including the pmapi toolkit to the libpapi.so shared library on AIX5.1. This OS hasa real run-time linker. Yeah!
* 2003-03-07 london — PAPI_MAX_PRESET_EVENTS was added to the strings but not added to the definition which messed up the synchronization, thanks Rick.
* 2003-03-07 london — Somehow INCLUDE=-I.. was lost, in the 2.3.3 release
* 2003-03-07 london — Changes made as suggested by Rick and Per
* 2003-03-06 Zhou Min — make some format change so that it can be complied successfully in itanium&itanium2
* 2003-03-06 Philip Mucci — Upped the iteration count in both tests.CVS: ----------------------------------------------------------------------
* 2003-03-06 Philip Mucci — Shared library changes. Added MAX_PRESETS to genpapifdef.c
* 2003-03-06 Philip Mucci — Removed TOOLPATH include line from Makefile. Fixed patchs to actual papi include files in papi_test.h
* 2003-03-06 Philip Mucci — Added fpapi_test.h that includes the appropriate fortran include files. All fortran tests should just include fpapi_test.h now.
* 2003-03-05 Zhou Min — changes made to match native.c in itanium&itanium2
* 2003-03-05 london — Changed to match tenth.c so Power 4 should pass now.
* 2003-03-04 Zhou Min — add a test file for branch trace buffer
* 2003-03-04 Zhou Min — Add Branch Trace Buffer support for PAPI_profile_hw, when the user use PAPI_BR_INS or native branch_events as the profile event, then the substrate can use the Branch Trace Buffer to extract the accurate branch instruction address as the profile address.
* 2003-03-04 london — Added support for perfctr-2.4.5 at Shirley's request for the papi-2-3-2 branch, I should be using import as Phil suggested, but I haven't looked up the semantics, but I will start using that for the main branch.
* 2003-03-04 london — Update to match 2.3.2 branch, I am sure there is a cvs command to do this automagically, but for the time being it was quicker to do it by hand.
* 2003-03-04 london — Fixing various fails to make that should pass (Like creating directories)
* 2003-03-04 Joseph Thomas — Minor changes to unsigned long long variables for uniformity.
* 2003-03-04 Joseph Thomas — Minor changes to unsigned long long variables for uniformity.
* 2003-03-03 london — Fixes for Cray T3E
* 2003-02-28 Dan Terpstra — Ooops. Need to include papi_test.h, not test_utils.h.
* 2003-02-28 Dan Terpstra — Changed Windows project files to reference source in ctests instead of tests.
* 2003-02-28 london — Need to include headers
* 2003-02-28 Zhou Min — remove support for pfmlib 0.06A and pfmlib-1.1 change the machine dependant structure in itanium/itanium2 increase PAPI_MAX_STR_LEN to 120
* 2003-02-27 london — Ignore failed mkdir
* 2003-02-27 Joseph Thomas — EventSetInfo is now EventSetInfo_t (in name only for the time-being).
* 2003-02-27 london — The ctests directory disappeared on the 2-3-2 branch after moving the tests to ctests directory, which possibly means other branches have lost it as well.  I am not sure renaming directories via mv in /cvs/homes is the best option if this is the case, I will check into it.
* 2003-02-26 Dan Terpstra — Rolled variable types from u_long_long back to long_long. Windows can't convert from unsigned long long directly to double. This seemed the easiest way around it. Also cast the output of the PAPI timing routines to long_long.
* 2003-02-26 Haihang You — remove codes for PFM06A which we don't support any more
* 2003-02-26 Dan Terpstra — Changes to let cpuid and linux-memory.c co-exist peacefully in the Win32 substrate. Required hiding local routines behind statics to avoid namespace collisions. Also required MASM syntax assembly constructs in linux-memory.c. These are hidden in #ifdefs. There is much duplicated functionality in cpuid, but for now it should work...
* 2003-02-26 Dan Terpstra — Ooops. Scoping will get you every time. PRESET_MASK was defined in papi_internal.h. That doesn't make it available to user code. I moved it from papi_internal.h to papiStdEventDefs.h
* 2003-02-26 london — This got removed
* 2003-02-26 Haihang You — add PRESET_MASK define
* 2003-02-26 Philip Mucci — Removed DBG from papi.h, Kevin, please tell me where this breaks
* 2003-02-26 london — Updated Makefile to work with ctests
* 2003-02-26 Philip Mucci — Added cast to (caddr_t) for prof->offset.
* 2003-02-26 london — Modified like the 2.3.2 branch
* 2003-02-26 Dan Terpstra — Mods in preparation for the definition of PAPI Native Events. The change in StdEventDefs.h is cosmetic and stylistic, but I prefer to use #defines instead of hard-coded bit patterns where possible. Native Event Tables become necessary for Cray X1, where the bit pattern for a native event requires 64-bits, plus a chip designator...
* 2003-02-26 Dan Terpstra — Mods to allow windows to use the same substrate header as linux-perfctr.
* 2003-02-26 Dan Terpstra — Mods to allow windows to use the same substrate header as linux-perfctr.
* 2003-02-26 Dan Terpstra — Mods to allow windows to use the same substrate header as linux-perfctr; Addition of a getpagesize() routine for windows
* 2003-02-26 Dan Terpstra — Mods to allow windows to use the same substrate header as linux-perfctr.
* 2003-02-26 Dan Terpstra — Mods to merge windows substrate definitions with linux-perfctr. This makes file naming a bit funky, but allows ia32 windows and linux substrates to share a common header file -- much easier for revision control.
* 2003-02-26 Dan Terpstra — Replace abort() with return(ESBSTR) for _papi_hwd_set_profile() and _papi_hwd_stop_profiling(). Part of the goal of eliminating abort()s where possible, and making substrates more consistent.
* 2003-02-25 london — Switched from tests to ctests
* 2003-02-25 Shirley Moore — added call to PAPI_shutdown before exit in test_skip and test_fail (needed on Alpha/DADD and shouldn't hurt elsewhere)
* 2003-02-25 Shirley Moore — changed LDFLAGS to new standard location of DADD library
* 2003-02-25 Shirley Moore — added _papi_hwd_stop_profiling dummy routine
* 2003-02-25 Shirley Moore — include and macros so that getpagesize is defined on the Cray T3E
* 2003-02-25 Shirley Moore — include and macros so that getpagesize is defined on the Cray T3E
* 2003-02-25 london — Fixes in 2-3-2 branch
* 2003-02-24 Joseph Thomas — Removed unnecessary check for NULL from several updated functions.
* 2003-02-21 Shirley Moore — changed ftests target to use FTOPTFLAGS instead of FOPTFLAGS - Fortran tests now pass on the T3E
* 2003-02-20 london — Forgot to make the default directory ./papi-2.4.5
* 2003-02-20 Nils Smeds — Removed #include <asm/system.h> as it seems not to be needed for libpfm-2 and it caused compilation problems on some systems. Now that support for older libpfm versions has been dropped this _should_ be safe.
* 2003-02-20 london — Readded Makefile.linux-perfctr, I changed the Makefile to support all perfctr versions with a simple editing of the Makefile, basically uncomment the version you want to use and put the location of the perfctr in correctly.  With this, I am going to remove all old perfctr versions, if someone wants to use an old version they can download it from Mikael's website and it will still work.
* 2003-02-20 Zhou Min — these programs now can be run in intanium2
* 2003-02-20 Zhou Min — Change the native event definition in itanium and itanium2, Add hardware profile , Data EAR events support in itanium2
* 2003-02-19 london — Removed perfctr-2.4.1 because 2.4.5 is compitable with the patches in 2.4.1, no need for both.  perfctr was removed, as I am not sure what was in that but it looked like a 2.4.1 or 2.4.0 release.  Makefile was updated, pruning of unneccesary directories will continue :)  And perfctr 2.4.5 is tested and working.
* 2003-02-19 london — This is the second time I have had to add ftests to the examples flag in the Makefile, make sure that this stays in the Makefile!
* 2003-02-19 london — New Makefile for the new perfctr stuff
* 2003-02-19 london — Added the perfctr-2.4.5 directory, hopefully this will work with none or minimal changes to PAPI
* 2003-02-19 london — These Makefiles are no longer relevant
* 2003-02-19 london — Removing Perf, that is really old at this point, no reason in keeping dead weight
* 2003-02-19 london — Removal of pfmon-1.1, from this point on libpfm 2.0 should be used
* 2003-02-19 london — Removing old libpfm, the next release will only support libpfm 2.0+
* 2003-02-19 london — Pfmon Removed for cleanup purposes, only libpfm 2.0 is supported from this point on.
* 2003-02-16 Haihang You — allocate.o only get compiled on power3 now
* 2003-02-14 london — EV7 was not being determined correctly, and missing a function. Thanks Paul.
* 2003-02-13 Haihang You — change #ifdef PAPI3.0 to #ifdef PAPI30 because it would cause compilation warnings on Power some small error fixes
* 2003-02-12 Haihang You — allocate.* contain our new counter allocation functions. remove those functions from aix-power.c, and did some modification in aix-power.h and Makefile.inc to make it compile as well
* 2003-02-12 Haihang You — this file contains predefined Native events, User can directly use the Native event's name without doing bit shift. This file should be included in user's code. Currently it only support power3. Maybe Itanium soon...
* 2003-02-12 Joseph Thomas — Updated the current function calls listed in papi.h making them pass variables in the same manner as the new version of PAPI.
* 2003-02-11 Nils Smeds — Now, being better educated, -Wall is in the commented part of the Makefile instead.
* 2003-02-11 Nils Smeds — Re-inserted a -Wall into CFLAGS. It must have gotten lost. We do want -Wall in the bug release don't we?
* 2003-02-11 london — Total cycles is a pain, expanded the range of correct values.
* 2003-02-11 london — These aren't supported on Itanium2 yet.
* 2003-02-10 london — Apparently too much optimization on the library, destroys profiling on Itanium, I will look into this more after the bug release.
* 2003-02-10 london — Removal of overlapping eventset tests
* 2003-02-10 london — Removal of overlapping eventset tests since Pentium 4 doesn't support it, and future releases won't either.
* 2003-02-10 london — Ooops accidently put -DITANIUM2 in topflags rather than optflags
* 2003-02-10 london — Itanium2 doesn't support native events, yet.
* 2003-02-10 london — Removed -DDEBUG, etc... from the Makefile for up and coming bug release.
* 2003-02-10 london — Itanium2, doesn't support hardware overflow....yet...
* 2003-02-09 london — Expanded the range of good values, cycles tend to depend on the load.
* 2003-02-09 london — Another printf changed to a DBG statement
* 2003-02-08 london — Only hardware support for libpfm2.0+, so I put a ifdef in to set early versions to no hardware support.
* 2003-02-08 london — The addresses for the various start/end segements were commented out and set to 0, I am not sure why, but this of course broke all the profiling. So if there was a reason on WHY this was commented out, please send a message to papi@cs.utk.edu
* 2003-02-08 london — Removed a printf and changed it to a DBG statement
* 2003-02-08 london — This should be PAPI_ESBSTR NOT PAPI_ESYS, sys means there is a system error, not that it isn't supported.
* 2003-02-07 Zhou Min — *** empty log message ***
* 2003-02-07 Zhou Min — *** empty log message ***
* 2003-02-07 london — ftests got removed from the examples directory, so they weren't being made by default.
* 2003-02-07 london — test_fail needed one more argument, IE the return value of why it failed.
* 2003-02-07 london — Ooops forgot to include the substrate so I could pick up DBG.
* 2003-02-06 Nils Smeds — This is Per Ekman's patch to fix the "events returned out of order" problem that was reported by Frank Deserno. The fix is to rebuild the selector bit pattern after each PAPI_add_event for all events in the event set involved. This is necessary as the underlying libpfm substrate reorders the counters.
* 2003-02-06 Zhou Min — earprofile.c used to test Data EAR events in itanium profilehw.c  test hardware profile support in itanium
* 2003-02-06 Zhou Min —  add two test files  earprofile.c  profilehw.c
* 2003-02-06 Zhou Min — add a function _papi_hwd_stop_profiling()     PAPI_profile_hw() to use hardware profile support in itanium
* 2003-02-03 london — Comments about mappings that nils didn't find in his version of the mappings.  All but one were IA64 calls, which will eventually be moved out most likely, the last one is listed as x86, that I found in the cpuid section of sandpile.org No code changes, just comments so if/when memory is rewritten we can remove those cases, if IA64 can't be merged with the x86 memoryinfo.
* 2003-02-03 Nils Smeds — Updated acquisition of memory information at library init:   - Support for Xeons (in perfctr-p4.c)   - TLB size now reported in number of entries (both Intel and AMD)   - TLB size for Intel CPUs is set up   - For AMD (which has 2 level TLB) the Data TLB and Instr TLB refers     to the number of entries in the L2 cache. The total number of entries     in the TLB is set to the sum of the L1 and L2 TLBs capabilities   - Several fixes to try to get the associativity reported correctly for     AMD CPUs   - For CPUs with a trace cache (Xeon/P4) the instruction cache is the     number of micro-ops (in Ks) instead of the cache size in KB. To     indicate this the line length is indicated as being 0.   - Something went strange with the inline assembler code ni my compiler     so I rewrote the cpuid inline assembler. I hope I got it right. The     numbers I get now are at least reasonable for the platforms I've     checked, even when compiling with optimization.
* 2003-01-31 london — Finished dynamic memory support for IA64 support.
* 2003-01-31 london — A few fixes, fix so linux-ia64 will compile, hopefully will have full support for ia64 later this afternoon. Unicos will be a while, at least till I can get access to a machine ;)
* 2003-01-31 london — Added support for dynamic memory information for solaris systems. It is possible that this will break on some solaris systems if it doesn't follow the /proc filesystem that is like linux.  All, our systems have this, so hopefully this won't be a problem.  In addition since I read in a binary file with sizeof(struct psinfo), if you compile this on one system and move it to a system with a slightly different psinfo structure, the results will be undefined (IE most likely crash and burn :) )
* 2003-01-31 london — Added dynamic memory support for aix platforms.
* 2003-01-31 Nils Smeds — Modified Intel P4 not yet supported to instead read: "not supported by this substrate"
* 2003-01-30 london — Support for dynamic memory information added for Alpha
* 2003-01-30 london — Removed a // comment Don't use // style comments in c files, since not all c compilers support them!!!
* 2003-01-30 london — Added declaration of touch_dummy function, to quiet warnings.
* 2003-01-30 london — Dynamic Memory information added for All linux OS's, ie IA64, IA32, and alpha linux.
* 2003-01-30 london — The ioctl of course wasn't that portable, I moved the call to the memory calls which are OS dependant, which should work with the ioctl. More checkins coming :)
* 2003-01-30 london — Initial dynamic memory support, only tested on an SGI, so if builds break on other platforms, yell at me ;) New command:  long PAPI_get_dmem_info(int option) Option can be one of: PAPI_GET_SIZE      - Size of process image in pages PAPI_GET_RESSIZE   - Resident set size in pages PAPI_GET_PAGESIZE  - Pagesize in bytes
* 2003-01-30 Nils Smeds — This must have been a typo earlier. This is how I interpret the Intel manual for the ESCR_T?_{OS,USR} bits.
* 2003-01-30 Nils Smeds — This is seems to be a working way of simulating a PAPI_reset for IA32 P4 in PAPI v.2. I did not touch the PAPI v.3 stuff.
* 2003-01-28 london — Removed comment
* 2003-01-28 london — Added new man page for getting memory information and updated hardware_info to see also the memory info.
* 2003-01-27 Nils Smeds — Typo in man (and HTML) page: Changed eventset to eventcode
* 2003-01-22 Philip Mucci — Added native_install target
* 2003-01-22 Philip Mucci — Initial revision
* 2003-01-21 Philip Mucci — Added typecast to caddr_t
* 2003-01-21 Zhou Min — Add this makefile to support libpfm2.0 in itanium
* 2003-01-21 Zhou Min — fix a minor bug in pfmwrap.h
* 2003-01-21 Joseph Thomas — *** empty log message ***
* 2003-01-21 Joseph Thomas — *** empty log message ***
* 2003-01-13 Nils Smeds — This is the patch suppied by Per Ekman, pek@pdc.kth.se providing the following:
* 2003-01-10 london — Added another test case that tries to add all available events one at a time, start/stop the eventset.  This test doesn't do any verification that the results are correct, simply that all of the mappings can indeed be used.
* 2003-01-10 london — First example, document simple and added the enviroment variable code here that was taken out of papi.c
* 2003-01-05 Nils Smeds — Expanded slightly on the test and added some informative descriptive output about what's going on.
* 2003-01-05 Nils Smeds — Modified printf format statements to remove compile time warnings on the IA32/Linux platform. Hopefully not creating warnings on other platforms by this. Only a cosmetic change, so feel free to roll back if it causes more problems than it saves.
* 2003-01-05 Nils Smeds — Renewed implementation of "non-decreasing" multiplexing counters. With PAPI compiled with -DMPX_NONDECR (default option) consequtive PAPI_read of the same event will never give decreasing results.
* 2003-01-04 Nils Smeds — -mpentiumpro is deprecated, new syntax is -march=pentiumpro
* 2003-01-04 Nils Smeds — Somehow a #define DEBUG had slipped into the CVS, removed now
* 2003-01-03 Nils Smeds — x86-events.h is not created by the Makefile any more and the contents is not used anyway so I removed ``#include "x86-events.h"´´
* 2002-12-18 Philip Mucci — Added '-' to chmod's in A) Added native_install target to B)
* 2002-12-17 Philip Mucci — Changes as recommended by Nils Smeds. smeds@pdc.kth.se
* 2002-12-16 Nils Smeds — Suggested implementation of two new functions. > int PAPI_get_multiplex(int EventSet); Inquire an eventset about if it is multiplexed or not > int PAPI_initialized(void); Is the PAPI library initialized?
* 2002-12-12 Philip Mucci — Fixes to make profiling 64 bit clean
* 2002-12-11 Philip Mucci — Build mendes-alt with the appropriate -DMULTIPLEX flag.
* 2002-12-11 Philip Mucci — Removed assert in MPX-shutdown causing failure of mendes-alt test case
* 2002-12-11 Philip Mucci — This fixes a bug reported on November 12th by Mike Marty. PAPI_rem_event wasn't working properly on this platform.
* 2002-12-11 Philip Mucci — All definitions transcribed from the IA32 Manual to p4_events.h.
* 2002-12-10 Philip Mucci — When using mkdir one must remember that it will cause an ERROR if it already exists. Use a '-' in front of it please in directories other than papi/src.
* 2002-12-10 london — Removed PAPI_add_env_event
* 2002-12-06 Nils Smeds — Documentation bug in the example code. PAPI_num_counters returns a non-negative number upon success. It only returns PAPI_OK on successful completion on a system with no counters...    :)
* 2002-12-05 london — Added a new function PAPI_add_env_event(int *EventSet, int *EventCode, char *env_variable)
* 2002-12-05 Dan Terpstra — Changes to make any-null work with the new memory structures. Thanks to Rick Kufrin for identifying this!
* 2002-12-04 Zhou Min — update the metrics of cache line size
* 2002-12-04 Zhou Min — set TLB size in irix machine
* 2002-12-04 Zhou Min — get the L1 data cache and L1 instruction cache size and L2 cache size
* 2002-12-04 Philip Mucci — Fixes for perfctr targets
* 2002-11-26 Haihang You — new power3 register allocation has made native event mapping easier and more effective. some words for user added in aix-power.README
* 2002-11-26 Haihang You — new power3 register allocation implementation. for native events, it will choose available register which the event can live on for you. So user need not think about native event mapping, when create a natve event EventCode.
* 2002-11-20 Philip Mucci — More shared library make fixes. Linux perfctr p4 now points to the latest perfctr release.
* 2002-11-17 Philip Mucci — More make fixes
* 2002-11-15 london — Removed at Paul Drongowski's request
* 2002-11-15 london — Added -lIEPCF90 -lF90 -lintrins Apparently the intel compiler needs this as reported by Rick Kufrin. Thanks Rick :)
* 2002-11-14 london — Commented out the following events: PAPI_L1_LDM, PAPI_L1_STM, PAPI_L2_DCM, PAPI_L2_LDM, PAPI_L2_STM They won't run even as a single event with memory.c, the encoding must be wrong, will try to figure it out later but doing the mapping on a P4 is the same as beating your head against a table, many times ;)
* 2002-11-14 london — Removed TOT_INS and FP_INS at same time as this currently doesn't work for P4.
* 2002-11-14 london — Changed so PAPI_set_debug is only called if tests aren't quiet
* 2002-11-14 london — Tests should be totally quiet except for PASSED/SKIPPED/FAILED in TESTS_QUIET mode.
* 2002-11-14 london — Added a PENTIUM4 define for native in Fortran, we really need to write a program that grabs the model number in fortran like we do in c.
* 2002-11-14 london — Added check to see if simultaneous eventsets are allowed.
* 2002-11-14 london — Changed TOT_INS & FP_INS to FP_INS & TOT_CYC Also, p4 still skips this as reset counters isn't supported yet.
* 2002-11-13 london — Check added for p4, haven't coded anything in yet, so this just skips currently (better than a coredump ;) )
* 2002-11-13 london — Didn't check to see if we actually had any valid events to count
* 2002-11-13 london — Changed events from TOT_INS & FP_INS to FP_INS/TOT_CYC or TOT_INS/TOT_CYC because p4 can't handle TOT_INS & FP_INS yet......
* 2002-11-13 london — P4 support doesn't support simultaneous eventsets running, so skipped the tests that do this with NO_SIMULT_EVENTSETS definition
* 2002-11-13 london — Typo fixed
* 2002-11-13 london — Changed _papi_hwd_add_event to return event not available when selector is == -1, not 0 because ffs(x) -1 would return -1 when not available. Phil, since you did the p4 substrate, am I missing anything? Stops the coredumps anyway :)
* 2002-11-01 Philip Mucci — Various path and flag fixes. Needed for 2.3 release.
* 2002-10-31 Philip Mucci — Added PAPI 2.3 version of the Pentium 4. Note that this has PAPI 3 like features like no-overlapping eventsets, so some test cases will fail. The register allocation scheme is non-existant. At the moment, whatever registers are specified in the preset is what register is programmed. Overflowing, Multiplexing, Profiling and Threading are all untested. But the zero test case runs, so that's enough for most for now.
* 2002-10-30 Dan Terpstra — Slight tweaks in the text.
* 2002-10-30 london — Changed an error message to debug only.  mpx_shutdown_timer was trying to shutdown a timer twice on solaris threaded programs (Basically it was being called multiple times), but shutting down twice doesn't hurt anything so I removed the error message from the regular build
* 2002-10-30 Dan Terpstra — Modified error messages to provide more context.
* 2002-10-30 Dan Terpstra — Modified to remove compile warnings, and to fix multiplex tests on sun.
* 2002-10-29 Dan Terpstra — For some reason, everything but this source file had been checked in.
* 2002-10-28 Shirley Moore — Changed OPTFLAGS from -g to -O
* 2002-10-28 Shirley Moore — fixed typo in ifdef
* 2002-10-28 Shirley Moore — call to dummy needed for Alpha
* 2002-10-28 Shirley Moore — enabled multiplexing on Alpha
* 2002-10-28 Shirley Moore — enabled multiplex tests for Alpha
* 2002-10-28 Shirley Moore — disabled overflow and enabled multplexing on Alpha
* 2002-10-28 Shirley Moore — added check for divide by zero
* 2002-10-28 Shirley Moore — fixed typo in README_DADD updated virtual_counters structure in virtual_counters.h
* 2002-10-27 Nils Smeds — PAPI_start reset counters, this is clear from the PAPI Software Specification, but not clear enough for me in the man page.
* 2002-10-25 london — Added UTILOBJS to the tests that didn't have that as a dependency
* 2002-10-25 Nils Smeds — Dummy arrays need to be initialized to NNaN (not NaN)
* 2002-10-25 Nils Smeds — The unicos-t3e substrate is named unicos-e5 :( This caused ftests/test_utils.F to be compiled without -O0
* 2002-10-25 Nils Smeds — The (still commented out) call to dummy(r) modified to be proper C
* 2002-10-25 Nils Smeds — No optimization on the CrayT3E requires -O0
* 2002-10-24 Philip Mucci — Revised error checking for PAPI_thread_init
* 2002-10-24 london — Converting to int * before check, seems to remove the NaN segfaults, (floating point exceptions).
* 2002-10-24 london — A few more modifications, probably still broken on the alpha.
* 2002-10-24 london — Slightly enlarged acceptable values for total cycles since these tests sometimes fail on an Alpha.
* 2002-10-24 london — Hopefully this fixes the segfaults on Alpha, someone want to verify?
* 2002-10-24 Dan Terpstra — Minor tweak to suppress unwanted printf on TESTS_QUIET in case 4
* 2002-10-24 Nils Smeds — >Arrays must be defined with constants not preinitialized variables on POWER Arrays must be defined with the right size ;-)
* 2002-10-24 Dan Terpstra — Arrays must be defined with constants not preinitialized variables on POWER.
* 2002-10-23 Philip Mucci — Updated for the new directory structure and notes about setting the APIC for the kernel.
* 2002-10-23 london — Removed C++ comment (//) as not all c compilers compile cleanly with this.  In the future we should use standard c /* */ style comments.  Also, as a side note if you compile the memory stuff with c++ comments in it, you all of a sudden need root to access the registers, go figure.....
* 2002-10-23 london — Extended range on error checking for total cycles
* 2002-10-23 Nils Smeds — I should now that it is [i][j] in C and not [i,j] :(
* 2002-10-23 Nils Smeds — Overhaul over the test case. The initial intention was to make sure that we tested both overflowing on event 0 and on event 1. Now it is back at this. The second good news is that this makes the test pass on the T3E again.
* 2002-10-23 london — Ooops changed threshold backdown to test hardware overflow on our AMD but it should really stay high, since most AMD systems probably won't have APIC support turned on unless they are multi-process systems.
* 2002-10-23 london — Changes for PAPI_num_counters broke mixing and matching flops test. Refixed this and added the matrix-hl.c to the test suite.  Guys when you change code, please run the test suite to make sure the fixes don't break something else.
* 2002-10-23 Nils Smeds — ...second try for readable output on the SGI...
* 2002-10-23 Nils Smeds — Missing line-feed added in output message
* 2002-10-23 Nils Smeds — Fix for the non-working PAPI_stop_counters. It turned out that PAPI_stop_counters called PAPI_num_counters which in turn always allocated a new event set for the high-level substrate.
* 2002-10-23 Dan Terpstra — added ref to new man page
* 2002-10-23 Dan Terpstra — added ref to new man page
* 2002-10-23 Nils Smeds — Ooops in previous commit fixed
* 2002-10-23 Nils Smeds — Variable not used warning messages fixed
* 2002-10-23 Nils Smeds — Variable not used warnings on SGI and Linux fixed
* 2002-10-22 Nils Smeds — "Variable used before set" warning fixed
* 2002-10-22 Nils Smeds — PAPI event sets are int and not unsigned (T3E and SGI complains)
* 2002-10-22 Dan Terpstra — new or recently updated html versions of man pages
* 2002-10-22 Shirley Moore — replaced usleep(1000) with sleep(1) on Cray T3E (finished the job for Dan :-)
* 2002-10-22 Shirley Moore — updated to new DADD release added four more events, two of them derived added call to clu_get_info to correctly determine number of nodes
* 2002-10-22 Dan Terpstra — replaced usleep(1000) with sleep(1) on Cray T3E
* 2002-10-22 Dan Terpstra — Removed profile fortran test
* 2002-10-22 Dan Terpstra — __FUNCTION__ is undefined on Windows and Alpha/Tru64. Who knows where else... I just removed it.
* 2002-10-22 Nils Smeds — Simplified event selection that tries to adapt to the platform in question. Now passes on AMD (instead of being skipped due to missing PAPI_FP_INS). The set of events attempted might need to be modified during regression tests on other platforms. But it should at least be a lot easier to make the right changes now.
* 2002-10-22 Dan Terpstra — Removed /t from output statements; suppressed printing of clockrate in QUIET mode; modified verification to compare against proper value.
* 2002-10-22 Dan Terpstra — Modified to accomodate removal of PAPIF_PROFIL external.
* 2002-10-22 Nils Smeds — - PAPIF_get_exe_info is defined with arguments of C_LONG_LONG, not C_INT - PAPIF_num_hwctrs should return C_INT and not C_LONG_LONG
* 2002-10-22 Nils Smeds — It takes a wicked mind to envision that someone wants to profile code using a Fortran interface. It looked good for symmetry, but passing u_short and size_t between Fortran and C will not work easily.
* 2002-10-21 Dan Terpstra — Windows doesn't have access to the #defines in event_codes.h
* 2002-10-21 Dan Terpstra — changed to handle __FUNCTION__ on Windows
* 2002-10-21 Dan Terpstra — changed target file name from .exe to .sys
* 2002-10-21 Dan Terpstra — version number change
* 2002-10-21 Dan Terpstra — syntax changes in some debug outputs for Windows
* 2002-10-21 Nils Smeds — Typo in a output message
* 2002-10-21 Nils Smeds — Pretty-fying of output of test cases. Introduced a new auxiliary function test_print_event_header() that prints a event set content used to be used before printing the counter values. Should also work on win32 if I didn't foul up.
* 2002-10-18 Nils Smeds — Somehow the dollar-signs had gone missing for run_tests.sh -v
* 2002-10-18 london — Upped threshold apparently the resolution of the timer isn't good enough on AMD.
* 2002-10-18 london — Reworked as Itanium would fail on this test when it shouldn't.
* 2002-10-18 Nils Smeds — Modified the error code exit when one or more counters register zero counts. Now it will say "Error calculating" instead of using a PAPI pre-defined internal error message.
* 2002-10-18 london — Added some more TESTS_QUIET conditionals to comply with the simple PASS FAIL that the other test programs follow.
* 2002-10-17 Philip Mucci — Added SHLIBDEPS to dependency of libpapi.so
* 2002-10-17 Philip Mucci — All users should always use Makefile.linux-perfctr from now on.
* 2002-10-17 Philip Mucci — Initial revision
* 2002-10-16 Nils Smeds — #include atomic.h in one place only, and assure that CONFIG_SMP is set at this time to get bus-locking atomic_* operations. This also makes -DPERFCTR24 a noop
* 2002-10-16 Philip Mucci — Missed one definition.
* 2002-10-16 Philip Mucci — Added new test case that measures overflowing with extraneous threads. Added extern TEST_QUIET to papi_test.h, minor debugging print outs in overflow_pthreads.c
* 2002-10-16 Philip Mucci — Fixes for AIX. As it turns out, profiling/overflowing and multithreading were always broken on this platform. I don't think anyone used it so the bug didn't manifest itself until my recent fixes to multiplexing. This was a nasty one. Took me a few days.
* 2002-10-16 london — Made the Added/exist/not exist messages not print if ran in quiet mode.
* 2002-10-16 Nils Smeds — Minor cosmetic change to remove a warning in GCC 3.x about __FUNCTION__ and string concatenation
* 2002-10-15 Dan Terpstra — Initialize the memory structure part of the system_info structure.
* 2002-10-14 Haihang You — add extern int TESTS_QUIET; to avoid compilation error
* 2002-10-13 Philip Mucci — Added new dervied PAPI_l2_DCM for i386 platforms.
* 2002-10-13 Philip Mucci — TEst case for new i386 derived metric L2_DCM
* 2002-10-11 Philip Mucci — PAPI_shutdown now calls MPX_shutdown to remove the global MPX thread list. Eventually the two lists will be unified and this won't be needed.
* 2002-10-11 Philip Mucci — We should be using TOPTFLAGS here instead of OTPFLAGS
* 2002-10-11 london — Had a stop_counters followed by a read_counters.  Removed the read_counters since it wasn't needed.
* 2002-10-11 london — Additions so that you can mix flops/high level calls.
* 2002-10-11 Dan Terpstra — Reduce loop counts to reasonable times for slower machines.
* 2002-10-11 Philip Mucci — Minor build flag fixes for the 2 platforms. -qpwr4 for Power4 -qpwr3 for aix5-power3. All other AIX platforms need -qarch=com.
* 2002-10-11 Philip Mucci — I hate test cases. My code is often more correct that the test cases themselves.
* 2002-10-10 Philip Mucci — Fixed my broken code with side effects.
* 2002-10-10 Dan Terpstra — Updates for 2.3 release.
* 2002-10-10 Shirley Moore — print message rather than failing when error exceeds 10 percent on Alpha/DADD
* 2002-10-10 Shirley Moore — added derived events PAPI_FLOPS and PAPI_IPS to Alpha/DADD substrate add check for divide by zero to PAPI_flops
* 2002-10-10 Dan Terpstra — Minor tweaks for cross referencing
* 2002-10-10 Dan Terpstra — Minor tweaks for cross referencing
* 2002-10-10 Philip Mucci — Small bug fixes w.r.t. presets used.
* 2002-10-09 Philip Mucci — AIX Bulletproof commit. Uses the dynamic linker to find thread functions if necessary.
* 2002-10-09 Dan Terpstra — Update project information to include dummy.c
* 2002-10-09 Dan Terpstra — Changes in masking off PRESET_MASK bit.
* 2002-10-09 Nils Smeds — Typo in test output
* 2002-10-09 Shirley Moore — Changes so that all tests now pass on Cray T3E (except that overflow tests occasionally fail as noted in unicos-ev5.README). Added conditional which Phil had removed back into ftests/Makefile.
* 2002-10-08 Philip Mucci — UltraSparc III fixes. Works on Solaris 5.8, 750Mhz Dual USIII SunFire 800
* 2002-10-08 Philip Mucci — Minor build fixes for going out the door. Mopstly prototypes for linux-memory.c
* 2002-10-08 Philip Mucci — Fortran binding for PAPI_num_hwctrs.
* 2002-10-08 Philip Mucci — Added solaris signal handling fixes. Warning about the Solaris 2.8 setitimer() bug put in the read me file. Basically setitimer() returns an undocumented -EPERM after you've called pthread_create.
* 2002-10-08 Philip Mucci — Super-fancy dynamic loader tricks to fix the situation where multiple threads are spawned outside of the main user module. Multithreaded-MPI for example. This situation occurs on Solaris when using ITIMER_REALPROF and on AIX when using ITIMER_PROF. It just sends a signal to one of the threads at random.
* 2002-10-08 Philip Mucci — Backed out 1.14 changes
* 2002-10-08 Philip Mucci — New PAPI_num_hwctrs API call
* 2002-10-08 Philip Mucci — New API call
* 2002-10-08 Philip Mucci — Added processing of PAPI_num_hwctrs man page.
* 2002-10-08 Philip Mucci — *** empty log message ***
* 2002-10-08 Philip Mucci — Updated the test suites. All these pass with my bug fixes and multiplex enhancements to be checked in, post 2.3.
* 2002-10-08 Philip Mucci — Updated the PAPI_get_virt_cyc call to be high performance, should be a few dozen cycles now
* 2002-10-07 Dan Terpstra — Minor update
* 2002-10-07 Dan Terpstra — Added a few more maskprogrammed events for POWER4 tests.
* 2002-10-04 london — Fix so that you can call flops after calling PAPI_start/stop counters. This does not work the other way around since there is no call to stop flops. I am working out details on that now, and should have something checked in by Monday.
* 2002-10-04 london — Fix so that you can call flops after calling PAPI_start/stop counters. This does not work the other way around since there is no call to stop flops. I am working out details on that now, and should have something checked in by Monday.
* 2002-10-04 Shirley Moore — removed digital ifdef's
* 2002-10-04 Shirley Moore — fixed memory allocation bugs for EventSetInfo latest field
* 2002-10-04 Philip Mucci — Small change to make sure it builds with a prexisting PAPI PerfCtr release
* 2002-10-04 Philip Mucci — Added info for building with a pre-existing PerfCtr distribution and removed USIII warning
* 2002-10-04 Shirley Moore — Change to EventSetInfo structure needed for alpha-dadd
* 2002-10-04 Dan Terpstra — Changes to fix decoding of PAPI events on 64-bit platforms, such as Tru64. Two sets of changes were made: 1. Where it didn't affect exposed interfaces, EventCodes were redefined as     unsigned int rather than int to prevent propagation of the sign bit. 2. In all affected cases, the XOR with PRESET_MASK was replaced with an     AND with PRESET_AND_MASK to guarantee proper indexing for both     signed and unsigned cases when propagated to 64 bits.
* 2002-10-01 Philip Mucci — Added test case for PAPI_describe_event
* 2002-10-01 Philip Mucci — Updated multiplexing to be monotonically non-decreasing and test case Updated linux-perfctr.c substrate for 2.4 release
* 2002-10-01 Philip Mucci — Patched 1.1 release
* 2002-10-01 Philip Mucci — 2.4.0 snapshot
* 2002-10-01 Dan Terpstra — More multiplexing stuff
* 2002-10-01 Philip Mucci — Updated for pfmon-1.1A
* 2002-10-01 Dan Terpstra — Replaced by LICENSE.txt
* 2002-10-01 Dan Terpstra — First cut at a history file. Please review and add info as appropriate.
* 2002-10-01 Dan Terpstra — Replaced by INSTALL.txt
* 2002-10-01 Dan Terpstra — Updated replacement for INSTALL
* 2002-09-25 Shirley Moore — Added back previous changes.
* 2002-09-25 Shirley Moore — Add back previous changes.
* 2002-09-25 Shirley Moore — added call to dummy from do_flops so as to foil the Compaq optimizer
* 2002-09-25 Shirley Moore — Oops -- clobbered Kevin's changes on my previous commit -- they're back now.
* 2002-09-25 Shirley Moore — added full pathname for test executables (needed by DADD on Alpha)
* 2002-09-25 Shirley Moore — added code for Alpha 21364 processor to get_system_info
* 2002-09-24 Dan Terpstra — Updated.
* 2002-09-24 Dan Terpstra — Replaced C++ style comments with C style.
* 2002-09-24 Dan Terpstra — Updated for POWER4 and AIX 5
* 2002-09-24 Dan Terpstra — Updated.
* 2002-09-24 Dan Terpstra — Updated.
* 2002-09-24 Dan Terpstra — Updated.
* 2002-09-22 Philip Mucci — Yes, it's Window's Allegro Common Lisp Bindings. For questions, see Richard Fatemen: fateman@cs.berkeley.edu
* 2002-09-17 london — One more fix for Itanium's, forgot to add memory stuff
* 2002-09-17 Dan Terpstra — minor text tweaks
* 2002-09-17 Dan Terpstra — updated to reflect current reality.
* 2002-09-17 Dan Terpstra — updated to reflect current reality.
* 2002-09-17 Dan Terpstra — Tweaks to the dates to reflect the PAPI 2.3 release.
* 2002-09-17 Dan Terpstra — Rebuilt from man sources for PAPI 2.3 release.
* 2002-09-17 Dan Terpstra — Updated to match current usage.
* 2002-09-17 Dan Terpstra — Updated to match current contents and usage.
* 2002-09-17 Dan Terpstra — This stuff is leftover from an earlier approach by Cricket to creating html from man pages. Supplanted by the manServer_papi perl script.
* 2002-09-17 Dan Terpstra — Replaced by cat_progref.bat
* 2002-09-17 Dan Terpstra — Now actually contains real information! Description of what's in the rest of the directory.
* 2002-09-17 Dan Terpstra — Updated for PAPI 2.3 release.
* 2002-09-17 Dan Terpstra — Updated to fix pathing problems.
* 2002-09-17 london — Fixes to ia64, new memory stuff, caused it not to compile.
* 2002-09-17 Dan Terpstra — More source documentation files for PAPI
* 2002-09-17 seymour — Added a README briefly describing the current state of the JNI wrapper code. Also included a simple example that makes a call from Java to PAPI. keith
* 2002-09-16 Dan Terpstra — FIrst entry of source documentation files (in Word format) for PAPI 2.1
* 2002-09-13 london — Just a dummy file, because Dan's wincvs doesn't checkout empty directories ;)
* 2002-09-13 Dan Terpstra — Replacement for the older COPYRIGHT file.
* 2002-09-11 Philip Mucci — How to use remote CVS? Look here.
* 2002-09-10 Philip Mucci — Added -a option for printing available eventsets suitable for parsing
* 2002-08-30 london — New call const PAPI_mem_info_t * PAPI_get_memory_info() This provides TLB through L3 hardware information. Implemented in linux and aix currently, working on the rest now.  Consider this Alpha at the moment.
* 2002-08-30 london — Latest perfctr release
* 2002-08-30 london — New call const PAPI_mem_info_t * PAPI_get_memory_info() This provides TLB through L3 hardware information. Implemented in linux and aix currently, working on the rest now.  Consider this Alpha at the moment.
* 2002-08-12 Nils Smeds — As results from some work I did for Wompat 2002 I change a number of cache protocol related events on the IA32.
* 2002-08-12 Nils Smeds — Minor Fortran standard fix (strings can not be emtpy in ANSI Fortran)
* 2002-08-12 Nils Smeds — Minor modifications to the 604e event map thanks to the map table submitted by Dong H. Ahn. I am sure that there are may more that can be looked into. Untested, but should be better than what is thre currently (if the events work as documented)
* 2002-08-02 Philip Mucci — Fixed the broken domain counting. User, Kernel, ALL now work nicely...
* 2002-08-02 Philip Mucci — Fixed the overflow case for pthreads. SA_SIGINFO was necessary for this case.
* 2002-07-31 london — Changes to some derived events in the Itanium 2 mapping.  Now all tests pass except second.c which is a domain problem and pthreads_profil which I have not looked at yet.
* 2002-07-31 london — Reversed the order of the events in the PAPI_L1_TCM derived event.  This produces a correct result.
* 2002-07-31 Dan Terpstra — Removed unused reference to x86-events.h
* 2002-07-31 london — This fixes most of the tests that were failing on Itanium 2. I have to send the number of physical counters that have to be read to perfmonctl now.  tenth.c is failing, because of a bad map I believe, second.c, memory.c and profile_pthreads all fail right now.  Expect checkins later today to fix those.
* 2002-07-31 london — Testing
* 2002-07-31 Dan Terpstra — testing
* 2002-07-31 london — Trying to figure out why my checkin messages aren't being sent
* 2002-07-31 Shirley Moore — Added files for the PAPI substrate for Alpha Tru64 Unix over DADD.  DADD stands for Dynamic Access to DCPI Data.
* 2002-07-30 Dan Terpstra — Kevin's got it right. We need to use long_longs not longs for consistency on the FORTRAN side. Longs will change size with the architecture, making the FORTRAN invalid. Long_longs will always be 64 bits, so they'll always map to INTEGER*8. Good catch, Nils.
* 2002-07-30 Zhou Min —  Update PAPI_label_event function because this function use the wrong index to get the event label.
* 2002-07-30 Dan Terpstra — Add error message for MultiProcessor Build.
* 2002-07-29 Philip Mucci — -O2 in the wrong place. tests should never be compiled with optimization.
* 2002-07-29 Philip Mucci — More fixes to support overflow on broken 2.4.16 kernels. Added includes to ftests/do_loops.c that were missing. Adding include sys/ucontect to linux-ia64.h.
* 2002-07-26 Philip Mucci — Removed -static build flag
* 2002-07-26 Philip Mucci — Fixes to the makefile.
* 2002-07-26 london — Changed integers to long_long for the various pointers since 64 bit systems use 64 bit pointers.
* 2002-07-26 london — Fixes so it compiles with pfm-0.6A again
* 2002-07-26 Dan Terpstra — Changes in the native event tables to support AIX 5.1 on 604 and 604e. Unfortunately, it hasn't been tested. I don't have access to such a system and Chris Chambreau @ LLNL is on vacation. Does anyone else have access to a 604/604e running AIX 5.1?
* 2002-07-25 london — Changed TLB_DM and TLB_IM to count only level 2 TLB misses, since that is where you get the overhead.
* 2002-07-25 london — Itanium 2 port
* 2002-07-24 Philip Mucci — Fixes to the global makefile. Please report errors to me.
* 2002-07-23 Philip Mucci — Removed conditional line that snuck in from the Alpha?linux port. Should be unnecessary. Fixed shared lib build on solaris.
* 2002-07-23 Philip Mucci — Removed IA64 hacks to fake out test suite.
* 2002-07-23 Philip Mucci — Removed building things statically...That's no fun at all on NFS
* 2002-07-23 Philip Mucci — Removed conditional code at the beginning of this makefile. This code belongs in the architecture specific makefiles in the top level directory. See tests/Makefile for how this works,
* 2002-07-23 Philip Mucci — Added Makefiles to master Makefile Modified IA64 Makefile to use g77 now that it works. Added back in interrupt support for the IA64
* 2002-07-16 london — Typo bug-fix
* 2002-07-10 Nils Smeds — Fixed un-initialized variable problem reported by Chengyu Sun. The test for test_pass still looks rather crude though. But at least it is correct C now.
* 2002-07-09 london — This is a fix that would cause a Pentium Pro with SMM (System Management Mode) support. This is found on P-Pros with serial numbers that start with sl or Family: 6, Model: 1, Stepping: 9 The problem is RDPMC can't be used in conjuction with SMM because it will believe that reserved space has been altered and enter a shutdown state. The fix right now, is to check the model and stepping and if it has SMM support, shutdown the winpmc service.
* 2002-07-08 london — Updated to perfctr-2.3.9
* 2002-07-05 london — Forgot to turn off debug
* 2002-07-05 london — Update to libpfm 1.1 the official release and prelim McKinley support that has not beed tested yet.
* 2002-07-05 london — Redefined PAPI_FP_INS and PAPI_FLOPS to map onto groups in the standard distribution POWER4.gps file.
* 2002-06-26 Zhou Min — To solve the warning information in papi_fwrappers.c
* 2002-06-26 Dan Terpstra — Fixes to make PAPI_label_event and PAPI_describe_event both accept an EventCode with the high bit set, like every other PAPI routine. Thanks to Leelinda Parker. Also a fix in thread handling to pass the Windows compiler.
* 2002-06-14 Philip Mucci — Fixes from Glenn Laguna [galagun@sandia.gov] for the Alpha Linux platform. Thanks Glenn!
* 2002-06-14 Dan Terpstra — Minor tweaks.
* 2002-06-12 Philip Mucci — Turned on hardware interrupt support for Pentium's by default. Let me know how it goes.
* 2002-06-11 Philip Mucci — Added a snapshot of Glenn Laguna's (galagun@sandia.gov) port of PAPI to the Linux/Alpha/Iprobe platform. Please report bugs to perfapi-devel@ptools.org
* 2002-06-06 Dan Terpstra — Changes for the way POWER4 currently defines PAPI_FLOPS. It counts PM_FPU_FIN and produces results that are consistently too high by 50%. Don't like it, but it works for now.
* 2002-06-06 Dan Terpstra — Changes for POWER4 event support.
* 2002-06-06 Dan Terpstra — Syntax mods for Windows, and event changes for Power4.
* 2002-06-06 Dan Terpstra — Mods for Power4 and to open margins for error testing.
* 2002-06-06 Dan Terpstra — Syntax mods for Windows.
* 2002-06-06 Dan Terpstra — Changes for POWER4 native event support.
* 2002-06-06 Dan Terpstra — New Power3/Power4/AIX4/AIX5 combined code base! - Fixed a bug in Power3 code that caused a crash for native events; - Patched the event names to support AIX 5 changes on Power3; - Changed directory pathing for AIX 5; - Merged code support for Power4 into h and c files:   - several routines are now conditionally compiled for P3 vs. P4; - Added 2 new make files for aix5-power3 and for power4. If someone more knowledgable than me wants to merge these make files, do so with my full blessing! Note that the _POWER4 define is required for conditional compiliation on POWER4. IBM may provide a system define, but I couldn't find one. Also, the P4 event table is still very incomplete. Extra help here would also be most welcome.
* 2002-06-05 Nils Smeds — Nobody's perfect... _NOW_ the parsing of the prtconf tree should work.
* 2002-06-05 Nils Smeds — Modified CPU detection. This is capable of detecting the UltraSPARC-IIe that I passed by. The following changes have been made:
* 2002-06-03 Philip Mucci — Can you believe IBM's xlf90 doesn't recognize a 'C' in Column 1 as a comment string? Someone went out of their way to break F77 compatibility, that what happens when you let engineers have their way. ;-)
* 2002-05-31 london — Now these programs actually check that there is something in the buffers before the tests are passed.  Before, these tests would pass even if the buffers were empty.
* 2002-05-31 Dan Terpstra — Fixed a pointer reference problem Phil introduced with his last round of changes. Gotta watch those warning messages, Phil! They can be deadly on other platforms...
* 2002-05-29 Philip Mucci — Fixed a bug in cleanup_eventset. Please remember that EventInfoArray can be a SPARSE ARRAY of length EventInfoArrayLength(ESI). Valid entries have a code != NULL. This array can be sparse because the user can add 5 events, and delete the first one, resulting in 0 X X X X. So we had better do the right thing.
* 2002-05-29 Philip Mucci — 1) More clean ups to makefile 2) extras.c had a function cleanup_all_master_eventsets that has been changed to    now call _papi_hwd_shutdown on the thread pointer. 3) PAPI_shutdown now does the right things 4) Added new string for error message "Shutdown called with other threads running    Eventsets"
* 2002-05-24 Nils Smeds — Changed nested if statement to elif statements Added elif case for Unicos to make sure ftests_util is compiled w. -O0
* 2002-05-23 Nils Smeds — ftests_util.F should _not_ be compiled with $(FOPTFLAGS), fixed by removing $(FOPTFLAGS) from the rule in the ftests_util.o target.
* 2002-05-23 Nils Smeds — _This_ is a commit of a spelling error in a C comment
* 2002-05-23 Nils Smeds — Fixed incorrect usage of PAPIF_perror in ftests_utils. The correct usage (according to man (3) PAPI_perror) is:        PAPIF_perror(C_INT code, C_STRING destination, C_INT check)
* 2002-05-23 Nils Smeds — The previous commit on this file was particular file was not a fix of a spelling error. Rather it contained some re-indentations and a more refined test of whether to use an alternative event or not:
* 2002-05-23 Nils Smeds — Spelling error in a comment
* 2002-05-21 Philip Mucci — It seems that everyone ignores this file (except me) so I am removing it.
* 2002-05-21 Philip Mucci — 1) Fixed the multiplex routines to work with PAPI_list_events 2) Added a new target to the included makefiles called 'native_install'    See Makefile.linux-perfctr-2.3 for how this works. It now installs the    perfctr library and header file. 3) Added a shared Makefile built to perfctr that is independent of the    perfctr release (for stability) 4) Fixed up shared library building on linux such that it sends the    proper args to the linker when building. For best results, you    had better set your DESTDIR variable at BUILD time. This is because    the GNU linker (and others) can embed the default search patch    into the library eliminating the need for setting LD_LIBRARY_PATH 5) PAPI shared library now correctly links to libperfctr.so. You should    never have to link with anything else other than PAPI now and the runtime    linker should do the rest.
* 2002-05-21 Nils Smeds — Removed the print-out of the event set until we have a working PAPI_list_events for multipexed events
* 2002-05-21 Nils Smeds — Replaced some references to "DOUBLE PRECISION" with "REAL*8" to circumvent complaints from Cray compilers
* 2002-05-18 Nils Smeds — Added utility routine PrintEventSet to ftests_util for easy use in other test routines when need arises
* 2002-05-15 Nils Smeds — Typo in my previous commit. An ">" should have been .GT.
* 2002-05-15 Nils Smeds — Minor modification for (outdated) pmtoolkit 1.2.2
* 2002-05-15 Nils Smeds — Added informative output of content in event sets. Maybe this should be put in ftests_util.F Modified the cpp test to try to identify the aix-power platform
* 2002-05-14 Nils Smeds — Modified fmultiplex1.F to list the events that really get added. Will also print a warning if the CPP case statement in test4 fails on the particular platform.
* 2002-05-10 london — Make dist and install were not working correctly because they were using the wrong substrate c file or wrong substrate Makefile.  Added a new variable MSUBSTR since with linux we have one substrate but several Makefiles.
* 2002-05-10 london — Fixes test failures on AMD: Skips test that fail due to resource conflicts (IE not enough counters) Upped threshold because software timer wasn't fine enough granularity to catch all the overflows.
* 2002-05-03 london — Update to new perfctr 2.3.7
* 2002-05-03 london — Update to new perfctr 2.3.7
* 2002-05-01 london — Split the files, itanium should be working now, I need to still reboot a hp0x machines to test the old pfmon stuff though.
* 2002-05-01 london — Removed to split the Makefile into one for pfmon 1.1 and one for pfmon-06a Really shouldn't need 06a anymore, but just incase someone can't upgrade to the newer kernel needed by 1.1 I will leave it.
* 2002-05-01 london — Was memcpy the wrong structure, which caused problems with native as the last counter wasn't being copied in before it was started.
* 2002-05-01 london — Don't compile pfmon by default, since this requires header files not on all systems.
* 2002-05-01 Nils Smeds — Cray T3Es don't like variables to be of type double precision, changed them to real*8
* 2002-05-01 Nils Smeds — Update to cover R14000 processors. These use the same counter set up as R12000.
* 2002-04-24 london — Port to pfmon-1.1, everything passes except native.c test file.  Will work on that next, need to seperate out another Makefile for pfm06A, since there were quite a few changes between the two, also need to check that PME_INST_FETCH_CYCLE is indeed PME_ITA_UNSTALLED_BACKEND_CYCLE from pfm06a to pfm1.1
* 2002-04-24 Dan Terpstra — Minor mods in error reporting on PAPI_stop
* 2002-04-24 Dan Terpstra — More changes to better utilize counter space: Now maps common metrics to multiple events for higher event availability. Also fixes a bug that prevented metrics from being moved if needed. Tests clean on Joel Malard's 2 event exclusivity test.
* 2002-04-16 Dan Terpstra — Minor cleanup
* 2002-04-16 Dan Terpstra — Don't disable Smoke Test button.
* 2002-04-16 Dan Terpstra — Modification to allow debug dll to install in appropriate directory after successful debug build
* 2002-04-16 Dan Terpstra — Fixed a bug in _papi_hwd_rem_event that would occasionally block a counter from further use. This bug is in code common to most substrates, but was already fixed everywhere except solaris, linux-perf, and Windows.
* 2002-04-16 Dan Terpstra — Fixed long-standing bug in PAPI_start_counters that could leave an event stranded in an event set if a later event could not be added. This could account for some of Joel Malard's problems in allocating events on Power3.
* 2002-04-03 Dan Terpstra — Major rewrite of Power3 substrate in preparation for group-based Power 4 substrate implementation. First, the search table was recast as a dense array of events terminated by a zero event. Next, the add_event logic was reworked to map ALL metrics to their best counter EVERY TIME an event is added. Metrics are mapped from most restrictive to least restrictive. This should result in a much better register utilization. The code has been "white-box" tested; i.e. it passes all the same tests it used to pass. It hasn't yet been "black-box" tested. I would appreciate it if someone could test all possible combinations of events and see if this version does better than what's reported by Joel Malard in /papi/src/aix-power.README...
* 2002-04-03 Dan Terpstra — The threshold was too tight to produce passing results on Power3. I bumped it from 50000 to 100000. It passes now, with about a 10% systematic error.
* 2002-03-18 Nils Smeds — Minor change. Made the substrate more polite, when run on a P4. It now prints a diagnostic message and returns with PAPI_ESBSTR when PAPI_library_init is run. Similarly, it will be more informative for new yet unsupported x86 clones.
* 2002-03-17 Nils Smeds — Missed to make a printf statement conditional on TESTS_QUIET==0
* 2002-03-17 Nils Smeds — Changed a hardcoded 0xdedbeef into its CPP define DEADBEEF.
* 2002-03-17 Nils Smeds — It is polite to fclose /proc/cpuinfo after fopening it...
* 2002-03-15 Nils Smeds — Modified some of the AMD events, removed some that don't exist and added some that I think can be measured. It is still unclear how much information you can get from the MOESI bits.
* 2002-03-15 Nils Smeds — Missed dereferencing a character pointer, fixed now
* 2002-03-15 Nils Smeds — More careful string handling. Removed possible fixed length string overruns.
* 2002-03-15 Nils Smeds — The Unit Mask bits are part of the counter command and need to be set and reset when the counter commands are modified. Up until now the mask bits have only been set, but never cleared ;-)
* 2002-03-14 Nils Smeds — Now recognizes AMD processors and uses native events that are available on that platform.
* 2002-03-14 Nils Smeds — We've got a dual AMD ;-)
* 2002-03-14 Nils Smeds — Cosmetic modification to the output produced by the test.
* 2002-03-11 Dan Terpstra — Changes to support program counter reporting for overflow, profiling. The good news is it looks like it works. The bad news is it now requires at least Windows 2000.
* 2002-03-11 Dan Terpstra — Changes to support program counter reporting for overflow, profiling. The good news is it looks like it works. The bad news is it now requires at least Windows 2000.
* 2002-03-11 Nils Smeds — L2 cache events that relates to instruction fetches is gradually converging. Thanks to Bjarke's experiments L2 I-cache misses (PAPI_L2_ICM) is changed to the event P6_BUS_TRAN_IFETCH (0x68) from P6_IFU_FETCH_MISS (0x81). L1 cache events is still measured using the event P6_L2_IFETCH (0xf28). The reason I stick to L2_IFETCH in favour of IFU_FETCH_MISS is that the former seems to give a 3 times higher count and fulfills the criterium: PAPI_L1_ICM + PAPI_L1_DCM ~ PAPI_L1_TCM. My guess is that IFU_IFETCH_MISS is broken (or at least the documentation is wrong)
* 2002-03-05 Philip Mucci — Removed x86-events.h file. This file is generated by the perfctr distribution. You should use the event_codes.h file found there.
* 2002-03-05 Philip Mucci — Fixes for 2.3.4 and added build of libperfctr.so shared library
* 2002-03-05 Philip Mucci — Fixes for 2.3.4 and added build of libperfctr.so shared library
* 2002-03-05 Philip Mucci — Update to 2.3.4
* 2002-03-05 Philip Mucci — Removed duplicate file
* 2002-03-05 Nils Smeds — After further experiments I've decided to revert the PAPI event mapping to before the discussion with Bjarke on the Ptools/perfapi list. My own experiments still are in favour of the "old" mapping.
* 2002-03-01 Nils Smeds — Modified the event mappings:   PAPI_L1_ICM  ->  IFU_IFETCH_MISS               was (L2_IFETCH)   PAPI_L2_ICM  ->  BUS_ITRAN_IFETCH (Mask=Self)  was (IFU_IFETCH_MISS) because the PAPI_L2_ICM was _definitely_ wrong. For consistency the event mappings:   PAPI_L1_ICH  ->  Modified to still be PAPI_L1_ICA - PAPI_L1_ICM   PAPI_L2_ICH  ->  Modified to still be PAPI_L2_ICA - PAPI_L2_ICM was modified as well.
* 2002-03-01 Nils Smeds — Made the build of PAPI depend on the date of ia32_presets.h
* 2002-02-27 Dan Terpstra — Splits the preset table out of the substrate and into an include file. That way both Windows and Linux can share the same preset data. I've wanted to do this for a while. Nils comments about table updates finally gave me the incentive.
* 2002-02-27 Dan Terpstra — Useful batch files for buidling and/or copying the driver to the appropriate location.
* 2002-02-27 Dan Terpstra — Ooops. I yanked these files from cvs when I shouldn't have....
* 2002-02-25 Shirley Moore — fixed recursive macro definition for FTOPTFLAGS
* 2002-02-22 Philip Mucci — Makefile.linux-ia64: Added -Vaxlib switch for Intel 5.0 and 6.0 efc compilers from Rick Kufrin (thanks!) tests/do_loops.c: Changed indexing on the buffer array to not overwrite the end of the allocated space, from Jacob Ramussen (thanks!)
* 2002-02-21 Nils Smeds — Hardware driven interrupt support for Linux added. In order to work correctly you will need Perfctr 2.3.3 or later, a Linux kernel supporting APIC and use the compile option -DPAPI_PERFCTR_INTR_SUPPORT when you compile PAPI.
* 2002-02-21 Nils Smeds — Added the possibility to use the command line option -v to run_tests.sh to run the tests in verbose mode. Also added a clause to skip the long-running test to overflow the counter (+30min)
* 2002-02-21 Nils Smeds — Makefile update to compile tests/overflow2
* 2002-02-21 Nils Smeds — Cosmetic changes to the output when tests are run in the verbose (default) mode. Added a second overflow case where counter1 is overflowing.
* 2002-02-20 Dan Terpstra — Updates to the structure of the WinPMC project.
* 2002-02-20 Dan Terpstra — Updates to the structure of the WinPMC project.
* 2002-02-20 Dan Terpstra — Updates to the structure of the WinPMC project.
* 2002-02-20 Dan Terpstra — Moved a library reference (winmm.lib) from the project pane to the link line.
* 2002-02-20 Dan Terpstra — Removed extraneous references and made debug and release versions of the projects each dependent on the appropriate WinPAPI library. This is of less use than it may appear, however, since the library is just a wrapper that vectors to the DLL, which in most cases will always be the Release version.
* 2002-02-18 Nils Smeds — For some reason the SHLIBOBJS didn't get into the Makefiles in the repository...
* 2002-02-17 Nils Smeds — This is just a fix for the NCSA request for perfctr 1.6 backwards compatibility. The backfix that was in the release can't have been working. Calling PAPI_get_virt_{cyc,usec} must have resulted in an infinite loop when PERFCTR16 was set at compile time. Now get_virt_usec uses times(2) as previously for PERFCTR16 while for other PERFCTR versions it uses get_virt_cyc which reads the virtual TSC.
* 2002-02-17 Nils Smeds — This fixes the build of x86-events.h in the papi/src directory and makes the copy of libperfctr.o depend on updates made to $(PERFCTR)/usr.lib/libperfctr.o (such as recompiles).
* 2002-02-13 Dan Terpstra — I had checked in the workspace instead of the project for this test. All better now...
* 2002-02-11 Dan Terpstra — Updated info in the Windows read-me file. Shoulda been done before the release, but...
* 2002-02-05 london — Changing default fortran optimization for the tests.
* 2002-02-05 london — Fix to support perfctr 1.6 as well, thanks Rick for pointing this out.
* 2002-02-05 london — Fixes for irix
* 2002-02-05 Shirley Moore — widened PAPI_TOT_CYC check to +-20% so ftests/first and ftests/third pass on the Cray T3E
* 2002-02-05 Dan Terpstra — Updated documentation to reflect the fact that PAPI *DOES* run correctly on a MultiProcessor Build of Windows!
* 2002-02-05 Dan Terpstra — Fix to fail properly from command line if test fails. My last fix was only half a fix.
* 2002-02-05 Nils Smeds — Missed a 1 before X in a format statement
* 2002-02-05 Nils Smeds — Put Fortran77 strings between \' and not \" (I thought the latter was an extension to the language abut no compiler has complained to me so far) Fixed string constants that needed to span over more than one line by use of the concatenation operator //. Which makes the examples print more nicely in g77 and pgf77 at least.
* 2002-02-05 Nils Smeds — Subroutine argument mis-match fixed.
* 2002-02-05 Nils Smeds — Minor cosmetic changes now that the strings get right
* 2002-02-05 Nils Smeds — Mispelling of a pre-processor name fixed. This was the reason why ftests/avail printed so badly (\0 characters weren't removed by the wrapper function)
* 2002-02-05 Nils Smeds — Some lines went past column 72 after TABS removal
* 2002-02-05 Nils Smeds — Sorry, I was wrong. The constants in linux-perfctr.h do fit into default int. The only thing I did was introducing possible overhead. Reverting back to previous version. Default int on Linux is 32bit > #define PERF_CTR_MASK          0xFF000000 [etc...]
* 2002-02-04 Shirley Moore — widened PAPI_TOT_CYC test to +-20% to pass on the T3E (this had already been done in tests/fifth.c)
* 2002-02-04 Shirley Moore — widened PAPI_TOT_CYC check to +-20% to pass on the T3E (this had already been done in tests/fourth.c)
* 2002-02-04 Nils Smeds — I might be wrong, but I _think_ these variables need to be long long or there is risk that using them in masks will not work... diff -r1.11 linux-perfctr.h 47,56c47,56 < #define PERF_CTR_MASK          0xFF000000 < #define PERF_INV_CTR_MASK      0x00800000 < #define PERF_ENABLE            0x00400000 < #define PERF_INT_ENABLE        0x00100000 < #define PERF_PIN_CONTROL       0x00080000 < #define PERF_EDGE_DETECT       0x00040000 < #define PERF_OS                0x00020000 < #define PERF_USR               0x00010000 < #define PERF_UNIT_MASK         0x0000FF00 < #define PERF_EVNT_MASK         0x000000FF --- > #define PERF_CTR_MASK          0xFF000000LL > #define PERF_INV_CTR_MASK      0x00800000LL > #define PERF_ENABLE            0x00400000LL > #define PERF_INT_ENABLE        0x00100000LL > #define PERF_PIN_CONTROL       0x00080000LL > #define PERF_EDGE_DETECT       0x00040000LL > #define PERF_OS                0x00020000LL > #define PERF_USR               0x00010000LL > #define PERF_UNIT_MASK         0x0000FF00LL > #define PERF_EVNT_MASK         0x000000FFLL
* 2002-02-04 Nils Smeds — The Fortran tests was not dependent on libpapi.a and thus was not rebuilt when PAPI was...
* 2002-02-04 Shirley Moore — set TOPTFLAGS and FTOPTFLAGS to -O0 on for Cray T3E in Makefile.unicos-t3e set FOPTFLAGS for ftests target to FTOPTFLAGS in Makefile.inc
* 2002-02-04 Shirley Moore — removed ifdef's for CRAY T3E and Alpha, querying for events should suffice
* 2002-02-04 Shirley Moore — changed to skip if events don't exist, consistent with tenth.c (except that tenth.c calls tests_fail which then calls tests_skip, but this doesn't work in Fortran on the T3E because although the return code from the query is not PAPI_OK, it is also not PAPI_ENOEVNT)
* 2002-02-04 Dan Terpstra — Removed -g and/or  -DDEBUG flags from compile flags for release.
* 2002-02-03 Nils Smeds — Changed some $(OPTFLAGS) into $(FOPTFLAGS) which is the preferred option when compiling Fortran programs when the Fortran compiler does not understand gcc compiler options.
* 2002-02-01 Shirley Moore — fixed Cray T3E ifdef
* 2002-02-01 london — Added the tests being skipped for itanium and alpha as known problems. (overflow and multiplexing respectively)
* 2002-02-01 london — Turn off multiplex for alpha till this can be fixed.
* 2002-02-01 london — Turn off multiplexing for alpha till this can be fixed.
* 2002-02-01 london — Turn off overflowing tests for Itanium till we can fix these.
* 2002-02-01 Dan Terpstra — An image was referenced absolute instead of relative.
* 2002-02-01 london — This is the final commit, it updates genpapifdef with Rick's suggestion, which now builds f77papi.h, f90papi.h and fpapi.h
* 2002-02-01 london — Missed something else..
* 2002-02-01 london — Didn't space out some of the lines far enough...
* 2002-02-01 london — Ok finally got it fixed.
* 2002-02-01 london — I will eventually get this right....
* 2002-02-01 london — This as messed up worse than I thought, Dan, be careful editing Makefiles ;)
* 2002-02-01 london — Somehow this got messed up with TABS in front of the variables and one of the variables being broke up on two lines, most likely someone cut and paste.
* 2002-02-01 london — Removed all the TABS sigh..... Why can't fortran just use TABS.
* 2002-02-01 london — Various fixes to make sure things compile on all platforms.
* 2002-02-01 london — *** empty log message ***
* 2002-02-01 london — Fixes so it works on all platforms
* 2002-02-01 london — Fixes to support 64 bit on irix, Phils changes didn't work so I had to move LIBRARY and SHLIB to the various Makefiles
* 2002-02-01 Dan Terpstra — Useful changes suggested by Nils...
* 2002-02-01 Dan Terpstra — Useful changes suggested by Nils...
* 2002-02-01 london — First round of changes to support ia64, the stuff Phil checked in wouldn't compile
* 2002-02-01 Dan Terpstra — Additional notes suggested by Nils...
* 2002-02-01 Nils Smeds — Removed redundant code
* 2002-02-01 Nils Smeds — Removed Tab characters and re-indented. Inserted line-breaks where CPP expansions caused line to expand beyond column 72
* 2002-01-31 london — Added support for itanium and count the following native events:
* 2002-01-30 london — This fixes a bug when removing things from an eventset, it never decremented the pec_cnt, this was checked in before but I did not reorder the pec_evt array, and this is necessary (I thought it was but tested to make sure).  This now removes old events from the array, this only effected eventsets that you remove less that you added to it, add a different event and then attempt to count it.
* 2002-01-30 london — Added a TOPTFLAGS to all Makefiles, these are the optimizations sent to the test suite.  When a NOOPT was specified (I found this after adding TOPTFLAGS ;), I set TOPTFLAGS to what that use to be, otherwise it is $(OPTFLAGS), when we turn on optimization for the release, we need to maybe change to a lower optimizational level on some platforms.
* 2002-01-30 Dan Terpstra — Minor documentation tweaks.
* 2002-01-30 Dan Terpstra — Restructuring MATLAB code.
* 2002-01-30 Dan Terpstra — Updated documentations for MATLAB flops.
* 2002-01-29 Shirley Moore — added calls to PAPIf_library_init All tests now pass on the T3E.
* 2002-01-29 Philip Mucci — Slight fixes to Makefile for 64 bit libraries.
* 2002-01-29 Philip Mucci — Makefile: Added optimization and better clean targets linux-ia64.README: Note about the scaling of FP_OPS_HI linux-ia64.c: ALWAYS scale FP_OPS_HI even if it is a native event. Sorry IA64 users, I know you will have to change your code, but this is the only way we could get the current setup working.
* 2002-01-29 Shirley Moore — ifdef for CrayT3E so that do_reads is not called in second (no /dev/zero on the T3E); widened PAPI_TOT_CYC verification in second.F to +-20% (as in second.c) so that second passes on the T3E
* 2002-01-29 london — Fix for Yogi, was not passing due to conflicts that shouldn't have existed.  Turns out it was a counter mask declared as a INTEGER*8
* 2002-01-29 london — Oooops typo that was making the program segfault ;)
* 2002-01-29 Dan Terpstra — Restructuring MATLAB code.
* 2002-01-29 Shirley Moore — changes for Cray T3E
* 2002-01-29 Shirley Moore — bug fix, second PAPI_TOT_IIS should be added to CostEventSet
* 2002-01-29 Nils Smeds — PAPI needs to be initialized _before_ calling PAPIf_query_event Removed numerous TAB characters that are not Fortran77 compliant
* 2002-01-29 Nils Smeds — Modified Fortran comments to start with ! in column 1 in fpapi.h. This makes fpapi.h #include-able in Fortran90 compilers that supports CPP
* 2002-01-28 Dan Terpstra — Version number change in info dialog.
* 2002-01-28 Dan Terpstra — Modified to SKIP execution on sun.
* 2002-01-28 Shirley Moore — ifdef's for Cray T3E so that do_reads is not called (no /dev/zero on Cray)
* 2002-01-28 Dan Terpstra — (re-)Clarified wording on FMADD instruction counting.
* 2002-01-28 Dan Terpstra — Bug fixes to earlier changes that dynamically test for FP_INS.
* 2002-01-28 Dan Terpstra — Made Fortran test current with recent C test changes.
* 2002-01-28 Dan Terpstra — Remove debug switch
* 2002-01-28 Dan Terpstra — Changed event table for PAPI_TOT_IIS and PAPI_TOT_INS to only run on counter 2. Although the hardware supports these events on both counters, the software currently cannot reallocate an event at run time. This causes conflicts and failures in some of our tests. The RIGHT solution is to make events dynamically relocatable. The EXPEDIENT solution is to rewrite the event table.
* 2002-01-28 Dan Terpstra — Modified SKIPPED syntax to match test_utils
* 2002-01-28 Dan Terpstra — Added PAPI_TOT_IIS to mask-programmed event list.
* 2002-01-28 Dan Terpstra — Remove a colon from a SKIPPED message. Sooner or later we'll get this right...
* 2002-01-25 Dan Terpstra — Dressup for the output when run in "not TESTS_QUIET" mode.
* 2002-01-24 Shirley Moore — removed comment that said this file should be modified for your platform
* 2002-01-24 Dan Terpstra — More minor output tweaks.
* 2002-01-24 Dan Terpstra — Added Joel Malard's exclusion table as a note. Clarified wording on FMADD instruction counting.
* 2002-01-23 Dan Terpstra — More minor output tweaks.
* 2002-01-23 Dan Terpstra — Remove MPX debug defines.
* 2002-01-22 Dan Terpstra — Calibrate was sick. It looks better now. Needs to be tested everywhere that supports Floating Point except Windows and Power.
* 2002-01-22 Dan Terpstra — Skip PAPI_CA_SHR because it occasionally got 0 counts on power3.
* 2002-01-18 Dan Terpstra — Wrapped a printf in case1 with TESTS_QUIET.
* 2002-01-18 Dan Terpstra — Added serial back to TARGETS
* 2002-01-18 Dan Terpstra — Spelling correction.
* 2002-01-18 Dan Terpstra — Removed -DNO_FLOPS
* 2002-01-18 Dan Terpstra — Elimination of #ifdef NO_FLOPS in all tests. Everything compiles and links on Win and Sparc...
* 2002-01-18 Dan Terpstra — Yet another syntax change to avoid overflow errors on Sparc.
* 2002-01-18 Dan Terpstra — More minor string changes for pretty printing on SKIPPED. Eventually I'm gonna get 'em all...
* 2002-01-18 london — Fix for compile warnings, Itanium complains about TABS as they are an extension to standard Fortran 95
* 2002-01-18 london — Fix to get rid of compile warning on the itanium
* 2002-01-18 london — Typo fixed
* 2002-01-18 Dan Terpstra — Added clockcore to project.
* 2002-01-17 Philip Mucci — Added native_clean target to all platforms. This target removes any native files required for the substrate.
* 2002-01-17 Philip Mucci — Removed the stdin and stdout and stderr files generated by the tester in the Makefiles clean target.
* 2002-01-17 Philip Mucci — Makefile: Changed clean target to do the *right* things
* 2002-01-17 london — Changes to remove reason for skipping when tests are run as quiet. Still gets printed in verbose mode.
* 2002-01-17 Dan Terpstra — More minor string changes for pretty printing on SKIPPED and FAILED.
* 2002-01-17 Dan Terpstra — Syntax error.
* 2002-01-17 london — Fixed Makefile bug, clockres_pthread wouldn't compile on IG.
* 2002-01-17 Dan Terpstra — Minor fixes for NO_FLOPS
* 2002-01-17 london — ANother typo introduced by removal of NO_FLOPS PAPI_events should have been PAPI_event
* 2002-01-17 Shirley Moore — fix for T3E getarg
* 2002-01-17 london — Fixed more warnings and undefined mask1 introduced by the NO_FLOPS stuff being removed.
* 2002-01-17 Shirley Moore — use PAPI_TOT_IIS if can't use PAPI_TOT_INS with PAPI_TOT_CYC (e.g., on the T3E)
* 2002-01-17 Shirley Moore — added multiplex target so that multiplex tests get built on T3E
* 2002-01-17 Dan Terpstra — Next pass at getting rid of #define NO_FLOPS for platforms without a FP instruction counter.
* 2002-01-17 london — This was incorrectly indexing EventCode, causing segfaults.
* 2002-01-17 london — Small fixes to prevent warning messages on linux.
* 2002-01-17 Dan Terpstra — First pass at getting rid of #define NO_FLOPS for platforms without a FP instruction counter.
* 2002-01-17 Dan Terpstra — More minor string changes for pretty printing on SKIPPED.
* 2002-01-17 Dan Terpstra — Removed an unused retval.
* 2002-01-16 Philip Mucci — Added 3 more events for the USIII.
* 2002-01-16 Philip Mucci — Ok folks,
* 2002-01-16 Dan Terpstra — Removed unreferenced variable.
* 2002-01-16 Dan Terpstra — Added automatic post-build generation of fpapi.h
* 2002-01-16 Dan Terpstra — Removed third-inv
* 2002-01-16 Dan Terpstra — Minor changes in post-build commands.
* 2002-01-16 Dan Terpstra — Added prototype for rand_r
* 2002-01-16 Dan Terpstra — Added code to support processor affinity. It still works on a single processor; now it needs to be tested on a multi-processor system...
* 2002-01-16 Dan Terpstra — Modified string formatting for {PASSED FAILED SKIPPED} conditions to provide prettier output and make the tests easier to scan.
* 2002-01-16 Dan Terpstra — Changed several long long declarations to long_long so that Windows won't complain.
* 2002-01-16 Dan Terpstra — Addded a dummy rand_r() routine to Windows as needed by mods in multiplex.c. Someday I'll need to go back and make that routine real...
* 2002-01-16 Philip Mucci — Better assert handling. Note that if you start threads before you use PAPI and then attempt to use either profiling or multiplexing, the code will fail. Why? Because there's a bug in Solaris setitimer()
* 2002-01-16 Philip Mucci — Fixed iteration definition in clockcore.c. The large number of stack memory was overflowing with a bunch of threads. The result?
* 2002-01-15 Philip Mucci — This commit should fix the problem where someone tries to multiplex a derived event. In other words, if you only have 2 counters on your system, and your trying to multiplex a derived event that requires 2 counters, it won't work because multiplexing needs to count PAPI_TOT_CYC along with whatever you are counting.
* 2002-01-15 london — Added a new test timer_overflow.c to check if a timer will overflow ;)
* 2002-01-15 Philip Mucci — There is no floating point instruction counter on the UltraSparc. Sorry folks!
* 2002-01-15 Philip Mucci — Added a new test case from John May, demonstrating a bug that currently shows up on AIX with multiplexing and extraneous threads. This has yet to be verified on other platforms.
* 2002-01-14 Philip Mucci — Fixed a bug on the athlon.
* 2002-01-12 Philip Mucci — Ok, this commit fixes a couple of things.
* 2002-01-11 london — Too big of a max value on linux, adjusted down for query the events verbosely.
* 2002-01-11 london — Updated to perfctr-2.3.3
* 2002-01-11 Dan Terpstra — Minor change to eliminate null-string warnings on Power.
* 2002-01-10 Dan Terpstra — Changes to handle native event initialization on AIX.
* 2002-01-10 Dan Terpstra — Comment out a couple unused variables in MPX_shutdown()
* 2002-01-10 london — Fixes pec_count not being decremented by removing an event, without this if you add and remove 4 events, the 5th one being added will not work.
* 2002-01-10 Shirley Moore — fixes for the Cray T3E; all tests now pass on the T3E
* 2002-01-09 Shirley Moore — added #ifdef's for CRAYT3E. Because John May's code assumes that PAPI_TOT_CYC can be used simultaneously with any other event without requiring multiplexing, and on the T3E, PAPI_TOT_CYC and PAPI_TOT_INS are on the same physical counter, PAPI_TOT_INS cannot be multiplexed on the T3E with the current code.  Other than that, multiplexing seems to work on the T3E.
* 2002-01-09 Shirley Moore — removed multiplex1_pthreads from MPX target and added new target MPXPTHR
* 2002-01-09 Dan Terpstra — Fix to suppress expected error messages.
* 2002-01-09 Dan Terpstra — Updated to fix error references.
* 2002-01-09 london — Changed PAPI_NOEVNT to PAPI_ENOEVNT
* 2002-01-08 Dan Terpstra — Removed mpi from TARGETS.
* 2002-01-08 Philip Mucci — Added comments about native events to README files.
* 2001-12-20 Dan Terpstra — Changes for new MatLab documentation.
* 2001-12-20 Dan Terpstra — Minor compile problem with null strings on Power
* 2001-12-18 Dan Terpstra — Updated spec for PAPI 2.1 release. You're welcome, Shirley.
* 2001-12-18 london — Fixed things being reversed on the two rows and their checks. How did this pass on anything else?
* 2001-12-18 Shirley Moore — minor grammatical edits
* 2001-12-18 Philip Mucci — Added thread info
* 2001-12-18 Philip Mucci — This commit fixes the but as reported where PAPI_set_domain does not act as excpeted. It appears someone hacked the code and didn't quite understand what it was supposed to do.
* 2001-12-17 Dan Terpstra — Added switch settings to Linux patch instructions.
* 2001-12-17 Dan Terpstra — Comment out definitions of unused variables.
* 2001-12-17 Dan Terpstra — Code error in call to PAPIf_library_init: would have worked with PAPI_VERSION == 1, but failed when PAPI_VERSION was set to 2. Has this been tested on all platforms?? Also, these routines (still) don't validate results, in both C and Fortran...
* 2001-12-17 Dan Terpstra — Make lines for multiplex 1 and 2 were incorrectly including 2 copies of ftests_util.o. This caused lots or errors on Linux-x86.
* 2001-12-14 Dan Terpstra — Minor polish of Kevin's major revision.
* 2001-12-14 Dan Terpstra — Release build of dlls.
* 2001-12-14 london — Removed and put in main directory
* 2001-12-14 london — Updated Install
* 2001-12-13 london — Added installation information on PAPI, including how to patch a kernel, etc.. Still need to add install information for the Alpha OS patch, and I need to find out if that is standard or is a special patch and where to get it. Also, I need to find out what software is required for SV1, SV2.
* 2001-12-13 london — Incremented the Current Version to 2, since some of the data structures will cause segfaults if you use an older header file.  Updated for the Friday release.
* 2001-12-13 london — Cast the ints to long long before doing the multiplication.
* 2001-12-13 Dan Terpstra — New format for MatLab / PAPI interface.
* 2001-12-13 Dan Terpstra — Minor documentation correction.
* 2001-12-13 Dan Terpstra — Updates for PAPI 2.1 Release.
* 2001-12-13 Dan Terpstra — Updates for PAPI 2.1 Release.
* 2001-12-13 Dan Terpstra — Addition of a few more manpages.
* 2001-12-13 Dan Terpstra — Deletion of a few unneeded leftover constants.
* 2001-12-13 Dan Terpstra — Minor tweaks on horizontal rule positioning.
* 2001-12-12 london — Updated to perfctr 2.3.2
* 2001-12-12 london — Updated to perfctr 2.3.2
* 2001-12-12 london — This was calling the wrong function and was segfaulting. It was calling PAPIf_set_domain instead of PAPIf_set_event_domain
* 2001-12-12 zlong — Passed $CC when making ftests.
* 2001-12-12 zlong — Removed do_reads implemented in Fortran, which doesn't work well.
* 2001-12-12 zlong — Changed fmultiplex1 and fmultiplex2 tests to call do_reads implemented in C (do_loops.c).
* 2001-12-11 london — Typo in second.F fixed, wasn't compiling before.
* 2001-12-11 Dan Terpstra — Fix for scaling of FMAs  on MIPS and Sparc.
* 2001-12-10 Philip Mucci — Added new code to support the UltraSparc III. None of that code has been tested as we don't have access to the platform. Also, added code for that platform to use the hardware overflow feature of the hardware.
* 2001-12-10 Dan Terpstra — Reorganized EXPORT list to allow for future expansion. Incorporated recently added routines. DANGER WILL ROBINSON: These changes will cause older test binaries to break when run on a new dll!
* 2001-12-10 Dan Terpstra — Rearranged routines to more closely match order in papi.c
* 2001-12-10 Dan Terpstra — Removed duplicate prototype for PAPI_state.
* 2001-12-07 Dan Terpstra — Added wrappers for PAPI_label_event, PAPI_lock, and PAPI_unlock to flesh out the Fortran interface.
* 2001-12-05 Dan Terpstra — Minor tweak of an error code returned by PAPI_thread_id to make it consistent with predefined values (it was returning -1).
* 2001-12-05 Dan Terpstra — Added PAPIf_thread_id to complement PAPIf_thread_init; Renamed PAPIf_set_domain1 to PAPIf_set_event_domain, Hopefully, this is more descriptive of its function.
* 2001-12-05 zlong — fixed a small bug in calculating total cyc/call pair
* 2001-12-04 zlong — fixed a small problem.
* 2001-12-04 zlong — Added two test cases for multiplex.
* 2001-12-04 zlong — Added multiplex function wrappers.
* 2001-12-04 seymour — Adding Java native wrappers to PAPI.  Some of the low-level functions are still unfinished, but most of it is there.  At this point, the code is primarily for experimentation and as such is not thoroughly tested.
* 2001-12-01 Shirley Moore — bug fix in get_system_info().  tests/profile now works. tests/sprofile fails with   open(/dev/zero): No such file or directory added dump_infoblk() for debugging
* 2001-11-29 london — Fixed a few typos
* 2001-11-29 Dan Terpstra — Reinstituted the pause() routine for Windows. Shirley, let me know if this is a problem for Cray.
* 2001-11-29 Dan Terpstra — Minor output formatting tweaks.
* 2001-11-29 Dan Terpstra — Removed implementation of PAPIF_get_all_events_verbose As implemented, it was redundant with PAPIF_get_event_verbose Since I don't know how to pass an array of structures back to Fortran, the simpler implementation is for Fortran to call PAPIF_get_event_verbose in a loop.
* 2001-11-29 Dan Terpstra — Removed call to PAPI_get_all_events_verbose and replaced with call to PAPI_get_event_verbose in a loop. See PAPI_fwrappers for reasons.
* 2001-11-29 Dan Terpstra — not used anymore
* 2001-11-28 Shirley Moore — ifdefs for Cray T3E
* 2001-11-28 Shirley Moore — ifdefs and bug fixes for Cray T3E
* 2001-11-28 london — Small fix should have returned P3 was returning P2
* 2001-11-27 Shirley Moore — added #include <limits.h>
* 2001-11-26 Dan Terpstra — Changes for updated look to documentation pages.
* 2001-11-26 Dan Terpstra — These were originally checked in as text. They are now rechecked as binary.
* 2001-11-26 Dan Terpstra — These were checked in as text. They need to be rechecked as binary.
* 2001-11-22 Nils Smeds — + Higher resolution virtual timers (micro-second resolution) for   linux-perfctr + Hook for developing support for overflow interrupts   (-DPAPI_PERFCTR_INTR_SUPPORT). Compiling without setting this   will still produce a working PAPI library with the same software   overflow as earlier.
* 2001-11-22 Nils Smeds — Fixed typo in output
* 2001-11-20 zlong — return PAPI_ESBSTR (Not supported in the substrate) in set_inherit functions.
* 2001-11-19 Dan Terpstra — Removed scaling for FMA and SLOPE from PAPI_flops call. Flops and other high level calls produced confilcting results, which are inconsistent with low level results. We decided that any fudging of the raw numbers should happen at a higher level than the PAPI code itself.
* 2001-11-15 zlong — a small fix.
* 2001-11-15 zlong — header.htm and footer.htm contains the header and footer of man pages. manServer_papi.pl will read them when converting man pages to html.
* 2001-11-15 zlong — Updated to read from header.htm and footer.htm when converting man pages into html.
* 2001-11-15 zlong — check in the image files needed by man pages.
* 2001-11-14 london — Typo fix in PAPI.3
* 2001-11-08 Dan Terpstra — Mapped virt_usec and virt_cycles onto their real counterparts, since they didn't work as is, and we're only measuring system wide anyway...
* 2001-11-08 Dan Terpstra — Minor fix to get TESTS_QUIET to work on Windows
* 2001-11-08 Dan Terpstra — Set all project line lengths to 132 to support __FILE__ expansion in preprocessor.
* 2001-11-08 Dan Terpstra — Conditional definition of DEBUG
* 2001-11-08 Dan Terpstra — Minor tweaks on smoke_test code
* 2001-11-07 Nils Smeds — PAPI_accum seemed not to have been updated for multiplexing support. This is probably how it should look. Phil?
* 2001-11-06 Dan Terpstra — Change project settings to remove optimizations on do_flops(). This makes all tests PASS!
* 2001-11-06 Dan Terpstra — Output format changes to match c version more closely.
* 2001-11-06 london — Removed Added Adding from being printed when TESTS_QUIET.
* 2001-11-06 Shirley Moore — added LDFLAGS to resolve getarg in ftests
* 2001-11-06 Dan Terpstra — Add / update projects for Windows Fortran tests and samples.
* 2001-11-06 Dan Terpstra — Parameter type corrections on strtest; Mods to ftests_util to allow Windows to pause for a keypress before exiting; Addition of cpause.c for Windows only, to implement the pause on exit.
* 2001-11-06 Nils Smeds — When accumulating values the array should be initialized first.
* 2001-11-05 Dan Terpstra — Added more DLL entry points for Fortran calls.
* 2001-11-05 Dan Terpstra — Added Smoke Test and Perfometer buttons. Added Fortran Tests & separated from C tests. Provided graceful failure path for multiprocessor installations.
* 2001-11-05 Dan Terpstra — This test now runs quiet when TESTS_QUIET is defined. What a pain!
* 2001-11-02 Dan Terpstra — New model for setting TESTS_QUIET to hide the uglies, esp on Windows.
* 2001-11-02 london — *** empty log message ***
* 2001-11-02 london — Changed compiler from f77 back to efc since f77 is broken.
* 2001-11-02 zlong — Added 4 event mapping: PAPI_BR_PRC, PAPI_BR_MSP, PAPI_BR_NTK, and PAPI_BR_TKN.
* 2001-11-02 zlong — set fortran compiler to f77
* 2001-11-02 Philip Mucci — Ok, we now have 2 releases of PerfCtr in this distribution, 1.6 and 2.3. Both have been tested. Some broken kernel releases like Redhat, need some tweaking with the includes, but everything seems to be working.
* 2001-11-01 Dan Terpstra — Changed a name from PAPIF_QUERY_ALL_EVENT_VERBOSE to PAPIF_QUERY_ALL_EVENTS_VERBOSE, since it seemed like a typo. This pushes the name to 30 chars. Is that bad on some platform?
* 2001-11-01 Dan Terpstra — New model for setting TESTS_QUIET to hide the uglies, esp on Windows.
* 2001-11-01 Dan Terpstra — Minor tweak in quiet execution mode.
* 2001-11-01 Dan Terpstra — Major rewrite to make calibrate do what we said it did. Works as expected on most platforms; unexplained erroneous behavior on Sun and MIPS.
* 2001-11-01 Dan Terpstra — Make TESTS_QUIET an extern so test_utils routines can access it. This is needed for Windows PASS/FAIL testing. Also subroutinize checking args for a smaller footprint.
* 2001-10-31 Dan Terpstra — Added the papi_fwrappers entry points.
* 2001-10-31 Dan Terpstra — Minor changes to support faster clock determination.
* 2001-10-31 london — Added revision and nrctr needed by the driver.
* 2001-10-31 Philip Mucci — Added more makefiles to Linux substrates, fixed multiplexing bug, added new test case
* 2001-10-31 london — New version of cpuinfo should be much faster.  Merged cpuinfo and the this version (for PAPI) into one file.  As such, this file grabs some information not used currently by PAPI such as amount of RAM, Virtual memory, L2,L1 info, etc.....
* 2001-10-30 Philip Mucci — -h
* 2001-10-30 Philip Mucci — Fixed IA64 from swapping counters, problem was in update_global_counters
* 2001-10-24 london — A fix to the event map on r12k processors. Event 6 is resolved conditionals not total branches, so we get total conditionals, and correctly predicted branches now (this one being derived). I temporarily removed cycles stalled for memory (event 14), as the manpage states that the counter is always 0 on current versions of the R12K processor. Thus we would be returning inaccurate results.
* 2001-10-24 Shirley Moore — added complete pathname for Intel Fortran compiler
* 2001-10-24 Shirley Moore — changes to upgrade to pfmlib 0.06a and to use the Intel 5.0 Fortran compiler
* 2001-10-24 Shirley Moore — added time.h to include files
* 2001-10-24 Shirley Moore — clarified comment about thread support on Tru64 Alpha and added osf to ifdef
* 2001-10-23 Dan Terpstra — Trying to get new calibrate to work on sparc and mips.
* 2001-10-22 london — A few more fixes before the code freeze. Mostly formating, and a few changes for different platforms.
* 2001-10-22 zlong — Small bug fixed.
* 2001-10-20 zlong — changed ftests_fail(__FILE__, retval) to ftest_fail(__FILE__, __LINE__, call, retval) made the output format same as c tests
* 2001-10-19 zlong — corrected the output format.
* 2001-10-19 london — One last set of changes before doing the code freeze. Still a couple more things on the way..
* 2001-10-19 Dan Terpstra — Algorithm was producing lots of flops, but not the theoretically correct number. Restructured to do what it says it does.
* 2001-10-18 Dan Terpstra — Fixed minor syntax errors that triggered warnings on Windows.
* 2001-10-11 london — Make sure the library is initialized before any other calls.
* 2001-10-10 zlong — Fixed the optimization problem with do_loop function on Solaris-ultra
* 2001-10-10 zlong — In xlf, -D flag does not mean #define. Removed it from FOPTFLAGS.
* 2001-10-10 zlong — fixed small bugs.
* 2001-10-10 zlong — fixed a bug
* 2001-10-10 zlong — ported to tru64-alpha: Added PAPI_TOT_INS(NO_FLOPS) support in second.F and profile.F. Simply pass the test case "tenth" on this platform, as we did in C test cases.
* 2001-10-10 zlong — For tru64-alpha, compile ftests_util.o with -g2 flag, to remove all the optimization. Without -g2 flag, do_flops function will be optimized, and those test cases using it won't get the desired results.
* 2001-10-10 zlong — Pass SUBSTR to ftests/Makefile.
* 2001-10-10 zlong — Turn on the NO_FLOP flag.
* 2001-10-10 Philip Mucci — Added MPI test case for AIX.
* 2001-10-03 Shirley Moore — fixed error
* 2001-10-03 Shirley Moore — mods for quiet mode
* 2001-10-03 Shirley Moore — more mods for quiet mode and to native to work on aix-power (but native.F still doesn't work on aix-power because CPP definition of _AIX is not getting picked up - but it works if _AIX is hard-coded)
* 2001-10-02 Shirley Moore — more tests_quiet mods
* 2001-10-02 Shirley Moore — reversed logic on tests_quiet (had it backwards before)
* 2001-10-02 Shirley Moore — changed test output to SKIPPED if not supported by substrate
* 2001-10-02 Shirley Moore — added explanation of test program output PASSED, FAILED, or SKIPPED
* 2001-10-02 Shirley Moore — These tests now read tests_quiet as an input.
* 2001-10-01 Shirley Moore — made case1.F equivalent to case1.c
* 2001-10-01 Shirley Moore — fixed syntax error in write statements
* 2001-10-01 Shirley Moore — changes to ftests so that they compile and run on SGI; second.F still failing
* 2001-10-01 Shirley Moore — added FFLAG -col120 so that ftests compile
* 2001-09-28 zlong — Ported to Alpha: 1. Alpha does not have PAPI_FP_INS event. 2. The output was wierd in Alpha
* 2001-09-27 Shirley Moore — added signal handler for alpha to start_timer
* 2001-09-27 Shirley Moore — changed Makefile.tru64-alpha to get rid of soname error
* 2001-09-27 Shirley Moore — changed tests to give appropriate results on alpha
* 2001-09-26 zlong — remove unused variables.
* 2001-09-26 zlong — ported to solaris-ultra: some lines are too long, so that the compiler complains.
* 2001-09-26 zlong — correct a small bug.
* 2001-09-26 zlong — The content is moved to PAPI_fwrappers.c
* 2001-09-26 zlong — ftests_wrappers.c is no longer needed in ftests/Makefile.
* 2001-09-26 zlong — Moved ftests/ftests_wrappers.c into papi_fwrappers.c
* 2001-09-26 Dan Terpstra — Minor changes to eliminate initialization warnings on solaris-ultra.
* 2001-09-26 zlong — ported to linux-perfctr: changed precompile flags
* 2001-09-26 zlong — Ported to tru64-alpha: Update native.F and avail.F: In this architecture, variable names are not allowed to be the same as program name. Update ftests_util.F: In this architecture, implicit none should be the second line in a precedure
* 2001-09-25 zlong — Added papif_query_all_event_verbose, and papif_query_event_verbose in ftests_wrappers.c Rewrite avail.F so that its output matches avail.c
* 2001-09-25 Dan Terpstra — A couple more tests had a double reference to ftest_utils that sun doesn't like.
* 2001-09-25 Dan Terpstra — Some tests had a double reference to ftest_utils that sun doesn't like.
* 2001-09-25 Dan Terpstra — Syntax error, but only for sun sparc
* 2001-09-25 Dan Terpstra — Removed name conflict with libpapi.a
* 2001-09-25 Dan Terpstra — Get rid of an unreferenced variable warning.
* 2001-09-25 Dan Terpstra — More minor mods. Added a miscellaneous #defines section for stuff like NUM_FLOPS.
* 2001-09-25 Dan Terpstra — Removed reference to papi_test.h, since it introduced pathing problems in the Makefile. Someday, I need to learn how to fix the pathing instead... At least it works again. Sorry Nils
* 2001-09-25 Dan Terpstra — Modified the new Fortran tests to remove reference to tests.h. These defines are now found in fpapi.h as produced by a newly modified genpapifdefs.c.
* 2001-09-20 zlong — Added new Fortran test cases
* 2001-09-20 zlong — Added New Fortran test cases.
* 2001-09-20 Dan Terpstra — WIndows Compaq Visual Fortran projects for PAPI Fortran test cases.
* 2001-09-20 Dan Terpstra — WIndows Visual C project to generate fpapi.h
* 2001-09-20 Dan Terpstra — Restructured. Now it's table driven instead of hard-coded. And it works for Windows.
* 2001-09-20 Dan Terpstra — Added Windows Compaq Visual Fortran string support.
* 2001-09-20 zlong — Test to make sure commit is working correctly
* 2001-09-20 Dan Terpstra — Minor grammer changes
* 2001-09-20 Dan Terpstra — Changed call to ftests_fail: wrong # of parameters.
* 2001-09-20 Shirley Moore — removed extra occurrences of do_loops from tests/Makefile
* 2001-09-20 Shirley Moore — fixed pthreads tests to give PASSED output on power3
* 2001-09-20 Shirley Moore — recommend using absolute pathname for install commented out read_cycle_counter in Makefile.tru64-alpha since we're not currently using it
* 2001-09-20 Nils Smeds — do_loops.o now in UTILOBJS, fix of target multiplex1_pthreads
* 2001-09-20 Shirley Moore — correction to tru64-alpha.README
* 2001-09-17 london — Small compiler warning fix
* 2001-09-17 london — Fix for syntax error on Make clean
* 2001-09-17 london — Fix so the test suite compiles on a power3a
* 2001-09-17 Dan Terpstra — Phooey. ..and AIX (at least) doesn't like '/*' inside a comment...
* 2001-09-17 Dan Terpstra — Phooey. I got stung by the lack of support for // single line comments again...
* 2001-09-06 Nils Smeds — By a mistake the difference between tests fourth and fourth-inv has disappeared. This makes fourth-inv add the events in opposite order in the two event sets again.
* 2001-09-05 london — Fixed a seg fault error, if the PFM device is busy _papi_hwd_shutdown would segfault because of testing of an unitialized variable.
* 2001-09-04 Dan Terpstra — Fixed compiler warning on unused variable.
* 2001-09-04 Dan Terpstra — Mods to string support. Short labels now supported for Perfometer. Keith - See new routine: int PAPI_label_event(int EventCode, char *label) Also strings have been moved to external header files and referenced by #define. This makes it readily possible for vendors and others to change or localize strings without changing the code body itself. See papiStrings.h and papiStrings_US.h for details.
* 2001-08-27 Shirley Moore — updated tru64-alpha.README file
* 2001-08-24 london — For more test changes
* 2001-08-24 Nils Smeds — Memory leak introduced by previous commit fixed. Tested on IRIX and Linux (using PGI pgcc).
* 2001-08-24 Nils Smeds — It's been a while since I visited this file. These edits should make it to better conform to the OpenMP standard. (Tested in IRIX only)
* 2001-08-24 london — Changes for Irix
* 2001-08-24 london — A revamp of our tests, finally they are almost in the new format (Thank goodness), now I just need to test on all the platforms.
* 2001-08-24 london — A few fixes for the alpha substrate, and a new tests script.
* 2001-08-20 Nils Smeds — PAPI_preset.3 sorted alphabetically for more easy reading.
* 2001-08-19 Nils Smeds — Modification of instruction cache related events on the linux-perfctr Pentium Pro/II/III platform. These were mixed up slightly in that you got more L2 instruction fetches than L1 instruction misses. linux-perf and Windows substrates not checked for the same (possible) mix-up.
* 2001-08-19 Nils Smeds — Small modifications to make the updated examples work. Makefile links to test_util.o, typos and multiple PAPI_shutdown:s fixed.
* 2001-08-19 Nils Smeds — The papi.c update 1.106 ->  1.107 made linux-perfctr.c dump core if there were eventsets defined at PAPI_shutdown. This fix makes _papi_hwd_shutdown a NOOP instead of doing a vperfctr_unlink(machdep->self) for each defined event set. Something sensible should probably be added to _papi_hwd_global_shutdown instead. Anyone having a good idea what?
* 2001-08-19 Nils Smeds — Calling PAPI_shutdown twice (without restarting PAPI) causes at least the linux-perfctr version to core dump. This fix catches a PAPI_shutdown where the library is not initialized, writes a warning and then returns.
* 2001-08-17 Dan Terpstra — Updates to m-files for MatLab.
* 2001-08-17 Dan Terpstra — Updates to documentation for MatLab and calibrate changes.
* 2001-08-17 london — A few changes to make test files work with the new test_util stuff.
* 2001-08-16 Dan Terpstra — Inital commit for Windows MatLab support.
* 2001-08-16 Dan Terpstra — Restructuring & code cleanup incorporating test results into PAPI_hl.
* 2001-08-16 Dan Terpstra — Minor formatting changes in the output.
* 2001-08-15 Dan Terpstra — Changes in PAPI_flops to handle processor specific calibration.
* 2001-08-15 Dan Terpstra — Minor resource cleanup
* 2001-08-14 Nils Smeds — Yet another test program. Runs through the available set of L1 cache events.
* 2001-08-14 Nils Smeds — london@cs.utk.edu (Kevin Scott London) wrote: > date: 2001/07/12 21:10:28;  author: london;  state: Exp;  lines: +8 -8 > This fixes PAPI to work with pmtoolkit version 1.3, but it breaks it > for anything before 1.3, I could put ifdef's in, but if IBM is going > to put 1.3 up on their webpage for download, do we really need 1.2 support?
* 2001-08-13 Dan Terpstra — Fix syntax problem in Windows code that caused compile warning on AIX.
* 2001-08-13 Shirley Moore — fixed bug in overflow_single_event.c widened error check for number of overflows to +/- 15% in overflow and overflow_single_event so that these tests now pass on alpha
* 2001-08-13 Shirley Moore — changes to PAPI_shutdown and to _papi_hwd_shutdown and _papi_hwd_shutdown_global to close the pfcntr device on shutdown; shutdown followed by reinit now works on alpha
* 2001-08-13 Shirley Moore — commented out call to PAPI_set_opt to set domain from mpx_insert_events The call to PAPI_set_opt to set granularity was already commented out. Since the only calls to mpx routines currently just get the current domain and granularity, these were essentially no-ops anyway, and they break on alpha. ---------------------------------------------------------------------- automatically CVS:  CVS: Modified Files:  CVS:    multiplex.c ----------------------------------------------------------------------
* 2001-08-13 Shirley Moore — implemented overflow handling
* 2001-08-10 Dan Terpstra — Modifications to new test code model and error messaging in test_utils
* 2001-08-10 Nils Smeds — Fixed mix-up in the printed table and the error check.
* 2001-08-10 Nils Smeds — A first minimal adaptation of the linux-perfctr substrate to use the perfctr-2.0 release. No new functionality added so far.
* 2001-08-09 Nils Smeds — The real perfctr-2.0 has been released so the pre4 files are obsolete. But anyway, just for the record a minor bug fix is incorporated. This fix is already in the linux-perfctr.c file
* 2001-08-08 Dan Terpstra — mods for avail.c
* 2001-08-08 Dan Terpstra — Oops. Left in a stray #define...
* 2001-08-08 Dan Terpstra — Overflow_single_event should now fail the same way as overflow.
* 2001-08-08 Shirley Moore — changed _papi_hwd_get_real_cycles and _papi_hwd_get_virt_cycles to not read the alpha cycle counters
* 2001-08-08 Dan Terpstra — Modified to test for required resources before executing.
* 2001-08-08 Dan Terpstra — Updated to new test coding model.
* 2001-08-08 Dan Terpstra — More informative calling sequence for test_fail() in test_utils.c
* 2001-08-08 Dan Terpstra — Syntax changes...
* 2001-08-08 Dan Terpstra — Modified to exit immediately with PAPI_ENOEVNT if NO_FLOPS.
* 2001-08-08 Nils Smeds — Fixed dependence on non-existing file
* 2001-08-08 Nils Smeds — Added diagnosis information (PASSED/FAILED) to the Fortran test cases. Moved the dummy routine into the new ftests_util.F where other routines are kept as well.
* 2001-08-08 Nils Smeds — Added FOPTFLAGS as a variable in top most makefiles to cover the cases where the Fortran compiler has other flags than the C compiler. (Third party compilers and some other cases)
* 2001-08-07 Dan Terpstra — Return SUCCESS if error is PAPI_ENOEVNT: event does not exist This way an unsupported eventwill still be logged, but not show up as an error when run_tests.sh is done.
* 2001-08-07 Dan Terpstra — Return SUCCESS if error is PAPI_ESBSTR: not supported by substrate. This way an unsupported feature will still be logged, but not show up as an error when run_tests.sh is done.
* 2001-08-07 Dan Terpstra — fixed typo...
* 2001-08-07 Dan Terpstra — Updated to new test coding model.
* 2001-08-07 Nils Smeds — One extraneous PAPI_start removed
* 2001-08-06 Dan Terpstra — Updated to new test coding model.
* 2001-08-06 Dan Terpstra — Minor mods for Windows compatibility; Code rearrangement for readability; Creation of test_pass and test_fail subroutines in test_utils.c
* 2001-08-06 Shirley Moore — removed extraneous lines so that case1.c and first.c compile on alpha, fixed typo in first.c
* 2001-08-06 Dan Terpstra — Mods to move the RDPMC test after the check for Uniprocessor free to prevent a crash on Multiprocessor systems.
* 2001-08-03 london — A few optimizations to determine the mhz rating a little quicker.
* 2001-08-03 Dan Terpstra — Round off correction in % error reporting.
* 2001-08-03 london — Took out some unused variables.
* 2001-08-03 london — Ooops, a few little mistakes fixed.
* 2001-08-03 london — A couple more tests that have been modified.
* 2001-08-03 london — Fixes for determing mhz rating on a laptop, basically the tsc doesn't get updated unless the cpu is doing work on laptops with speedstep technology, because of this we need a loop that does busy work while the mhz rating is determined.
* 2001-08-03 london — A few fixes to alpha basically sending some stuff the new tests need and fixing a formatting string in tru64-alpha.c when debug information is printed.
* 2001-08-03 london — First round of changes to tests to make the output make more sense, and to automate the task of checking a PAPI installation a little better. More test cases will be checked in as I complete them.
* 2001-08-03 Dan Terpstra — Modified to support % error and command line argument {1,2,3} for which test to perform. If no argument, all three run.
* 2001-08-02 Dan Terpstra — Output format changes: added %error
* 2001-08-02 Dan Terpstra — Fixed syntax problem with calibrate
* 2001-08-01 Dan Terpstra — Added FLOPS Calibration Routine: Computes actual and theoretical FLOPS for order 1, 2, and 3 operations. Currently only tested on Windows. Requires new PAPI_hl.c
* 2001-08-01 Dan Terpstra — FLOPS Calibration Routine: Computes actual and theoretical FLOPS for order 1, 2, and 3 operations. Currently only tested on Windows. Requires new PAPI_hl.c
* 2001-08-01 Dan Terpstra — Several changes to allow reset capability and improve accuracy: 	NOTE: Calling semantics have changed! 	Now, if flpins < 0 (an invalid value) a PAPI_reset is issued to reset the 	counter values. The internal start time is also reset. This should be a 	benign change, exept in the rare case where a user passes an uninitialized 	(and possibly negative) value for flpins to the routine *AFTER* it has been 	called the first time. This is unlikely, since the first call clears and 	returns this value.
* 2001-07-31 Shirley Moore — fixed bug in update_global_hwcounters; tests first, third, fourth, fifth now give what appear to be correct results.
* 2001-07-31 london — Falling back to using clock_gettime and getrusage for PAPI_get_real_usec and PAPI_get_virt_usec respectively until we can work out the bug in RTC on multiprocessor alphas.
* 2001-07-31 Dan Terpstra — This file hides differences btwn Windows and Unix for test routines.
* 2001-07-30 Dan Terpstra — This test isn't particularly useful for the Windows release.
* 2001-07-30 Dan Terpstra — Ooops. Can't build the DLL without this file...
* 2001-07-30 Dan Terpstra — Minor changes to add the new splash screen.
* 2001-07-20 Dan Terpstra — Mods to create a DLL instead of a Static Lib
* 2001-07-20 Dan Terpstra — Added warning that this test takes a while... Fixed %lld to %I64d format problems for Windows.
* 2001-07-20 Dan Terpstra — Modified splash screen to add team member names.
* 2001-07-20 Dan Terpstra — Removed eventname because it is SOOO boring.
* 2001-07-20 Dan Terpstra — Updates for documentation.
* 2001-07-20 Dan Terpstra — Changes to support Windows:   - long long to long_long;   - %lld to %I64d conditional define   - header rearrangement Compiled on linux, irix, solaris; Tested against solaris
* 2001-07-20 Dan Terpstra — Microsoft Visual C++ project files for a collection of the test applications.
* 2001-07-20 Dan Terpstra — Introductory documentation for the Windows installation.
* 2001-07-18 Dan Terpstra — Minor changes for case-consistency.
* 2001-07-13 Shirley Moore — added defined(mips) to check for platforms for multiplex tests
* 2001-07-13 Shirley Moore — changed PAPI_set_opt for PAPI_SET_MULTIPLEX to return PAPI_OK if max degree of multiplexing is <= num_cntrs; e.g., PAPI_set_multiplex will be a noop in this case; multiplex tests now work on irix-mips.
* 2001-07-12 london — This fixes PAPI to work with pmtoolkit version 1.3, but it breaks it for anything before 1.3, I could put ifdef's in, but if IBM is going to put 1.3 up on their webpage for download, do we really need 1.2 support?
* 2001-06-29 Dan Terpstra — Changes in table format so that it will work with manServer_papi.pl to convert to html. Unfortunately, the table still won't display on any man system I've tried...
* 2001-06-29 Dan Terpstra — Minor changes for case sensitivity in input file names for Linux. This script now works on both Windows and Linux. It must be run in papi/man, and assumes the existence of papi/man/man3 and papi/man/html. You can edit the script to point to different directories.
* 2001-06-29 Dan Terpstra — Minor changes for compatibility between Perl 5.6.1 on Windows and Perl 5.005_03 on Linux. Also changes to force lower case output and link names for compatibility between output generated in Windows and Linux.
* 2001-06-27 Dan Terpstra — Minor bug in .h file dependencies...
* 2001-06-26 Dan Terpstra — Removal of Phil's "woeful excuse" bug
* 2001-06-25 Dan Terpstra — Minor tweaks on the #include list.
* 2001-06-25 Dan Terpstra — Since Windows doesn't support unix style signals, this file required some significant restructuring. The signalling code was isolated into platform independent wrappers that call platform dependent routines. It compiles and links, but I haven't been able to carefully test it yet. Caveat Emptor.
* 2001-06-25 Dan Terpstra — Mostly changing unix style long long to platform neutral long_long, and a few other minor changes for Windows compatbility.
* 2001-06-25 Dan Terpstra — Mostly changing unix style long long to platform neutral long_long. Changes in header stuff for Windows, and conditional compilation for timer routines and routines in unix but not in Windows.
* 2001-06-25 Dan Terpstra — Mostly changing unix style long long to platform neutral long_long, and a few other minor changes for Windows compatbility.
* 2001-06-25 Dan Terpstra — Since there's a new group of man pages, we need a new batch file to convert them to html.
* 2001-06-25 Dan Terpstra — Adding _lock, etc.html to the repository. Also updated papi.html to reference these new pages. Thanks, Nils, for the quick implementation.
* 2001-06-24 Philip Mucci — More suuport for Alpha: clocks don't work though
* 2001-06-24 Philip Mucci — IA64 fix, function descriptors now!
* 2001-06-24 Philip Mucci — Added new pfmlib from Stephane
* 2001-06-24 Philip Mucci — *** empty log message ***
* 2001-06-22 Dan Terpstra — Some compilers (particularly Solaris?) don't like the // single line comment syntax. Bummer
* 2001-06-22 Dan Terpstra — ANSI (and Microsoft) don't support the 'long long' data type. I've replaced it with long_long and u_long_long, which resolve to platform specific variants of the same thing.
* 2001-06-22 Dan Terpstra — Minor changes: Case sensitivity problems; files were lower case, but refs were U/L, and UNIX cares even though Windows doesn't...
* 2001-06-22 Dan Terpstra — Minor changes: Case sensitivity problems; files were lower case, but refs were U/L, and UNIX cares even though Windows doesn't... Also, tables currently don't convert properly. See PAPIF.html.
* 2001-06-22 Dan Terpstra — Commented out currently unimplemented man pages: _lock, _unlock, _save, _restore
* 2001-06-22 Nils Smeds — Number of man pages left to do is decreasing...
* 2001-06-22 Nils Smeds — Missing stubs for PAPI_save/restore added (still no functionality though). Final(?) missing man pages added.
* 2001-06-21 Dan Terpstra — Commit of development resources for Windows PAPI port. This code is UNDER DEVELOPMENT. It requires changes to common PAPI code that have not yet been commited. For further information, contact dan terpstra <terpstra@cs.utk.edu>
* 2001-06-21 Philip Mucci — Minor fixes for the real EV67 CPU like PSC has
* 2001-06-20 Dan Terpstra — These files have been moved to a subordinate folder for later checkin
* 2001-06-19 Dan Terpstra — A collection of html files representing the contents of the PAPI man pages. To regenerate these files, run the perl script in the man directory. If someone wants to turn the Windows papiman.bat file into a make script for unix, go for it! To view these files, check 'em out of the repository and point your browser at /papi/man/html/PAPI.html.
* 2001-06-19 Dan Terpstra — A Perl script and a (Windows) batch file to convert our existing man pages into fully formatted and linked HTML files
* 2001-06-19 Dan Terpstra — Minor changes to eliminate a few obsolete function references, such as PAPI_lock and _unlock, PAPI_save and _restore.
* 2001-06-18 Nils Smeds — Minor clarification added
* 2001-06-18 Nils Smeds — New man pages added to the manual section and removed from the TODO list. Maybe not too informative in all aspects, but they are there at least.
* 2001-06-18 Nils Smeds — Trivial formatting changes
* 2001-06-12 Philip Mucci — Added a hack: the tests use PAPI_TOT_INS instead of PAPI_FP_INS as the default event to count. Why? Because the @#$%^& alpha can't count FP instructions.
* 2001-06-12 Philip Mucci — Ported the driver to the V5.1 pfm mod by Bill Gray. Seems to work. My real time calls seem to have wrapping issues, so this port isn't done. But it works so far.
* 2001-06-02 Shirley Moore — Added more events.  Couldn't add most of the branch events that use masks because the names alone don't work and cause the tests to Abort.
* 2001-06-02 Shirley Moore — fixes so that compile works on Cray T3E
* 2001-05-31 Philip Mucci — Fixes for IA64 build and T3E, multiplexing should work there now
* 2001-05-28 Nils Smeds — Re-committing changes lost by previous commit.
* 2001-05-24 Shirley Moore — Added info about n32-bit and 64-bit versions and setting LD_LIBRARYN32_PATH and LD_LIBRARY64_PATH.
* 2001-05-16 Nils Smeds — Man page updates and additions. Some documentation TODOs removed and some added.
* 2001-05-08 Nils Smeds — This is the last functional check of the CVS. Please ignore yet again.
* 2001-05-08 nils — This is only a functional check of the CVS. Please ignore.
* 2001-05-07 nils — Minor bug fix and more accurate resolution determination for low-resolution timers (as e.g. the current virtual linux timer)
* 2001-05-07 nils — This might be a little pre-mature, but in that case I trust that the PAPI group removes the files. This is a simple attempt to adapt the linux-perfctr substrate to the coming 2.0 of the perfctr library.
* 2001-05-07 nils — This sets up two (unused) integers in _papi_system_info.
* 2001-05-02 Nils Smeds — This is just a test of committing through ssh - please ignore
* 2001-05-02 nils — This is an attempt to more robustly determine the type of CPU you are running on. In particular the IPxx and R1x000 versions are gotten directly from the system independently. The PAPI CPU model string now contains both these. Further the PAPI model integer is composed as: IPnum * 256 + Chip version where Chip version depends on your type of Rxxk processor.
* 2001-05-01 Dan Terpstra — Initial comit for Windows port
* 2001-05-01 Dan Terpstra — fix for get_virt_cycles() routine
* 2001-05-01 Dan Terpstra — fix for get_virt_cycles routine
* 2001-05-01 nils — Updates to the IRIX substrate so that it compiles after the multiplex modifications made to the general library. No review of multiplexing has been done for this substrate and functionality is as before (that is multiplexing is always enabled). This probably needs to be done by someone more talented than I.
* 2001-04-28 nils — Addition of PAPI_accum_counters to the High-level API and corresponding documentation updates and example files.
* 2001-04-27 Nils Smeds — PAPI_resume_counters was a bad idea from the start. Don't PAPI_stop_counters instead and use a call to PAPI_read_counters which resets counters to 0 after a section of code you don't want measured.
* 2001-04-27 Nils Smeds — A tentative suggestion for adding a resume command to the High-Level PAPI interface. This will allow the High-Level user the ability to stop the counts during I/O or part of the code s/he does not want to measure.
* 2001-04-19 nils — Fixed an incorrect format statement in fmatrix*papi.F
* 2001-04-14 Philip Mucci — Fixed to new header structure...
* 2001-04-14 Philip Mucci — Added a more complete list of things TO DO in PAPI. Hint hint hint folks...
* 2001-04-12 nils — Modified source to work around a bug in the g77 compiler. Tried to make the output more selfinstructive. (Test 7 for describe event should return an incorrect name e.g.)
* 2001-04-12 Philip Mucci — Fixes for multiplexing on the power architecture. Untested.
* 2001-04-12 Philip Mucci — Multiplexing works now on Solaris 2.8 and UltraSparc.
* 2001-04-12 Philip Mucci — Things to do for source/docs
* 2001-04-12 Philip Mucci — Fixed clean stage
* 2001-04-12 Philip Mucci — Multiplexing code from John May, hacked by me
* 2001-04-12 Philip Mucci — This commit is a snapshot of multiplex support. Many things have changed, but this does work under Linux at the moment. It still has to be tested on other platforms. There are two new calls for multiplexing, see the new test cases for usage and documentation.
* 2001-04-05 nils — Added macro for CPP to the benefit of users not using GNU make. This will enforce CPP to be "cc -E" for users using GNU make as well (on T3E that is).
* 2001-04-05 nils — Added PAPIF_describe_event subroutine to the Fortran interface. Modified man page and string handling test case accordingly.
* 2001-04-05 nils — Fixed possible pointer running out-of-bounds in string conversions
* 2001-04-04 nils — Clarification of how to use PAPI_describe_event
* 2001-04-03 nils — Fixed a integer cast problem on SGI. PAPI_L1_DCM gets promoted to integer*8 and can not be passed as actual argument, but must be copied into a temporary integer*4 for correct behaviour.
* 2001-04-03 nils — String handling is no fun, neither in Fortan nor C. Fixed one more "special" case.
* 2001-04-03 nils — Added dummy calls to test/flops.c and ftests/flops.F so that the flops are not removed by a smart compiler
* 2001-04-02 nils — papi_fwrappers.c: + Fortran  calling interface design change. The length argument is   dropped to the subroutine     PAPIF_perror(C_INT code, C_STRING destination, C_INT check)   The length argument was not used for all implementations and by this change   the string interface is now the same for all Fortran calls to PAPI. + String copying between C and Fortran reviewed and CRAYT3E and UNIX   fortran cases merged as much as possible.
* 2001-03-30 nils — PAPI_num_counters now produces error codes as in the original documentation, manual page back-ported to reflect this.
* 2001-03-29 Philip Mucci — Updated for 1.6.1 of PerfCtr release from Mikael.
* 2001-03-29 nils — Manual page overhaul. Attempted to have a more unified layout and tried to clarify indistinct descriptions. Several instances where the development has out-run the documentation rectified as e.g. the usage of PAPI_library_init in several examples. Numerous new errors probably introduced instead of the old ones.
* 2001-03-29 nils — PAPI_num_counters now returns PAPI_EINVAL on library version mis-match as described in the PAPI_num_counters(3) man page.
* 2001-03-29 Philip Mucci — *** empty log message ***
* 2001-03-29 Philip Mucci — Links with static lib always
* 2001-03-29 Philip Mucci — Backed out last changed. Removed -lmach dep.
* 2001-03-29 Philip Mucci — Added bug for Pentium and bug for Linux build.
* 2001-03-29 Philip Mucci — This test now works on all systems.
* 2001-03-29 Philip Mucci — More shared library fixes. Shared library build still fails on Linux for some reason. It's the run time linker path problem again. Damn.
* 2001-03-28 london — Ugh, try this one more time.
* 2001-03-28 london — OOps, accidently removed a $ back in now.
* 2001-03-28 london — Added a CPP definition to Makefile.solaris-ultra to get rid of the fortran wrapper problems, Changed Makefile.inc to link in libpapi.a for genpapifdef instead of -lpapi as it was picking up libpapi.so
* 2001-03-28 nils — Fixed erroneous PAPI_perror string for PAPI_ENOTRUN
* 2001-03-28 nils — Minor updates to the documentation.
* 2001-03-28 Philip Mucci — Fixed redirect man instruction
* 2001-03-28 Philip Mucci — Fixed man pages from Nils.
* 2001-03-19 Philip Mucci — Shared library fixes. run script fixes...
* 2001-03-19 Philip Mucci — Added PAPI Spec to the to do list...
* 2001-03-17 Philip Mucci — *** empty log message ***
* 2001-03-17 Philip Mucci — �/�g[<[+U�^eS�����GE[HAyzy���gY��އ��PZ����F�3���l'HF8`�K/G+���"8���N B�B�"`EO
* 2001-03-17 Philip Mucci — Numerous shared library fixes. Tru64 timers now work and are highly accurate. I tried to make the alpha port work like PCL and bind to the CPU, but that doesn't work either on my systems. And I can't test PCL with the native compiler. Please won't COMPAQ help us? Also, debugging messages disabled.
* 2001-03-17 Philip Mucci — Man page fixes, thanks to Clark Coleman for the bugs.
* 2001-03-17 Philip Mucci — The outstanding list of TODO things for PAPI. Everyone should be looking at this!
* 2001-03-05 Philip Mucci — Small build fixes for the Linux Perfctr PAPI Release, nothing critical, also a fix for the SP
* 2001-03-04 Philip Mucci — How to use CVS
* 2001-03-02 london — Changed the way fortran wrappers are built so all combinations exist in a library not just one.  Different compilers were using different forms, so it is just easier to include them all.
* 2001-02-09 Philip Mucci — Added temporary -DPERFCTR18 fix for PerfCtr 1.8 series... Please don't use them yet. Use the ones in the PAPI repository...
* 2001-02-09 Philip Mucci — Stephane's documentation files now present.
* 2001-02-09 Philip Mucci — Updated some of the test cases.
* 2001-02-09 Philip Mucci — This commit adds Stephane's PFM library to the tree. This is an incomplete snapshot.
* 2001-02-09 Philip Mucci — This commit fixes the following bugs:
* 2001-01-31 london — Addition of PAPI_flops test examples, and some small fixes to PAPI_flops
* 2001-01-31 london — Change to PAPI_flops which fixes a bug in fortran and makes the total floating point operations less likely to overflow.
* 2001-01-31 london — Change to PAPI_flops, so total floating point operations won't overflow as easy.
* 2001-01-16 london — Another change to make sure verification matches what the output is suppose to be.
* 2001-01-16 london — Added verification on SGI, PAPI_DOM_ALL and PAPI_DOM_KERNEL can only be set by root on IRIX, therefor the verification looked wrong if not run as root.
* 2001-01-16 london — Small fix to make sure verification matched what actual results should be.
* 2000-12-07 Shirley Moore — fix to _papi_hwd_init in irix-mips.c to properly handle thread initialization of counter control block
* 2000-12-01 Philip Mucci — Simple update...
* 2000-12-01 Philip Mucci — more error checking
* 2000-12-01 Philip Mucci — Fixed Linux perfctr substrate. Theoretically if you install Mikaels patchon 2.2 this should work
* 2000-11-30 Philip Mucci — IRIX bug fix, some code for per node and system counting not working yet
* 2000-11-29 Philip Mucci — New files
* 2000-11-26 Philip Mucci — New snapshot for perfctr 1.6
* 2000-11-26 Philip Mucci — SMP and OMP still get SIGTERM from IRIX. ANy ideas?
* 2000-11-26 Philip Mucci — Removed need for data files.
* 2000-11-26 Philip Mucci — Fixed bug in IRIX substrate. Renamed Makefiles on Linux for either version of the patch.
* 2000-11-26 Philip Mucci — Cleaned up the patch a bit. No change in functionality.
* 2000-11-17 Philip Mucci — Patch for latest RH 6.2EE, they added system calls which broke entry.S
* 2000-11-17 Philip Mucci — Updated to 1.5.3 snapshot from Mikael.
* 2000-11-03 Philip Mucci — Makefile fixes and new perfctr release
* 2000-11-02 Philip Mucci — Alpha EV6 fixes, it still doesn't always work. Why?
* 2000-11-02 Philip Mucci — Could these man pages have been any worse?
* 2000-10-30 Philip Mucci — *** empty log message ***
* 2000-10-30 Philip Mucci — Bug fix in papi.c, fixed some makefile issues. Improved README and INSTALL files. Also added a binary distribution target to generate a binary kit.
* 2000-10-30 Philip Mucci — Bug fixes for native events
* 2000-10-27 london — Added a man page for PAPI_flops
* 2000-10-27 london — PAPI_simple renamed to PAPI_flops
* 2000-10-26 london — New call PAPI_simple, this call will initialize the library if not initialized, and setup PAPI_FP_INS and PAPI_TOT_CYC events to be monitored and start the counters.  Repeated calls to the function will read the counters:
* 2000-10-20 Philip Mucci — More man page updates
* 2000-10-20 Philip Mucci — More man page fixes
* 2000-10-19 Philip Mucci — First real man page fix, small build fix for Solaris
* 2000-10-18 Philip Mucci — EV6 updates. Sort of working...
* 2000-10-11 Philip Mucci — More fixes for the Alpha 21264, still no go
* 2000-09-15 Philip Mucci — 
* 2000-09-15 Philip Mucci — Initial revision
* 2000-09-15 Philip Mucci — Added 2.4-test8 support with latest perfctr distribution.
* 2000-09-14 Philip Mucci — Linux SuperCluster release. Ok, all the platforms have some sort of virtual timer functionality. So you can now tell how many usecs you've spent in user land. It's not accurate though.
* 2000-09-07 Philip Mucci — Build fix for t3E, Fortran MHZ is still broken Kevin!
* 2000-08-31 london — Fixes for CrayT3E fortran support.
* 2000-08-23 Philip Mucci — Added PAPI_describe_event from nils a, added lperfex skeleton for use with LD_PRELOAD
* 2000-08-16 Philip Mucci — Dumb editing mistake, replaced shutdown call
* 2000-08-07 Philip Mucci — Flags fixes. T3E fixes.
* 2000-08-07 Philip Mucci — Flags fixes.
* 2000-08-07 Philip Mucci — T3E fixes from Charles Aldarondo of Cray. Thanks Charles. Makefile optimizations for all platforms.
* 2000-08-03 Philip Mucci — Added c++ ifdef
* 2000-07-31 Nathan Garner — _papi_hwd_get_virt_cycles wasn't passing the eventsetinfo parameter to _papi_hwd_get_virt_usec
* 2000-07-27 Philip Mucci — Removed aix makefile
* 2000-07-27 Philip Mucci — More install fixes
* 2000-07-27 Philip Mucci — MOre fixes for the install phase
* 2000-07-27 Philip Mucci — Fixed Fortran tests
* 2000-07-24 Philip Mucci — Fixes from Nils and Anders, 1 fairly important missing n
* 2000-07-19 Philip Mucci — More changes from Nils Smeds smeds@pdc.kth.se Anders Nilsson anni@pdc.kth.se
* 2000-07-19 Philip Mucci — Greatly changed test suite. Looks a little nicer now. Plus a script to run them.
* 2000-07-19 Philip Mucci — My slightly different version of libperfctr without pthread locks.
* 2000-07-19 Philip Mucci — Lots of cleanups and better string handling.
* 2000-07-19 Philip Mucci — Overheals for 1.1. Now we mahe multithreaded profiling and counter overflow and it's fully without and thread specific functionality. Also, additions for Linux 2.4. It now works great thanks to Mikael Petterson, and it's much faster.
* 2000-07-19 Philip Mucci — Fixed up a few things in the spec
* 2000-07-19 Philip Mucci — Added the patch for Redhat 6.2
* 2000-07-19 Philip Mucci — Fixed up the prototypes for these two functions. They need to be documented further.
* 2000-07-19 Philip Mucci — Added file to install the makefiles and build the scripts.
* 2000-07-19 Philip Mucci — *** empty log message ***
* 2000-06-29 london — Fixed the fortran wrappers for the Cray T3E and some compiling issues with the new papi code on the crayt3e.
* 2000-06-21 Philip Mucci — Fixes for recent AIX pmtoolkit, sprofil() now works can can measure disjointed text segments.
* 2000-06-21 Philip Mucci — Multithreaded overflowing working for Solaris and Linux x.86 < 2.4
* 2000-06-21 Philip Mucci — PAPI_sprofil() now works on disjoint text segments, just like IRIX sprofil()
* 2000-06-20 Philip Mucci — More fixes for the Alpha, still no workie
* 2000-06-19 Philip Mucci — More fixes for multithreaded profiling and overflow, plus a PAPI_sprofil() call for doing multiple disjoint text segments
* 2000-06-16 Philip Mucci — More bones for the Alpha, why doesn't someone do the presets for me?
* 2000-06-16 Philip Mucci — Rename of T3E lock init fn
* 2000-06-16 Philip Mucci — Ok, I've revamped thread support again. Now I have paved the way for Multithreaded profiling. That means gprof like hw profiling per thread. It's not tested yet. But the support is there. I will write a test case sometime.
* 2000-06-13 london — Makefile changes for the Fortran T3E wrappers
* 2000-06-13 london — T3E fortran wrapper changes
* 2000-06-12 Philip Mucci — Added new error codes and PAPI_strerror function
* 2000-06-06 Philip Mucci — This could be considered the 1.1 release, but I haven't tested it yet. For those of you using this library, I highly recommend you download this snapshot via: icl.cs.utk.edu/projects/papi/snapshot.cgi and then yell at me when it breaks. I've got stuff to do for other people in the meantime.
* 2000-06-06 Philip Mucci — This could be considered the 1.1 release, but I haven't tested it yet. For those of you using this library, I highly recommend you download this snapshot via: icl.cs.utk.edu/projects/papi/snapshot.cgi and then yell at me when it breaks. I've got stuff to do for other people in the meantime.
* 2000-06-06 Philip Mucci — ../CVSROOT/loginfo
* 2000-06-06 Philip Mucci — This could be considered the 1.1 release, but I haven't tested it yet. For those of you using this library, I highly recommend you download this snapshot via: icl.cs.utk.edu/projects/papi/snapshot.cgi and then yell at me when it breaks. I've got stuff to do for other people in the meantime.
* 2000-06-06 Philip Mucci — This could be considered the 1.1 release, but I haven't tested it yet. For those of you using this library, I highly recommend you download this snapshot via: icl.cs.utk.edu/projects/papi/snapshot.cgi and then yell at me when it breaks. I've got stuff to do for other people in the meantime.
* 2000-05-22 london — Changes to some man pages.
* 2000-05-22 Nathan Garner — API Spec web page added.
* 2000-05-19 london — Oops
* 2000-05-19 london — Makefile for fortran, papi.c to change a int to unsigned.
* 2000-05-19 london — New Man Pages for PAPI 1.0
* 2000-05-17 Philip Mucci — Fixed bugs from John May, and updated the high level functions
* 2000-05-16 london — Solaris fortran wrappers
* 2000-05-16 london — Fortran fix for Linux
* 2000-05-16 Philip Mucci — Fix for shutdown everything.
* 2000-05-16 Philip Mucci — Fix for shutdown everything.
* 2000-05-16 Philip Mucci — Early man pages
* 2000-05-15 london — Whoops
* 2000-05-15 london — Bug on Irix causing infinite loop. Please use unsigned ints when shifting on IRIX
* 2000-05-15 london — Fortran fixes and drivers for FTN tests from Kevin
* 2000-05-15 london — Fortran test cases from Kevin.
* 2000-05-15 Philip Mucci — Linux patches to support dynamic loading
* 2000-05-15 Philip Mucci — T3E updates and tested
* 2000-05-15 Philip Mucci — Bug fixes for SGI, SUN
* 2000-05-15 Philip Mucci — Bug fixes for SGI, SUN
* 2000-05-15 Philip Mucci — Added support for threads on AIX again, fixed bugs reported by John May
* 2000-05-12 Philip Mucci — Fixes for everything but AIX events and Cray T3E locking
* 2000-05-12 Philip Mucci — Added Linux spinlocks
* 2000-05-12 Philip Mucci — API is now fully reentrant.
* 2000-04-14 Philip Mucci — This should work, testing remote....
* 2000-04-13 Philip Mucci — Still fixing IRIX and AIX, Linux, Solaris are working
* 2000-04-12 Philip Mucci — Added 20 new presets, 2 new functions, fixed bugs and Solaris 8 support
* 2000-04-06 london — Fixed a crash bug with PAPI_get_hardware_info in fortran, the program would crash if PAPI_get_hardware_info failed. Kevin
* 2000-04-06 london — Cleaned up the wrappers, and added fortran support for PAPI_get_hardware_info Kevin
* 2000-04-03 london — Fortran wrappers are added the following calls are not supported at the moment:  PAPI_add_pevent, PAPI_get_executable_info, PAPI_get_hardware_info, PAPI_get_overflow_address, PAPI_overflow, PAPI_profil, PAPI_query_all_events_verbose, PAPI_query_event_verbose, PAPI_set_opt All fortran calls have an additional argument (INTEGER) for the return code. Kevin
* 2000-03-16 Philip Mucci — Added files for Solaris 5.8 BETA REFRESH...Currently waitring for a debugger
* 2000-03-10 Philip Mucci — Fix for the T3E add problem...
* 2000-03-09 Nathan Garner — Added a buglist file for PAPI.
* 2000-03-09 Nathan Garner — Changes in color name handling in the Perfometer (unfinished).
* 2000-02-25 Nathan Garner — *** empty log message ***
* 2000-02-09 Philip Mucci — New test for SHMEM/threads
* 2000-02-09 Philip Mucci — T3E version is now working, just threads to do
* 2000-02-04 Philip Mucci — Fixed erroneous reporting bug
* 2000-02-04 Philip Mucci — Makefile updates, fixes for the new release of PMAPI and some updating of the T3E
* 2000-02-03 Philip Mucci — Bug fixes and test cases from Dave M of psrv.
* 2000-02-03 Philip Mucci — Patch for Redhat 6.1
* 2000-02-03 Philip Mucci — Fix for SGI and new test case
* 1999-12-13 Philip Mucci — Lots of changes. Pthread support for IBM. New functions. SGI and T3E almost working. Skeletions for Tru64. Loads of new test files.
* 1999-08-17 Philip Mucci — Simple fix
* 1999-08-17 Philip Mucci — Redesigned the test program to demonstrate common bugs.
* 1999-08-17 Philip Mucci — Added new function papi_describe_all_events
* 1999-08-13 Philip Mucci — Getting ready for release
* 1999-08-13 Philip Mucci — Added support for 2.2.10 and cleanup up the examples
* 1999-08-11 Philip Mucci — Working Linux snapshot with all the goodies. Also removed the keyword comments that were getting us
* 1999-08-11 Philip Mucci — New working example programs. Fixed headers
* 1999-08-11 Philip Mucci — Added test program for fastwrite and cycle counter
* 1999-08-11 Philip Mucci — Added fastwrite and all the goodies.
* 1999-07-26 gho —  this is the example program demonstrating the use of PAPI_profil()
* 1999-07-26 gho —  fixes, large and small. PAPI_profil() works, with a new example program. Currently, profiling and overflow is limited to 1 eventset. These additions are by Phil.
* 1999-07-21 Philip Mucci — Added new option to support DEC and IRIX. PAPI_SET_ATTACH to attach to another process.
* 1999-07-20 gho — new example files that Phil added. I tweaked the src/ files a little to fix some minor bugs these examples brought out.
* 1999-07-20 gho — Alright, this is a working snapshot of Phil's latest changes merged with my latest changes, basically everything except profil(), and derived metrics. -george
* 1999-07-19 Philip Mucci — This is a first snapshot of Linux kernel support for Redhat 5.2 and 6.0. I've added new system calls and made some far more efficient. Most importantly, I've added: - fast configure - fast read - fast reset counter - child inheritance - child propagtion - fix for SYS flag not being cleared
* 1999-07-19 Philip Mucci — This is a first snapshot of Linux kernel support for Redhat 5.2 and 6.0. I've added new system calls and made some far more efficient. Most importantly, I've added: - fast configure - fast read - fast reset counter - child inheritance - child propagtion - fix for SYS flag not being cleared
* 1999-07-16 gho — these are from Phil's tree. CVS did not merge them with the newest version, nor did it warn that these were modified from an old version. I'll merge by hand again.
* 1999-07-13 gho — minor modifications from completing low-level routines; test program using vectorized adds() and removes()
* 1999-07-13 gho — minor modifications from completing low-level routines
* 1999-07-13 gho — my last changes for filling out remaining user low-level routines
* 1999-06-28 gho — updated preset_map (linux-pentium.c) and papiStdEventDefs.h with the new or rearranged events from unicos-ev5.c
* 1999-06-04 deane — remove extra functions.
* 1999-06-04 deane — code clean-up
* 1999-06-03 gho — merged differences between phil's last commit and george's commit that conflicted with each other
* 1999-05-28 gho — here's the multiple start/stop example mentoined in the previous log message
* 1999-05-28 gho — have multiple start/stops working. have not tested thoroughly. will add third.c to tests/ directory, showing 2 eventsets start 1 read 1 start 2 read 2 stop 1 stop 2
* 1999-05-28 gho — added some more routines for merging and unmerging machdeps. not complete, so untested, but didn't break anything- first.c still works -g.
* 1999-05-27 gho — alright, i hope this doesn't mess things up. phil, i know it's not supposed to do this, but cvs is allowing commits with modified non-current versions of files. Your commits Thursday afternoon were files that were old and different from my modifications late Wednesday night. To test this, I made modifications to my old files without doing a cvs update, and it is now allowing me to check these in without complaint. So, these are the files that have my correct changes, including changes that work properly with your new first.c file, but they do not contain the set of modifications you last checked in, with the exception of first.c
* 1999-05-27 Philip Mucci — Ok, I really goofed on that last commit. Added new calls and tests...
* 1999-05-27 Philip Mucci — Patches to get closer to building.
* 1999-05-27 Philip Mucci — New query routines...
* 1999-05-27 Philip Mucci — Ok, the T3E port is complete but untested. I'm waiting for Kevin to come to work and log me in to one. I have made some more changes to papi.c. With a lot of cleanup and much better error handling. Also I have added some more presets. I'm sure this build will fail, but I need to get a snapshot in so George can keep working on multiple start/stop.
* 1999-05-27 gho — fixed and tested some preliminary high level structures and routines for merging eventsets, nothing is left broken, first.c still works, and no new compile warnings.
* 1999-05-26 gho — had to fix a bug in substrate, so that first.c would run correctly. what happened:   PAPI_TOT_INS is added, which can use either counter in linux,   so it was added to general purpose counter 1, out of 2.   When PAPI_FP_INS is added next, it can only use counter 1,   so conflict is returned. What I added was code to test and   move the eventcode for PAPI_TOT_INS to counter 2, and add the eventcode   for PAPI_FP_INS to counter 1.
* 1999-05-26 Philip Mucci — <   if (*name) --- >   if (name)
* 1999-05-26 gho — began adding the routines for handling multiple running EventSets- not done yet, i think that i see a better way to set things up than what i have. other than that, fixed some prototypes, and added the new query routine to linux-pentium.c so that it's not broken.
* 1999-05-25 Philip Mucci — Added 2 new functions.
* 1999-05-24 Philip Mucci — Hi all,
* 1999-05-24 Philip Mucci — Quick fix for Makefile.aix
* 1999-05-24 Philip Mucci — Added Makefile for AIX. Make at the top level must be done with make -f Makefile.aix now.
* 1999-05-18 deane — papi_hl.c -- revise per instructions
* 1999-05-14 gho — took care of bug- now fills counter array properly with less than 3 events
* 1999-05-14 Philip Mucci — Finished tree restrutcuring and Makefile cleanup. You should all recheck out a new tree
* 1999-05-12 deane — papi.c -- add functions PAPI_init()                         PAPI_state(int EventSet, int *status)
* 1999-05-12 deane — papi.c -- add functions PAPI_init()                         PAPI_state(int EventSet, int *status)
* 1999-04-28 deane — support.c shows user which standard events are supported on current platform
* 1999-04-13 gho — fixed a couple of things in the examples i forgot earlier
* 1999-04-13 gho — changed some comment lines, nothing interesting
* 1999-04-13 gho — added new example file. uses option structures to change domain for eventset, also shows use of more than one eventset (not simultaneous) added functions for PAPI_set_opt, _papi_set_domain more will follow
* 1999-04-13 Philip Mucci — Fixed memory bugs, fixed SGI substrate, ANY substrate now works, automatic makefile
* 1999-04-13 Philip Mucci — Major integration with George's snapshot. Everything compiles. I'm sure I broke first again with my changes. Another iteration tomorrow. SGI substrate now works ! Apparently the kernel doesn't scale the multiplexed counts so PAPI has to do it. Ugh.
* 1999-04-12 gho —  merged changes phil made with substrate prototypes, option structures, etc. with the re-written papi.c that i did to make it work. domain stuff has not been added yet to higher level.
* 1999-04-12 gho — added first.c to EXAMPLES in Makefile, first.c is the first test file to use Low-Level API the way it will be used by a User.
* 1999-04-12 gho — made changes to work with new stuff
* 1999-04-12 Philip Mucci — Latest snapshot
* 1999-04-12 Philip Mucci — Renamed hwd_control_state to hwd_control_state_t, fixing example for SGI
* 1999-04-12 Philip Mucci — Fixes to get the example working, plus the new header files
* 1999-04-12 Philip Mucci — Abstracted 2 header files for linux/IRIX substrates. Quick prototype and option fixes to the linux substrate. IRIX compiles.
* 1999-04-09 Philip Mucci — Real Makefile!
* 1999-04-09 Philip Mucci — Makefile fixes. Default target is LINUX. Fixed small #ifdef deal too. LINUX_PENTIUM is no longer required.
* 1999-04-09 Philip Mucci — Changes some of the prototypes. We really want unsigned int's for our events and unsigned long long for the CPU counters. Internally, we keep events as int's. Why? because of 2's complement.
* 1999-04-09 Philip Mucci — Presents for the SGI done. Data structures look ok. Will test soon.
* 1999-04-09 Philip Mucci — Not working yet, I'm sure I broke a lot. But this has the option stuff in the right places.
* 1999-04-09 Philip Mucci — Major changes to the option structures and the substrate interface. Efficient and clean. Removed hwd_set/get_opt for hwd_ctl. Substrate now gets to see the EventSetInfo structure.
* 1999-04-09 Philip Mucci — A null substrate that works and builds on any platforms. Reads/writes work. Every read returns 1 more than the last. This reflects major changes in papi.h papi_internal.h and other files.
* 1999-03-31 Philip Mucci — Added more irix goodies, helped out the option cause. GEORGE! Bug fixed pevent (extra was undefined...)
* 1999-03-26 gho — modified these to work with new calls, they still do the same thing as they used to. you can change the domain setting if you want and play.
* 1999-03-26 gho — have added low-level and substrate level set_domain/granularity routines. Phil, I did this differently from what we had discussed. I have some reasons, so maybe we can talk about it sometime and see if I need to change it back to what I was doing before. Added a new example file to show results of this platform's domain settings: PAPI_USR, PAPI_KERNEL, and PAPI_ALL.
* 1999-03-25 deane — function modified: int PAPI_list_events
* 1999-03-24 deane — First I did a cvs update papi.c to get all of George's changes and not be rude to what he did today.
* 1999-03-24 gho — fixed some typos in reset(), and started set_granularity, set_domain, will be worked on more tonight
* 1999-03-24 gho — made read, write, start, stop, reset, handle EventSetInfo and errors like accum does, by phil - sorry, when i wrote them i didn't know about num_counters and lookupEventSet like i should have
* 1999-03-24 gho — took care of a few typecast warnings and a bug in add_event
* 1999-03-23 gho — made some changes to make some things work again.
* 1999-03-23 Philip Mucci — Makefile fixes...
* 1999-03-23 Philip Mucci — You guys couldn't code your way out of a cardboard box.
* 1999-03-23 Philip Mucci — Added 2 functions...
* 1999-03-23 deane — fix typo  [ replace "TBL" with "TLB"  3 times ]
* 1999-03-22 deane — The following functions were added:
* 1999-03-22 gho — in _init() added timing routine to enter estimated proc mhz into _papi_system_info.mhz , added appropriate include files
* 1999-03-22 gho — fixed read, accumulate, stop, and respective prototypes and calls, to have no third argument. substrate level read() now indicates non-used counter value array element by setting it to -1.
* 1999-03-22 Philip Mucci — Checked in system info structure skeletoon.
* 1999-03-22 Philip Mucci — Added overflow and multiplex options. Overflow almost works. Multiplex skeleton is there.
* 1999-03-18 deane — correct typo
* 1999-03-18 deane — in papi.c:
* 1999-03-17 Philip Mucci — Fixed the header of each source file
* 1999-03-17 deane — Add new utility functions that are called by low level functions:
* 1999-03-16 deane — Got rid of a few lines of comments.
* 1999-03-16 gho — only fixed return codes- phil, still thinkning about best way to implement to get/set_opt, ran into some unexpected things, sorry it's not done yet.
* 1999-03-11 gho — second example file, Makefile makes this too. neato
* 1999-03-11 gho — first example file- Makefile will make this automatically
* 1999-03-11 gho — little changes for compilation
* 1999-03-11 gho — made some changes to make it work- i'll add an example file in a while
* 1999-03-11 Philip Mucci — More compile fixes. Overflow is almost complete. Added a couple of utility functions for the papi.c file. Functions like lookup_EventSet event_is_in_eventset, and the like.
* 1999-03-08 Philip Mucci — Bug fixes for add events...cleaned up error handling...all compile errors are gone.
* 1999-03-08 gho —  int papi.c: low-level start, stop, reset, accumulate, read, write functions  Note: untested, but has been compiled.   -george
* 1999-03-05 gho — made whatever changes necessary to compile- now compiles with warnings, using the Makefile Phil did.
* 1999-03-05 Philip Mucci — Lots of fixes...papi.c compiles...PLease try AND follow my lead Guys.
* 1999-03-01 deane — The prototypes from papi.c were stated twice.  I eliminated second set.
* 1999-02-28 deane — I wrote 2 new functions: 1. int PAPI_load_event(EventSetInfo *thisESI, int EventSetIndex); 2. int PAPI_load_dataSlotArrayElement(EventSetInfo *ESI);
* 1999-02-28 deane — I have simplified the error handling by replacing papi_perror and papi_strerror with papi_error.
* 1999-02-28 deane — Revision of papi_state function to conform to new definitions in papi_internal.h.
* 1999-02-28 deane — Revised the function PAPI_shutdown in papi.c.
* 1999-02-28 deane — Revised the function PAPI_shutdown in papi.c and placed the prototype in papi.h
* 1999-02-28 deane — Revised the function PAPI_shutdown in papi.c and placed the prototype in papi.h
* 1999-02-27 deane — introduce globals:  DynamicArray PAPI_EVENT_MAP; 		    int          PAPI_ERR_LEVEL;
* 1999-02-26 deane — Updating functions: _papi_expandDA                     papi_allocate_EventSet                     papi_free_EventSet
* 1999-02-26 deane — #define PAPI_INIT_SLOTS  64
* 1999-02-26 gho — lots of changes- it compiles! woohoo! not tested yet thought, stay tuned...
* 1999-02-26 gho — some include file changes, almost have it compiling
* 1999-02-26 gho — some minor things from meeting
* 1999-02-26 deane — #define PAPI_MAX_PRESET_EVENTS 64 /*The maximum number of preset events                                 defined*/
* 1999-02-26 gho — in start, have appropriate lines for starting TSC, thanks to Phil
* 1999-02-19 gho — _add, _rem, _stop, are there now. sorry if there are typos and whatnot.
* 1999-02-19 gho — have _add part for presets, will do non -preset part after lunch
* 1999-02-19 gho — _start, _reset, _read, _write done
* 1999-02-19 gho — changed arg for a couple fxns from long long *events to long long events[]
* 1999-02-19 gho — fleshed out int _papi_hwd_start, more functions to follow soon....
* 1999-02-18 gho — added most know presets, added new number codes for _hwd_preset structure
* 1999-02-16 deane — _papi_err_level is defined twice in papi_internal.h
* 1999-02-16 deane — revision of one line of comment:
* 1999-02-16 deane — There are two definitions for the function _papi_err_level in papi_internal.h.  I commented out the first one, but left the line in the file because I do not know which is the correct definition. extern int _papi_err_level; extern int _papi_err_level(int level); /* get/set error level */
* 1999-02-16 deane — added functions:
* 1999-02-16 deane — 3 names in _EventSetInfo data structure modified to be more explicit.
* 1999-02-14 browne — added PAPI_state() to papi.c added declarations for evmap and _papi_err_level to papi_internal.h
* 1999-02-14 deane — The files: papi_internal.h     and    papi.c
* 1999-02-13 deane — I have put the function _papi_expandDA into papi.c
* 1999-02-13 deane — The following changes were made to papi_internal.h:
* 1999-02-13 deane — The following line was added to papi_internal.h:
* 1999-02-13 deane — This update was done to correct the line
* 1999-02-13 deane — *** empty log message ***
* 1999-02-12 Philip Mucci — First revision of cricket's standardized definitions. To be finxed shortly.
* 1999-02-10 Philip Mucci — Ok, I already screwed up. Fixed the keyword logs
* 1999-02-10 Philip Mucci — First revisions from George
