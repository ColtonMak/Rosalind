# Introduction to the Bioinformatics Armory

from Bio.Seq import Seq

seq = Seq(input())
a = str(seq.count("A"))
c = str(seq.count("C"))
g = str(seq.count("G"))
t = str(seq.count("T"))

print(a+" "+c+" "+g+" "+t)