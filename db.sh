#!/usr/bin/env bash

##
## ensure script stops on errors
set -eu
set -o pipefail

##
## load your data into a Postgres DB
csvsql data.csv --db=postgresql:///dataset --insert

## Rename Capital Date, Season, FT to small else it will give error