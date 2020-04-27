# UT-TOR-DATA-PT-01-2020-U-C Week 11
# Web Design Challenge
# Data Import, Transformation, Export for display (html) and charting (csv)
# (c) Boris Smirnov

# Basically, this module was copy-pasted from a notebook where I debugged this code

# Depedences
import pandas as pd

# Files with translation tables
parties_fname = 'all_parties_2015.csv' # List of parties with party codes and different versiona of names
provinces_fname = 'provinces_ids.csv' # List or province names, codes and abbreviations
ro2003_fname = 'ro2003.csv' # Representation order 2003 with mappings from FED names to FED Ids

# Dictionary tables
ro2003_df = pd.read_csv(ro2003_fname)
provinces_df = pd.read_csv(provinces_fname)

# Political Parties Conundrum
# ============================
parties_df = pd.read_csv(parties_fname)

# Extending dictionary with parties that participated in elections before 2015
CAP_party = { # 1997-2017
    'Id': 'CAP',
    'Long Name (en)': 'Canadian Action Party',
    'Long Name (fr)': 'Parti action canadienne',
    'Short Name (fr)': 'Action canadienne',
    'Short Name (en)': 'Canadian Action',
    'Candidate Suffix': 'Canadian Action/Action canadienne'
}

FPNP_party = { # 2004-2013
    'Id': 'FPNP',
    'Long Name (en)': 'First Peoples National Party of Canada',
    'Long Name (fr)': 'First Peoples National Party of Canada',
    'Short Name (fr)': 'FPNP',
    'Short Name (en)': 'FPNP',
    'Candidate Suffix': 'FPNP/FPNP'
}

WBP_party = { # 2005-2014
    'Id': 'WBP',
    'Long Name (en)': 'Western Block Party',
    'Long Name (fr)': 'Western Block Party',
    'Short Name (fr)': 'WBP',
    'Short Name (en)': 'WBP',
    'Candidate Suffix': 'WBP/WBP'
}

NLFP_party = { # 2004-2011
    'Id': 'NLFP',
    'Long Name (en)': 'Newfoundland and Labrador First Party',
    'Long Name (fr)': 'Newfoundland and Labrador First Party',
    'Short Name (fr)': 'NL First Party',
    'Short Name (en)': 'NL First Party',
    'Candidate Suffix': 'NL First Party/NL First Party'
}

PPP_party = { # 2006-2011
    'Id': 'PPP',
    'Long Name (en)': "People's Political Power Party of Canada",
    'Long Name (fr)': 'Pouvoir Politique du Peuple du Canada',
    'Short Name (fr)': 'PPP',
    'Short Name (en)': 'PPP',
    'Candidate Suffix': 'PPP/PPP'
}

WLP_party = { # 2007-2010
    'Id': 'WLP',
    'Long Name (en)': 'Work Less Party',
    'Long Name (fr)': 'Work Less Party',
    'Short Name (fr)': 'Work Less Party',
    'Short Name (en)': 'Work Less Party',
    'Candidate Suffix': 'Work Less Party/Work Less Party'
}

NCA_party = {
    'Id': 'NCA',
    'Long Name (en)': 'National Citizens Alliance of Canada',
    'Long Name (fr)': 'Alliance Nationale des Citoyens du Canada',
    'Short Name (fr)': 'Alliance Nationale Citoyens',
    'Short Name (en)': 'National Citizens Alliance',
    'Candidate Suffix': 'National Citizens Alliance/Alliance Nationale Citoyens'
}

SCC_party = {
    'Id': 'SCC',
    'Long Name (en)': 'Stop Climate Change',
    'Long Name (fr)': 'Arrêtons le changement climatique',
    'Short Name (fr)': 'Arrêtonslechangementclimatique',
    'Short Name (en)': 'Stop Climate Change',
    'Candidate Suffix': 'Stop Climate Change/Arrêtonslechangementclimatique'
}

VCP_party = {
    'Id': 'VCP',
    'Long Name (en)': 'Veterans Coalition Party of Canada',
    'Long Name (fr)': 'Parti de la coalition des anciens combattants du Canada',
    'Short Name (fr)': 'CAC',
    'Short Name (en)': 'VCP',
    'Candidate Suffix': 'VCP/CAC'
}

