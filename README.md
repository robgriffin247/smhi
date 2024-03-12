# SMHI 

Code and documentation made to try the SMHI API. Aim, collect climate data from SMHI.

### Steps:

1. added poetry with `poetry init`
1. activated a `poetry shell`
1. added dependencies with
```{bash}
poetry add requests
poetry add pandas
```
1. created functions to make api requests and return dataframes with stations, parameters, metobs (historic and recent)
    - **TODO** metobs functions need work, as the column names may vary between parameters (fine for recent, historic needs overhaul)
1. **TODO** created staging scripts for chosen climate data; consider which datasets are parent/child (e.g. do I need to download daily max air temp, or can I take hourly data and derive the max daily to reduce api activity?)