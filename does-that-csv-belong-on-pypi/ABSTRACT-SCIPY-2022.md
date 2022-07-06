# Talk Abstract

This document contains the contents of the abstract submitted to the SciPy 2022 conference committee in February 2022.

<hr>

If you could reduce the size of a popular Python package by 5 MB, would it matter?

In my opinion, the answer is "yes". This talk presents an argument supporting that position.

## What, specifically, will attendees learn from the talk?

### short outline

(00:00 - 03:00) What is a Python package and what files does it usually contain?
(03:00 - 15:00) Specific examples of issues caused by larger package distributions.
(15:00 - 20:00) Specific examples of unnecessary files in some popular packages on PyPI.
(20:00 - 24:00) Guidance on how to keep packages small (e.g. with MANIFEST.in) and how to measure the impact of changes on package size
(24:00 - 25:00) Call to action to go try to contribute changes like these in open source projects.

### longer outline

Attendees will learn about the types of files that Python packages should contain, at a level of detail much more specific than ".py files and a license".

Next, they'll learn about all of the specific negative impacts of unnecessarily-large packages. This section of the talk will be the longest, and is intended to get attendees thinking holistically and creatively about all the places that a Python package can travel to.

For example, a larger package tarball means:

* increased outbound data transfer for package repositories like PyPI and conda-forge
    - exacerbated by the fact that newer versions of the pip resolver now often download multiple versions of the same package while searching for compatible sets of versions
* increased inbound data transfer for anyone installing packages
    - extra problematic in the presence of weak or unreliable internet connections
* increased storage footprint for package repositories like PyPI and conda-forge
* increased image size for container images, which implies:
    - increased storage footprint
    - longer pull times for Docker images
    - which, on services like Kubernetes or Amazon ECS, may translate to increased latency when running containerized Python tasks
* increased storage footprint in the places where people run Python code
    - a few MB can be meaningful in storage-sensitive settings like Raspberry Pi / Arduino, or in function-as-a-service cloud services like AWS Lambda (250MB limit for packages, https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) or Google Cloud Functions (500MB limit for packages, https://cloud.google.com/functions/quotas)

After these examples, attendees will learn about some broad classes of "unnecessary files" found in popular Python packages.
Examples will include test code / data, rendered documentation files, and continuous-integration configs / scripts.
The goal of this discussion will be to teach attendees some common patterns to look out for.

Attendees will also learn how to reduce the size of packages (e.g. by using rules in a MANIFEST.in file), and how to measure the compressed and uncompressed size of Python packages.

## Who is the intended audience for the talk?

Anyone developing Python packages, or looking for ideas on how to contribute back to the packages they use.

## How do we know you're qualified to talk about this topic?

I have been a maintainer on LightGBM (https://github.com/microsoft/LightGBM) since 2018.
That project includes a Python package which wraps a large C++ library.

I have firsthand professional experience dealing with the package-size constraints on AWS Lambda, trying to create a Python Lambda using scikit-learn + pandas + lightgbm and doing things like this: https://github.com/jameslamb/talks/blob/a08a519324859e0c3712badf8479bd4a5ad1a2ac/cloud-intro/scripts/create-layers.sh#L49-L52.

I have firsthand experience proposing changes similar to those mentioned in this talk and working with maintainers to get those changes merged into popular projects:

* https://github.com/pandas-dev/pandas/pull/38846
* https://github.com/pandas-dev/pandas/issues/30741#issuecomment-752751976
* https://github.com/microsoft/LightGBM/pull/3579
* https://github.com/microsoft/LightGBM/pull/3639
* https://github.com/dmlc/xgboost/pull/6565

I've given previous conference talks about open source and Python software. For example:

* "How Distributed LightGBM on Dask Works" (Dask Distributed Summit): https://zoom.us/rec/play/9rwWWxsUq9FiF1oP-ZOwTYoUw3JvI6CgHfhCdS1kQipiOAwR95nwHtELNK4GjFQINWB1DTFl0_9bm1_L.GR3TFusllitynPlt?continueMode=true&_x_zm_rtaid=6y6ososIT12VbHwTYkM8Hg.1644469209953.f5594cbe8503307ac7c98a1cfd1adcde&_x_zm_rhtaid=958
* "You can and should do open source" (Catboost conference): https://www.youtube.com/watch?v=ObzrXjqWcTY&t=9200s
* other talks at https://github.com/jameslamb/talks

## Other Notes

Thanks very much for considering me!