CNP_party = {
    'Id': 'CNP',
    'Long Name (en)': 'Canadian Nationalist Party',
    'Long Name (fr)': 'Parti Nationaliste Canadien',
    'Short Name (fr)': 'Nationaliste',
    'Short Name (en)': 'Nationalist',
    'Candidate Suffix': 'Nationalist/Nationaliste'
}

PPC_party = {
    'Id': 'PPC',
    'Long Name (en)': "People's Party of Canada",
    'Long Name (fr)': 'Parti populaire du Canada',
    'Short Name (fr)': 'Parti populaire',
    'Short Name (en)': "People's Party",
    'Candidate Suffix': "People's Party/Parti populaire"
}

PIQ_party = {
    'Id': 'PIQ',
    'Long Name (en)': "Parti pour l'Indépendance du Québec",
    'Long Name (fr)': "Parti pour l'Indépendance du Québec",
    'Short Name (fr)': "Pour l'Indépendance du Québec",
    'Short Name (en)': "Pour l'Indépendance du Québec",
    'Candidate Suffix': "Pour l'Indépendance du Québec/Pour l'Indépendance du Québec"
}

CFF_party = {
    'Id': 'CFF',
    'Long Name (en)': "Canada's Fourth Front",
    'Long Name (fr)': 'Quatrième front du Canada',
    'Short Name (fr)': "QFC - Quatrième front du Canada",
    'Short Name (en)': "CFF - Canada's Fourth Front",
    'Candidate Suffix': "CFF - Canada's Fourth Front/QFC - Quatrième front du Canada"
}

parties_df = parties_df.append(
    [CAP_party, FPNP_party, WBP_party, NLFP_party, PPP_party, WLP_party,
    NCA_party, SCC_party, VCP_party, CNP_party, PPC_party, PIQ_party, CFF_party],
    ignore_index=True)

# As it appears, the idea of 'Candidate Suffix' column wasn't good
# Fixing it with adding new 'Tail' column which contains party name 'signatures' that I'll
# match against candidate names to find out his/her party affiliation
parties_df['Tail'] = parties_df['Candidate Suffix'].apply(lambda s: s.rsplit('/', 1)[-1].casefold())

# Ad hoc case for NPD, that was named slightly differently in 2004 and 2006 data
ndp_dict = parties_df[parties_df['Id'] == 'NDP'].to_dict('records')[0]
ndp_dict['Tail'] = 'n.p.d.'

# Ad hoc case for Marijuana Party, that was named slightly differently in 2004 and 2006 data
# 'Parti Marijuana' -> 'Radical Marijuana' in table12
mar_dict = parties_df[parties_df['Id'] == 'MAR'].to_dict('records')[0]
mar_dict['Tail'] = 'parti marijuana'

# Ad hoc case for Animal Alliance Environment Voters Party of Canada, that was named slightly differently in 2006, 2008, 2019 data
# 'AACEV Party of Canada' -> 'Animal Alliance Environment Voters Party of Canada'
aa_dict = parties_df[parties_df['Id'] == 'AA'].to_dict('records')[0]
aa_dict['Tail'] = 'aacev party of canada'
aa2_dict = parties_df[parties_df['Id'] == 'AA'].to_dict('records')[0]
aa2_dict['Tail'] = 'aaev party of canada'
aa3_dict = parties_df[parties_df['Id'] == 'AA'].to_dict('records')[0]
aa3_dict['Tail'] = 'parti protection animaux'

# Ad hoc case for Rhinoceros Party, that was named slightly differently in 2008 data
# 'neorhino.ca' -> Rhinoceros Party
rhi_dict = parties_df[parties_df['Id'] == 'RHI'].to_dict('records')[0]
rhi_dict['Tail'] = 'neorhino.ca'

# Ad hoc case for Rhinoceros Party, that was named slightly differently in 2011 data
pir_dict = parties_df[parties_df['Id'] == 'PIR'].to_dict('records')[0]
pir_dict['Tail'] = 'parti pirate'

# Ad hoc case for Christian Heritage Party, that was named slightly differently in 2011 data
chp_dict = parties_df[parties_df['Id'] == 'CHP'].to_dict('records')[0]
chp_dict['Tail'] = 'phc canada'

# 2019 - a whole bunch of ad hocs (((((
ml_dict = parties_df[parties_df['Id'] == 'ML'].to_dict('records')[0]
ml_dict['Tail'] = 'ml'

rhi2_dict = parties_df[parties_df['Id'] == 'RHI'].to_dict('records')[0]
rhi2_dict['Tail'] = 'parti rhinocéros party'

