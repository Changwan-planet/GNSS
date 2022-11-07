#!/bin/bash

path=/home/changwan/MODULE

gfortran -g GNSS_correction3.f90 $path/MD_BASIC.f90 -o test

