def capitalize_last_names():
    with open("surnames.txt", 'r') as f:
        last_names = f.readlines()

    modified_last_names = []
    for name in last_names:
        name = name.strip()
        if name.startswith("MC"):
            modified_last_names.append(name[:1].capitalize() + name[1:2].lower() + name[2:3].capitalize() + name[3:].lower())
        else:
            modified_last_names.append(name[:1].capitalize() + name[1:].lower())

    with open("surnames1.txt", 'w') as f:
        f.write('\n'.join(modified_last_names))

if __name__ == '__main__':
    capitalize_last_names()
