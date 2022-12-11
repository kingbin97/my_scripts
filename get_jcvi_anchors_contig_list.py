#!/usr/bin/env python
import os,sys

# bed_file = './longstitch_v3_A.bed'
# anchors_file = './longstitch_v3_A.longstitch_v3_B.anchors'
# contig_length = './A.length.txt'
bed_file = sys.argv[1]
anchors_file = sys.argv[2]
contig_length = sys.argv[3]


def get_bed_dict(bed_file):
    global bed_dict
    bed_dict = {}
    with open(bed_file) as read_bed:
        for line_bed in read_bed:
            line_bed = line_bed.strip().split("\t")
            bed_key = line_bed[3]
            bed_value = line_bed[0]
            bed_dict[bed_key] = bed_value
    print(bed_dict)

def get_anchors_contig(anchors_file):
    write_out = open('./out.txt','w')
    contig_dict = {}
    all_contig_set = set()
    anchors_contig_set = set()
    with open(anchors_file) as read_anchors:
        for line_anchors in read_anchors:
            if line_anchors.startswith("#"):
                pass
            else:
                line_anchors = line_anchors.strip().split("\t")
                all_contig_set.add(bed_dict[line_anchors[0]])
                if bed_dict[line_anchors[0]] == bed_dict[line_anchors[1]]:
                    pass
                else:
                    write_out.write(f"{bed_dict[line_anchors[0]]}\t{bed_dict[line_anchors[1]]}\n")

    write_out.close()


get_bed_dict(bed_file)
get_anchors_contig(anchors_file)
