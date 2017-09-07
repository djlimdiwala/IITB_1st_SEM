fstarcsort --sort_type=olabel {160}.fsa.txt {160}.fsa.txt
fstarcsort --sort_type=ilabel E.fst E.fst
fstcompose {160}.fsa.txt E.fst me.fst
fstarcsort --sort_type=olabel me.fst me.fst
fstarcsort --sort_type=ilabel TI.fst TI.fst
fstcompose me.fst TI.fst met.fst
fstarcsort --sort_type=olabel met.fst met.fst
fstarcsort --sort_type=ilabel G.fst G.fst
fstcompose met.fst G.fst metg.fst
fstdraw --isymbols=isyms.txt --osymbols=osyms.txt metg.fst metg.dot
dot -Tps metg.dot >metg.ps
fstprint --isymbols=isyms.txt --osymbols=osyms.txt metg.fst text.fst
