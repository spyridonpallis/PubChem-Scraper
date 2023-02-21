import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Draw

# Prompt the user for a molecule name
molecule_name = input("Enter a molecule name: ")

# Search for the molecule using PubChemPy
results = pcp.get_compounds(molecule_name, 'name')

# Check if any results were found
if not results:
    print(f"No results found for '{molecule_name}'.")
else:
    # Get the first result and retrieve the 2D structure as a SMILES string
    compound = results[0]
    smiles = compound.isomeric_smiles

    # Use RDKit to convert the SMILES string to a molecule objectA
    mol = Chem.MolFromSmiles(smiles)

    # Use RDKit to draw the molecule and display it in a window
    Draw.MolToFile(mol, "molecule.png")
    Draw.MolToImage(mol).show()