uni_dict = parties_df[parties_df['Id'] == 'UNI'].to_dict('records')[0]
uni_dict['Tail'] = 'upc'

ind_dict = parties_df[parties_df['Id'] == 'IND'].to_dict('records')[0]
ind_dict['Tail'] = 'indépendant(e)'


# Extended party list will be used for assigning party Ids to the candidates
parties_ext_df = parties_df.append(
    [ndp_dict, mar_dict, aa_dict, aa2_dict, aa3_dict, rhi_dict, pir_dict, chp_dict, ml_dict, rhi2_dict, uni_dict, ind_dict],
    ignore_index=True).copy()

# The function is used in DataFrame apply() to find candidates Party Ids
# when adding 'Party Id' column
# This function uses Ad Hoc dictionary parties_ext_df with additional rows
def find_party_id(candidate):
    global parties_ext_df
    tail = candidate.rsplit('/', 1)[-1].casefold()
    return parties_ext_df.loc[parties_ext_df['Tail'] == tail]['Id'].item()

# Data import and transformation
# ===============================

# Transormation rules for table_tableau11.csv files
# 2019, 2015, 2011, 2008 - identical column names
# 2006 and 2004 - different column names
transformation11 = {
    2008 : {
        'drop' : [
            'Province',
            'Population',
            'Electors/Électeurs',
            'Polling Stations/Bureaux de scrutin',
            'Valid Ballots/Bulletins valides',
            'Percentage of Valid Ballots /Pourcentage des bulletins valides',
            'Rejected Ballots/Bulletins rejetés',
            'Percentage of Rejected Ballots /Pourcentage des bulletins rejetés',
            'Percentage of Voter Turnout/Pourcentage de la participation électorale'
        ],
        'rename': {
            'Electoral District Name/Nom de circonscription': 'FED Name',
            'Electoral District Number/Numéro de circonscription' : 'FED Id',
            'Total Ballots Cast/Total des bulletins déposés': 'Ballots',
            'Elected Candidate/Candidat élu': 'Winner' # I need winning party id
        }
    },
    2006 : {
        'drop' : [
            'Province',
            'Population',
            'Electors/Électeurs',
            'Polling Stations/Bureaux de scrutin',
            'Valid Ballots/Bulletins valides',
            'Percentage of Valid Ballots /Pourcentage des bulletins valides',
            'Rejected Ballots/Bulletins rejetés',
            'Percentage of Rejected Ballots /Pourcentage des bulletins rejetés',
            'Percentage of Voter Turnout/Pourcentage de la participation électorale'
        ],
        'rename': {
            'Electoral District/Circonscription': 'FED Name',
            'Total Ballots Cast/Total des bulletins déposés': 'Ballots',
            'Elected Candidate/Candidat élu': 'Winner' # I need winning party id
        }
    },
    2004 : {
        'drop' : [
            'Province',
            'Population',
            'Electors',
            'Total Polls',
            'Valid Ballots',
            'Valid Ballots Percent',
            'Rejected Ballots',
            'Rejected Ballots Percent',
            'Voter Turnout'
        ],
        'rename': {
            'District': 'FED Name',
            'Total Ballots': 'Ballots',
            'Candidate': 'Winner' # I need winning party id
        }
    }
}

# The funcions reads table_tableau11.csv for a given year,
# removes unneeded columns, rename columns, adds FED Ids where necessary
# Retuns DataFrame
def load_table11(year):

    # Initializing local variables
    # ============================

    trans_id = year
    
    # Choose wich tranformation to apply:
    # there are separate rules for 2004 and 2006, all other years are processed as 2008
    if year > 2008:
        trans_id = 2008

    table11_fname = str(year) + '/table_tableau11.csv'

    # Data load and transformation
    # ============================
    table11_df = pd.read_csv(table11_fname)
    table11_df.drop(columns=transformation11[trans_id]['drop'], inplace=True)
    table11_df.rename(columns=transformation11[trans_id]['rename'], inplace=True)

    # Adding missing 'FED Id' to 2004 and 2006 data
    if year == 2004:
        ids_df = ro2003_df[['FED Name 2004', 'FED Id']].set_index('FED Name 2004')
    elif year == 2006:
        ids_df = ro2003_df[['FED Name 2008', 'FED Id']].set_index('FED Name 2008')

    if year < 2008:
        # The order of columns here will be slightly different
        table11_df = pd.merge(table11_df, ids_df, how='left', left_on='FED Name', right_index=True)

    # Add column with winning party Id, and remove unneeded columns
    # Similarly to parties_df['Tail'], add temporary column for matching Party Id
    table11_df['Tail'] = table11_df['Winner'].apply(lambda s: s.rsplit('/', 1)[-1].casefold())
    table11_df['Party Id'] = table11_df['Winner'].apply(find_party_id)
    table11_df.drop(columns=['Winner', 'Tail'], inplace=True)

    # Now we have 'Party Id' and 'FED Id' for merging
    return table11_df



