def what_to_do(instructions):
    if instructions.startswith("Simon says") or instructions.endswith("Simon says"):
        return "I " + instructions.replace('Simon says', '').strip()
    else:
        return "I won't do it!"
