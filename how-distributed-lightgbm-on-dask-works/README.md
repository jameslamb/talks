# How Distributed LightGBM Works

> In this talk, attendees will learn about LightGBM, a popular gradient boosting library from Microsoft. After a high-level overview of the LightGBM algorithm, the talk will describe strategies for distributed training of gradient boosted decision tree (GBDT) models generally, and distributed training of LightGBM models specifically.

> With this base established, the bulk of the talk will cover the current state of LightGBM's Dask integration. Attendees will learn the division of responsibilities between Dask and LightGBM's existing distributed training framework, which is written in C++. The talk will also cover the specific components of the Dask ecosystem that LightGBM relies on.

> The talk offers details on distributed LightGBM training, and describes the main implementation of it using Dask. Attendees will learn which pieces of the Dask ecosystem LightGBM relies on, and what challenges LightGBM faces in using Dask to wrap existing distributed training code written in C++.

## Where this talk has been given

* (virtual) [Dask Distributed Summit 2021](https://summit.dask.org/schedule/presentation/29/how-distributed-lightgbm-on-dask-works/), May 2021 ([video](https://zoom.us/rec/share/2MDNheUjidMT7EOcVuD0qnCph3OGnk9Wjf6QZo-8YLO95bzCEHaiDH6I5LmeqXE.Y87S6St0o2DuG29G) | [slides](https://docs.google.com/presentation/d/1ZsM0aOfRG0ZS3rG5T-Prf0NNUY3ZAsP-G-WTDZ-zi-0/edit?usp=sharing))
