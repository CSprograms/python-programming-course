"""
NCERT Supplementary Program - Unit 6: Tuples and Dictionaries

Maharashtra

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
stateCapital = {'AndhraPradesh':'Hyderabad', 'Bihar':'Patna',
                'Maharashtra':'Mumbai',  'Rajasthan':'Jaipur'}
print(stateCapital.get('Bihar'))             # i
print(stateCapital.keys())                   # ii
print(stateCapital.values())                 # iii
print(stateCapital.items())                  # iv
print(len(stateCapital))                     # v
print('Maharashtra' in stateCapital)         # vi
print(stateCapital.get('Assam'))             # vii  -> None
del stateCapital['Rajasthan']
print(stateCapital)                          # viii