# Transormation rules for table_tableau11.csv files
# 2019, 2015, 2011, 2008 - identical column names
# 2006 and 2004 - different column names
transformation12 = {
    2008 : {
        'drop' : [
            'Candidate Residence/Résidence du candidat',
            'Candidate Occupation/Profession du candidat',
            'Percentage of Votes Obtained /Pourcentage des votes obtenus',
            'Majority/Majorité',
            'Majority Percentage/Pourcentage de majorité'
        ],
        'rename': {
            'Province': 'Province Name',
            'Electoral District/Circonscription': 'FED Name',
            'Electoral District Number/Numéro de circonscription': 'FED Id',
            'Candidate/Candidat': 'Candidate',
            'Votes Obtained/Votes obtenus': 'Votes'
        }
    },
    2006 : {
        'drop' : [
            'Candidate Residence/Résidence du candidat',
            'Candidate Occupation/Profession du candidat',
            'Percentage of Votes Obtained /Pourcentage des votes obtenus',
            'Majority/Majorité',
            'Majority Percentage/Pourcentage de majorité'
        ],
        'rename': {
            'Province': 'Province Name',
            'Electoral District/Circonscription': 'FED Name',
            'Candidate/Candidat': 'Candidate',
            'Votes Obtained/Votes obtenus': 'Votes'
        }
    },
    2004 : {
        'drop' : [
            'Residence',
            'Occupation',
            'Number of Votes Percent',
            'Number Majority',
            'Majority Percent'
        ],
        'rename': {
            'Province': 'Province Name',
            'District': 'FED Name',
            'Candidate': 'Candidate',
            'Number of Votes': 'Votes'
        }
    }
}

# The funcions reads table_tableau11.csv for a given year,
# removes unneeded columns, rename columns, adds FED Ids where necessary
# Retuns DataFrame
def load_table12(year):

    # Initializing local variables
    # ============================

    trans_id = year
    
    # Choose wich tranformation to apply:
    # there are separate rules for 2004 and 2006, all other years are processed as 2008
    if year > 2008:
        trans_id = 2008

    table12_fname = str(year) + '/table_tableau12.csv'

    # Data load and transformation
    # ============================
    table12_df = pd.read_csv(table12_fname)
    table12_df.drop(columns=transformation12[trans_id]['drop'], inplace=True)
    table12_df.rename(columns=transformation12[trans_id]['rename'], inplace=True)

    # Adding missing 'FED Id' to 2004 and 2006 data
    if year == 2004:
        ids_df = ro2003_df[['FED Name 2004', 'FED Id']].set_index('FED Name 2004')
    elif year == 2006:
        ids_df = ro2003_df[['FED Name 2008', 'FED Id']].set_index('FED Name 2008')

    if year < 2008:
        # The order of columns here will be slightly different
        table12_df = pd.merge(table12_df, ids_df, how='left', left_on='FED Name', right_index=True)

    # Add column with winning party Id, and remove unneeded columns
    # Similarly to parties_df['Tail'], add temporary column for matching Party Id
    table12_df['Tail'] = table12_df['Candidate'].apply(lambda s: s.rsplit('/', 1)[-1].casefold())
    table12_df['Party Id'] = table12_df['Candidate'].apply(find_party_id)
    table12_df.drop(columns=['Candidate', 'Tail'], inplace=True)

    # Removing french part in provinces names and adding province abbreviations (Canada post codes)
    table12_df['Province Name'] = table12_df['Province Name'].map(lambda name: name.split('/', 1)[0])
    table12_df['Province'] = table12_df['Province Name'].map(lambda name: provinces_df[provinces_df['Province Name (en)'] == name]['Alpha code'].item())

    # Now we have 'Party Id' and 'FED Id' for merging, 'Province' for compact display
    return table12_df
