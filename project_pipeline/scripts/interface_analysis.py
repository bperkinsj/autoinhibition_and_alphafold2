'''
Analyze the quality of PDB files based on the percentage of residues in the inhibitory and active domains.
'''
import pandas as pd
import main


# Define the path of the CIF files and the reference dataframe
all_cif_path = 'data/input/RCSB_cif/'
df_prot = pd.read_csv(snakemake.input[0], sep = '\t')
best_cif_path = 'data/input/RCSB_cif_best/'

# Get the percentage of residues in the inhibitory and active domains
'''
Columns of data frame after this step: ['gene_name', 'uniprot', 'protein_length', 'region_1', 'region_2', 'region_1_len', 
                                 'region_2_len', 'pdb', 'pdb_length', 'resolution',
                                 'model', 'chain', 'auth_offset', 'pdb residues in region_1', 'pdb residues in region_2', 
                                 'percent_region_1', 'percent_region_2']
'''

print('Finding best files...')
df_prot = main.find_domain_completeness(df_prot, all_cif_path)

# Save several data frames with differentiating quality of domains: both domains with 80% of residues, domain 1 with 80% of residues,
# domain 2 with 80% of residues, and both domains with 60% of residues

df_list = main.save_domain_quality_files(df_prot, snakemake.output[0], snakemake.output[1], snakemake.output[2], snakemake.output[3], snakemake.output[4])

# Merge the dataframes into one and save all files into one folder
dfs_merged = pd.concat(df_list).drop_duplicates(keep='first').reset_index(drop = True)

# Copy the files for each dataframe into new folders
print('Found best files. Copying...')
copy_result = main.copy_best_files(dfs_merged, all_cif_path, best_cif_path)
print(copy_result)

# Use the dataframe with at least 60% of residues in both domains to find the interfaces
df_60 = df_list[3]

# Get the interacting residues
print('Finding interfaces...')
df_60_interacting = main.get_interfaces(df_60, best_cif_path)

# Get the largest interfaces
print('Finding largest interfaces...')
df_60_largest_interfaces = main.largest_interface(df_60_interacting)

# Save the dataframe with the interacting residues
print('Saving interfaces...')
df_60_largest_interfaces.to_csv(snakemake.output[5], sep = '\t', index = False)