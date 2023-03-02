import pickle

def assemble(Title, Desc, Template, Email, Purpose, Org, Role):
	if Template:
		with open(Template, 'rb') as f:
			Template = f.readlines()
	return {"Title": Title, "Desc": Desc, "Template": Template, "Email": Email, "Purpose": Purpose, "Org": Org, "Role": Role}

def ncode(Dict):
	return pickle.dumps(Dict)