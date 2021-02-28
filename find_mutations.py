from Bio.SeqIO import parse 
from Bio.SeqRecord import SeqRecord 
from Bio.Seq import Seq 
from Bio.Data import IUPACData

print("\n\nOriginal virus genome from Wuhan China\n\n\n\n")
file = open("ref_sequence.gb") 
records = parse(file, "genbank") 
for record in records:    
	print("Id: %s" % record.id) 
	print("Name: %s" % record.name) 
	print("Description: %s" % record.description) 
	print("Annotations: %s" % record.annotations) 
	#print("Sequence Data: %s" % record.seq) 
	print("Sequence Alphabet: %s" % record.seq.alphabet)
	len_wuhan=len(record.seq)
	seq_wuhan=str(record.seq)
	print("The length of sequence from China is", len_wuhan)
	print("*************")

print("\n\n\nVirus genome from India\n\n\n\n")
file = open("telengana_30april.gb") 
records = parse(file, "genbank") 
for record in records:    
	print("Id: %s" % record.id) 
	print("Name: %s" % record.name) 
	print("Description: %s" % record.description) 
	print("Annotations: %s" % record.annotations) 
	#print("Sequence Data: %s" % record.seq) 
	print("Sequence Alphabet: %s" % record.seq.alphabet)
	len_india=len(record.seq)
	seq_india=str(record.seq)
	print("The length of sequence from India is", len_india)
	print("*************\n\n\n\n")
	
print("Mismatches or Mutations are observed at\n\n")
print("Index         Base Pair China     Base Pair India\n\n\n")
base_pair_index=1

for bp_china,bp_india in zip(seq_wuhan,seq_india):
	if bp_china != bp_india:
		print(f"{base_pair_index:5})                   {bp_china:15} {bp_india:15}")
	base_pair_index+=1


