# corresponds to the Knorr_pyrazole_synthesis *see rxn variable below
# assigned by looking at smiles-to-image
amine_h2=35
amine_hr=36
oxygen_ring=102
carbonyl_ring=34
alpha_c=7
carbonyl_non_ring=1
oxygen_non_ring=101

rxn='[O:101]=[C:1]([C:2]([O:3][CH2:4][CH3:5])=[O:6])[CH:7]1[CH2:8][CH2:9][c:10]2[c:11]([cH:12][n:13][n:14]2[C:15]([c:16]2[cH:17][cH:18][cH:19][cH:20][cH:21]2)([c:22]2[cH:23][cH:24][cH:25][cH:26][cH:27]2)[c:28]2[cH:29][cH:30][cH:31][cH:32][cH:33]2)[C:34]1=[O:102].[NH2:35][NH:36][CH2:37][CH2:38][OH:39].[H+:301].[H+:302]>>[c:1]1([C:2]([O:3][CH2:4][CH3:5])=[O:6])[c:7]2[c:34]([n:36]([CH2:37][CH2:38][OH:39])[n:35]1)-[c:11]1[c:10]([n:14]([C:15]([c:16]3[cH:17][cH:18][cH:19][cH:20][cH:21]3)([c:22]3[cH:23][cH:24][cH:25][cH:26][cH:27]3)[c:28]3[cH:29][cH:30][cH:31][cH:32][cH:33]3)[n:13][cH:12]1)[CH2:9][CH2:8]2'
t_rxn='[N:1]-[N:2].[O:6]=[C:3]-[C:4]-[C:5]=[O:7]>>[n:1]1:[n:2]:[c:3]:[c:4]:[c:5]:1'
# this is the original output of the MechFinder.get_LRT procedure
#replacement_dict={1: 35, 2: 36, 3: 34, 4: 7, 5: 1, 6: 102, 7: 101}
replacement_dict={1: amine_h2, 2: amine_hr, 3: carbonyl_ring, 4: alpha_c, 5: carbonyl_non_ring, 6: oxygen_ring, 7: oxygen_non_ring}
'''
{
35: 1,   amine_h2
36: 2,   amine_hr
34: 3,   carbonyl_ring
7: 4,    alpha_c
1: 5,    carbonyl_non_ring
102: 6,  oxygen_ring
101: 7   oxygen_non_ring
}
'''
# fmap is the inverse of the replacement_dict output of the MechFinder.get_LRT procedure
fmap={
    amine_h2: 1, 
    amine_hr: 2, 
    carbonyl_ring: 3, 
    alpha_c: 4, 
    carbonyl_non_ring: 5, 
    oxygen_ring: 6, 
    oxygen_non_ring: 7
}
'''
[N:1]-[N:2].[O:6]=[C:3]-[C:4]-[C:5]=[O:7]>>[n:1]1:[n:2]:[c:3]:[c:4]:[c:5]:1
'''
t_mech=[(2, 3), ([3, 6], 8), (6, 2.1), ([2.1, 2], 2), (2, [2, 3]), ([3, 6], 6), (1, 5), ([5, 7], 9),  (7, 1.1), ([1.1, 1], 1), (1, [1, 5]), ([5, 7], 7), ([4.1, 4], [4, 5]), ([5, 1], 1)]
# t_mech atom -> rmap inverse

remap={
    amine_h2: 2,
    carbonyl_non_ring: 3,
    oxygen_non_ring: 6,
    amine_hr: 1,
    carbonyl_ring: 5,
    oxygen_ring: 7,
    alpha_c: 4
}
#remap_inv = {v: k for k, v in remap.items()}
print(remap) # use output to overwrite the return value of replacement_dict from MechFinder.get_electron_path to test/debug
#print(f'remap_inv: {remap_inv}')
elec_path_remap = {k: remap[v] for k, v in replacement_dict.items()}
print(elec_path_remap)

def get_new_id(id):
    try:
        if isinstance(id, int):
            return elec_path_remap[id]
        elif isinstance(id, list):
            return [get_new_id(i) for i in id]
        elif isinstance(id, float):
            return elec_path_remap[int(id)] + .1
        return elec_path_remap[id]
    except KeyError:
        # might be one of the ids on the reagents
        return id

new_epath = [ (get_new_id(src), get_new_id(dest)) for src, dest in t_mech]
print(f'new epath: {new_epath}')
# instead of updating the mapping, we need to update the electron_path.


'''
amine_h2=35
amine_hr=36
oxygen_ring=102
carbonyl_ring=34
alpha_c=7
carbonyl_non_ring=1
oxygen_non_ring=101
'''

