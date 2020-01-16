# Introduction to Protein Databases

from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw(input())
record